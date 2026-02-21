---
name: debug
description: Systematically diagnose and fix bugs through structured investigation, hypothesis testing, and root cause analysis. Use when encountering errors, unexpected behavior, performance issues, or intermittent failures.
---

# Debug

A skill for systematically diagnosing and fixing bugs using debugging methods, effective tooling, and root cause analysis.

## Overview

This skill helps you:

- Analyze error messages and stack traces effectively
- Reproduce bugs consistently
- Form and test hypotheses about root causes
- Use debugging tools strategically
- Fix bugs at their source (not just symptoms)
- Prevent regressions with tests
- Debug across different environments and platforms

## Core Capabilities

### 1. Error Analysis

Extract maximum information from errors:

- **Read Stack Traces**: Identify the error origin and call path
- **Parse Error Messages**: Understand what the error is telling you
- **Identify Error Types**: Distinguish syntax, runtime, logic, and performance errors
- **Find Error Context**: Locate relevant code and state
- **Spot Patterns**: Recognize common error signatures

### 2. Bug Reproduction

Create reliable reproduction steps:

- **Isolate Variables**: Identify minimal conditions that trigger the bug
- **Create Minimal Reproductions**: Strip away unnecessary complexity
- **Document Steps**: Record exact steps to reproduce
- **Test Consistency**: Verify bug reproduces reliably
- **Capture State**: Record relevant inputs, configuration, environment

### 3. Hypothesis Formation

Apply scientific method to debugging:

- **Observe**: Gather facts about the bug
- **Hypothesize**: Form theories about the root cause
- **Test**: Design experiments to validate or invalidate hypotheses
- **Conclude**: Determine actual cause based on evidence
- **Iterate**: Refine hypothesis if tests disprove it

### 4. Strategic Debugging

Use effective debugging techniques:

- **Binary Search**: Divide and conquer to locate bugs
- **Logging**: Add strategic log statements
- **Breakpoints**: Pause execution at key points
- **Rubber Duck Debugging**: Explain problem to clarify thinking
- **Time-Travel Debugging**: Step backwards through execution
- **Differential Debugging**: Compare working vs broken states

### 5. Root Cause Analysis

Fix the underlying problem:

- **Distinguish Symptoms from Causes**: Don't just patch symptoms
- **Trace to Origin**: Follow the chain of causation
- **Identify Contributing Factors**: Understand the full context
- **Fix Fundamentally**: Address the actual problem
- **Prevent Recurrence**: Add tests, refactor, improve design

### 6. Tool Mastery

Leverage debugging tools effectively:

- **Browser DevTools**: Console, debugger, network, performance profiling
- **IDE Debuggers**: Breakpoints, watch expressions, call stacks
- **Logging Frameworks**: Structured logging with levels
- **Profilers**: CPU, memory, network profiling
- **Monitoring Tools**: Error tracking, performance monitoring
- **Network Analysis**: Request/response inspection, timing

## When to Use This Skill

Use this skill when:

- Encountering error messages or exceptions
- Code behaves unexpectedly
- Tests are failing
- Performance is degraded
- Intermittent bugs appear occasionally
- Production issues need investigation
- Regressions occur after changes
- Code works locally but fails in production
- Memory leaks or resource exhaustion
- Race conditions or timing issues

## Workflow

### The Scientific Debugging Method

1. **Observe**
   - What is the actual behavior?
   - What is the expected behavior?
   - What error messages or symptoms appear?
   - When does the bug occur?
   - What is different between working and broken states?

2. **Reproduce**
   - Find minimal steps to trigger the bug
   - Test reproduction consistency
   - Document exact conditions
   - Capture relevant state and inputs

3. **Isolate**
   - Narrow down to specific code area
   - Remove irrelevant variables
   - Create minimal failing example
   - Identify boundary between working and broken

4. **Hypothesize**
   - Form theories about the cause
   - Consider multiple possibilities
   - Rank hypotheses by likelihood
   - Identify ways to test each hypothesis

5. **Test**
   - Design experiments to test hypotheses
   - Add logging or breakpoints
   - Try potential fixes in isolation
   - Observe results carefully
   - Validate or invalidate hypothesis

6. **Fix**
   - Implement solution addressing root cause
   - Verify fix resolves the bug
   - Ensure no new bugs introduced
   - Add tests to prevent regression
   - Document the issue and solution

7. **Reflect**
   - How could this bug have been prevented?
   - What can we learn for the future?
   - Should architecture be improved?
   - Are similar bugs lurking elsewhere?

## Reading Stack Traces

### Anatomy of a Stack Trace

```
Error: Cannot read property 'name' of undefined
    at getUserDisplayName (user-utils.js:45:18)
    at renderUserCard (components/UserCard.jsx:23:30)
    at App (components/App.jsx:67:12)
    at processChild (react-dom.js:3215:14)
    at resolve (react-dom.js:3014:5)
```

**Reading from top to bottom:**

1. **Error message**: "Cannot read property 'name' of undefined"
   - Trying to access `.name` on `undefined`

2. **Error location**: `user-utils.js:45:18`
   - File: user-utils.js
   - Line: 45
   - Column: 18
   - This is where the error occurred

3. **Call stack**: Shows how we got there
   - `getUserDisplayName` called at user-utils.js:45
   - Called by `renderUserCard` at UserCard.jsx:23
   - Called by `App` at App.jsx:67
   - Called by React internals

**Debugging strategy:**

- Start at the top (error location)
- Look at `user-utils.js` line 45
- Check what's undefined
- Trace back through call stack if needed
- Look at `renderUserCard` to see what it passed to `getUserDisplayName`

### Common Error Types and Meanings

**JavaScript/TypeScript:**

```javascript
// TypeError: Cannot read property 'x' of undefined
// Cause: Trying to access property on undefined/null
const name = user.name; // user is undefined

// ReferenceError: x is not defined
// Cause: Variable doesn't exist in scope
console.log(nonExistentVariable);

// SyntaxError: Unexpected token
// Cause: Invalid syntax
const obj = { key: value }; // Extra comma in some contexts

// RangeError: Maximum call stack size exceeded
// Cause: Infinite recursion
function recurse() {
  recurse();
}
```

**Python:**

```python
# AttributeError: 'NoneType' object has no attribute 'x'
# Cause: Trying to access attribute on None
name = user.name  # user is None

# NameError: name 'x' is not defined
# Cause: Variable doesn't exist
print(non_existent_variable)

# IndexError: list index out of range
# Cause: Accessing invalid list index
item = items[100]  # items has < 100 elements

# KeyError: 'key'
# Cause: Dictionary key doesn't exist
value = dictionary['missing_key']
```

## Debugging Techniques

### Binary Search Debugging

Quickly locate bugs by dividing the search space:

```javascript
// Bug: Function returns wrong result
function processData(data) {
  const cleaned = cleanData(data);
  const validated = validateData(cleaned);
  const transformed = transformData(validated);
  const enriched = enrichData(transformed);
  return formatData(enriched);
}

// Strategy: Check midpoint
function processData(data) {
  const cleaned = cleanData(data);
  const validated = validateData(cleaned);
  const transformed = transformData(validated);
  console.log("After transform:", transformed); // Check midpoint
  const enriched = enrichData(transformed);
  return formatData(enriched);
}

// If transformed is correct, bug is in enrichData or formatData
// If transformed is wrong, bug is in cleanData, validateData, or transformData
// Repeat, dividing search space in half each time
```

### Strategic Logging

Add meaningful log statements:

```javascript
// Poor logging
console.log("here");
console.log("got here too");
console.log(data); // No context

// Good logging
console.log("Processing user data:", { userId, userName: data?.name });
console.log("Validation result:", { isValid, errors });
console.log("Transform input/output:", { input: data, output: transformed });
```

### Breakpoint Debugging

Use debugger strategically:

```javascript
function calculateTotal(items) {
  let total = 0;

  debugger; // Pause here to inspect items

  for (const item of items) {
    // Conditional breakpoint: only pause if item.price > 100
    if (item.price > 100) {
      debugger;
    }

    total += item.price * item.quantity;
  }

  debugger; // Pause here to inspect total

  return total;
}
```

### Rubber Duck Debugging

Explain the problem step-by-step:

1. "This function should calculate the total price..."
2. "It loops through each item..."
3. "Wait, I'm not checking if item.price exists..."
4. "That's the bug!"

Often, explaining the problem reveals the solution.

### Differential Debugging

Compare working vs broken states:

```javascript
// Working state (yesterday's commit)
function processUser(user) {
  return {
    id: user.id,
    name: user.name,
  };
}

// Broken state (current code)
function processUser(user) {
  return {
    id: user.id,
    name: user.profile.name, // user.profile might be undefined!
  };
}

// Difference: Changed user.name to user.profile.name
// Hypothesis: user.profile is sometimes undefined
// Test: Add check for user.profile existence
```

### Time-Travel Debugging

Step backwards through execution:

- Use debugging tools that support time-travel (rr, Chrome DevTools)
- Record execution and replay
- Step backwards to see how state changed
- Understand the sequence leading to the bug

## Common Bug Patterns

### Null/Undefined Errors

```javascript
// Bug: Accessing property on null/undefined
const userName = user.name; // user might be null

// Fix: Optional chaining
const userName = user?.name;

// Fix: Null check
const userName = user ? user.name : "Unknown";

// Fix: Default value
const userName = user?.name ?? "Unknown";
```

### Off-by-One Errors

```javascript
// Bug: Loop goes one too far
for (let i = 0; i <= array.length; i++) {
  // Should be i < array.length
  console.log(array[i]); // Last iteration: array[array.length] is undefined
}

// Fix
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}
```

### Race Conditions

```javascript
// Bug: Async operations complete in unpredictable order
let data = null;

fetchData().then((result) => {
  data = result;
});

// This might run before data is set!
console.log(data); // null

// Fix: Wait for promise
const data = await fetchData();
console.log(data); // Correct value
```

### Type Coercion Issues

```javascript
// Bug: Unexpected type coercion
const result = "5" + 3; // '53' (string concatenation, not 8)
const isEqual = 0 == "0"; // true (loose equality)
const isFalsy = "" == false; // true (both falsy)

// Fix: Use strict equality and explicit conversions
const result = parseInt("5", 10) + 3; // 8
const isEqual = 0 === "0"; // false (strict equality)
const isEmpty = str === ""; // Explicit check
```

### Mutation Bugs

```javascript
// Bug: Unintended mutation
const original = { name: "John", age: 30 };
const updated = original;
updated.age = 31;
console.log(original.age); // 31 (oops! mutated original)

// Fix: Create new object
const updated = { ...original, age: 31 };
console.log(original.age); // 30 (original unchanged)
```

### Closure Issues

```javascript
// Bug: Loop variable captured incorrectly
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 3, 3, 3 (all closures reference same `i`)

// Fix: Use let (block scope)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 0, 1, 2

// Fix: Create new scope with IIFE
for (var i = 0; i < 3; i++) {
  (function (j) {
    setTimeout(() => console.log(j), 100);
  })(i);
}
```

### Memory Leaks

```javascript
// Bug: Event listeners not cleaned up
function createComponent() {
  const element = document.createElement("div");

  element.addEventListener("click", handleClick);

  return element;
}

// If component is removed but listener remains, memory leak!

// Fix: Remove listeners when done
function createComponent() {
  const element = document.createElement("div");

  element.addEventListener("click", handleClick);

  // Cleanup function
  return {
    element,
    destroy() {
      element.removeEventListener("click", handleClick);
    },
  };
}
```

## Tool-Specific Guidance

### Chrome DevTools

**Console:**

- `console.log()` - General logging
- `console.table()` - Display arrays/objects as tables
- `console.trace()` - Show call stack
- `console.time()` / `console.timeEnd()` - Measure execution time
- `console.assert()` - Log if assertion fails

**Debugger:**

- Set breakpoints by clicking line numbers
- Conditional breakpoints: right-click breakpoint, add condition
- Step over (F10), step into (F11), step out (Shift+F11)
- Watch expressions to monitor variables
- Call stack shows execution path

**Network Tab:**

- Monitor HTTP requests
- Check request/response headers
- Inspect payload and response data
- View timing information
- Filter by type, search requests

**Performance Tab:**

- Record runtime performance
- Identify slow functions
- Find layout thrashing
- Analyze frame rate
- Detect memory issues

### VS Code Debugger

**Configuration (.vscode/launch.json):**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Program",
      "program": "${workspaceFolder}/index.js",
      "console": "integratedTerminal"
    }
  ]
}
```

**Features:**

- Breakpoints (click line number)
- Logpoints (log without stopping)
- Conditional breakpoints
- Watch variables
- Debug console for expressions
- Call stack navigation

### Node.js Debugging

```bash
# Start with inspector
node --inspect index.js

# Start and break immediately
node --inspect-brk index.js

# Connect Chrome DevTools
# Open chrome://inspect in Chrome
# Click "inspect" on your process
```

**Debug in code:**

```javascript
debugger; // Breaks when inspector attached
```

### React DevTools

- Inspect component tree
- View props and state
- Trace component updates
- Profile performance
- Identify unnecessary re-renders

### Python Debugger (pdb)

```python
import pdb

def buggy_function(x):
    pdb.set_trace()  # Break here
    result = x * 2
    return result

# Commands:
# n (next) - Execute next line
# s (step) - Step into function
# c (continue) - Continue execution
# p variable - Print variable
# l (list) - Show code context
# q (quit) - Exit debugger
```

## Debugging by Environment

### Local Development

- Use debugger liberally
- Add detailed logging
- Experiment freely
- Use time-travel debugging
- Profile performance

### Staging/QA

- Reproduce production-like conditions
- Check environment differences
- Verify integrations
- Test with production data (sanitized)
- Monitor logs and metrics

### Production

- Use error tracking (Sentry, Rollbar)
- Analyze logs and metrics
- Add temporary logging (carefully)
- Reproduce locally if possible
- Use feature flags to isolate issues
- Avoid debugging in production directly

## Performance Debugging

### Identify Slow Code

```javascript
// Measure execution time
console.time("operation");
expensiveOperation();
console.timeEnd("operation");

// Profile with browser DevTools
// Performance tab → Record → Stop → Analyze
```

### Common Performance Issues

**N+1 Queries:**

```javascript
// Bad: N+1 database queries
for (const user of users) {
  const posts = await db.getPosts(user.id); // Separate query per user
}

// Good: Single query
const allPosts = await db.getPostsForUsers(users.map((u) => u.id));
```

**Inefficient Algorithms:**

```javascript
// Bad: O(n²)
function findDuplicates(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) return true;
    }
  }
  return false;
}

// Good: O(n)
function findDuplicates(arr) {
  const seen = new Set();
  for (const item of arr) {
    if (seen.has(item)) return true;
    seen.add(item);
  }
  return false;
}
```

**Unnecessary Re-renders (React):**

```javascript
// Bad: Creates new object every render
function Parent() {
  const config = { mode: "light" }; // New object each time
  return <Child config={config} />;
}

// Good: Memoize or move outside
const CONFIG = { mode: "light" };

function Parent() {
  return <Child config={CONFIG} />;
}
```

## Debugging Checklist

### Before Debugging

- [ ] Can you reproduce the bug consistently?
- [ ] Do you have the full error message and stack trace?
- [ ] Do you know the expected vs actual behavior?
- [ ] Have you checked recent code changes?
- [ ] Have you searched for similar issues?

### During Debugging

- [ ] Are you using the scientific method?
- [ ] Have you formed a clear hypothesis?
- [ ] Are you testing one variable at a time?
- [ ] Are you checking your assumptions?
- [ ] Are you documenting your findings?

### After Fixing

- [ ] Does the fix address the root cause?
- [ ] Have you tested the fix thoroughly?
- [ ] Have you added tests to prevent regression?
- [ ] Have you checked for similar bugs elsewhere?
- [ ] Have you documented the issue and solution?

## Prevention Strategies

### Defensive Programming

```javascript
// Validate inputs
function divide(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Arguments must be numbers");
  }
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

// Use assertions
function processUser(user) {
  console.assert(user !== null, "User should not be null");
  console.assert(user.id, "User should have an ID");
  // ...
}
```

### Fail Fast

```javascript
// Bad: Fail silently
function getUser(id) {
  try {
    return database.findUser(id);
  } catch (error) {
    return null; // Swallows error
  }
}

// Good: Fail loudly
function getUser(id) {
  return database.findUser(id); // Let error propagate
}
```

### Logging

```javascript
// Structured logging
logger.info("User login", {
  userId: user.id,
  timestamp: new Date(),
  ip: request.ip,
});

// Log levels
logger.debug("Detailed debugging info");
logger.info("General information");
logger.warn("Warning condition");
logger.error("Error condition", { error, context });
```

### Testing

- Write unit tests for individual functions
- Integration tests for component interactions
- E2E tests for critical user flows
- Test edge cases and error conditions
- Maintain high test coverage

## Common Pitfalls

- **Assuming** instead of verifying
- **Changing multiple things** at once
- **Not reproducing** the bug first
- **Fixing symptoms** instead of root causes
- **Not adding tests** after fixing
- **Giving up too quickly** on difficult bugs
- **Not asking for help** when stuck
- **Not documenting** the bug and fix

## Communication

When debugging with others:

- **Share context**: Provide full error messages, steps to reproduce
- **Show your work**: Explain what you've tried
- **Be specific**: "The app crashes when..." not "It doesn't work"
- **Provide code**: Share minimal reproduction
- **Ask focused questions**: "Why does X happen when Y?"
- **Document findings**: Help others who encounter the same bug

## Conclusion

The debug skill provides a systematic approach to finding and fixing bugs. By using the scientific method, strategic tools, and effective techniques, you can debug efficiently and fix issues at their root cause.

Remember: debugging is a skill that improves with practice. The more bugs you fix, the better you become at recognizing patterns, forming hypotheses, and finding solutions quickly.
