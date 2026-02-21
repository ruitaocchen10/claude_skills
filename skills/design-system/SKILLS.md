---
name: design-system
description: Create and maintain design systems with components, tokens, documentation, and guidelines. Use when building a UI component library, establishing design standards, or documenting visual language across projects.
---

# Design System

A skill for creating comprehensive design systems that establish consistent visual language, component libraries, and design guidelines across products and platforms.

## Overview

This skill helps you:

- Create design token systems (colors, typography, spacing, etc.)
- Document UI components with specifications and variants
- Establish accessibility standards and guidelines
- Build style guides with usage examples
- Generate cross-platform design assets
- Maintain design-code synchronization

## Core Capabilities

### 1. Design Tokens

Create systematic, scalable design tokens:

- **Color Systems**: Primitive and semantic color palettes with accessibility considerations
- **Typography Scales**: Font families, sizes, weights, line heights, and hierarchies
- **Spacing Systems**: Consistent spacing scales for layout and components
- **Elevation & Shadows**: Shadow tokens for depth and layering
- **Border Radius**: Corner radius scales for component styling
- **Animation**: Duration, easing, and motion tokens
- **Breakpoints**: Responsive design breakpoints

### 2. Component Specifications

Document components comprehensively:

- **Anatomy**: Visual breakdown of component parts
- **Variants**: Different states and configurations
- **States**: Default, hover, focus, active, disabled, error, loading
- **Props/API**: Component interface and configuration options
- **Usage Guidelines**: When to use, best practices, do's and don'ts
- **Accessibility**: ARIA patterns, keyboard navigation, screen reader support
- **Examples**: Code examples showing common use cases

### 3. Style Guides

Create comprehensive documentation:

- **Design Principles**: Core values guiding design decisions
- **Visual Language**: Photography, illustration, iconography guidelines
- **Voice & Tone**: Content and communication guidelines
- **Patterns**: Common UI patterns and templates
- **Layout Systems**: Grid systems and page templates
- **Responsive Behavior**: How components adapt across screen sizes

## When to Use This Skill

Use this skill when:

- Starting a new product and need consistent design foundation
- Building a component library for reuse across projects
- Establishing design standards for a team or organization
- Migrating from inconsistent UI to systematic design
- Creating white-label or themeable products
- Documenting existing design patterns
- Onboarding designers or developers to design standards
- Synchronizing design tools (Figma, Sketch) with code

## Workflow

### Creating a Design System from Scratch

1. **Define Design Principles**
   - Establish core values (e.g., accessible, efficient, friendly)
   - Document design philosophy
   - Create decision-making framework

2. **Establish Foundation Tokens**
   - Define color palettes (primitive and semantic)
   - Create typography scale
   - Set spacing system
   - Define elevation and shadows
   - Establish border radius scale
   - Set animation tokens

3. **Build Component Library**
   - Identify needed components
   - Document each component thoroughly
   - Create variants and states
   - Build accessibility into every component
   - Provide code examples

4. **Create Documentation**
   - Write style guide
   - Document patterns
   - Create usage examples
   - Build do's and don'ts
   - Add migration guides if replacing old system

5. **Implement Across Platforms**
   - Export tokens to CSS variables, JS constants, mobile formats
   - Build component implementations
   - Create tooling for designers (Figma plugins, etc.)
   - Set up synchronization workflows

### Maintaining an Existing Design System

1. **Audit Current State**
   - Review existing tokens and components
   - Identify inconsistencies
   - Document gaps
   - Note deprecated patterns

2. **Plan Updates**
   - Prioritize improvements
   - Plan migration paths
   - Consider backwards compatibility
   - Version appropriately

3. **Implement Changes**
   - Update tokens
   - Modify components
   - Update documentation
   - Create migration guides

4. **Communicate Updates**
   - Announce changes to team
   - Provide upgrade paths
   - Document breaking changes
   - Offer support during migration

## Design Token Structure

### Primitive Tokens

Base values that are platform-agnostic:

```javascript
// Colors
color.blue.50: '#eff6ff'
color.blue.100: '#dbeafe'
color.blue.500: '#3b82f6'
color.blue.900: '#1e3a8a'

// Spacing
spacing.1: '4px'
spacing.2: '8px'
spacing.4: '16px'
spacing.8: '32px'

// Typography
fontSize.xs: '12px'
fontSize.sm: '14px'
fontSize.base: '16px'
fontSize.lg: '18px'

fontWeight.normal: 400
fontWeight.medium: 500
fontWeight.bold: 700
```

### Semantic Tokens

Purpose-driven tokens that reference primitives:

```javascript
// Semantic colors
color.primary: color.blue.500
color.text.primary: color.gray.900
color.text.secondary: color.gray.600
color.background.primary: color.white
color.border.default: color.gray.300
color.error: color.red.500
color.success: color.green.500

// Semantic spacing
spacing.component.padding: spacing.4
spacing.component.gap: spacing.3
spacing.section.margin: spacing.8

// Component-specific
button.padding.vertical: spacing.2
button.padding.horizontal: spacing.4
button.borderRadius: borderRadius.md
```

## Component Documentation Template

```markdown
# [Component Name]

## Overview

Brief description of the component's purpose and use cases.

## Anatomy

Visual diagram or description of component parts:
- Element 1: Description
- Element 2: Description
- Element 3: Description

## Variants

### [Variant Name]

Description and use case for this variant.

**Example:**
[Code example]

## States

- **Default**: Normal resting state
- **Hover**: Cursor over component
- **Focus**: Keyboard focus or active interaction
- **Active**: Being clicked/pressed
- **Disabled**: Cannot be interacted with
- **Loading**: Async operation in progress
- **Error**: Validation or system error

## Props/API

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | 'primary' \| 'secondary' | 'primary' | Visual style variant |
| size | 'sm' \| 'md' \| 'lg' | 'md' | Component size |
| disabled | boolean | false | Whether component is disabled |

## Accessibility

- **Keyboard Navigation**: [Describe keyboard interactions]
- **Screen Reader**: [Describe ARIA labels and announcements]
- **Focus Management**: [Describe focus behavior]
- **Color Contrast**: Meets WCAG AA standards (4.5:1 minimum)

## Usage Guidelines

### When to Use

- Use case 1
- Use case 2

### When Not to Use

- Anti-pattern 1
- Anti-pattern 2

### Best Practices

- Do: [Recommendation]
- Don't: [Anti-pattern]

## Examples

### Basic Usage

[Code example with explanation]

### Advanced Usage

[Code example with explanation]

## Related Components

- [Component A]: Use when [scenario]
- [Component B]: Use when [scenario]
```

## Token Export Formats

### CSS Variables

```css
:root {
  /* Colors */
  --color-primary: #3b82f6;
  --color-text-primary: #111827;
  --color-background: #ffffff;

  /* Spacing */
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-4: 16px;

  /* Typography */
  --font-size-base: 16px;
  --font-weight-normal: 400;
  --line-height-normal: 1.5;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
}
```

### JavaScript/TypeScript

```typescript
export const tokens = {
  color: {
    primary: '#3b82f6',
    text: {
      primary: '#111827',
      secondary: '#6b7280',
    },
    background: '#ffffff',
  },
  spacing: {
    1: '4px',
    2: '8px',
    4: '16px',
  },
  fontSize: {
    sm: '14px',
    base: '16px',
    lg: '18px',
  },
} as const;

export type ColorToken = keyof typeof tokens.color;
```

### Tailwind Configuration

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
        secondary: '#8b5cf6',
      },
      spacing: {
        '1': '4px',
        '2': '8px',
        '4': '16px',
      },
      fontSize: {
        'xs': '12px',
        'sm': '14px',
        'base': '16px',
      },
    },
  },
};
```

### iOS (Swift)

```swift
extension UIColor {
    static let primary = UIColor(hex: "#3b82f6")
    static let textPrimary = UIColor(hex: "#111827")
    static let backgroundPrimary = UIColor.white
}

extension CGFloat {
    static let spacing1: CGFloat = 4
    static let spacing2: CGFloat = 8
    static let spacing4: CGFloat = 16
}
```

### Android (Kotlin)

```kotlin
object DesignTokens {
    object Color {
        val Primary = Color(0xFF3B82F6)
        val TextPrimary = Color(0xFF111827)
        val BackgroundPrimary = Color.White
    }

    object Spacing {
        val Spacing1 = 4.dp
        val Spacing2 = 8.dp
        val Spacing4 = 16.dp
    }
}
```

## Accessibility Standards

### Color Contrast

Follow WCAG guidelines:

- **Normal text**: Minimum 4.5:1 contrast ratio (AA) or 7:1 (AAA)
- **Large text** (18pt+ or 14pt+ bold): Minimum 3:1 (AA) or 4.5:1 (AAA)
- **UI components**: Minimum 3:1 for interactive elements

### Focus Indicators

- Visible focus states for all interactive elements
- Minimum 3:1 contrast for focus indicators
- At least 2px thick outline or equivalent

### Typography

- Minimum font size 16px for body text (mobile)
- Line height between 1.4-1.6 for readability
- Sufficient spacing between paragraphs
- Support for text resizing up to 200%

### Component Accessibility

Every component should include:

- Proper ARIA roles and labels
- Keyboard navigation support
- Screen reader announcements
- Focus management
- Error messaging

## Theming Strategies

### Single Theme with Customization

Allow token overrides:

```javascript
const theme = createTheme({
  colors: {
    primary: '#3b82f6', // Default
  },
});

// User customization
const customTheme = createTheme({
  colors: {
    primary: '#8b5cf6', // Override
  },
});
```

### Multi-Theme Support

Light and dark modes:

```css
:root {
  --color-background: #ffffff;
  --color-text: #111827;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #ffffff;
}
```

### White-Label Systems

Complete token replacement:

```javascript
const brandATheme = {
  colors: { /* Brand A tokens */ },
  spacing: { /* Brand A tokens */ },
};

const brandBTheme = {
  colors: { /* Brand B tokens */ },
  spacing: { /* Brand B tokens */ },
};
```

## Versioning Design Systems

### Semantic Versioning

- **Major (1.0.0 → 2.0.0)**: Breaking changes (removed components, changed APIs)
- **Minor (1.0.0 → 1.1.0)**: New features (new components, new variants)
- **Patch (1.0.0 → 1.0.1)**: Bug fixes, documentation updates

### Migration Guides

Provide clear upgrade paths:

```markdown
# Migrating from v1 to v2

## Breaking Changes

### Button Component

**Before (v1):**
```jsx
<Button type="primary">Click me</Button>
```

**After (v2):**
```jsx
<Button variant="primary">Click me</Button>
```

**Reason:** Renamed `type` to `variant` for consistency across components.

### Automated Migration

Run this codemod:
```bash
npx @company/codemod button-type-to-variant
```
```

## Documentation Best Practices

1. **Visual Examples**: Show, don't just tell
2. **Live Previews**: Interactive component demos when possible
3. **Code Examples**: Provide copy-paste ready code
4. **Do's and Don'ts**: Visual examples of correct and incorrect usage
5. **Rationale**: Explain why guidelines exist
6. **Search**: Make documentation searchable
7. **Versioning**: Show which version introduced features
8. **Changelog**: Keep detailed change log

## Platform-Specific Considerations

### Web

- Support multiple CSS methodologies (CSS-in-JS, modules, utility-first)
- Provide framework-specific implementations (React, Vue, Svelte)
- Consider bundle size impact
- SSR compatibility
- CSS custom properties for runtime theming

### Mobile (iOS/Android)

- Native token formats
- Platform-specific components (iOS vs Material Design)
- Handle platform differences gracefully
- Support system dark mode
- Consider platform guidelines (HIG, Material Design)

### Desktop

- Larger touch targets may not be needed
- Keyboard navigation critical
- Context menus and right-click patterns
- Window management considerations

## Tools and Integration

### Design Tool Integration

- **Figma**: Use Figma Tokens plugin, Variables API
- **Sketch**: Use Sketch libraries and symbols
- **Adobe XD**: Component libraries and design tokens

### Code Generation

- Generate component boilerplate from specs
- Auto-generate documentation from code
- Sync tokens between design tools and code

### Testing

- Visual regression testing (Chromatic, Percy)
- Accessibility testing (axe, Pa11y)
- Component testing (Storybook)
- Token validation

## Common Patterns

### Atomic Design Methodology

- **Atoms**: Basic building blocks (buttons, inputs)
- **Molecules**: Simple component groups (search form)
- **Organisms**: Complex components (header, card)
- **Templates**: Page layouts
- **Pages**: Specific instances

### Compound Components

Components that work together:

```jsx
<Select>
  <Select.Trigger>Choose an option</Select.Trigger>
  <Select.Menu>
    <Select.Option value="1">Option 1</Select.Option>
    <Select.Option value="2">Option 2</Select.Option>
  </Select.Menu>
</Select>
```

### Composition Patterns

Building complex UIs from simple primitives:

```jsx
<Card>
  <Card.Header>
    <Card.Title>Title</Card.Title>
  </Card.Header>
  <Card.Body>
    Content
  </Card.Body>
  <Card.Footer>
    <Button>Action</Button>
  </Card.Footer>
</Card>
```

## Examples

### Example: Color System

```markdown
# Color System

## Principles

- Accessible: All color combinations meet WCAG AA standards
- Purposeful: Every color has a specific semantic meaning
- Scalable: Multiple shades for flexibility

## Palette Structure

### Primitive Colors

Base color values organized in scales:

- **Gray**: 50, 100, 200, ..., 900 (neutral colors)
- **Blue**: Primary brand color
- **Red**: Error and destructive actions
- **Green**: Success and positive actions
- **Yellow**: Warnings and caution

### Semantic Colors

Purpose-driven color assignments:

| Token | Value | Usage |
|-------|-------|-------|
| color.text.primary | gray.900 | Main body text |
| color.text.secondary | gray.600 | Supporting text |
| color.background.primary | white | Main background |
| color.background.secondary | gray.50 | Subtle background |
| color.border.default | gray.300 | Default borders |
| color.primary | blue.500 | Primary actions |
| color.error | red.500 | Errors |
| color.success | green.500 | Success states |

## Accessibility

All color combinations tested for contrast:

- Text on backgrounds: 4.5:1 minimum
- Interactive elements: 3:1 minimum
- Focus indicators: 3:1 minimum

## Usage

### Do
- Use semantic tokens (color.primary, color.error)
- Ensure sufficient contrast
- Test with color blind simulation

### Don't
- Don't use color alone to convey information
- Don't use primitive tokens directly in components
- Don't create custom colors outside the system
```

### Example: Button Component

```markdown
# Button

## Overview

Buttons trigger actions and events. They're used for forms, dialogs, and to trigger navigation.

## Anatomy

1. Container (background, border, padding)
2. Label text
3. Optional icon (leading or trailing)
4. Optional loading indicator

## Variants

### Primary

For the main action on a page or in a section.

```jsx
<Button variant="primary">Save Changes</Button>
```

### Secondary

For secondary actions that complement the primary action.

```jsx
<Button variant="secondary">Cancel</Button>
```

### Tertiary

For the least prominent actions, or when many actions appear together.

```jsx
<Button variant="tertiary">Learn More</Button>
```

### Destructive

For actions that delete or remove data.

```jsx
<Button variant="destructive">Delete Account</Button>
```

## Sizes

- **sm**: Compact spaces, dense UIs
- **md**: Default size for most use cases
- **lg**: Prominent calls-to-action

## States

- **Default**: Ready for interaction
- **Hover**: Cursor over button
- **Focus**: Keyboard focus visible
- **Active**: Being clicked
- **Disabled**: Cannot be interacted with
- **Loading**: Async action in progress

## Accessibility

- **Keyboard**: Activates with Space or Enter
- **Screen Reader**: Label announced, state conveyed
- **Focus**: Visible focus indicator (2px outline, 3:1 contrast)
- **Disabled**: aria-disabled="true", not keyboard focusable

## Usage Guidelines

### When to Use

- Submitting forms
- Triggering actions (save, delete, create)
- Opening modals or dialogs
- Navigation to important pages

### When Not to Use

- For navigation between pages (use links)
- For opening menus (use menu button)
- For toggling state (use toggle or checkbox)

### Best Practices

- **Do**: Use clear, action-oriented labels ("Save Changes", not "Click Here")
- **Do**: Limit to one primary button per section
- **Do**: Place primary action on the right (in LTR languages)
- **Don't**: Use disabled buttons without explanation
- **Don't**: Make buttons too small (minimum 44x44px touch target)
- **Don't**: Use all caps unless it's part of your brand

## Examples

### With Icon

```jsx
<Button variant="primary" iconLeading={<PlusIcon />}>
  Add Item
</Button>
```

### Loading State

```jsx
<Button variant="primary" loading>
  Saving...
</Button>
```

### Full Width

```jsx
<Button variant="primary" fullWidth>
  Continue
</Button>
```

## Related Components

- **Link Button**: Use Link component styled as a button for navigation
- **Icon Button**: Use for icon-only actions
- **Menu Button**: Use to trigger dropdown menus
```

## Communication with Users

When working with users on design systems:

- **Understand Context**: What platforms? What team size? Existing patterns?
- **Start Small**: Begin with foundations, add components incrementally
- **Prioritize**: Focus on most-used components first
- **Show Examples**: Provide visual and code examples
- **Explain Rationale**: Help them understand why guidelines exist
- **Be Flexible**: Design systems should enable, not constrain
- **Iterate**: Systems evolve based on usage and feedback

## Conclusion

The design-system skill helps you build comprehensive, accessible, and maintainable design systems that scale across products and platforms. Use it to establish consistency, improve development velocity, and create better user experiences through systematic design.

Whether you're creating a new design system from scratch, documenting an existing one, or maintaining and evolving a mature system, this skill provides the structure and best practices to succeed.
