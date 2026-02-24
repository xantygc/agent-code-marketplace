---
allowed-tools: Bash(git checkout:*), Bash(git branch:*), Bash(git status:*)
description: Create a new feature branch
---

## Context

- Current branch: !`git branch --show-current`
- All branches: !`git branch -a`

## Your task

Create a new feature branch following the Git Flow convention with a Jira ID.

1. Ask the user for:
   - Jira ticket ID (e.g., PROJ-123)
   - Feature description (short, kebab-case, e.g., "user-authentication")

2. Create a branch with the format: `feature/JIRA-ID-description`
   Example: `feature/PROJ-123-user-authentication`

3. Check out the new branch

4. Confirm to the user that the branch was created successfully

Use the format that allows automatic Jira ID extraction by the validation scripts.
