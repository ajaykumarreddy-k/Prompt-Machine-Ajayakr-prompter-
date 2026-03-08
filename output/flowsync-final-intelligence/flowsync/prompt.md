# FlowSync — Frontend Prompt

### Instruction Set for Compiling DataGrid Component

#### Overview:
This document provides detailed instructions for compiling the `DataGrid` component using the FloatUI framework and Tailwind CSS. The `DataGrid` is designed to handle complex data display scenarios with ease, offering features such as sorting, filtering, pagination, and more.

#### Step 1: Setup Environment
1. **Install Node.js**: Ensure you have Node.js installed on your system.
2. **Create a New Project**:
   ```bash
   npx create-react-app my-app
   cd my-app
   ```
3. **Install FloatUI and Tailwind CSS**:
   ```bash
   npm install @floatui/core @floatui/data-grid tailwindcss postcss autoprefixer
   ```

#### Step 2: Configure Tailwind CSS
1. **Initialize Tailwind Configuration**:
   - Create a `tailwind.config.js` file in the root of your project.
   - Add the following configuration to `tailwind.config.js`:
     ```js
     module.exports = {
       content: [
         './src/**/*.{js,jsx,ts,tsx}',
       ],
       theme: {
         extend: {},
       },
       plugins: [],
     }
     ```
2. **Install PostCSS and Tailwind CLI**:
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

#### Step 3: Import FloatUI Core and DataGrid in Your Project
1. **Import FloatUI Components**:
   In your `src/index.js` or `App.js`, import the necessary components.
   ```jsx
   import { DataGrid } from '@floatui/data-grid';
   import 'tailwindcss/tailwind.css'; // Import Tailwind CSS

   function App() {
     return (
       <div className="min-h-screen bg-gray-100">
         <DataGrid />
       </div>
     );
   }

   export default App;
   ```

#### Step 4: Define Data and Columns
1. **Define Data**:
   ```jsx
   const data = [
     { id: 1, name: 'John Doe', age: 30 },
     { id: 2, name: 'Jane Smith', age: 25 },
     // Add more rows as needed
   ];
   ```
2. **Define Columns**:
   ```jsx
   const columns = [
     { field: 'id', header: 'ID' },
     { field: 'name', header: 'Name' },
     { field: 'age', header: 'Age' },
   ];
   ```

#### Step 5: Implement DataGrid Component
1. **Update App.js**:
   ```jsx
   import React, { useState } from 'react';
   import { DataGrid } from '@floatui/data-grid';

   function App() {
     const [data, setData] = useState([
       { id: 1, name: 'John Doe', age: 30 },
       { id: 2, name: 'Jane Smith', age: 25 },
     ]);

     const columns = [
       { field: 'id', header: 'ID' },
       { field: 'name', header: 'Name' },
       { field: 'age', header: 'Age' },
     ];

     return (
       <div className="min-h-screen bg-gray-100">
         <DataGrid
           rows={data}
           columns={columns}
           pageSize={5} // Optional: Set the number of items per page
           onSort={(sortModel) => console.log(sortModel)}
           onFilter={(filterModel) => console.log(filterModel)}
         />
       </div>
     );
   }

   export default App;
   ```

#### Step 6: Run Your Application
1. **Start Development Server**:
   ```bash
   npm start
   ```
2. **Verify Functionality**: Open your browser and navigate to `http://localhost:3000`. You should see the DataGrid component rendering with sample data.

### Conclusion:
This instruction set provides a comprehensive guide for compiling the `DataGrid` component using FloatUI and Tailwind CSS. By following these steps, you can integrate advanced data display features into your React application efficiently. Adjustments may be necessary based on specific project requirements or additional features needed.