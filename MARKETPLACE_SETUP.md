# Marketplace Setup Guide

This document explains how to properly set up and install the Pecholata Marketplace for Claude Code.

## Directory Structure

```
personal-code-marketplace/
├── .claude-plugin/
│   └── marketplace.json        # Marketplace configuration (REQUIRED)
├── skills/
│   └── git-workflow/           # Git workflow skill
│       ├── SKILL.md            # Main skill definition
│       ├── README.md           # Skill documentation
│       ├── scripts/            # Python validation scripts
│       │   ├── extract_jira_id.py
│       │   ├── validate_commit_message.py
│       │   └── validate_branch_commits.sh
│       ├── references/         # Documentation
│       │   ├── conventional-commits-guide.md
│       │   └── commit-examples.md
│       └── assets/             # Templates
│           └── mr-template.md
├── README.md
├── LICENSE
└── .gitignore
```

## Key Points

### 1. `.claude-plugin/` Directory

**CRITICAL:** The `marketplace.json` file MUST be inside the `.claude-plugin/` directory.

- ✅ `.claude-plugin/marketplace.json` (CORRECT)
- ❌ `marketplace.json` at root (WRONG - causes ENOTDIR error)

Claude Code specifically looks for `.claude-plugin/marketplace.json` when loading marketplaces.

### 2. Skill References

In `marketplace.json`, skills are referenced by their directory path:

```json
{
  "plugins": [
    {
      "name": "git-workflow",
      "skills": [
        "./skills/git-workflow"
      ]
    }
  ]
}
```

Claude Code automatically looks for `SKILL.md` inside the specified directory.

### 3. Installation Methods

**Local Installation:**
```bash
/plugin marketplace add /path/to/personal-code-marketplace
```

**Remote Installation:**
```bash
/plugin marketplace add https://github.com/xantygc/agent-code-marketplace.git
```

After installation, restart Claude Code.

## Verification

After installation, verify the marketplace is loaded:

1. Run `/plugin` in Claude Code
2. You should see "pecholata-marketplace" listed
3. The "git-workflow" skill should be available

## Troubleshooting

### Error: ENOTDIR: not a directory, scandir

**Cause:** `marketplace.json` is not in `.claude-plugin/` directory.

**Solution:** Ensure `marketplace.json` is at `.claude-plugin/marketplace.json`, not at the root.

### Skill not loading

**Cause:** Incorrect path in `marketplace.json` or missing `SKILL.md`.

**Solution:** 
1. Verify skill path in marketplace.json: `"./skills/git-workflow"`
2. Verify `SKILL.md` exists at `skills/git-workflow/SKILL.md`

### Scripts not executable

**Cause:** Script files don't have execute permissions.

**Solution:**
```bash
chmod +x skills/git-workflow/scripts/*.py
chmod +x skills/git-workflow/scripts/*.sh
```

## Standards Followed

This marketplace follows the official Claude Code marketplace standards:

- Marketplace metadata in `.claude-plugin/marketplace.json`
- Skills organized in `skills/` directory
- Each skill has a `SKILL.md` file
- Frontmatter in `SKILL.md` with name and description
- Supporting files in skill subdirectories

## References

- [Anthropic Agent Skills](https://github.com/anthropics/anthropic-agent-skills)
- [Claude Code Plugins](https://github.com/anthropics/claude-code-plugins)
