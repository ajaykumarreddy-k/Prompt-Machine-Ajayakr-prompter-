# FlowSync — Frontend Prompt

To generate clean, modular React components based on the provided context and instructions, we'll break down each component into its own file with a clear structure. Let's start by defining the `CTASection` component.

### CTASection Component

#### File: CTASection.js

```javascript
import React from 'react';
import { Button } from '../Button/Button'; // Assuming you have a Button component defined elsewhere

const CTASection = ({ title, description, buttonLabel, buttonText }) => {
  return (
    <section className="cta-section">
      <div className="container">
        <h2 className="title">{title}</h2>
        <p className="description">{description}</p>
        <Button
          label={buttonLabel}
          text={buttonText}
          variant="primary"
        />
      </div>
    </section>
  );
};

export default CTASection;
```

### Explanation:

1. **Import Statements**: Import necessary components and styles.
2. **Component Definition**: Define the `CTASection` component as a functional component.
3. **Props**: Accept props for title, description, button label, and button text.
4. **Rendering**:
   - Use a `<section>` element with a class name to style it.
   - Inside the section, use a container div to center content.
   - Add an H2 tag for the title and a P tag for the description.
   - Include a `Button` component for the call-to-action button.

### Button Component (Assumed)

#### File: Button.js

```javascript
import React from 'react';

const Button = ({ label, text, variant }) => {
  return (
    <button className={`btn btn-${variant}`}>
      {label} <span>{text}</span>
    </button>
  );
};

export default Button;
```

### Explanation:

1. **Import Statements**: Import necessary components.
2. **Component Definition**: Define the `Button` component as a functional component.
3. **Props**: Accept props for label, text, and variant (e.g., primary, secondary).
4. **Rendering**:
   - Use a `<button>` element with class names to style it based on the variant.

### Usage Example

```javascript
import React from 'react';
import CTASection from './CTASection';

const App = () => {
  return (
    <div>
      <CTASection
        title="Join Our Community"
        description="Get access to exclusive resources and support."
        buttonLabel="Sign Up Now"
        buttonText="Free Trial"
      />
    </div>
  );
};

export default App;
```

### Explanation:

1. **Import Statements**: Import the `CTASection` component.
2. **Component Definition**: Define a simple app component that uses the `CTASection` component.

This approach ensures each component is modular, clean, and easy to maintain. Each file corresponds to an AST node as required.