#!/usr/bin/env bash
# Bad Apples India — Build Script
# Usage: ./scripts/build.sh
# Produces a deployable _site/ directory
set -euo pipefail
cd "$(dirname "$0")/.."

SITE_DIR="_site"
rm -rf "$SITE_DIR"
mkdir -p "$SITE_DIR/data"

# Build feed from incident data
# data/incidents/*.json (individual entries) -> merged into _site/data/feed.json
# data/incidents.json (master database) -> copied directly
if [ -f data/incidents.json ]; then
  cp data/incidents.json "$SITE_DIR/data/incidents.json"
fi

# Build combined feed from individual incident files
echo '[' > "$SITE_DIR/data/feed.json"
first=true
for f in data/incidents/*.json; do
    [ -f "$f" ] || continue
    # Skip TEMPLATE
    basename "$f" | grep -q '^TEMPLATE' && continue
    $first || echo ',' >> "$SITE_DIR/data/feed.json"
    first=false
    # Each incident file is a JSON array with one element — extract it
    cat "$f" >> "$SITE_DIR/data/feed.json"
done
echo ']' >> "$SITE_DIR/data/feed.json"

# If no individual incidents, copy from main incidents.json incidents array
incidents_count=$(jq '.incidents | length' data/incidents.json 2>/dev/null || echo 0)
if [ "$(jq length "$SITE_DIR/data/feed.json" 2>/dev/null || echo 0)" -eq 0 ]; then
  # Extract the incidents array from the main JSON
  jq '.incidents' data/incidents.json > "$SITE_DIR/data/feed.json" 2>/dev/null || true
fi

# Copy HTML + resources
cp index.html "$SITE_DIR/index.html"
cp constitution.html "$SITE_DIR/constitution.html" 2>/dev/null || true
cp CONSTITUTION.md "$SITE_DIR/CONSTITUTION.md" 2>/dev/null || true

# Copy assets
[ -d assets ] && cp -r assets "$SITE_DIR/assets" 2>/dev/null || true

# Create sitemap
cat > "$SITE_DIR/sitemap.xml" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://cashlessconsumer.github.io/bad-apples-india/</loc><priority>1.0</priority></url>
  <url><loc>https://cashlessconsumer.github.io/bad-apples-india/constitution</loc><priority>0.8</priority></url>
</urlset>
EOF

# robots.txt
cat > "$SITE_DIR/robots.txt" << 'EOF'
User-agent: *
Allow: /
Sitemap: https://cashlessconsumer.github.io/bad-apples-india/sitemap.xml
EOF

echo "✓ Built to $SITE_DIR/"
du -sh "$SITE_DIR" | awk '{print "  "$0}'
echo "  Deploy: npx gh-pages -d _site  or  deploy _site/ to Vercel"
