#!/usr/bin/env python3
"""
Extract Jira ID from git branch name.

Usage:
    python extract_jira_id.py [branch_name]

If no branch name is provided, uses the current git branch.
Returns the Jira ID if found, empty string otherwise.
"""

import re
import sys
import subprocess


def get_current_branch():
    """Get the current git branch name."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def extract_jira_id(branch_name):
    """
    Extract Jira ID from branch name.

    Supports patterns like:
    - feature/PROJ-123-description
    - bugfix/PROJ-456-fix-bug
    - PROJ-789-some-feature
    - hotfix/PROJECT-111
    """
    # Pattern: One or more uppercase letters, hyphen, one or more digits
    pattern = r'([A-Z]+-\d+)'
    match = re.search(pattern, branch_name)

    if match:
        return match.group(1)
    return ""


def main():
    if len(sys.argv) > 1:
        branch_name = sys.argv[1]
    else:
        branch_name = get_current_branch()
        if not branch_name:
            print("Error: Not in a git repository", file=sys.stderr)
            sys.exit(1)

    jira_id = extract_jira_id(branch_name)
    print(jira_id)

    # Exit with code 1 if no Jira ID found
    sys.exit(0 if jira_id else 1)


if __name__ == "__main__":
    main()
