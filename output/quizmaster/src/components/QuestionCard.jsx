import React from 'react';

const QuestionCard = ({ data, selected, onSelect }) => (
  <div className="mt-8">
    <h3 className="text-xl font-semibold">{data.question}</h3>
    {data.options.map((option) => (
      <button
        key={option}
        onClick={() => onSelect(option)}
        className={`w-full mt-4 py-2 rounded-lg ${selected === option ? 'bg-green-500 text-white' : 'bg-zinc-100'}`}
      >
        {option}
      </button>
    ))}
  </div>
);

export default QuestionCard;
