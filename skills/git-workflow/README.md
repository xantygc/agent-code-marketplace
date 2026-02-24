# Git Workflow Skill

Git workflow automation with Jira integration and Conventional Commits format.

## Features

- **Git Flow Branch Management**: Create feature, release, and hotfix branches
- **Automatic Jira ID Extraction**: Extract Jira IDs from branch names
- **Conventional Commits**: Format commits as `type(scope): JIRA-ID description`
- **Commit Message Validation**: Validate before committing
- **Merge Request Creation**: Generate MRs with templates
- **Flow Status Dashboard**: View comprehensive Git Flow status

## Available Commands

After installing the marketplace, the following slash commands are available:

### Branch Management

- **`/feature`** - Create a new feature branch
  - Format: `feature/JIRA-ID-description`
  - Example: `feature/PROJ-123-user-authentication`

- **`/release`** - Create a release branch
  - Format: `release/X.Y.Z`
  - Example: `release/1.2.0`

- **`/hotfix`** - Create a hotfix branch
  - Format: `hotfix/JIRA-ID-description`
  - Example: `hotfix/PROJ-456-security-patch`

### Workflow Commands

- **`/finish`** - Complete and merge current branch
  - Merges feature/hotfix/release branches following Git Flow
  - Automatically creates tags for releases
  - Cleans up merged branches

- **`/flow-status`** - Show Git Flow status
  - Displays current branch state
  - Lists all active feature/hotfix/release branches
  - Shows recent commits and tags
  - Provides recommendations

## Usage

### Automatic Activation

This skill is automatically invoked by Claude Code when you:

1. Request to create a commit
2. Ask to create a merge request
3. Mention Jira IDs in commits
4. Need to validate commit messages

### Manual Invocation

Use the slash commands listed above to explicitly invoke Git Flow operations.

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
