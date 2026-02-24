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

1. Run the plugin command in Claude Code:
```
/plugin
```

2. When prompted for "marketplace source", enter the **absolute path** to your cloned repository:
```
/mnt/c/projects/agent-code-marketplace
```
Or on Windows:
```
C:\projects\agent-code-marketplace
```

3. Restart Claude Code to load the plugins

#### Option B: Remote Installation

1. Run the plugin command:
```
/plugin
```

2. Enter the marketplace URL:
```
https://raw.githubusercontent.com/xantygc/agent-code-marketplace/master/marketplace.json
```

3. Restart Claude Code

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

### python-poetry-dev
Modern Python development workflow with Poetry 2.3 and Ruff linting.

**Features:**
- Poetry 2.3+ for dependency management and virtual environments
- Ruff for fast, comprehensive linting (10-100x faster than traditional tools)
- Production-ready project templates (pyproject.toml, ruff.toml)
- Dependency groups (dev, test, docs)
- CI/CD integration examples (GitHub Actions, GitLab CI)
- Migration guides from pip/requirements.txt

**Use cases:**
- New Python project setup
- Migrating from pip to Poetry
- Setting up modern linting and code quality tools
- Building Python packages or applications

## 🔧 Development

### Project Structure

```
.
├── marketplace.json          # Marketplace configuration
├── skills/
│   └── git-workflow/        # Git workflow skill
│       ├── SKILL.md         # Skill documentation
│       ├── scripts/         # Python validation scripts
│       ├── references/      # Commit examples and guides
│       └── assets/          # Templates
└── README.md
```

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
