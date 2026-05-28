---
name: test
description: Create comprehensive test suites with unit tests, integration tests, and e2e tests following best practices for coverage, maintainability, and reliability. Use when writing tests for new code, improving test coverage, or establishing testing strategies.
---

# Test

A skill for creating comprehensive, maintainable test suites that ensure code quality, prevent regressions, and enable confident refactoring.

## Overview

This skill helps you:

- Write effective unit tests for functions and classes
- Create integration tests for module interactions
- Build end-to-end tests for user workflows
- Follow testing best practices and patterns
- Achieve meaningful test coverage
- Test edge cases and error conditions
- Mock dependencies appropriately
- Structure tests for maintainability

## Core Capabilities

### 1. Unit Testing

Test individual functions and components in isolation:

- **Pure Functions**: Test inputs → outputs
- **Classes**: Test methods and state changes
- **Components**: Test rendering and behavior
- **Edge Cases**: Test boundary conditions
- **Error Handling**: Test error scenarios
- **Mocking**: Isolate units from dependencies

### 2. Integration Testing

Test how modules work together:

- **Module Interactions**: Test interfaces between components
- **Database Operations**: Test queries and transactions
- **API Endpoints**: Test request/response handling
- **State Management**: Test state changes across components
- **Service Integration**: Test multiple services working together

### 3. End-to-End Testing

Test complete user workflows:

- **User Journeys**: Test realistic user scenarios
- **Critical Paths**: Test essential business flows
- **Cross-Browser**: Test across different browsers
- **Real Environment**: Test against actual (or staging) backend
- **User Interactions**: Test clicks, forms, navigation

### 4. Test Organization

Structure tests effectively:

- **AAA Pattern**: Arrange, Act, Assert
- **Descriptive Names**: Clear test descriptions
- **One Assertion Focus**: Each test validates one thing
- **Test Isolation**: Tests don't depend on each other
- **Setup/Teardown**: Proper test fixture management

### 5. Test Coverage

Measure and improve coverage:

- **Line Coverage**: Which lines are executed
- **Branch Coverage**: Which branches are taken
- **Function Coverage**: Which functions are called
- **Meaningful Coverage**: Test important behaviors, not just lines
- **Coverage Gaps**: Identify untested code

### 6. Test Maintenance

Keep tests valuable over time:

- **Refactor Tests**: Keep tests clean like production code
- **Avoid Brittleness**: Tests shouldn't break on minor changes
- **Test Data Management**: Maintain realistic test data
- **Update Tests**: Keep tests current with code changes
- **Remove Obsolete Tests**: Delete tests for removed features

## When to Use This Skill

Use this skill when:

- Writing tests for new features
- Improving coverage for existing code
- Setting up testing infrastructure
- Debugging failing tests
- Refactoring code (tests ensure correctness)
- Fixing bugs (add tests to prevent regression)
- Reviewing code (suggest test improvements)
- Teaching testing practices
- Establishing team testing standards

## Workflow

### Test-Driven Development (TDD)

1. **Write Failing Test**
   - Write test for desired behavior
   - Test fails (red)

2. **Implement Minimal Code**
   - Write just enough code to pass
   - Test passes (green)

3. **Refactor**
   - Improve code quality
   - Tests ensure correctness

4. **Repeat**
   - Continue for next behavior

### Testing Existing Code

1. **Understand the Code**
   - Read implementation
   - Identify behaviors to test
   - Note edge cases

2. **Write Tests**
   - Start with happy path
   - Add edge cases
   - Add error cases
   - Test boundary conditions

3. **Verify Coverage**
   - Run coverage report
   - Identify gaps
   - Add missing tests

4. **Refactor**
   - Improve test quality
   - Remove duplication
   - Enhance readability

## Testing Patterns

### AAA Pattern (Arrange-Act-Assert)

```javascript
test('adds two numbers correctly', () => {
  // Arrange: Set up test data
  const a = 5;
  const b = 3;

  // Act: Execute the code under test
  const result = add(a, b);

  // Assert: Verify the result
  expect(result).toBe(8);
});
```

### Test Isolation

```javascript
// Bad: Tests depend on each other
let user;

test('creates user', () => {
  user = createUser('John');
  expect(user.name).toBe('John');
});

test('updates user', () => {
  updateUser(user, { name: 'Jane' }); // Depends on previous test!
  expect(user.name).toBe('Jane');
});

// Good: Tests are independent
test('creates user', () => {
  const user = createUser('John');
  expect(user.name).toBe('John');
});

test('updates user', () => {
  const user = createUser('John'); // Create fresh user
  updateUser(user, { name: 'Jane' });
  expect(user.name).toBe('Jane');
});
```

### Descriptive Test Names

```javascript
// Bad: Vague test names
test('test 1', () => { /* ... */ });
test('works', () => { /* ... */ });
test('user', () => { /* ... */ });

// Good: Descriptive test names
test('returns null when user not found', () => { /* ... */ });
test('throws error when email is invalid', () => { /* ... */ });
test('calculates total price including tax', () => { /* ... */ });
```

## Unit Testing Examples

### Testing Pure Functions

```javascript
// Function to test
function calculateDiscount(price, discountPercent) {
  if (price < 0 || discountPercent < 0 || discountPercent > 100) {
    throw new Error('Invalid input');
  }
  return price * (1 - discountPercent / 100);
}

// Tests
describe('calculateDiscount', () => {
  test('calculates 10% discount correctly', () => {
    expect(calculateDiscount(100, 10)).toBe(90);
  });

  test('calculates 50% discount correctly', () => {
    expect(calculateDiscount(200, 50)).toBe(100);
  });

  test('returns original price with 0% discount', () => {
    expect(calculateDiscount(100, 0)).toBe(100);
  });

  test('returns 0 with 100% discount', () => {
    expect(calculateDiscount(100, 100)).toBe(0);
  });

  test('throws error for negative price', () => {
    expect(() => calculateDiscount(-10, 10)).toThrow('Invalid input');
  });

  test('throws error for discount over 100%', () => {
    expect(() => calculateDiscount(100, 150)).toThrow('Invalid input');
  });

  test('throws error for negative discount', () => {
    expect(() => calculateDiscount(100, -10)).toThrow('Invalid input');
  });
});
```

### Testing Classes

```javascript
// Class to test
class Counter {
  constructor(initialValue = 0) {
    this.value = initialValue;
  }

  increment() {
    this.value++;
  }

  decrement() {
    this.value--;
  }

  reset() {
    this.value = 0;
  }
}

// Tests
describe('Counter', () => {
  test('initializes with 0 by default', () => {
    const counter = new Counter();
    expect(counter.value).toBe(0);
  });

  test('initializes with provided value', () => {
    const counter = new Counter(5);
    expect(counter.value).toBe(5);
  });

  test('increments value', () => {
    const counter = new Counter();
    counter.increment();
    expect(counter.value).toBe(1);
  });

  test('decrements value', () => {
    const counter = new Counter(5);
    counter.decrement();
    expect(counter.value).toBe(4);
  });

  test('resets to 0', () => {
    const counter = new Counter(10);
    counter.reset();
    expect(counter.value).toBe(0);
  });

  test('handles multiple operations', () => {
    const counter = new Counter();
    counter.increment();
    counter.increment();
    counter.decrement();
    expect(counter.value).toBe(1);
  });
});
```

### Testing React Components

```jsx
// Component to test
function Greeting({ name, isLoading }) {
  if (isLoading) {
    return <div>Loading...</div>;
  }

  return <div>Hello, {name}!</div>;
}

// Tests
import { render, screen } from '@testing-library/react';

describe('Greeting', () => {
  test('renders greeting with name', () => {
    render(<Greeting name="John" />);
    expect(screen.getByText('Hello, John!')).toBeInTheDocument();
  });

  test('shows loading state', () => {
    render(<Greeting name="John" isLoading={true} />);
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });

  test('does not show name when loading', () => {
    render(<Greeting name="John" isLoading={true} />);
    expect(screen.queryByText('Hello, John!')).not.toBeInTheDocument();
  });
});
```

### Testing Async Functions

```javascript
// Async function to test
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) {
    throw new Error('User not found');
  }
  return response.json();
}

// Tests
describe('fetchUser', () => {
  test('fetches user successfully', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ id: 1, name: 'John' }),
      })
    );

    const user = await fetchUser(1);

    expect(user).toEqual({ id: 1, name: 'John' });
    expect(fetch).toHaveBeenCalledWith('/api/users/1');
  });

  test('throws error when user not found', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: false,
      })
    );

    await expect(fetchUser(999)).rejects.toThrow('User not found');
  });
});
```

## Mocking and Stubbing

### Mocking Dependencies

```javascript
// Module with dependency
import { database } from './database';

export async function getUser(id) {
  return await database.findUser(id);
}

// Test with mock
import { getUser } from './user-service';
import { database } from './database';

jest.mock('./database');

describe('getUser', () => {
  test('returns user from database', async () => {
    // Mock the database response
    database.findUser.mockResolvedValue({ id: 1, name: 'John' });

    const user = await getUser(1);

    expect(user).toEqual({ id: 1, name: 'John' });
    expect(database.findUser).toHaveBeenCalledWith(1);
  });
});
```

### Spy on Functions

```javascript
// Test that a function is called
const logger = {
  log: jest.fn(),
  error: jest.fn(),
};

function processData(data) {
  logger.log('Processing data');
  if (!data) {
    logger.error('No data provided');
    return null;
  }
  return data.toUpperCase();
}

test('logs when processing data', () => {
  processData('hello');
  expect(logger.log).toHaveBeenCalledWith('Processing data');
});

test('logs error when no data', () => {
  processData(null);
  expect(logger.error).toHaveBeenCalledWith('No data provided');
});
```

### Mocking Timers

```javascript
// Function using setTimeout
function delayedGreeting(name, callback) {
  setTimeout(() => {
    callback(`Hello, ${name}!`);
  }, 1000);
}

// Test with fake timers
jest.useFakeTimers();

test('calls callback after delay', () => {
  const callback = jest.fn();

  delayedGreeting('John', callback);

  // Callback not called yet
  expect(callback).not.toHaveBeenCalled();

  // Fast-forward time
  jest.runAllTimers();

  // Now callback called
  expect(callback).toHaveBeenCalledWith('Hello, John!');
});
```

## Integration Testing

### Testing API Endpoints

```javascript
// Express API endpoint
app.post('/api/users', async (req, res) => {
  const { name, email } = req.body;

  if (!name || !email) {
    return res.status(400).json({ error: 'Name and email required' });
  }

  const user = await database.createUser({ name, email });
  res.status(201).json(user);
});

// Integration test
import request from 'supertest';
import app from './app';

describe('POST /api/users', () => {
  test('creates user successfully', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'john@example.com' });

    expect(response.status).toBe(201);
    expect(response.body).toMatchObject({
      name: 'John',
      email: 'john@example.com',
    });
  });

  test('returns 400 when name missing', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'john@example.com' });

    expect(response.status).toBe(400);
    expect(response.body.error).toBe('Name and email required');
  });
});
```

### Testing Database Operations

```javascript
// Database function
async function createUser(userData) {
  const user = await db.users.create(userData);
  return user;
}

// Integration test
describe('createUser', () => {
  beforeEach(async () => {
    // Clear database before each test
    await db.users.deleteMany({});
  });

  test('creates user in database', async () => {
    const userData = { name: 'John', email: 'john@example.com' };
    const user = await createUser(userData);

    expect(user.id).toBeDefined();
    expect(user.name).toBe('John');
    expect(user.email).toBe('john@example.com');

    // Verify in database
    const dbUser = await db.users.findById(user.id);
    expect(dbUser).toBeTruthy();
  });
});
```

## End-to-End Testing

### Testing User Workflows (Playwright)

```javascript
import { test, expect } from '@playwright/test';

test('user can sign up and log in', async ({ page }) => {
  // Navigate to sign up page
  await page.goto('/signup');

  // Fill out sign up form
  await page.fill('input[name="email"]', 'test@example.com');
  await page.fill('input[name="password"]', 'SecurePass123');
  await page.fill('input[name="confirmPassword"]', 'SecurePass123');

  // Submit form
  await page.click('button[type="submit"]');

  // Verify redirect to dashboard
  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('h1')).toContainText('Welcome');

  // Log out
  await page.click('button[aria-label="Logout"]');

  // Verify redirect to home
  await expect(page).toHaveURL('/');

  // Log back in
  await page.goto('/login');
  await page.fill('input[name="email"]', 'test@example.com');
  await page.fill('input[name="password"]', 'SecurePass123');
  await page.click('button[type="submit"]');

  // Verify logged in
  await expect(page).toHaveURL('/dashboard');
});
```

### Testing Form Validation

```javascript
test('shows validation errors', async ({ page }) => {
  await page.goto('/signup');

  // Submit empty form
  await page.click('button[type="submit"]');

  // Verify error messages
  await expect(page.locator('text=Email is required')).toBeVisible();
  await expect(page.locator('text=Password is required')).toBeVisible();

  // Fill invalid email
  await page.fill('input[name="email"]', 'invalid-email');
  await page.click('button[type="submit"]');

  // Verify email error
  await expect(page.locator('text=Please enter a valid email')).toBeVisible();
});
```

## Test Coverage

### Measuring Coverage

```bash
# JavaScript (Jest)
npm test -- --coverage

# Python (pytest with coverage)
pytest --cov=myapp tests/

# Coverage report shows:
# - Line coverage: % of lines executed
# - Branch coverage: % of branches taken
# - Function coverage: % of functions called
```

### Interpreting Coverage

```
File          | % Stmts | % Branch | % Funcs | % Lines |
--------------|---------|----------|---------|---------|
user.js       |   85.71 |    66.67 |     100 |   85.71 |
database.js   |     100 |      100 |     100 |     100 |
```

**Analysis:**
- `user.js`: Good statement/line coverage, but branch coverage could improve
- Missing branches likely in conditional logic (if/else not fully tested)
- `database.js`: Fully covered

### Meaningful Coverage

```javascript
// Bad: 100% coverage but tests nothing meaningful
function add(a, b) {
  return a + b;
}

test('add function exists', () => {
  expect(add).toBeDefined(); // Useless test
});

// Good: Tests actual behavior
test('adds two numbers correctly', () => {
  expect(add(2, 3)).toBe(5);
  expect(add(-1, 1)).toBe(0);
  expect(add(0, 0)).toBe(0);
});
```

## Framework-Specific Patterns

### Jest (JavaScript)

```javascript
describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  test('adds numbers', () => {
    expect(calculator.add(2, 3)).toBe(5);
  });

  test('subtracts numbers', () => {
    expect(calculator.subtract(5, 3)).toBe(2);
  });
});
```

### pytest (Python)

```python
import pytest

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add(self, calculator):
        assert calculator.add(2, 3) == 5

    def test_subtract(self, calculator):
        assert calculator.subtract(5, 3) == 2

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)
```

### RSpec (Ruby)

```ruby
RSpec.describe Calculator do
  let(:calculator) { Calculator.new }

  describe '#add' do
    it 'adds two numbers' do
      expect(calculator.add(2, 3)).to eq(5)
    end
  end

  describe '#divide' do
    it 'raises error when dividing by zero' do
      expect { calculator.divide(10, 0) }.to raise_error(ZeroDivisionError)
    end
  end
end
```

## Testing Best Practices

### Do's

- **Test behavior, not implementation**: Test what code does, not how
- **One assertion per test**: Focus each test on one thing
- **Use descriptive names**: Test names should explain what they test
- **Test edge cases**: Boundary values, null, empty, large inputs
- **Keep tests simple**: Tests should be easier than production code
- **Make tests fast**: Slow tests discourage running them
- **Isolate tests**: Tests should not depend on each other
- **Use meaningful data**: Test data should be realistic

### Don'ts

- **Don't test private methods**: Test public interface
- **Don't test framework code**: Trust the framework
- **Don't repeat production logic**: Don't duplicate implementation
- **Don't make tests brittle**: Avoid tight coupling to implementation
- **Don't skip error cases**: Test failures, not just success
- **Don't hardcode values**: Use variables for clarity
- **Don't write flaky tests**: Tests should be deterministic

## Common Pitfalls

### Testing Implementation Details

```javascript
// Bad: Tests implementation
test('updates state variable', () => {
  const component = new Component();
  component.handleClick();
  expect(component._internalState).toBe(true); // Testing internals
});

// Good: Tests behavior
test('shows success message after click', () => {
  render(<Component />);
  fireEvent.click(screen.getByRole('button'));
  expect(screen.getByText('Success!')).toBeInTheDocument();
});
```

### Brittletle Tests

```javascript
// Bad: Breaks on any HTML change
expect(container.innerHTML).toBe('<div class="greeting">Hello, John</div>');

// Good: Tests meaningful behavior
expect(screen.getByText('Hello, John')).toBeInTheDocument();
```

### Test Data Pollution

```javascript
// Bad: Tests affect each other
let users = [];

test('adds user', () => {
  users.push({ name: 'John' });
  expect(users.length).toBe(1);
});

test('counts users', () => {
  expect(users.length).toBe(0); // Fails! Previous test polluted data
});

// Good: Clean state for each test
let users;

beforeEach(() => {
  users = [];
});

test('adds user', () => {
  users.push({ name: 'John' });
  expect(users.length).toBe(1);
});

test('counts users', () => {
  expect(users.length).toBe(0); // Passes
});
```

## Test Pyramid

```
        /\
       /  \
      / E2E \        Few: Slow, expensive, fragile
     /______\
    /        \
   /Integration\     Some: Test module interactions
  /____________\
 /              \
/  Unit Tests    \   Many: Fast, cheap, focused
/________________\
```

**Guidelines:**
- **Many unit tests**: Fast, focused, test individual units
- **Some integration tests**: Test module interactions
- **Few E2E tests**: Test critical user journeys

## Accessibility Testing

```javascript
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

test('has no accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

## Visual Regression Testing

```javascript
// Using Percy or Chromatic
test('matches visual snapshot', async ({ page }) => {
  await page.goto('/');
  await percySnapshot(page, 'Homepage');
});
```

## Performance Testing

```javascript
test('renders large list efficiently', () => {
  const items = Array.from({ length: 10000 }, (_, i) => ({ id: i }));

  const start = performance.now();
  render(<ItemList items={items} />);
  const duration = performance.now() - start;

  expect(duration).toBeLessThan(1000); // Should render in < 1 second
});
```

## Communication with Users

When working with users on tests:

- **Understand requirements**: What behavior needs testing?
- **Clarify edge cases**: What should happen when...?
- **Discuss coverage goals**: What coverage % is appropriate?
- **Explain trade-offs**: Test speed vs thoroughness
- **Show value**: How tests prevent bugs and enable refactoring
- **Teach patterns**: Share testing best practices

## Conclusion

The test skill helps you create comprehensive, maintainable test suites that ensure code quality and prevent regressions. By following best practices for unit, integration, and E2E testing, you can build confidence in your code and ship with fewer bugs.

Remember: tests are an investment. They take time upfront but save time in the long run by catching bugs early, enabling refactoring, and documenting expected behavior.
