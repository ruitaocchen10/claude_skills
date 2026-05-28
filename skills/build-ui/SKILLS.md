---
name: build-ui
description: Build user interfaces from designs, mockups, or descriptions with best practices for structure, accessibility, and responsiveness. Use when implementing UI components, converting designs to code, or creating layouts from scratch.
---

# Build UI

A skill for implementing user interfaces from designs, specifications, or descriptions with a focus on semantic HTML, accessibility, responsiveness, and modern best practices.

## Overview

This skill helps you:

- Convert designs and mockups into production-ready code
- Build responsive, mobile-first layouts
- Implement accessible UI components
- Structure semantic, maintainable HTML/JSX
- Create reusable component architectures
- Handle forms with validation
- Optimize UI performance

## Core Capabilities

### 1. Design to Code Conversion

Transform designs into implementation:

- **Analyze Designs**: Extract spacing, typography, colors, components
- **Identify Patterns**: Spot reusable components and layouts
- **Implement Faithfully**: Match design specifications precisely
- **Handle Edge Cases**: Account for long text, missing images, errors
- **Responsive Behavior**: Adapt layouts across screen sizes
- **Interactive States**: Implement hover, focus, active, disabled states

### 2. Semantic HTML Structure

Build accessible, well-structured markup:

- **Semantic Elements**: Use appropriate HTML5 elements (header, nav, main, article, aside, footer)
- **Heading Hierarchy**: Proper h1-h6 structure
- **Lists**: Use ul/ol for lists, not divs
- **Forms**: Proper label/input associations, fieldsets
- **ARIA**: Add ARIA attributes when semantic HTML isn't enough
- **Landmark Regions**: Define page regions for screen readers

### 3. Responsive Design

Create layouts that work across devices:

- **Mobile-First**: Start with mobile layout, enhance for larger screens
- **Flexible Grids**: Use flexbox and grid for fluid layouts
- **Responsive Images**: Proper srcset, sizes, and lazy loading
- **Breakpoints**: Strategic breakpoints based on content
- **Touch Targets**: Minimum 44x44px for interactive elements
- **Viewport Meta**: Proper viewport configuration

### 4. Accessibility (A11y)

Build interfaces everyone can use:

- **Keyboard Navigation**: Full keyboard support (Tab, Enter, Space, Arrows)
- **Focus Management**: Visible focus indicators, logical tab order
- **Screen Readers**: Proper ARIA labels and announcements
- **Color Contrast**: WCAG AA compliance (4.5:1 for text, 3:1 for UI)
- **Alternative Text**: Descriptive alt text for images
- **Error Handling**: Clear, accessible error messages
- **Skip Links**: Allow skipping to main content

### 5. Component Patterns

Implement common UI patterns:

- **Buttons**: Primary, secondary, tertiary, destructive variants
- **Forms**: Inputs, textareas, selects, checkboxes, radios
- **Navigation**: Headers, navbars, breadcrumbs, tabs
- **Modals & Dialogs**: Accessible overlays with focus trapping
- **Tooltips & Popovers**: Contextual information displays
- **Cards**: Content containers with consistent structure
- **Lists & Tables**: Data display components
- **Loading States**: Skeletons, spinners, progress indicators

### 6. Performance Optimization

Build fast, efficient UIs:

- **Lazy Loading**: Load images and components on demand
- **Code Splitting**: Split bundles for faster initial load
- **Virtualization**: Render only visible items in long lists
- **Memoization**: Prevent unnecessary re-renders
- **Debouncing/Throttling**: Optimize event handlers
- **Critical CSS**: Inline critical styles
- **Resource Hints**: Preload, prefetch, preconnect

## When to Use This Skill

Use this skill when:

- Converting Figma, Sketch, or Adobe XD designs to code
- Building UI from wireframes or mockups
- Implementing component libraries
- Creating landing pages or marketing sites
- Building application interfaces
- Prototyping user interfaces quickly
- Refactoring existing UI for better accessibility or responsiveness
- Teaching UI implementation best practices

## Workflow

### Converting Design to Code

1. **Analyze the Design**
   - Identify components and their variants
   - Extract design tokens (colors, spacing, typography)
   - Note responsive behavior and breakpoints
   - Identify interactive states
   - Check for accessibility requirements

2. **Plan Component Structure**
   - Decide on component hierarchy
   - Identify reusable components
   - Plan props/API for configurability
   - Consider state management needs

3. **Implement Markup**
   - Start with semantic HTML structure
   - Use appropriate elements for content
   - Add ARIA attributes where needed
   - Ensure proper heading hierarchy

4. **Apply Styles**
   - Implement mobile-first responsive styles
   - Match design specifications precisely
   - Handle all interactive states
   - Ensure accessibility (contrast, focus indicators)

5. **Add Interactivity**
   - Implement event handlers
   - Add keyboard navigation
   - Manage focus states
   - Handle loading and error states

6. **Test & Refine**
   - Test across browsers and devices
   - Verify keyboard navigation
   - Test with screen readers
   - Check color contrast
   - Validate HTML

### Building from Description

1. **Clarify Requirements**
   - Understand the purpose and use cases
   - Identify required functionality
   - Determine target devices
   - Check for accessibility needs

2. **Choose Appropriate Patterns**
   - Select suitable UI patterns
   - Consider established conventions
   - Ensure consistency with existing UI

3. **Implement & Iterate**
   - Build initial version
   - Gather feedback
   - Refine based on usage

## HTML Structure Best Practices

### Semantic Markup Example

```html
<!-- Good: Semantic HTML -->
<article>
  <header>
    <h2>Article Title</h2>
    <p class="metadata">By Author Name • January 1, 2024</p>
  </header>

  <div class="content">
    <p>Article content...</p>
  </div>

  <footer>
    <button type="button">Like</button>
    <button type="button">Share</button>
  </footer>
</article>

<!-- Bad: Div soup -->
<div class="article">
  <div class="header">
    <div class="title">Article Title</div>
    <div class="metadata">By Author Name • January 1, 2024</div>
  </div>

  <div class="content">
    <div class="paragraph">Article content...</div>
  </div>

  <div class="footer">
    <div class="like-button">Like</div>
    <div class="share-button">Share</div>
  </div>
</div>
```

### Form Accessibility

```html
<!-- Accessible form -->
<form>
  <div class="form-field">
    <label for="email">Email Address</label>
    <input
      type="email"
      id="email"
      name="email"
      aria-describedby="email-hint email-error"
      aria-invalid="false"
      required
    />
    <p id="email-hint" class="hint">We'll never share your email</p>
    <p id="email-error" class="error" role="alert" aria-live="polite">
      <!-- Error message appears here -->
    </p>
  </div>

  <button type="submit">Sign Up</button>
</form>
```

### Navigation Structure

```html
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/" aria-current="page">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/services">Services</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>
</header>
```

## Responsive Design Patterns

### Mobile-First CSS

```css
/* Base styles (mobile) */
.container {
  padding: 16px;
}

.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

/* Tablet (640px+) */
@media (min-width: 640px) {
  .container {
    padding: 24px;
  }

  .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
  }

  .grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
  }
}
```

### Fluid Typography

```css
/* Responsive font sizes using clamp */
h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
}

p {
  font-size: clamp(1rem, 2.5vw, 1.125rem);
}
```

### Responsive Images

```html
<picture>
  <source
    media="(min-width: 1024px)"
    srcset="hero-large.jpg"
  />
  <source
    media="(min-width: 640px)"
    srcset="hero-medium.jpg"
  />
  <img
    src="hero-small.jpg"
    alt="Description of image"
    loading="lazy"
    width="800"
    height="600"
  />
</picture>
```

## Component Implementation Examples

### Button Component (React)

```jsx
// Accessible, flexible button component
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'tertiary' | 'destructive';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
}

export function Button({
  variant = 'primary',
  size = 'md',
  loading = false,
  disabled = false,
  children,
  onClick,
  type = 'button',
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`btn btn-${variant} btn-${size}`}
      onClick={onClick}
      disabled={disabled || loading}
      aria-busy={loading}
    >
      {loading && <Spinner aria-hidden="true" />}
      <span>{children}</span>
    </button>
  );
}
```

### Modal Component (React)

```jsx
// Accessible modal with focus trapping
export function Modal({ isOpen, onClose, title, children }) {
  const modalRef = useRef(null);

  // Focus trap
  useEffect(() => {
    if (!isOpen) return;

    const modal = modalRef.current;
    const focusableElements = modal.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];

    firstElement?.focus();

    function handleTab(e) {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        }
      } else {
        if (document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
    }

    modal.addEventListener('keydown', handleTab);
    return () => modal.removeEventListener('keydown', handleTab);
  }, [isOpen]);

  // Close on Escape
  useEffect(() => {
    function handleEscape(e) {
      if (e.key === 'Escape') onClose();
    }

    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      return () => document.removeEventListener('keydown', handleEscape);
    }
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="modal-overlay"
      onClick={onClose}
      role="presentation"
    >
      <div
        ref={modalRef}
        className="modal"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
      >
        <header className="modal-header">
          <h2 id="modal-title">{title}</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close modal"
            className="modal-close"
          >
            <CloseIcon aria-hidden="true" />
          </button>
        </header>

        <div className="modal-body">
          {children}
        </div>
      </div>
    </div>
  );
}
```

### Form with Validation (React)

```jsx
export function SignUpForm() {
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});

  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const email = formData.get('email');
    const password = formData.get('password');

    const newErrors = {};

    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!validateEmail(email)) {
      newErrors.email = 'Please enter a valid email';
    }

    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      // Submit form
    }
  }

  return (
    <form onSubmit={handleSubmit} noValidate>
      <div className="form-field">
        <label htmlFor="email">Email</label>
        <input
          type="email"
          id="email"
          name="email"
          aria-describedby="email-error"
          aria-invalid={!!errors.email}
          onBlur={() => setTouched({ ...touched, email: true })}
        />
        {touched.email && errors.email && (
          <p id="email-error" className="error" role="alert">
            {errors.email}
          </p>
        )}
      </div>

      <div className="form-field">
        <label htmlFor="password">Password</label>
        <input
          type="password"
          id="password"
          name="password"
          aria-describedby="password-error password-hint"
          aria-invalid={!!errors.password}
          onBlur={() => setTouched({ ...touched, password: true })}
        />
        <p id="password-hint" className="hint">
          At least 8 characters
        </p>
        {touched.password && errors.password && (
          <p id="password-error" className="error" role="alert">
            {errors.password}
          </p>
        )}
      </div>

      <button type="submit">Sign Up</button>
    </form>
  );
}
```

## Accessibility Checklist

### Keyboard Navigation

- [ ] All interactive elements accessible via Tab
- [ ] Logical tab order (matches visual flow)
- [ ] Enter/Space activates buttons and links
- [ ] Arrow keys navigate menus and lists
- [ ] Escape closes modals and dropdowns
- [ ] No keyboard traps

### Focus Management

- [ ] Visible focus indicators on all interactive elements
- [ ] Focus indicators have 3:1 contrast minimum
- [ ] Focus moves logically through interface
- [ ] Focus trapped in modals
- [ ] Focus restored when closing modals/menus

### Screen Reader Support

- [ ] All images have appropriate alt text
- [ ] Form inputs have associated labels
- [ ] Error messages announced with aria-live
- [ ] Loading states announced
- [ ] Page title describes content
- [ ] Heading hierarchy is logical
- [ ] Landmark regions defined

### Color & Contrast

- [ ] Text has 4.5:1 contrast (normal) or 3:1 (large)
- [ ] UI components have 3:1 contrast
- [ ] Information not conveyed by color alone
- [ ] Focus indicators visible for all users

### Content

- [ ] Language declared in HTML
- [ ] Content is readable and understandable
- [ ] Link text is descriptive
- [ ] Error messages are clear and helpful

## Performance Optimization

### Image Optimization

```jsx
// Lazy load images
<img
  src="image.jpg"
  alt="Description"
  loading="lazy"
  width="800"
  height="600"
/>

// Responsive images
<img
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w
  "
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 800px"
  src="image-800.jpg"
  alt="Description"
/>
```

### Code Splitting (React)

```jsx
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <HeavyComponent />
    </Suspense>
  );
}
```

### Virtualized Lists (React)

```jsx
import { FixedSizeList } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}
```

## Framework-Specific Patterns

### React

- Component composition
- Hooks for state and effects
- Context for shared state
- Prop drilling vs state management
- Controlled vs uncontrolled components

### Vue

- Single-file components
- Composition API vs Options API
- V-model for two-way binding
- Slots for content distribution
- Composables for reusable logic

### Svelte

- Reactive declarations
- Stores for shared state
- Transitions and animations
- Two-way binding
- Compile-time optimization

### Vanilla JS

- Web Components
- Custom Elements
- Shadow DOM for encapsulation
- Template literals for markup
- Event delegation

## Common Pitfalls to Avoid

### Accessibility

- Missing alt text on images
- Poor color contrast
- No keyboard navigation
- Inaccessible modals (no focus trap)
- Divs/spans as buttons (use button element)
- Missing form labels
- No skip links

### HTML

- Non-semantic markup (div soup)
- Incorrect heading hierarchy
- Missing lang attribute
- Inline styles (hard to maintain)
- Missing viewport meta tag

### CSS

- Desktop-first (should be mobile-first)
- Fixed pixel widths (use relative units)
- !important overuse
- Deeply nested selectors
- No fallbacks for modern features

### Performance

- Not lazy loading images
- Loading all JavaScript upfront
- No code splitting
- Not optimizing images
- Blocking rendering with scripts

### Responsive Design

- Not testing on real devices
- Assuming viewport sizes
- Fixed heights breaking layouts
- Tiny touch targets on mobile
- Horizontal scrolling on mobile

## Testing UI Components

### Visual Testing

- Test across browsers (Chrome, Firefox, Safari, Edge)
- Test on real devices (iOS, Android)
- Test at different viewport sizes
- Test with browser zoom (up to 200%)
- Test in high contrast mode

### Accessibility Testing

- Automated testing (axe, Lighthouse, Pa11y)
- Keyboard navigation testing
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Color contrast checking
- HTML validation

### Functional Testing

- User interactions work correctly
- Forms validate properly
- Error states display correctly
- Loading states appear/disappear
- Animations complete without jank

## Communication with Users

When building UI for users:

- **Clarify Requirements**: Understand the use case and constraints
- **Show Previews**: Share work-in-progress for feedback
- **Explain Decisions**: Why certain patterns or approaches
- **Flag Accessibility**: Highlight a11y features implemented
- **Discuss Trade-offs**: Performance vs features, complexity vs maintainability
- **Iterate**: Expect refinement based on real usage

## Conclusion

The build-ui skill helps you create high-quality user interfaces that are accessible, responsive, performant, and maintainable. Use it whenever you're converting designs to code, building components from scratch, or implementing UI features.

By following semantic HTML practices, accessibility guidelines, mobile-first responsive design, and modern performance optimizations, you'll build interfaces that work well for all users across all devices.
