#!/bin/bash
set -e

REPO_NAME="n8n-portfolio"
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Initialising repo: $REPO_NAME"

cd "$BASE"

git init
git checkout -b main
git config user.email "rahulreddy12365@gmail.com"
git config user.name "Aravind Kumar"
git add .
git commit -m "Initial commit: n8n AI Agent Portfolio (Streamlit app)"

gh repo create "$REPO_NAME" \
  --public \
  --description "Streamlit portfolio showcasing 9 n8n AI agents across Healthcare, Transportation and Construction" \
  --source=. \
  --remote=origin \
  --push

echo ""
echo "Done! Live at: https://github.com/data-geek-astronomy/$REPO_NAME"
echo ""
echo "To run locally:"
echo "  cd $BASE"
echo "  pip install streamlit"
echo "  streamlit run app.py"
