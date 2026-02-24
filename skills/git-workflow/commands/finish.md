---
allowed-tools: Bash(git checkout:*), Bash(git merge:*), Bash(git branch:*), Bash(git status:*), Bash(git push:*), Bash(git tag:*)
description: Complete and merge current branch
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status`
- Unpushed commits: !`git log @{u}.. --oneline 2>/dev/null || echo "No upstream branch"`
- All branches: !`git branch -a`

## Your task

Complete and merge the current feature/hotfix/release branch following Git Flow conventions.

1. **Verify the current branch type**:
   - Feature branch: merge into develop
   - Hotfix branch: merge into both main and develop
   - Release branch: merge into both main and develop, then tag

2. **Pre-merge checks**:
   - Ensure all changes are committed
   - Ensure the branch is pushed to origin (if not, push it first)

3. **Merge strategy**:
   - For feature branches: `git checkout develop && git merge --no-ff <branch-name>`
   - For hotfix branches:
     - `git checkout main && git merge --no-ff <branch-name>`
     - `git checkout develop && git merge --no-ff <branch-name>`
   - For release branches:
     - `git checkout main && git merge --no-ff <branch-name>`
     - Create tag: `git tag -a vX.Y.Z -m "Release version X.Y.Z"`
     - `git checkout develop && git merge --no-ff <branch-name>`

4. **Post-merge**:
   - Push all merged branches and tags
   - Ask user if they want to delete the finished branch
   - If yes: `git branch -d <branch-name> && git push origin --delete <branch-name>`

5. Confirm completion with summary of what was merged

**Important**: Always use `--no-ff` (no fast-forward) to preserve branch history.
