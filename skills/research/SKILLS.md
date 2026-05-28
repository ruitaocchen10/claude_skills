---
name: research
description: Conduct systematic research on codebases, APIs, libraries, patterns, and technical problems through structured exploration and documentation. Use when learning a new codebase, evaluating libraries, understanding complex systems, or investigating technical solutions.
---

# Research

A skill for conducting systematic technical research on codebases, libraries, APIs, patterns, and solutions through structured exploration, analysis, and documentation.

## Overview

This skill helps you:

- Explore and understand unfamiliar codebases systematically
- Research and evaluate libraries and frameworks
- Investigate APIs and their capabilities
- Map system architecture and data flows
- Compare technical solutions and alternatives
- Document findings clearly and comprehensively
- Identify patterns and conventions in code
- Conduct security analysis and vulnerability research

## Core Capabilities

### 1. Codebase Exploration

Systematically understand existing code:

- **Architecture Mapping**: Identify overall structure and organization
- **Pattern Recognition**: Spot design patterns and conventions
- **Dependency Analysis**: Understand module relationships
- **Entry Points**: Find main execution paths
- **Code Flow Tracing**: Follow execution through the system
- **Convention Identification**: Discover naming, structure, and style patterns

### 2. Library/Framework Evaluation

Research and compare technical options:

- **Feature Analysis**: What capabilities does it provide?
- **API Surface**: How is it used? What's the learning curve?
- **Trade-offs**: What are strengths and weaknesses?
- **Ecosystem**: Community size, maintenance, documentation quality
- **Compatibility**: Does it work with existing stack?
- **Performance**: Speed, bundle size, resource usage
- **Alternatives**: What other options exist?

### 3. API Research

Understand API capabilities and usage:

- **Endpoint Discovery**: What endpoints exist?
- **Request/Response Formats**: What data structures are used?
- **Authentication**: How is access controlled?
- **Rate Limits**: What restrictions exist?
- **Error Handling**: How are errors reported?
- **Examples**: Collect usage examples
- **Edge Cases**: Identify limitations and special cases

### 4. Architecture Documentation

Map and document system structure:

- **Component Diagram**: Visual representation of system parts
- **Data Flow**: How information moves through the system
- **Integration Points**: External dependencies and APIs
- **State Management**: How state is stored and modified
- **Deployment Architecture**: Infrastructure and hosting
- **Security Model**: Authentication, authorization, data protection

### 5. Comparative Analysis

Evaluate multiple solutions:

- **Feature Matrix**: Side-by-side capability comparison
- **Performance Benchmarks**: Speed and resource usage
- **Developer Experience**: Ease of use, documentation, tooling
- **Community & Support**: Maintenance, popularity, help availability
- **Cost Analysis**: Pricing, licensing, operational costs
- **Risk Assessment**: Vendor lock-in, deprecation risk, security

### 6. Security Research

Analyze security characteristics:

- **Vulnerability Scanning**: Identify known vulnerabilities
- **Attack Surface Analysis**: Potential security weaknesses
- **Dependency Audit**: Check for vulnerable dependencies
- **Best Practices**: Security patterns and anti-patterns
- **Compliance**: Regulatory requirements (GDPR, HIPAA, etc.)

## When to Use This Skill

Use this skill when:

- Learning a new codebase (new job, open source contribution)
- Evaluating libraries or frameworks for a project
- Investigating technical solutions to a problem
- Understanding how existing systems work
- Debugging unfamiliar code
- Planning architecture or refactoring
- Creating documentation for a system
- Conducting security audits
- Researching best practices or patterns
- Making technical decisions (build vs buy)

## Workflow

### Exploring a New Codebase

1. **High-Level Overview**
   - Read README, documentation
   - Check package.json / dependencies
   - Identify language, framework, tools
   - Understand project purpose

2. **Identify Entry Points**
   - Find main files (index.js, main.py, app.js, etc.)
   - Locate startup/initialization code
   - Identify key routes or commands

3. **Map Architecture**
   - Identify directory structure
   - Understand module organization
   - Note major components
   - Identify patterns (MVC, layered, etc.)

4. **Trace Key Flows**
   - Follow a typical user action through code
   - Trace data from input to output
   - Understand state management
   - Note important transformations

5. **Identify Conventions**
   - Naming conventions
   - Code organization patterns
   - Testing approach
   - Error handling style

6. **Document Findings**
   - Create architecture diagram
   - Document key components
   - Note important patterns
   - Highlight gotchas or complexities

### Evaluating a Library

1. **Define Requirements**
   - What problem needs solving?
   - What features are required?
   - What constraints exist? (size, performance, compatibility)

2. **Research Candidates**
   - Search for potential libraries
   - Check npm/PyPI/etc. for options
   - Read documentation overview
   - Check GitHub stars, issues, recent activity

3. **Analyze Each Option**
   - Feature completeness
   - API design and ergonomics
   - Bundle size / performance
   - Documentation quality
   - Community and support
   - Maintenance and updates
   - License compatibility

4. **Compare Options**
   - Create feature comparison matrix
   - Benchmark performance if needed
   - Test integration with existing code
   - Evaluate learning curve

5. **Make Recommendation**
   - Rank options by criteria
   - Document trade-offs
   - Provide clear recommendation
   - Explain reasoning

### Researching an API

1. **Find Documentation**
   - Official API docs
   - OpenAPI/Swagger specs
   - SDKs and client libraries
   - Example code

2. **Understand Authentication**
   - API keys, OAuth, JWT, etc.
   - How to obtain credentials
   - How to include auth in requests

3. **Explore Endpoints**
   - List available endpoints
   - Understand request/response formats
   - Note required vs optional parameters
   - Test endpoints with example requests

4. **Identify Patterns**
   - REST conventions
   - Error response format
   - Pagination approach
   - Versioning strategy

5. **Check Limitations**
   - Rate limits
   - Data size limits
   - Feature restrictions on free tier
   - Regional availability

6. **Document Usage**
   - Create usage examples
   - Note common patterns
   - Document error handling
   - List important gotchas

## Research Methodologies

### Top-Down Approach

Start broad, then go deep:

1. **Overview**: Understand the big picture
2. **Components**: Identify major parts
3. **Details**: Dive into specific areas
4. **Synthesis**: Connect the pieces

**When to use**: New codebases, understanding architecture

### Bottom-Up Approach

Start specific, then generalize:

1. **Example**: Find a specific usage example
2. **Trace**: Follow execution through code
3. **Generalize**: Understand the pattern
4. **Map**: Build mental model from specifics

**When to use**: Debugging, understanding specific features

### Breadth-First Search

Explore widely before going deep:

1. **Survey**: Look at all major areas
2. **Categorize**: Group similar components
3. **Prioritize**: Identify most important areas
4. **Deep Dive**: Focus on priorities

**When to use**: Time-constrained research, getting overview

### Depth-First Search

Follow one path completely before exploring others:

1. **Choose Path**: Pick one area to understand
2. **Follow Completely**: Trace it to full understanding
3. **Repeat**: Move to next area
4. **Connect**: Link understandings together

**When to use**: Understanding complex flows, debugging specific issues

## Documentation Templates

### Codebase Overview

```markdown
# [Project Name] Architecture

## Overview

High-level description of what the project does and its purpose.

## Technology Stack

- **Language**: JavaScript/TypeScript
- **Framework**: React
- **Build Tool**: Vite
- **Testing**: Jest, React Testing Library
- **State Management**: Redux
- **API**: REST API with Express backend

## Project Structure

```
src/
  components/    # React components
  services/      # API and business logic
  store/         # Redux store and slices
  utils/         # Utility functions
  hooks/         # Custom React hooks
  types/         # TypeScript type definitions
```

## Key Components

### Component A
Purpose and responsibility

### Component B
Purpose and responsibility

## Data Flow

1. User interaction triggers action
2. Action dispatched to Redux store
3. Reducer updates state
4. Components re-render with new state

## Important Patterns

- All API calls go through services layer
- Components use custom hooks for data fetching
- Error boundaries catch rendering errors
- Form validation uses Yup schemas

## Entry Points

- Main: `src/main.tsx`
- Routes: `src/App.tsx`
- API: `src/services/api.ts`

## Testing Strategy

- Unit tests for utils and services
- Component tests with React Testing Library
- Integration tests for user flows
- E2E tests with Playwright (critical paths only)

## Deployment

- Build: `npm run build`
- Preview: `npm run preview`
- Deploy: Automated via GitHub Actions to Vercel
```

### Library Comparison

```markdown
# [Problem] Library Comparison

## Requirements

- Must support [feature A]
- Should be under 50kb gzipped
- Active maintenance (commits in last 3 months)
- TypeScript support

## Candidates

| Feature | Library A | Library B | Library C |
|---------|-----------|-----------|-----------|
| Bundle Size | 15kb | 45kb | 120kb |
| TypeScript | ✅ Built-in | ✅ Via @types | ❌ |
| Feature X | ✅ | ✅ | ✅ |
| Feature Y | ✅ | ❌ | ✅ |
| Weekly Downloads | 1M | 500K | 2M |
| Last Updated | 2 days ago | 1 week ago | 6 months ago |
| GitHub Stars | 15K | 8K | 25K |
| Open Issues | 45 | 120 | 300 |

## Detailed Analysis

### Library A

**Pros:**
- Small bundle size
- Excellent TypeScript support
- Active maintenance
- Great documentation

**Cons:**
- Smaller community than Library C
- Missing advanced feature Z

**Best for:** Most projects, especially with TypeScript

### Library B

**Pros:**
- Good balance of features and size
- Stable API

**Cons:**
- Missing Feature Y
- Requires separate TypeScript types

**Best for:** Projects not needing Feature Y

### Library C

**Pros:**
- Most features
- Largest community
- Extensive examples

**Cons:**
- Very large bundle size
- No TypeScript support
- Maintenance concerns (6 months since update)

**Best for:** Projects needing advanced features, can tolerate size

## Recommendation

**Library A** is recommended for most use cases because:
- Meets all requirements
- Best bundle size
- Active maintenance
- Excellent developer experience

Consider Library C only if advanced feature Z is critical and bundle size is not a concern.
```

### API Documentation

```markdown
# [API Name] Usage Guide

## Authentication

```javascript
const apiKey = process.env.API_KEY;
const headers = {
  'Authorization': `Bearer ${apiKey}`,
  'Content-Type': 'application/json',
};
```

## Base URL

```
https://api.example.com/v1
```

## Endpoints

### GET /users/:id

Get user by ID.

**Request:**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.example.com/v1/users/123
```

**Response (200 OK):**
```json
{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com",
  "createdAt": "2024-01-15T10:30:00Z"
}
```

**Error Responses:**
- `404 Not Found`: User doesn't exist
- `401 Unauthorized`: Invalid API key
- `429 Too Many Requests`: Rate limit exceeded

### POST /users

Create a new user.

**Request:**
```javascript
const response = await fetch('https://api.example.com/v1/users', {
  method: 'POST',
  headers,
  body: JSON.stringify({
    name: 'Jane Doe',
    email: 'jane@example.com',
  }),
});
```

**Response (201 Created):**
```json
{
  "id": "124",
  "name": "Jane Doe",
  "email": "jane@example.com",
  "createdAt": "2024-01-15T10:35:00Z"
}
```

## Rate Limits

- 1000 requests per hour per API key
- Rate limit headers included in responses:
  - `X-RateLimit-Limit`: Total requests allowed
  - `X-RateLimit-Remaining`: Requests remaining
  - `X-RateLimit-Reset`: Timestamp when limit resets

## Pagination

Paginated endpoints use cursor-based pagination:

```javascript
GET /users?limit=10&cursor=abc123
```

Response includes `nextCursor` for fetching next page:

```json
{
  "data": [...],
  "nextCursor": "xyz789"
}
```

## Error Handling

All errors follow this format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "field": "email"
  }
}
```

Common error codes:
- `VALIDATION_ERROR`: Request validation failed
- `NOT_FOUND`: Resource doesn't exist
- `UNAUTHORIZED`: Invalid credentials
- `RATE_LIMITED`: Too many requests
```

## Research Tools

### Code Search

- **GitHub Code Search**: Search across public repositories
- **grep/ripgrep**: Search within local codebase
- **ag (The Silver Searcher)**: Fast code search
- **IDE Find**: Use IDE's find/search features

### Static Analysis

- **TypeScript**: Type checking reveals structure
- **ESLint**: Code quality and patterns
- **SonarQube**: Code quality and security
- **Dependency analyzers**: Understand package relationships

### Runtime Analysis

- **Debugger**: Step through code execution
- **Profiler**: Identify performance bottlenecks
- **Network inspector**: Analyze API calls
- **Console logging**: Trace execution flow

### Documentation

- **JSDoc/TSDoc**: Code documentation
- **Swagger/OpenAPI**: API documentation
- **Storybook**: Component documentation
- **README files**: Project-level docs

### Dependency Analysis

- **npm ls / yarn why**: Dependency tree
- **Dependency-cruiser**: Visualize dependencies
- **Bundlephobia**: Package size analysis
- **npmgraph**: Dependency graph visualization

## Research Strategies

### Following the Code

```javascript
// Start: User clicks button
<button onClick={handleSubmit}>Submit</button>

// Trace: What does handleSubmit do?
function handleSubmit() {
  dispatch(createUser(formData)); // Goes to Redux
}

// Trace: What does createUser do?
function createUser(data) {
  return async (dispatch) => {
    const user = await api.createUser(data); // Goes to API
    dispatch({ type: 'USER_CREATED', user });
  };
}

// Trace: What does api.createUser do?
async function createUser(data) {
  return fetch('/api/users', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

// Complete understanding: Button → Redux action → API call → Server
```

### Finding Examples

```bash
# Find all usages of a function
grep -r "functionName" src/

# Find test files for examples
find . -name "*.test.js" -exec grep -l "ComponentName" {} \;

# Search documentation
grep -r "## Examples" docs/
```

### Understanding Dependencies

```bash
# What packages does this project use?
cat package.json | jq '.dependencies'

# Why is this package included?
npm why lodash

# What does this package do?
npm info lodash description
```

## Security Research

### Vulnerability Scanning

```bash
# JavaScript
npm audit
yarn audit

# Python
pip-audit
safety check

# Ruby
bundle audit
```

### Dependency Analysis

```bash
# Check for outdated packages
npm outdated

# Analyze dependency tree
npm ls

# Check for known vulnerabilities
snyk test
```

### Code Analysis

```bash
# Static analysis for security
eslint --plugin security

# Find secrets in code
gitleaks detect

# SAST scanning
semgrep --config=auto
```

## Performance Research

### Bundle Analysis

```bash
# Analyze webpack bundle
npx webpack-bundle-analyzer

# Analyze vite bundle
npx vite-bundle-visualizer
```

### Profiling

```javascript
// Performance measurement
console.time('operation');
expensiveOperation();
console.timeEnd('operation');

// Memory profiling (Chrome DevTools)
// 1. Open DevTools
// 2. Memory tab
// 3. Take heap snapshot
// 4. Compare snapshots to find leaks
```

### Benchmarking

```javascript
// Simple benchmark
const iterations = 10000;

console.time('approach1');
for (let i = 0; i < iterations; i++) {
  approach1();
}
console.timeEnd('approach1');

console.time('approach2');
for (let i = 0; i < iterations; i++) {
  approach2();
}
console.timeEnd('approach2');
```

## Common Research Patterns

### Understanding a Feature

1. Find where feature is used (UI, tests, docs)
2. Trace from UI to implementation
3. Understand data flow
4. Identify dependencies
5. Check for tests
6. Read related documentation

### Investigating a Bug

1. Reproduce the issue
2. Find relevant code
3. Understand expected behavior
4. Trace execution
5. Identify deviation
6. Check recent changes

### Evaluating Performance

1. Measure baseline
2. Identify bottlenecks (profiling)
3. Research optimization techniques
4. Implement improvements
5. Measure impact
6. Document findings

## Communication

When presenting research findings:

- **Structure**: Start with summary, then details
- **Visual Aids**: Use diagrams, charts, tables
- **Examples**: Provide concrete code examples
- **Trade-offs**: Explain pros and cons clearly
- **Recommendation**: Make clear suggestions
- **Sources**: Link to documentation and references
- **Actionable**: Provide next steps

## Research Checklist

### Before Starting

- [ ] Defined research question clearly
- [ ] Identified what success looks like
- [ ] Set time limits for research
- [ ] Determined required vs nice-to-have information

### During Research

- [ ] Taking notes as you go
- [ ] Documenting sources and links
- [ ] Testing claims/assumptions
- [ ] Tracking questions that arise
- [ ] Organizing findings logically

### After Research

- [ ] Summarized key findings
- [ ] Documented important details
- [ ] Made clear recommendations
- [ ] Identified gaps in knowledge
- [ ] Created action items

## Best Practices

### Effective Research

1. **Start with Questions**: What do you need to know?
2. **Use Multiple Sources**: Documentation, code, tests, community
3. **Verify Information**: Test claims yourself
4. **Document as You Go**: Don't rely on memory
5. **Know When to Stop**: Diminishing returns after a point

### Efficient Learning

1. **Prioritize**: Focus on most important areas first
2. **Skip Irrelevant**: Don't need to understand everything
3. **Use Examples**: Learn from working code
4. **Ask Questions**: Community, colleagues, documentation
5. **Hands-On**: Experiment and test your understanding

### Quality Documentation

1. **Clear Structure**: Organize logically
2. **Visual Aids**: Diagrams help understanding
3. **Examples**: Show, don't just tell
4. **Concise**: Respect reader's time
5. **Actionable**: Provide next steps

## Conclusion

The research skill helps you systematically explore and understand codebases, libraries, APIs, and technical solutions. By following structured methodologies, using effective tools, and documenting findings clearly, you can quickly build understanding of unfamiliar systems and make informed technical decisions.

Whether you're exploring a new codebase, evaluating libraries, researching APIs, or investigating solutions to technical problems, systematic research saves time, reduces risk, and leads to better outcomes.
