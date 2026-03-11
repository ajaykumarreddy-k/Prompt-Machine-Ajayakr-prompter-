import { FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import { motion, AnimatePresence } from 'framer-motion';

const GlassTestimonialsSection = ({ testimonials }) => {
  const [activeIndex, setActiveIndex] = useState(0);

  const handlePrev = () => {
    setActiveIndex((prevIndex) => (prevIndex - 1 + testimonials.length) % testimonials.length);
  };

  const handleNext = () => {
    setActiveIndex((prevIndex) => (prevIndex + 1) % testimonials.length);
  };

  return (
    <section className="py-16 md:py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="relative">
          <motion.div
            initial={{ x: -200, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ duration: 0.5, ease: 'easeInOut' }}
            className="absolute left-0"
            onClick={handlePrev}
          >
            <FaArrowLeft className="text-4xl text-slate-900" />
          </motion.div>
          <motion.div
            initial={{ x: 200, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ duration: 0.5, ease: 'easeInOut' }}
            className="absolute right-0"
            onClick={handleNext}
          >
            <FaArrowRight className="text-4xl text-slate-900" />
          </motion.div>
          <div className="flex flex-col space-y-4">
            {testimonials.map((testimonial, index) => (
              <div
                key={index}
                className={`relative ${activeIndex === index ? 'opacity-100' : 'opacity-0'}`}
              >
                <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-lg shadow-lg p-6">
                  <p className="text-lg text-slate-900">{testimonial.text}</p>
                  <p className="text-base text-slate-900 mt-2">{testimonial.name}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default GlassTestimonialsSection;
