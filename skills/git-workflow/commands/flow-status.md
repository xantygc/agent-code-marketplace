---
allowed-tools: Bash(git branch:*), Bash(git status:*), Bash(git log:*), Bash(git tag:*)
description: Show Git Flow status
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status`
- All local branches: !`git branch --format='%(refname:short)|%(upstream:short)|%(upstream:track)'`
- All remote branches: !`git branch -r`
- Recent tags: !`git tag -l --sort=-version:refname`
- Recent commits on current branch: !`git log --oneline -10`

## Your task

Display a comprehensive Git Flow status report.

Show the following information in a well-formatted, easy-to-read layout:

1. **Current State**:
   - Current branch name and type (feature/hotfix/release/main/develop)
   - Working directory status (clean or uncommitted changes)
   - Number of unpushed commits (if any)

2. **Active Branches**:
   - Feature branches (list all `feature/*` branches)
   - Hotfix branches (list all `hotfix/*` branches)
   - Release branches (list all `release/*` branches)
   - For each branch, show if it's ahead/behind remote

3. **Main Branches**:
   - Status of `main` (or `master`)
   - Status of `develop` (if exists)
   - Show commits ahead/behind origin for each

4. **Recent Activity**:
   - Last 5 commits on current branch
   - Latest release tag (if any)

5. **Recommendations**:
   - Suggest next actions based on current branch type
   - Warn about uncommitted changes
   - Highlight branches that might need attention (far behind, not pushed, etc.)

Use colors, emojis, or formatting to make the output clear and scannable. Group related information together.
