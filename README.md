# Pecholata Marketplace

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-agent--code--marketplace-blue?logo=github)](https://github.com/xantygc/agent-code-marketplace)

**Personal marketplace for Claude Code skills and automations.** Custom skills for development workflows, including Git automation with Jira integration and GitLab-compatible commit formats.

## 🚀 Quick Start

### Installation

Add the marketplace to Claude Code using one of these methods:

#### Method 1: Remote Installation (Recommended)

```bash
/plugin marketplace add https://github.com/xantygc/agent-code-marketplace.git
```

#### Method 2: Local Installation (For Development)

1. Clone the repository:
```bash
git clone https://github.com/xantygc/agent-code-marketplace.git
cd agent-code-marketplace
```

2. Add to Claude Code:
```bash
/plugin marketplace add /path/to/agent-code-marketplace
```

On Windows:
```cmd
/plugin marketplace add C:\projects\agent-code-marketplace
```

### After Installation

1. **Restart Claude Code** to load the marketplace
2. Verify installation by running `/plugin` - you should see "pecholata-marketplace"
3. Skills are now available for use

### Using the Skills

The skills are automatically invoked by Claude Code when relevant. For example:

```
# Git workflow skill activates automatically when you:
- "Create a commit with these changes"
- "Create a merge request"
- "Validate my commit messages"

# Or explicitly invoke it:
/git-workflow
```

## 📦 Available Skills

### git-workflow
Git workflow automation with Jira integration and GitLab-compatible commit format.

**Features:**
- Automatic Jira ID extraction from branch names
- Conventional Commits format: `type(scope): JIRA-ID description`
- GitLab commit message validation
- Merge request creation with templates

**Slash Commands:**
- `/feature` - Create a new feature branch (`feature/JIRA-ID-description`)
- `/release` - Create a release branch (`release/X.Y.Z`)
- `/hotfix` - Create a hotfix branch (`hotfix/JIRA-ID-description`)
- `/finish` - Complete and merge current branch (following Git Flow)
- `/flow-status` - Show comprehensive Git Flow status and recommendations

All commands are available immediately after installation. See [git-workflow README](skills/git-workflow/README.md) for detailed usage.

## 🔧 Development

### Project Structure

```
.
├── .claude-plugin/
│   └── marketplace.json     # Marketplace configuration (REQUIRED)
├── skills/
│   └── git-workflow/        # Git workflow skill
│       ├── .claude-plugin/
│       │   └── plugin.json  # Plugin metadata
│       ├── SKILL.md         # Main skill definition
│       ├── README.md        # Skill documentation
│       ├── commands/        # Slash commands
│       │   ├── feature.md   # /feature command
│       │   ├── release.md   # /release command
│       │   ├── hotfix.md    # /hotfix command
│       │   ├── finish.md    # /finish command
│       │   └── flow-status.md # /flow-status command
│       ├── scripts/         # Python validation scripts
│       │   ├── extract_jira_id.py
│       │   ├── validate_commit_message.py
│       │   └── validate_branch_commits.sh
│       ├── references/      # Documentation
│       │   ├── conventional-commits-guide.md
│       │   └── commit-examples.md
│       └── assets/          # Templates
│           └── mr-template.md
├── MARKETPLACE_SETUP.md     # Setup guide
└── README.md
```

**Important:** The `marketplace.json` file MUST be inside the `.claude-plugin/` directory. This is the standard location where Claude Code looks for marketplace configuration.

### Adding New Skills

1. Create a new directory under `skills/`
2. Add a `SKILL.md` file with the skill definition
3. Update `marketplace.json` to include the new skill
4. Test locally before pushing

### Commit Format

This repository uses GitLab-compatible conventional commits:

```
type(scope): JIRA-ID description

Examples:
- feat(auth): AZ-123 add OAuth2 login support
- fix(api): AZ-456 handle null response in user endpoint
- docs(readme): AZ-789 add installation instructions
```

**Valid types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`, `revert`

## 📖 Documentation

For more information about Claude Code and skill development:
- [Claude Code Documentation](https://docs.anthropic.com/claude/docs/claude-code)
- [Skill Development Guide](https://docs.anthropic.com/claude/docs/skills)


## Attribution

This marketplace is maintained by Santiago Gonzalez (santiago.gonzalez.courel@gmail.com).

**Original Project:**
- Based on [claude-code-templates](https://github.com/davila7/claude-code-templates) by Daniel Avila - Licensed under MIT License
- Agents Collection from [wshobson](https://github.com/wshobson/agents) - Licensed under MIT License
- Commands from [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Licensed under CC0 1.0 Universal

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Support

For issues or questions, contact Santiago Gonzalez at santiago.gonzalez.courel@gmail.com or create an issue in the [GitHub repository](https://github.com/xantygc/agent-code-marketplace/issues).
