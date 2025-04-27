#!/usr/bin/env bash
set -euo pipefail

# 1) Run pre-commit
echo "🧪 Running pre-commit hooks…"
if ! pre-commit run --all-files; then
  echo
  echo "✋ pre-commit found issues. Please fix them before committing."
  exit 1
fi

# 2) Let the user pick files to add
echo
echo "📂 Here are your modified/untracked files:"
git status --short

echo
read -p "Which files would you like to stage? (e.g. file1.py file2.txt): " files
if [[ -z "${files// /}" ]]; then
  echo "No files provided—aborting."
  exit 1
fi

git add $files
echo "✅ Staged: $files"

# 3) Ask for a commit message
echo
read -p "Enter commit message: " msg
if [[ -z "${msg// /}" ]]; then
  echo "Empty commit message—aborting."
  exit 1
fi

git commit -m "$msg"
echo "✅ Committed."

# 4) Push to the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
echo
echo "📤 Pushing to origin/$current_branch..."
git push origin "$current_branch"
echo "🎉 Done!"
