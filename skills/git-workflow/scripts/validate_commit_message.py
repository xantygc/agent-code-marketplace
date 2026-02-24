#!/usr/bin/env python3
"""
Validate commit message follows the format: type(scope): JIRA-ID message

Usage:
    python validate_commit_message.py "commit message"

Returns 0 if valid, 1 if invalid.
Prints validation errors to stderr.
"""

import re
import sys


# Conventional Commit types
VALID_TYPES = [
    'feat',     # New feature
    'fix',      # Bug fix
    'docs',     # Documentation changes
    'style',    # Code style changes (formatting, missing semi colons, etc)
    'refactor', # Code refactoring
    'perf',     # Performance improvements
    'test',     # Adding or updating tests
    'build',    # Build system or external dependencies
    'ci',       # CI/CD changes
    'chore',    # Other changes that don't modify src or test files
    'revert',   # Revert a previous commit
]


def validate_commit_message(message):
    """
    Validate commit message format.

    Expected format: type(scope): JIRA-ID message
    Example: feat(auth): PROJ-123 add login functionality

    Returns (is_valid, error_message)
    """
    # Split into lines to get just the subject line
    lines = message.strip().split('\n')
    subject = lines[0].strip()

    # Pattern: type(scope): JIRA-ID message
    # - type: Must be one of the valid types
    # - scope: Optional, alphanumeric with hyphens
    # - JIRA-ID: One or more uppercase letters, hyphen, one or more digits
    # - message: Any text (can start with uppercase)
    pattern = r'^([a-z]+)(?:\(([a-z0-9\-]+)\))?:\s*([A-Z]+-\d+)\s+(.+)$'

    match = re.match(pattern, subject)

    if not match:
        return False, "Format must be: type(scope): JIRA-ID message"

    commit_type, scope, jira_id, description = match.groups()

    # Validate commit type
    if commit_type not in VALID_TYPES:
        return False, f"Invalid type '{commit_type}'. Must be one of: {', '.join(VALID_TYPES)}"

    # Validate description is not empty
    if not description:
        return False, "Description cannot be empty"

    # Validate description doesn't end with period
    if description.endswith('.'):
        return False, "Description should not end with a period"

    return True, None


def main():
    if len(sys.argv) < 2:
        print("Error: Commit message required", file=sys.stderr)
        print("Usage: validate_commit_message.py \"commit message\"", file=sys.stderr)
        sys.exit(1)

    commit_message = sys.argv[1]
    is_valid, error = validate_commit_message(commit_message)

    if is_valid:
        print("✓ Commit message is valid")
        sys.exit(0)
    else:
        print(f"✗ Invalid commit message: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
