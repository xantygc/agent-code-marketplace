---
name: git-workflow
description: "Git workflow automation with Jira integration and Conventional Commits. Use when the user requests to: (1) Create commits, (2) Create or publish Merge Requests/Pull Requests on GitLab, (3) Validate commit messages, (4) Check commit formatting, (5) Perform commit+push+MR workflow, (6) Mentions Jira IDs in commits, or (7) References Conventional Commits format. Handles automatic Jira ID extraction from branch names and enforces commit message format type(scope): JIRA-ID message."
commands:
  - feature
  - release
  - hotfix
  - finish
  - flow-status
---

# Git Workflow with Jira Integration

Automate Git workflows following Conventional Commits with mandatory Jira ID prefixes for GitLab projects.

## Core Workflow

### Creating a Commit

When the user requests a commit:

1. **Extract Jira ID** from current branch name:
   ```bash
   python scripts/extract_jira_id.py
   ```

   If extraction fails (exit code 1), ask the user for the Jira ID.

2. **Determine commit type and scope**:
   - Analyze the changes to classify the commit type (feat, fix, docs, etc.)
   - See references/conventional-commits-guide.md for all valid types
   - Identify the scope (component/area affected)

3. **Draft commit message** following this format:
   ```
   type(scope): JIRA-ID description

   [Optional body with details]

   ```

   **Rules:**
   - Always use ENGLISH in commit message and description. Only ENGLISH is accepted.
   - No period at end of subject line
   - Use imperative mood ("add" not "added")
   - Keep subject line under 72 characters
   - Description can start with uppercase or lowercase

4. **Validate message** before committing:
   ```bash
   python scripts/validate_commit_message.py "commit message"
   ```

5. **Create the commit**:
   ```bash
   git add <files>
   git commit -m "$(cat <<'EOF'
   type(scope): JIRA-ID description

   Detailed description if needed.

   EOF
   )"
   ```

### Creating a Merge Request

When the user requests to create an MR (with or without prior commit):

1. **Ensure changes are committed** (follow commit workflow above if needed)

2. **Push to remote**:
   ```bash
   git push -u origin HEAD
   ```

3. **Generate MR description** using the template in assets/mr-template.md:
   - Summary: Brief description of the MR
   - Changes: Detailed list of modifications
   - Related Issues: Link to Jira ticket
   - Testing: How changes were tested
   - Checklist: Standard verification items

4. **Create MR using GitLab CLI**:
   ```bash
   gitlab mr create --title "Brief title" --description "$(cat <<'EOF'
   [MR description from template]
   EOF
   )"
   ```

   Or use `gh` command if configured for GitLab.

### Full Workflow (Commit + Push + MR)

When the user requests "commit and create MR" or similar:

1. Follow **Creating a Commit** workflow
2. Follow **Creating a Merge Request** workflow

Run these sequentially, not in parallel (commit must complete before push/MR).

### Validating Existing Commits

When the user wants to validate commits in the current branch:

```bash
bash scripts/validate_branch_commits.sh [base_branch]
```

This validates all commits in the current branch against main/master (or specified base branch).

## Additional Guidelines

### When to Load References

- **Always available**: This SKILL.md body is loaded
- **Load on demand**:
  - references/conventional-commits-guide.md: When user needs details about commit types or format rules
  - references/commit-examples.md: When user asks for examples or is confused about format

### Scope Selection

Common scopes by area:
- Frontend: `ui`, `components`, `styles`, `routes`
- Backend: `api`, `auth`, `db`, `models`, `services`
- Infrastructure: `docker`, `k8s`, `ci`, `deploy`
- Testing: `unit`, `integration`, `e2e`

Choose the most specific scope that accurately describes the change.

### Breaking Changes

For backward-incompatible changes, add in commit body:
```
BREAKING CHANGE: Description of what breaks and how to migrate.
```

### Multiple Changes

If a single request involves multiple logical changes:
1. Ask user if they should be separate commits
2. If yes, create multiple commits with appropriate messages
3. Each commit should be atomic and independently meaningful

## Scripts Reference

All scripts are in the `scripts/` directory:

- **extract_jira_id.py**: Extract Jira ID from branch name
  - Usage: `python scripts/extract_jira_id.py [branch_name]`
  - Returns: Jira ID (e.g., "PROJ-123") or empty string
  - Exit code: 0 if found, 1 if not found

- **validate_commit_message.py**: Validate single commit message
  - Usage: `python scripts/validate_commit_message.py "message"`
  - Returns: Success/failure with error details
  - Exit code: 0 if valid, 1 if invalid

- **validate_branch_commits.sh**: Validate all commits in branch
  - Usage: `bash scripts/validate_branch_commits.sh [base_branch]`
  - Validates all commits in current branch vs base
  - Exit code: 0 if all valid, 1 if any invalid

## Examples

### Example 1: Simple Commit

User: "Create a commit with these changes"

Steps:
1. Extract Jira ID: `python scripts/extract_jira_id.py` → "PROJ-123"
2. Analyze changes → determined as bug fix in API
3. Draft message: `fix(api): PROJ-123 handle null response in user endpoint`
4. Validate: `python scripts/validate_commit_message.py "fix(api): PROJ-123 handle null response in user endpoint"`
5. Create commit with message

### Example 2: Commit + MR

User: "Commit these changes and create a merge request"

Steps:
1. Create commit (follow Example 1)
2. Push: `git push -u origin HEAD`
3. Generate MR description using assets/mr-template.md
4. Create MR with GitLab CLI

### Example 3: Validate Existing Commits

User: "Check if my commits follow the correct format"

Steps:
1. Run: `bash scripts/validate_branch_commits.sh`
2. Report results to user
3. If invalid commits found, offer to help fix them

## Error Handling

- **No Jira ID found**: Ask user for Jira ID
- **Invalid commit message format**: Show validation error and suggest correction
- **Push fails**: Check if branch is up to date, suggest pull/rebase
- **MR creation fails**: Verify GitLab CLI is configured and user has permissions
