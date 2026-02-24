# Commit Message Examples

## Good Examples

### Feature Addition

```
feat(auth): PROJ-123 add OAuth2 login support

Implement OAuth2 authentication flow with Google and GitHub providers.
Users can now sign in using their existing accounts.

- Add OAuth2 service with provider configuration
- Create callback endpoints for auth flow
- Update login UI with provider buttons

```

### Bug Fix

```
fix(api): PROJ-456 prevent null pointer in user lookup

Handle case where user ID doesn't exist in database.
Previously would throw NullPointerException.

```

### Documentation

```
docs(api): PROJ-789 add authentication examples

Add code examples for API authentication in multiple languages.
Includes Python, JavaScript, and curl examples.

```

### Refactoring

```
refactor(services): PROJ-234 extract email sending logic

Move email sending logic from UserService to new EmailService.
Improves separation of concerns and testability.

```

### Performance

```
perf(db): PROJ-567 add index on user email column

Query performance improved from 500ms to 50ms for user lookups by email.

```

### Test Addition

```
test(auth): PROJ-890 add integration tests for login flow

Add comprehensive tests covering success and failure scenarios:
- Valid credentials
- Invalid credentials
- Expired tokens
- Missing parameters

```

### Breaking Change

```
feat(api): PROJ-345 migrate to v2 authentication

BREAKING CHANGE: Authentication API has been redesigned.
- Endpoints moved from /auth/* to /v2/auth/*
- Token format changed from JWT to opaque tokens
- Refresh token flow now required

Migration guide: https://docs.example.com/migration-v2

```

### Simple Fix (Minimal Body)

```
fix(ui): PROJ-678 correct button alignment in header

```

### Chore

```
chore(deps): PROJ-901 update dependencies to latest versions

- axios: 0.27.2 → 1.6.0
- react: 18.2.0 → 18.3.1
- typescript: 5.0.4 → 5.5.3

```

## Bad Examples (and Why)

### ❌ Missing Jira ID

```
feat(auth): add login
```
**Problem**: No Jira ID in message

**Fixed**:
```
feat(auth): PROJ-123 add login
```

### ❌ Period at End

```
feat(auth): PROJ-123 add login functionality.
```
**Problem**: Subject line should not end with period

**Fixed**:
```
feat(auth): PROJ-123 add login functionality
```

### ❌ Vague Description

```
fix(api): PROJ-123 fix bug
```
**Problem**: Too vague, doesn't explain what was fixed

**Fixed**:
```
fix(api): PROJ-123 handle null response in user endpoint
```

### ❌ Wrong Tense

```
feat(auth): PROJ-123 added login functionality
```
**Problem**: Should use imperative mood ("add" not "added")

**Fixed**:
```
feat(auth): PROJ-123 add login functionality
```

### ❌ Multiple Changes in One Commit

```
feat(auth): PROJ-123 add login and refactor database and update docs
```
**Problem**: Should be split into separate commits

**Fixed**: Split into three commits:
```
feat(auth): PROJ-123 add login functionality
refactor(db): PROJ-123 optimize user queries
docs(api): PROJ-123 update authentication guide
```

### ❌ Missing Type

```
PROJ-123: add login functionality
```
**Problem**: No commit type specified

**Fixed**:
```
feat(auth): PROJ-123 add login functionality
```

### ❌ Invalid Type

```
feature(auth): PROJ-123 add login
```
**Problem**: "feature" should be "feat"

**Fixed**:
```
feat(auth): PROJ-123 add login
```
