#!/bin/bash
#
# Validate all commits in current branch against main/master
# Checks that each commit follows the format: JIRA-ID: type(scope): message
#
# Usage: ./validate_branch_commits.sh [base_branch]
#
# If base_branch is not provided, uses 'main' or 'master' (whichever exists)

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Determine base branch
if [ -n "$1" ]; then
    BASE_BRANCH="$1"
else
    # Check if main exists, otherwise use master
    if git show-ref --verify --quiet refs/heads/main; then
        BASE_BRANCH="main"
    elif git show-ref --verify --quiet refs/heads/master; then
        BASE_BRANCH="master"
    else
        echo "Error: Could not determine base branch (tried 'main' and 'master')" >&2
        exit 1
    fi
fi

# Get current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$CURRENT_BRANCH" = "$BASE_BRANCH" ]; then
    echo "Error: Already on $BASE_BRANCH. Switch to a feature branch first." >&2
    exit 1
fi

echo "Validating commits in '$CURRENT_BRANCH' against '$BASE_BRANCH'..."
echo

# Get list of commits in current branch not in base branch
COMMITS=$(git log --pretty=format:"%H" "$BASE_BRANCH..$CURRENT_BRANCH")

if [ -z "$COMMITS" ]; then
    echo "No commits to validate (branch is up to date with $BASE_BRANCH)"
    exit 0
fi

# Count total commits
TOTAL=$(echo "$COMMITS" | wc -l | tr -d ' ')
INVALID=0

echo "Found $TOTAL commit(s) to validate:"
echo

# Validate each commit
while IFS= read -r commit; do
    message=$(git log --format=%s -n 1 "$commit")
    short_commit=$(echo "$commit" | cut -c1-7)

    # Run validation script
    if python3 "$SCRIPT_DIR/validate_commit_message.py" "$message" > /dev/null 2>&1; then
        echo "✓ $short_commit: $message"
    else
        echo "✗ $short_commit: $message"
        python3 "$SCRIPT_DIR/validate_commit_message.py" "$message" 2>&1 | sed 's/^/  /'
        INVALID=$((INVALID + 1))
    fi
done <<< "$COMMITS"

echo
echo "────────────────────────────────────────"
echo "Total: $TOTAL | Valid: $((TOTAL - INVALID)) | Invalid: $INVALID"

if [ "$INVALID" -gt 0 ]; then
    echo
    echo "Some commits do not follow the required format."
    echo "Expected format: JIRA-ID: type(scope): message"
    echo "Example: PROJ-123: feat(auth): add login functionality"
    exit 1
fi

echo
echo "All commits are valid! ✓"
exit 0
