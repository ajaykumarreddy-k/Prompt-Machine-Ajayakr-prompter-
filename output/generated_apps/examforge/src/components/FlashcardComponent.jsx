import React from 'react';
import { Container } from './Container';

const FlashcardComponent = ({ data, layout }) => {
  return (
    <Container className={layout === "Grid" ? "grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5" : ""}>
      {data.map((item) => (
        <div key={item.id} className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
          {/* Flashcard content */}
        </div>
      ))}
    </Container>
  );
};

export default FlashcardComponent;
