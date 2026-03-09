### File Structure

src/
├── components/
│   ├── FeaturesSection.jsx
│   ├── ProductShowcase.jsx
│   └── StatisticCard.jsx
├── pages/
│   ├── Home.jsx
│   └── About.jsx
└── App.jsx

### Code Generation

#### `src/components/FeaturesSection.jsx`

import React from 'react';
import { Grid, Col } from '@nextui-org/react';

const FeaturesSection = () => {
  return (
    <div className="max-w-7xl px-6 py-16 mx-auto rounded-lg">
      <Grid.Container gap={2} justify="center" css={{ mb: '$4' }}>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h3 className="text-xl font-bold">Feature 1</h3>
            <p className="mt-2 text-gray-700">Description of feature 1.</p>
          </div>
        </Grid>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h3 className="text-xl font-bold">Feature 2</h3>
            <p className="mt-2 text-gray-700">Description of feature 2.</p>
          </div>
        </Grid>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h3 className="text-xl font-bold">Feature 3</h3>
            <p className="mt-2 text-gray-700">Description of feature 3.</p>
          </div>
        </Grid>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h3 className="text-xl font-bold">Feature 4</h3>
            <p className="mt-2 text-gray-700">Description of feature 4.</p>
          </div>
        </Grid>
      </Grid.Container>
    </div>
  );
};

export default FeaturesSection;

#### `src/components/ProductShowcase.jsx`

import React from 'react';
import { Grid, Col } from '@nextui-org/react';

const ProductShowcase = () => {
  return (
    <div className="max-w-7xl px-6 py-16 mx-auto rounded-lg">
      <Grid.Container gap={2} justify="center" css={{ mb: '$4' }}>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg overflow-hidden">
            <img src="/path/to/product1.jpg" alt="Product 1" className="w-full h-96 object-cover" />
            <h3 className="text-xl font-bold mt-4">Product 1</h3>
            <p className="mt-2 text-gray-700">Description of product 1.</p>
          </div>
        </Grid>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg overflow-hidden">
            <img src="/path/to/product2.jpg" alt="Product 2" className="w-full h-96 object-cover" />
            <h3 className="text-xl font-bold mt-4">Product 2</h3>
            <p className="mt-2 text-gray-700">Description of product 2.</p>
          </div>
        </Grid>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg overflow-hidden">
            <img src="/path/to/product3.jpg" alt="Product 3" className="w-full h-96 object-cover" />
            <h3 className="text-xl font-bold mt-4">Product 3</h3>
            <p className="mt-2 text-gray-700">Description of product 3.</p>
          </div>
        </Grid>
        <Grid xs={12} sm={6}>
          <div className="p-4 bg-white shadow-md rounded-lg overflow-hidden">
            <img src="/path/to/product4.jpg" alt="Product 4" className="w-full h-96 object-cover" />
            <h3 className="text-xl font-bold mt-4">Product 4</h3>
            <p className="mt-2 text-gray-700">Description of product 4.</p>
          </div>
        </Grid>
      </Grid.Container>
    </div>
  );
};

export default ProductShowcase;

#### `src/components/StatisticCard.jsx`

import React from 'react';
import { Card, CardBody } from '@nextui-org/react';

const StatisticCard = ({ title, value }) => {
  return (
    <Card isPressable className="p-4 bg-white shadow-md rounded-lg">
      <CardBody>
        <h3 className="text-xl font-bold">{title}</h3>
        <p className="mt-2 text-gray-700">{value}</p>
      </CardBody>
    </Card>
  );
};

export default StatisticCard;

#### `src/pages/Home.jsx`

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import FeaturesSection from '../components/FeaturesSection';
import ProductShowcase from '../components/ProductShowcase';

const Home = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/features" element={<FeaturesSection />} />
        <Route path="/showcase" element={<ProductShowcase />} />
      </Routes>
    </div>
  );
};

export default Home;

#### `src/pages/About.jsx`

import React from 'react';
import { Routes, Route } from 'react-router-dom';

const About = () => {
  return (
    <div>
      <Routes>
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
};

export default About;

#### `src/App.jsx`

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
};

export default App;

This setup follows the blueprint and generates clean, modular React components with direct Tailwind injection.