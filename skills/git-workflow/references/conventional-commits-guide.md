# Conventional Commits Quick Reference

## Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(api): add user endpoint` |
| `fix` | Bug fix | `fix(login): resolve token expiration` |
| `docs` | Documentation only | `docs(readme): update installation steps` |
| `style` | Code style/formatting | `style(header): fix indentation` |
| `refactor` | Code restructuring | `refactor(utils): simplify date parsing` |
| `perf` | Performance improvement | `perf(db): add index to users table` |
| `test` | Adding/updating tests | `test(auth): add login test cases` |
| `build` | Build system changes | `build(deps): update webpack to v5` |
| `ci` | CI/CD changes | `ci(github): add test workflow` |
| `chore` | Maintenance tasks | `chore(deps): update dependencies` |
| `revert` | Revert previous commit | `revert: undo feature X` |

## Format Rules

### Subject Line (First Line)

**Required format:** `JIRA-ID: type(scope): description`

- **JIRA-ID**: Project key and issue number (e.g., PROJ-123)
- **type**: One of the types above
- **scope**: Optional, component/area affected (lowercase, alphanumeric with hyphens)
- **description**: Brief summary (lowercase, no period at end)

**Examples:**
```
PROJ-123: feat(auth): add two-factor authentication
PROJ-456: fix(api): handle null response in user endpoint
PROJ-789: docs: update API documentation
```

### Body (Optional)

- Blank line after subject
- Explain the **why**, not the what (code shows the what)
- Wrap at 72 characters
- Use bullet points for multiple items

### Footer (Optional)

- Blank line after body
- Reference related issues: `Refs: PROJ-123`
- Note breaking changes: `BREAKING CHANGE: API endpoint renamed`
- Co-authors: `Co-Authored-By: Name <email>`

## Best Practices

1. **Keep subject line under 72 characters**
2. **Use imperative mood**: "add feature" not "added feature"
3. **Don't capitalize first letter of description**
4. **No period at end of subject line**
5. **Separate scope from description with colon and space**
6. **One logical change per commit**

## Breaking Changes

For changes that break backward compatibility:

```
PROJ-123: feat(api): change authentication method

BREAKING CHANGE: Authentication now requires JWT tokens instead of API keys.
All clients must update their authentication logic.
```

## Common Scopes by Area

- **Frontend**: `ui`, `components`, `styles`, `routes`
- **Backend**: `api`, `auth`, `db`, `models`, `services`
- **Infrastructure**: `docker`, `k8s`, `ci`, `deploy`
- **Tooling**: `build`, `scripts`, `config`
- **Testing**: `unit`, `integration`, `e2e`
