import { Button } from '@/components/ui/button';

const GlassContactSection = () => {
  return (
    <section className="py-16 md:py-24">
      <div className="max-w-7xl mx-auto px-6">
        <h2 className="text-3xl font-bold text-slate-900 mb-4">Contact Us</h2>
        <form className="space-y-4">
          <div className="flex flex-col space-y-2">
            <label htmlFor="name" className="text-slate-900">Name</label>
            <input
              id="name"
              type="text"
              className="bg-white/10 border border-white/20 rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Your Name"
            />
          </div>
          <div className="flex flex-col space-y-2">
            <label htmlFor="email" className="text-slate-900">Email</label>
            <input
              id="email"
              type="email"
              className="bg-white/10 border border-white/20 rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Your Email"
            />
          </div>
          <div className="flex flex-col space-y-2">
            <label htmlFor="message" className="text-slate-900">Message</label>
            <textarea
              id="message"
              className="bg-white/10 border border-white/20 rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Your Message"
            />
          </div>
          <Button type="submit">Send Message</Button>
        </form>
      </div>
    </section>
  );
};

export default GlassContactSection;
