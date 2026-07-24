#!/usr/bin/env node
/**
 * Bad Apples India — Incident Entry Scripter
 * Usage: node scripts/add-incident.js
 * Creates a new entry scaffold and prints JSON to stdout.
 */

const crypto = require("crypto");

function generateId(location, state) {
  const code = (state || "XX").slice(0, 2).toUpperCase();
  const distCode = (location || "XX").slice(0, 2).toUpperCase();
  const year = new Date().getFullYear();
  const seq = Date.now().toString(36).slice(-4).toUpperCase();
  return `${code}-${distCode}-${year}-${seq}`;
}

const entry = {
  id: generateId(process.argv[2] || "", process.argv[3] || ""),
  date: new Date().toISOString().split("T")[0],
  location: process.argv[2] || "Location",
  district: process.argv[4] || "",
  state: process.argv[3] || "Delhi",
  officers: [
    {
      name: process.argv[5] || "Officer Name (required)",
      badge: process.argv[6] || "",
      rank: process.argv[7] || "",
      station: process.argv[8] || "",
    },
  ],
  description: "Enter factual description here.",
  evidence: [
    {
      type: "video",
      url: "",
      embed_url: "",
      description: "Evidence description",
    },
  ],
  source: "Source attribution",
  source_url: "",
  legal_status: "complaint_filed",
  category: "other",
  tags: [],
  submitted_at: new Date().toISOString(),
  verified: false,
};

console.log(JSON.stringify(entry, null, 2));
console.log("\n// Copy this into data/incidents.json or data/incidents/<id>.json");
console.log("// Usage: node scripts/add-incident.js 'New Delhi' 'Delhi' 'Central' 'Constable Name' 'DL-12345' 'Constable' 'Paharganj'");
