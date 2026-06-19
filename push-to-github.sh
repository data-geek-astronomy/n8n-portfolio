#!/bin/bash
set -e

REPO_NAME="ai-agent-portfolio"
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Pushing to GitHub: $REPO_NAME ==="
cd "$BASE"

git init
git checkout -b main
git config user.email "aravind.kumar.nalukurthi@gmail.com"
git config user.name "Aravind Kumar Nalukurthi"
git add .
git commit -m "Initial commit: AI Agent Portfolio — 9 n8n agents across Healthcare, Transportation, Construction"

gh repo create "$REPO_NAME" \
  --public \
  --description "AI Agent Portfolio — 9 production n8n workflow agents powered by GPT-4o across Healthcare, Transportation and Construction" \
  --source=. \
  --remote=origin \
  --push

echo ""
echo "Done! Repo live at: https://github.com/data-geek-astronomy/$REPO_NAME"
echo ""
echo "=== Enabling GitHub Pages ==="
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/data-geek-astronomy/$REPO_NAME/pages" \
  -f "source[branch]=main" \
  -f "source[path]=/" 2>/dev/null || \
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  "/repos/data-geek-astronomy/$REPO_NAME/pages" \
  -f "source[branch]=main" \
  -f "source[path]=/" 2>/dev/null || true

echo ""
echo "GitHub Pages will be live in ~60 seconds at:"
echo "  https://data-geek-astronomy.github.io/$REPO_NAME/"
echo ""
echo "Optional: Also deploy the Streamlit app"
echo "  1. Go to https://share.streamlit.io"
echo "  2. Click 'New app'"
echo "  3. Select repo: data-geek-astronomy/$REPO_NAME"
echo "  4. Branch: main   |   Main file: app.py"
echo "  5. Click Deploy"
