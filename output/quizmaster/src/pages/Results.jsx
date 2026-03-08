import React from 'react';
import Navbar from '../components/Navbar';
import ScoreSummary from '../components/ScoreSummary';
import ResultsSummary from '../components/ResultsSummary';
import Footer from '../components/Footer';

const Results = ({ score }) => (
  <div className="Container">
    <Section>
      <Stack>
        <Navbar />
        <ScoreSummary score={score} />
        <ResultsSummary details={`You scored ${score}/10`}/>
        <Footer />
      </Stack>
    </Section>
  </div>
);

export default Results;
