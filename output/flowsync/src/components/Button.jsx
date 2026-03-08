```jsx
const Button = ({ children, ...props }) => {
  return (
    <button className={`bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all ${props.className}`} {...props}>
      {children}
    </button>
  );
};

export default Button;
```
