---
allowed-tools: Bash(git checkout:*), Bash(git branch:*), Bash(git status:*)
description: Create a release branch
---

## Context

- Current branch: !`git branch --show-current`
- All branches: !`git branch -a`
- Recent tags: !`git tag -l --sort=-version:refname | head -10`

## Your task

Create a new release branch following the Git Flow convention.

1. Ask the user for the release version (e.g., "1.2.0")

2. Create a branch with the format: `release/X.Y.Z`
   Example: `release/1.2.0`

3. Check out the new branch from the current branch (typically 'develop' or 'main')

4. Confirm to the user that the release branch was created successfully

Release branches are used to prepare a new production release. They allow for minor bug fixes and preparing metadata for a release.
