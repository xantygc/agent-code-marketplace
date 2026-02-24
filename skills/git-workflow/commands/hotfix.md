---
allowed-tools: Bash(git checkout:*), Bash(git branch:*), Bash(git status:*)
description: Create a hotfix branch
---

## Context

- Current branch: !`git branch --show-current`
- All branches: !`git branch -a`
- Recent tags: !`git tag -l --sort=-version:refname | head -10`

## Your task

Create a new hotfix branch following the Git Flow convention with a Jira ID.

1. Ask the user for:
   - Jira ticket ID (e.g., PROJ-456)
   - Hotfix description (short, kebab-case, e.g., "critical-security-patch")

2. Create a branch with the format: `hotfix/JIRA-ID-description`
   Example: `hotfix/PROJ-456-critical-security-patch`

3. Check out the new branch from 'main' (or 'master')

4. Confirm to the user that the hotfix branch was created successfully

Hotfix branches are used to quickly patch production releases and must include a Jira ID for tracking.
