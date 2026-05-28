---
name: write-specs
description: Generate and update technical specifications for software projects based on descriptions and code changes. Use when users want to create initial specs from a project/feature description, update specs based on code changes, or maintain comprehensive documentation of features, architecture, and APIs.
---

# Write Specs

A skill for creating and maintaining technical specifications for software development projects.

## Overview

This skill helps you:

- Generate initial technical specifications from project descriptions
- Update specifications when code changes
- Maintain consistency between code and documentation
- Create comprehensive feature specs, API documentation, and architecture diagrams

## Core Capabilities

### 1. Generate Initial Specs

Create comprehensive specifications from a project description including:

- **Feature Specifications**: User stories, acceptance criteria, UI/UX details
- **Technical Architecture**: Data models, component hierarchy, application structure
- **API Documentation**: Public interfaces, protocols, and key methods
- **Implementation Plan**: Phased development approach with priorities

### 2. Update Specs from Code Changes

Analyze code changes and update specifications to reflect:

- New features added
- Modified data models or APIs
- Changed user flows
- Updated dependencies or architecture decisions

### 3. Maintain Spec-Code Alignment

Ensure specifications remain accurate by:

- Detecting drift between specs and implementation
- Flagging outdated sections
- Suggesting updates based on code analysis

## When to Use This Skill

Use this skill when:

- Starting a new project and need initial specifications
- Code has changed and specs need updating
- Onboarding new developers who need current documentation
- Planning features and need structured specs
- Conducting code reviews and need to verify spec compliance

## Workflow

### Creating Initial Specs

1. **Gather Requirements**
   - Read project description
   - Understand core features
   - Identify technical constraints (platform, frameworks, languages, etc.)

2. **Analyze Structure**
   - Review existing code if any
   - Identify patterns and conventions
   - Note dependencies and frameworks

3. **Generate Specs**
   - Create feature specifications
   - Document data models
   - Outline component/module hierarchy
   - Define APIs and interfaces
   - Create implementation roadmap

4. **Output**
   - Write specs to markdown files
   - Organize by category (features, architecture, API)
   - Include diagrams where helpful (using mermaid)

### Updating Specs from Code Changes

1. **Analyze Changes**
   - Read current specifications
   - Review changed code files
   - Identify what has changed (features, models, APIs, UI)

2. **Detect Drift**
   - Compare specs to actual implementation
   - Flag discrepancies
   - Identify new features not in specs

3. **Update Specs**
   - Modify relevant sections
   - Add new features/APIs
   - Update diagrams
   - Mark deprecated items

4. **Validate**
   - Ensure specs match implementation
   - Check for completeness
   - Verify consistency across documents

## Specification Structure

### Feature Specifications (`features/`)

For each major feature:

```markdown
# [Feature Name]

## Overview

High-level description of the feature

## User Stories

- As a [user], I want [goal] so that [benefit]

## Acceptance Criteria

- [ ] Specific testable criteria
- [ ] Edge cases covered

## UI/UX Details

- Screen layouts / page flows
- Navigation patterns
- User interactions

## Technical Notes

- Implementation considerations
- Dependencies
- Performance requirements
```

### Architecture Documentation (`architecture/`)

```markdown
# Architecture Overview

## Application Structure

- Application entry point
- Module organization
- Navigation/routing patterns
- State management approach

## Data Layer

### Models

- Entity definitions
- Relationships
- Validation rules

### Persistence

- Storage strategy (database, files, cache)
- Synchronization approach

## Business Logic Layer

- Service/controller organization
- Domain logic patterns
- Integration points

## Presentation Layer (if applicable)

- Component/view hierarchy
- Reusable components
- Styling approach

## Integration Layer

- External API integrations
- Message queues
- Third-party services
```

### API Documentation (`api/`)

```markdown
# [Component/Module] API

## Public Interfaces

### [Class/Interface/Function Name]

Purpose and usage

#### Methods/Functions

- `methodName(param: Type) -> ReturnType`
  - Description
  - Parameters
  - Returns
  - Exceptions/Errors
  - Example usage

#### Properties/Fields

- `propertyName: Type`
  - Description
  - Default value
  - Constraints
```

### Implementation Roadmap (`roadmap.md`)

```markdown
# Implementation Roadmap

## Phase 1: Core Features

- [ ] Task 1
- [ ] Task 2

## Phase 2: Enhanced Features

- [ ] Task 3

## Phase 3: Polish

- [ ] Task 4

## Future Considerations

- Feature ideas for later
```

## Best Practices

### For Initial Spec Generation

1. **Start Broad, Then Detailed**: Begin with high-level overview, then drill down
2. **Include Examples**: Show concrete usage examples for APIs and features
3. **Visual Aids**: Use mermaid diagrams for flows and architecture
4. **Prioritize**: Mark features as MVP, nice-to-have, or future
5. **Be Specific**: Avoid vague language; include concrete acceptance criteria

### For Spec Updates

1. **Track Changes**: Note what changed and why
2. **Version**: Consider dating major updates
3. **Deprecation**: Clearly mark deprecated features
4. **Cross-Reference**: Link related specs together
5. **Changelog**: Maintain a summary of spec changes

### Platform-Specific Considerations

#### Web Applications

1. **Component Structure**: Document component composition and reusability
2. **State Management**: Be explicit about state management approach (Redux, Context, Vuex, etc.)
3. **Routing**: Document page structure and navigation
4. **API Integration**: Specify REST/GraphQL patterns and data fetching strategies
5. **Responsive Design**: Note breakpoints and mobile considerations
6. **Accessibility**: Include WCAG compliance notes, ARIA labels, keyboard navigation

#### Backend Services

1. **API Design**: Document RESTful endpoints, GraphQL schemas, or RPC methods
2. **Data Models**: Specify database schemas, migrations, and relationships
3. **Authentication**: Document auth flows, token management, permission models
4. **Error Handling**: Define error codes, status codes, and error responses
5. **Scalability**: Note caching strategies, rate limiting, load balancing
6. **Deployment**: Document containerization, environment configs, CI/CD

#### Mobile Applications

1. **Platform Support**: Specify iOS/Android versions, cross-platform frameworks
2. **Navigation**: Document screen flows and navigation patterns
3. **State Management**: Define state approach (Redux, MobX, Provider, etc.)
4. **Offline Support**: Specify data persistence and sync strategies
5. **Platform Features**: Document use of cameras, GPS, notifications, etc.
6. **Accessibility**: Include screen reader support, dynamic type, platform guidelines

#### Desktop Applications

1. **Platform Support**: Specify OS compatibility (Windows, macOS, Linux)
2. **Framework**: Document framework choice (Electron, Qt, native)
3. **Window Management**: Define multi-window behavior, modals, dialogs
4. **File System**: Document file handling, storage locations, permissions
5. **Updates**: Specify auto-update mechanisms
6. **Keyboard Shortcuts**: Document hotkeys and accessibility features

#### CLI Tools

1. **Command Structure**: Document command syntax, subcommands, flags
2. **Input/Output**: Specify stdin/stdout behavior, exit codes
3. **Configuration**: Document config files, environment variables
4. **Error Messages**: Define user-friendly error output
5. **Help Text**: Include comprehensive usage documentation

## Communication with Users

When working with users on specs:

- **Clarify Scope**: Ask what level of detail they need
- **Confirm Understanding**: Summarize back the requirements
- **Highlight Decisions**: Point out architectural choices made
- **Flag Uncertainties**: Note areas that need user input
- **Iterative**: Expect multiple rounds of refinement

## Output Format

Generate specifications as markdown files organized in a logical directory structure:

```
specs/
   overview.md              # Project overview and goals
   features/               # Feature specifications
      user-authentication.md
      data-export.md
      notifications.md
   architecture/           # Technical architecture
      app-structure.md
      data-models.md
      api-design.md
   api/                    # API documentation
      auth-service.md
      data-service.md
   roadmap.md             # Implementation plan
```

## Common Patterns

### Web Frontend Applications

- Document component hierarchies and reusable UI elements
- Specify state management patterns and data flow
- Define API integration approaches
- Note routing and navigation structure
- Include styling system (CSS-in-JS, modules, preprocessors)

### Backend REST APIs

- Document endpoint definitions and HTTP methods
- Specify request/response formats
- Define authentication and authorization
- Note database schema and relationships
- Include error handling conventions

### Mobile Applications

- Navigation patterns (tab-based, stack-based, drawer)
- Data persistence strategies
- Platform-specific feature usage
- Push notification handling
- Offline/online sync mechanisms

### Microservices

- Service boundaries and responsibilities
- Inter-service communication patterns
- Data ownership and consistency
- Deployment and orchestration
- Monitoring and observability

### Data-Driven Applications

- CRUD operation patterns
- Data validation and constraints
- Synchronization strategies
- Offline support approaches
- Caching mechanisms

## Examples

### Example: Feature Spec for User Authentication

```markdown
# User Authentication

## Overview

Users can create accounts, log in, and manage their authentication credentials.

## User Stories

- As a new user, I want to create an account so I can access the application
- As a returning user, I want to log in with my credentials
- As a user, I want to reset my password if I forget it
- As a user, I want to stay logged in across sessions

## Acceptance Criteria

- [ ] Users can register with email and password
- [ ] Passwords must meet security requirements (min 8 chars, mixed case, numbers)
- [ ] Users receive email verification after registration
- [ ] Users can log in with verified credentials
- [ ] Failed login attempts are rate-limited
- [ ] Users can request password reset via email
- [ ] Sessions persist across browser restarts (remember me)
- [ ] Users can log out and invalidate their session

## UI/UX Details

- Registration form with email, password, confirm password fields
- Login form with email, password, remember me checkbox
- Password reset flow with email input and confirmation
- Clear error messages for validation failures
- Loading states during authentication operations

## Technical Notes

- Use bcrypt for password hashing
- JWT tokens for session management
- Email service integration for verification
- Rate limiting on login endpoint (5 attempts per 15 minutes)
- HTTPS required for all auth endpoints
```

### Example: Data Model Documentation (Multi-Language)

#### Python (using dataclass)

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    """Represents a user account in the system."""
    id: str
    email: str
    password_hash: str
    created_at: datetime
    email_verified: bool = False
    last_login: Optional[datetime] = None
```

#### TypeScript

```typescript
interface User {
  /** Unique identifier for the user */
  id: string;

  /** User's email address (unique) */
  email: string;

  /** Hashed password (bcrypt) */
  passwordHash: string;

  /** Account creation timestamp */
  createdAt: Date;

  /** Whether email has been verified */
  emailVerified: boolean;

  /** Last successful login timestamp */
  lastLogin?: Date;
}
```

### Example: API Documentation

````markdown
# Authentication API

## POST /api/auth/register

Register a new user account.

### Request Body

```json
{
  "email": "user@example.com",
  "password": "SecurePass123"
}
```
````

### Response (201 Created)

```json
{
  "id": "usr_1234567890",
  "email": "user@example.com",
  "emailVerified": false,
  "createdAt": "2024-01-15T10:30:00Z"
}
```

### Error Responses

- `400 Bad Request`: Invalid email format or weak password
- `409 Conflict`: Email already registered
- `429 Too Many Requests`: Rate limit exceeded

### Example

**cURL**

```bash
curl -X POST https://api.example.com/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"SecurePass123"}'
```

**Python (requests)**

```python
import requests

response = requests.post(
    "https://api.example.com/api/auth/register",
    json={"email": "user@example.com", "password": "SecurePass123"}
)
user = response.json()
```

**JavaScript (fetch)**

```javascript
const response = await fetch("https://api.example.com/api/auth/register", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    email: "user@example.com",
    password: "SecurePass123",
  }),
});
const user = await response.json();
```

```

## Error Handling

When generating or updating specs:
- **Missing Information**: Flag sections that need user input
- **Ambiguity**: Ask clarifying questions
- **Inconsistency**: Point out conflicts between specs and code
- **Incomplete Code**: Note when code doesn't match typical patterns

## Integration with Development

Specifications should:
- Guide implementation (developers reference specs while coding)
- Inform code review (reviewers check against specs)
- Support testing (test cases derived from acceptance criteria)
- Aid onboarding (new developers read specs to understand system)

## Version Control

Recommend:
- Store specs in git alongside code
- Review spec changes in PRs
- Keep specs updated with each feature PR
- Use conventional commits for spec changes

## Conclusion

The write-specs skill bridges the gap between ideas and implementation by creating and maintaining clear, comprehensive technical documentation. Use it at the start of a project to define what you're building, and throughout development to keep documentation in sync with reality.

This skill works across any programming language, framework, or platform - whether you're building web applications, backend services, mobile apps, CLI tools, or desktop software.
```
