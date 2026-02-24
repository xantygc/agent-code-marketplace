# Pecholata Marketplace

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-agent--code--marketplace-blue?logo=github)](https://github.com/xantygc/agent-code-marketplace)

**Personal marketplace for Claude Code skills and automations.** Custom skills for development workflows, including Git automation with Jira integration and GitLab-compatible commit formats.

## 🚀 Quick Start

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/xantygc/agent-code-marketplace.git

# Navigate to the project directory
cd agent-code-marketplace
```

### 2. Install the Marketplace in Claude Code

There are two ways to add the marketplace to Claude Code:

#### Option A: Local Installation (Recommended for Development)

1. Use the plugin marketplace command:
```
/plugin marketplace add /path/to/agent-code-marketplace
```
Or on Windows:
```
/plugin marketplace add C:\projects\agent-code-marketplace
```

2. Restart Claude Code to load the marketplace

**Note:** Claude Code will automatically detect the `.claude-plugin/marketplace.json` file.

#### Option B: Remote Installation (via Git)

1. Add the marketplace via Git URL:
```
/plugin marketplace add https://github.com/xantygc/agent-code-marketplace.git
```

2. Restart Claude Code

Claude Code will clone the repository and automatically detect the marketplace configuration.

### 3. Use the Skills

Once installed, the skills are available:

```
# Use git-workflow for commits with Jira integration
/git-workflow

# Or invoke via Claude Code conversation
"Create a commit with Jira ID AZ-123"
```

## 📦 Available Skills

### git-workflow
Git workflow automation with Jira integration and GitLab-compatible commit format.

**Features:**
- Automatic Jira ID extraction from branch names
- Conventional Commits format: `type(scope): JIRA-ID description`
- GitLab commit message validation
- Merge request creation with templates

**Commands available after installation:**
- `/feature` - Create a new feature branch
- `/release` - Create a release branch
- `/hotfix` - Create a hotfix branch
- `/finish` - Complete and merge current branch
- `/flow-status` - Show Git Flow status

## 🔧 Development

### Project Structure

```
.
├── .claude-plugin/
│   └── marketplace.json     # Marketplace configuration (REQUIRED)
├── skills/
│   └── git-workflow/        # Git workflow skill
│       ├── SKILL.md         # Skill documentation
│       ├── scripts/         # Python validation scripts
│       ├── references/      # Commit examples and guides
│       └── assets/          # Templates
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
