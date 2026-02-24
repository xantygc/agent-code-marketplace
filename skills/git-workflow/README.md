# Git Workflow Skill

Git workflow automation with Jira integration and Conventional Commits format.

## Features

- Automatic Jira ID extraction from branch names
- Conventional Commits format: `type(scope): JIRA-ID description`
- GitLab commit message validation
- Merge request creation with templates
- Commit message validation before committing

## Usage

This skill is automatically available once the marketplace is installed. Claude Code will use it when:

1. You request to create a commit
2. You ask to create a merge request
3. You mention Jira IDs in commits
4. You need to validate commit messages

## Structure

- `SKILL.md` - Main skill definition
- `scripts/` - Python validation scripts
  - `extract_jira_id.py` - Extract Jira ID from branch names
  - `validate_commit_message.py` - Validate commit message format
  - `validate_branch_commits.sh` - Validate all commits in a branch
- `references/` - Documentation and examples
  - `conventional-commits-guide.md` - Complete guide to conventional commits
  - `commit-examples.md` - Real-world commit examples
- `assets/` - Templates
  - `mr-template.md` - Merge request template

## Requirements

- Python 3.6+
- Git
- GitLab CLI (optional, for MR creation)

## License

MIT License - See LICENSE file in repository root
