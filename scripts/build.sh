#!/usr/bin/env bash
# Bad Apples India — Build Script
# Usage: ./scripts/build.sh
# Produces a deployable _site/ directory with data inlined into the HTML.

set -euo pipefail
cd "$(dirname "$0")/.."

SITE_DIR="_site"
mkdir -p "$SITE_DIR"

# ── 1. Combine all incident JSONs into a single feed ──
TMP_DATA=$(mktemp)
echo '[' > "$TMP_DATA"
first=true
for f in data/incidents/*.json; do
    [ -f "$f" ] || continue
    [ "$(basename "$f")" = "TEMPLATE.json" ] && continue
    $first || echo ',' >> "$TMP_DATA"
    first=false
    cat "$f" >> "$TMP_DATA"
done
echo ']' >> "$TMP_DATA"

# Validate JSON
python3 -m json.tool "$TMP_DATA" > /dev/null 2>&1 || { echo "❌ Invalid JSON in incidents"; exit 1; }

# ── 2. Inline the data into index.html ──
DATA_JSON=$(cat "$TMP_DATA")
rm "$TMP_DATA"

# Use awk to replace the empty INCIDENTS array with actual data
awk -v data="$DATA_JSON" '
/const INCIDENTS = \[\];/ { print "const INCIDENTS = " data ";"; next }
{ print }
' index.html > "$SITE_DIR/index.html"

# ── 3. Copy supporting pages ──
cp constitution.html "$SITE_DIR/constitution.html"
cp CONSTITUTION.md "$SITE_DIR/CONSTITUTION.md" 2>/dev/null || true

# ── 4. Copy assets ──
cp -r assets "$SITE_DIR/assets" 2>/dev/null || true

# ── 5. Robots + sitemap ──
cat > "$SITE_DIR/robots.txt" << 'EOF'
User-agent: *
Allow: /
EOF

cat > "$SITE_DIR/sitemap.xml" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://cashlessconsumer.github.io/bad-apples-india/</loc><priority>1.0</priority></url>
  <url><loc>https://cashlessconsumer.github.io/bad-apples-india/constitution.html</loc><priority>0.8</priority></url>
</urlset>
EOF

echo "✓ Built to $SITE_DIR/"
echo "  $(wc -c < "$SITE_DIR/index.html") bytes"
echo "  Deploy: npx gh-pages -d _site  or  deploy _site/ to Vercel"
