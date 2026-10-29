#!/usr/bin/env python3
"""Longitudinal watch on Instagram account @yourvijayamani (BAI-2026-010 pretext artifact).

Deterministic loop (no LLM): probes the logged-out profile via agent-browser,
records state, alerts Discord #osint only on confirmed change.
Predictions under watch (FABRICATION-FORENSICS.md §5):
  - liveness/deletion, follower/following/post counts, bio/page-id drift.
Runtime state: watch-state/ (gitignored). Log: watch.log (gitignored).
"""
import json
import os
import random
import re
import subprocess
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(HERE, "watch-state")
STATE_JSONL = os.path.join(STATE_DIR, "state.jsonl")
LOCK = os.path.join(STATE_DIR, "lock")
LOG = os.path.join(HERE, "watch.log")
PROFILE_URL = "https://www.instagram.com/yourvijayamani/"
INTERVAL = 7200  # 2h
DISCORD_CHANNEL = "1540886408355516477"  # LogicPlay #osint
KEYS = ("followers", "following", "posts", "alive", "page_id")


def log(msg):
    with open(LOG, "a") as f:
        f.write("%s %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))


def acquire_lock():
    os.makedirs(STATE_DIR, exist_ok=True)
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        return fd
    except FileExistsError:
        pid = ""
        try:
            with open(LOCK) as f:
                pid = f.read().strip()
        except Exception:
            pass
        stale = time.time() - os.path.getmtime(LOCK) > 3 * 3600
        dead = bool(pid) and not os.path.exists("/proc/%s" % pid)
        if stale or dead:
            os.remove(LOCK)
            return acquire_lock()
        raise SystemExit("another watch instance holds the lock")


def probe():
    """Return state dict from logged-out profile page via agent-browser."""
    out = {}
    r = subprocess.run(["agent-browser", "open", PROFILE_URL], capture_output=True, text=True, timeout=120)
    time.sleep(4)
    js = ("JSON.stringify({title: document.title, "
          "desc: (document.querySelector('meta[name=\"description\"]')||{}).content||'', "
          "gone: document.body.innerText.indexOf('Sorry, this page isn') > -1, "
          "id: (document.body.innerHTML.match(/profilePage_([0-9]+)/)||[])[1]||''})")
    e = subprocess.run(["agent-browser", "eval", js], capture_output=True, text=True, timeout=60)
    try:
        out = json.loads(json.loads(e.stdout))
    except Exception:
        return {"alive": None, "challenge": True}
    desc = out.get("desc", "") or ""
    m = re.search(r"([\d,]+)\s*Followers,\s*([\d,]+)\s*Following,\s*([\d,]+)\s*Posts", desc)
    alive = bool(m) and not out.get("gone") and ("@yourvijayamani" in (out.get("title", "") or ""))
    st = {"alive": alive if (m or out.get("gone")) else None}
    if m:
        st["followers"] = int(m.group(1).replace(",", ""))
        st["following"] = int(m.group(2).replace(",", ""))
        st["posts"] = int(m.group(3).replace(",", ""))
    if out.get("id"):
        st["page_id"] = out["id"]
    return st


def last_state():
    if not os.path.exists(STATE_JSONL):
        return None
    with open(STATE_JSONL) as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
    return json.loads(lines[-1]) if lines else None


def record(state, kind):
    line = dict(state)
    line["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    line["kind"] = kind
    with open(STATE_JSONL, "a") as f:
        f.write(json.dumps(line) + "\n")


def alert(changes):
    tok = os.environ.get("DISCORD_BOT_TOKEN")
    body = ("[yourvijayamani-watch] BAI-2026-010 pretext account changed: " +
            ", ".join("%s %s->%s" % c for c in changes) +
            " (UTC " + time.strftime("%Y-%m-%d %H:%M") + "). " + PROFILE_URL)
    if not tok:
        log("ALERT (no bot token, local only): " + body)
        return
    req = urllib.request.Request(
        "https://discord.com/api/v10/channels/%s/messages" % DISCORD_CHANNEL,
        data=json.dumps({"content": body}).encode(),
        headers={"Authorization": "Bot " + tok, "Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=30)
        log("alert posted: " + body)
    except Exception as ex:
        log("alert post failed: %s | %s" % (ex, body))


def main():
    acquire_lock()
    log("watch started (interval %ds)" % INTERVAL)
    while True:
        try:
            cur = probe()
            prev = last_state()
            if cur.get("challenge") and not prev:
                record(cur, "challenge")
                log("probe challenge-walled, no baseline yet")
            elif prev is None:
                record(cur, "baseline")
                log("baseline: %s" % json.dumps(cur))
            else:
                changes = [(k, prev.get(k), cur.get(k)) for k in KEYS
                           if cur.get(k) is not None and prev.get(k) != cur.get(k)]
                if changes:
                    record(cur, "change")
                    alert(changes)
                    log("change: %s" % json.dumps(changes))
                else:
                    record(cur, "steady")
        except Exception as ex:
            log("probe error: %r" % ex)
        time.sleep(INTERVAL + random.randint(0, 300))


if __name__ == "__main__":
    main()
