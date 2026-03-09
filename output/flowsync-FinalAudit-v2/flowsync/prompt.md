# FlowSync — Frontend Prompt

### AST-CENTRIC IMPLEMENTATION CONTRACT

This application MUST be built exactly following the provided JSON AST.

### 1. AST LAYOUT INSTRUCTIONS
{
  "pages": [
    {
      "name": "Overview",
      "route": "/",
      "state_contract": {},
      "layout": {
        "type": "PageLayout",
        "children": [
          {
            "type": "Navbar",
            "props": [],
            "responsibilities": [
              "Provides navigation options for the user"
            ]
          },
          {
            "type": "StatCard",
            "props": [
              "title",
              "stats"
            ],
            "responsibilities": [
              "Displays key statistics or metrics"
            ]
          },
          {
            "type": "ActivityFeed",
            "props": [
              "items"
            ],
            "responsibilities": [
              "Shows recent activities or events"
            ]
          },
          {
            "type": "ProductShowcase",
            "props": [
              "title",
              "items"
            ],
            "responsibilities": [
              "Highlights featured products or services"
            ]
          },
          {
            "type": "DataGrid",
            "props": [
              "data",
              "filters"
            ],
            "responsibilities": [
              "Displays tabular data with filtering options"
            ]
          },
          {
            "type": "FeaturesSection",
            "props": [
              "title",
              "features"
            ],
            "responsibilities": [
              "Lists key features or benefits of the product"
            ]
          },
          {
            "type": "PricingPreview",
            "props": [],
            "responsibilities": [
              "Provides a preview of pricing plans"
            ]
          },
          {
            "type": "ChartWidget",
            "props": [
              "data"
            ],
            "responsibilities": [
              "Displays data in chart form"
            ]
          },
          {
            "type": "UserMenu",
            "props": [],
            "responsibilities": [
              "Provides user-specific options or actions"
            ]
          },
          {
            "type": "CTASection",
            "props": [
              "title",
              "ctaText"
            ],
            "responsibilities": [
              "Encourages users to take a specific action"
            ]
          },
          {
            "type": "HeroSection",
            "props": [
              "title",
              "description",
              "image"
            ],
            "responsibilities": [
              "Highlights key information or features with an image"
            ]
          },
          {
            "type": "TestimonialsSection",
            "props": [
              "testimonials"
            ],
            "responsibilities": [
              "Displays customer testimonials or reviews"
            ]
          },
          {
            "type": "BenefitsSection",
            "props": [
              "title",
              "benefits"
            ],
            "responsibilities": [
              "Lists the benefits of using the product"
            ]
          },
          {
            "type": "Footer",
            "props": [],
            "responsibilities": [
              "Provides footer content such as links or contact information"
            ]
          }
        ]
      }
    },
    {
      "name": "Analytics",
      "route": "/analytics",
      "state_contract": {},
      "layout": {
        "type": "PageLayout",
        "children": [
          {
            "type": "Navbar",
            "props": [],
            "responsibilities": [
              "Provides navigation options for the user"
            ]
          },
          {
            "type": "ChartWidget",
            "props": [
              "data"
            ],
            "responsibilities": [
              "Displays data in chart form"
            ]
          },
          {
            "type": "DataGrid",
            "props": [
              "data",
              "filters"
            ],
            "responsibilities": [
              "Displays tabular data with filtering options"
            ]
          },
          {
            "type": "Footer",
            "props": [],
            "responsibilities": [
              "Provides footer content such as links or contact information"
            ]
          }
        ]
      }
    },
    {
      "name": "Settings",
      "route": "/settings",
      "state_contract": {},
      "layout": {
        "type": "PageLayout",
        "children": [
          {
            "type": "Navbar",
            "props": [],
            "responsibilities": [
              "Provides navigation options for the user"
            ]
          },
          {
            "type": "Footer",
            "props": [],
            "responsibilities": [
              "Provides footer content such as links or contact information"
            ]
          }
        ]
      }
    }
  ],
  "discarded_components": [
    {
      "component": "Sidebar",
      "discard_reason": "Not used in layout"
    }
  ]
}

### 2. COMPONENT RESPONSIBILITIES (EXTRACTED)
- Navbar: Provides navigation options for the user
- StatCard: Displays key statistics or metrics
- ActivityFeed: Shows recent activities or events
- ProductShowcase: Highlights featured products or services
- DataGrid: Displays tabular data with filtering options
- FeaturesSection: Lists key features or benefits of the product
- PricingPreview: Provides a preview of pricing plans
- ChartWidget: Displays data in chart form
- UserMenu: Provides user-specific options or actions
- CTASection: Encourages users to take a specific action
- HeroSection: Highlights key information or features with an image
- TestimonialsSection: Displays customer testimonials or reviews
- BenefitsSection: Lists the benefits of using the product
- Footer: Provides footer content such as links or contact information
- Navbar: Provides navigation options for the user
- ChartWidget: Displays data in chart form
- DataGrid: Displays tabular data with filtering options
- Footer: Provides footer content such as links or contact information
- Navbar: Provides navigation options for the user
- Footer: Provides footer content such as links or contact information

### 3. DESIGN SYSTEM (STRICT ENFORCEMENT)
- **Palette**: Minimal Editorial
- **Primary**: zinc-900
- **Secondary**: zinc-500
- **Accent**: red-500
- **Mandatory Tokens**: `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, `bg-zinc-50`
- **FORBIDDEN (REJECT CODE IF PRESENT)**: `rounded-xl`, `container`, `bg-gradient`

### 4. ROUTING & FOLDER CONTRACT
- **Engine**: `react-router-dom`
- **Structure**: 
  - `src/pages/`: Overview, Analytics, Settings
  - `src/components/`: ActivityFeed, BenefitsSection, CTASection, ChartWidget, DataGrid, FeaturesSection, Footer, HeroSection, Navbar, PricingPreview, ProductShowcase, StatCard, TestimonialsSection, UserMenu
  - `src/App.jsx`: Routing definitions for /, /analytics, /settings

### 5. KNOWLEDGE BASE INTELLIGENCE
===================================================
=== REFS: STATCARD ===
==================================================
QUERY: StatCard
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.766
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.765
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: ACTIVITYFEED ===
==================================================
QUERY: ActivityFeed
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.758
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.757
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: PRODUCTSHOWCASE ===
==================================================
QUERY: ProductShowcase
CONTEXT (2 chunks):
============================================================

[1] source=21dev  tag=animations  score=0.753
data-[side=top]:slide-in-from-bottom-2", className )} {...props} /> )); TooltipContent.displayName = TooltipPrimitive.Content.displayName; // Dialog Components const Dialog = DialogPrimitive.Root; const DialogPortal = DialogPrimitive.Portal; const DialogOverlay = React.forwardRef< React.ElementRef<typeof DialogPrimitive.Overlay>, React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay> >(({ className, ...props }, ref) => ( <DialogPrimitive.Overlay ref={ref} className={cn( "fixed inset-0 z-50 bg-black/60 backdrop-blur-sm data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0", className )} {...props} /> )); DialogOverlay.displayName = DialogPrimitive.Overlay.displayName; const DialogContent = React.forwardRef< React.ElementRef<typeof DialogPrimitive.Content>, React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content> >(({ className, children, ...props }, ref) => ( <DialogPortal> <DialogOverlay /> <DialogPrimitive.Content ref={ref} className={cn( "fixed left-[50%] top-[50%] z-50 grid w-full max-w-[90vw] md:max-w-[800px] translate-x-[-50%] translate-y-[-50%] gap-4 border border-[#333333] bg-[#1F2023] p-0 shadow-xl duration-300 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 rounded-2xl", className )} {...props} > {children} <DialogPrimitive.Close className="absolute right-4 top-4 z-10 rounded-full bg-[#2E3033]/80 p-2 hover:bg-[#2E3033] transition-all"> <X className="h-5 w-5 text-gray-200 hover:text-white" /> <span className="sr-only">Close</span> </DialogPrimitive.Close> </DialogPrimitive.Content> </DialogPortal> )); DialogContent.displayName = DialogPrimitive.Content.displayName; const DialogTitle = React.forwardRef< React.ElementRef<typeof DialogPrimitive.Title>, React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title> >(({ className, ...props }, ref) => ( <DialogPrimitive.Title ref={ref} className={cn("text-lg font-semibold leading-none tracking-tight text-gray-100", className)} {...props} /> )); DialogTitle.displayName = DialogPrimitive.Title.displayName; // Button Component interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { variant?: "default" | "outline" | "ghost"; size?: "default" | "sm" | "lg" | "icon"; } const Button = React.forwardRef<HTMLButtonElement, ButtonProps>( ({ className, variant = "default", size = "default", ...props }, ref) => { const variantClasses = { default: "bg-white hover:bg-white/80 text-black", outline: "border border-[#444444] bg-transparent hover:bg-[#3A3A40]", ghost: "bg-transparent hover:bg-[#3A3A40]", }; const sizeClasses = { default: "h-10 px-4 py-2", sm: "h-8 px-3 text-sm", lg: "h-12 px-6", icon: "h-8 w-8 rounded-full aspect-[1/1]", }; return ( <button className={cn( "inline-flex items-center justify-center font-medium transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50", variantClasses[variant], sizeClasses[size], className )} ref={ref} {...props} /> ); } ); Button.displayName = "Button"; // VoiceRecorder Component interface VoiceRecorderProps { isRecording: boolean; onStartRecording: () => void; onStopRecording: (duration: number) => void; visualizerBars?: number; } const VoiceRecorder: React.FC<VoiceRecorderProps> = ({ isRecording, onStartRecording, onStopRecording, visualizerBars = 32, }) => { const [time, setTime] = React.useState(0); const timerRef = React.useRef<NodeJS.Timeout | null>(null); React.useEffect(() => { if (isRecording) { onStartRecording(); timerRef.current = setInterval(() => setTime((t) => t + 1), 1000); } else { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } onStopRecording(time); setTime(0); } return () => { if (timerRef.current) clearInterval(timerRef.current); }; }, [isRecording, time, onStartRecording, onStopRecording]); const formatTime = (seconds: number) => { const mins = Math.floor(seconds / 60); const secs = seconds % 60; return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`; }; return ( <div className={cn( "flex flex-col items-center justify-center w-full transition-all duration-300 py-3", isRecording ? "opacity-100" : "opacity-0 h-0" )} > <div className="flex items-center gap-2 mb-3"> <div className="h-2 w-2 rounded-full bg-red-500 animate-pulse" /> <span className="font-mono text-sm text-white/80">{formatTime(time)}</span> </div> <div className="w-full h-10 flex items-center justify-center gap-0.5 px-4"> {[...Array(visualizerBars)].map((_, i) => ( <div key={i} className="w-0.5 rounded-full bg-white/50 animate-pulse" style={{ height: `${Math.max(15, Math.random() * 100)}%`, animationDelay: `${i * 0.05}s`, animationDuration: `${0.5 + Math.random() * 0.5}s`, }} /> ))} </div> </div> ); }; // ImageViewDialog Component interface ImageViewDialogProps { imageUrl: string | null; onClose: () => void; } const ImageViewDialog: React.FC<ImageViewDialogProps> = ({ imageUrl, onClose }) => { if (!imageUrl) return null; return ( <Dialog open={!!imageUrl} onOpenChange={onClose}> <DialogContent className="p-0 border-none bg-transparent shadow-none max-w-[90vw] md:max-w-[800px]"> <DialogTitle className="sr-only">Image Preview</DialogTitle> <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0, scale: 0.95 }} transition={{ duration: 0.2, ease: "easeOut" }} className="relative bg-[#1F2023] rounded-2xl overflow-hidden shadow-2xl" > <img src={imageUrl} alt="Full preview" className="w-full max-h-[80vh] object-contain rounded-2xl" /> </motion.div> </DialogContent> </Dialog> ); }; // PromptInput Context and Components interface PromptInputContextType { isLoading: boolean; value: string; setValue: (value: string) => void; maxHeight: number | string; onSubmit?: () => void; disabled?: boolean; } const PromptInputContext = React.createContext<PromptInputContextType>({ isLoading: false, value: "", setValue: () => {}, maxHeight: 240, onSubmit: undefined, disabled: false, }); function usePromptInput() { const context = React.useContext(PromptInputContext); if (!context)
----------------------------------------

[2] source=21dev  tag=effects  score=0.749
asChild?: boolean } const Button = React.forwardRef<HTMLButtonElement, ButtonProps>( ({ className, variant, size, asChild = false, ...props }, ref) => { const Comp = asChild ? Slot : "button" return ( <Comp className={cn(buttonVariants({ variant, size, className }))} ref={ref} {...props} /> ) } ) Button.displayName = "Button" export { Button, buttonVariants, liquidbuttonVariants, LiquidButton } const liquidbuttonVariants = cva( "inline-flex items-center transition-colors justify-center cursor-pointer gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-[color,box-shadow] disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive", { variants: { variant: { default: "bg-transparent hover:scale-105 duration-300 transition text-primary", destructive: "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40", outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground", secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80", ghost: "hover:bg-accent hover:text-accent-foreground", link: "text-primary underline-offset-4 hover:underline", }, size: { default: "h-9 px-4 py-2 has-[>svg]:px-3", sm: "h-8 text-xs gap-1.5 px-4 has-[>svg]:px-4", lg: "h-10 rounded-md px-6 has-[>svg]:px-4", xl: "h-12 rounded-md px-8 has-[>svg]:px-6", xxl: "h-14 rounded-md px-10 has-[>svg]:px-8", icon: "size-9", }, }, defaultVariants: { variant: "default", size: "xxl", }, } ) function LiquidButton({ className, variant, size, asChild = false, children, ...props }: React.ComponentProps<"button"> & VariantProps<typeof liquidbuttonVariants> & { asChild?: boolean }) { const Comp = asChild ? Slot : "button" return ( <> <Comp data-slot="button" className={cn( "relative", liquidbuttonVariants({ variant, size, className }) )} {...props} > <div className="absolute top-0 left-0 z-0 h-full w-full rounded-full shadow-[0_0_6px_rgba(0,0,0,0.03),0_2px_6px_rgba(0,0,0,0.08),inset_3px_3px_0.5px_-3px_rgba(0,0,0,0.9),inset_-3px_-3px_0.5px_-3px_rgba(0,0,0,0.85),inset_1px_1px_1px_-0.5px_rgba(0,0,0,0.6),inset_-1px_-1px_1px_-0.5px_rgba(0,0,0,0.6),inset_0_0_6px_6px_rgba(0,0,0,0.12),inset_0_0_2px_2px_rgba(0,0,0,0.06),0_0_12px_rgba(255,255,255,0.15)] transition-all dark:shadow-[0_0_8px_rgba(0,0,0,0.03),0_2px_6px_rgba(0,0,0,0.08),inset_3px_3px_0.5px_-3.5px_rgba(255,255,255,0.09),inset_-3px_-3px_0.5px_-3.5px_rgba(255,255,255,0.85),inset_1px_1px_1px_-0.5px_rgba(255,255,255,0.6),inset_-1px_-1px_1px_-0.5px_rgba(255,255,255,0.6),inset_0_0_6px_6px_rgba(255,255,255,0.12),inset_0_0_2px_2px_rgba(255,255,255,0.06),0_0_12px_rgba(0,0,0,0.15)]" /> <div className="absolute top-0 left-0 isolate -z-10 h-full w-full overflow-hidden rounded-md" style={{ backdropFilter: 'url("#container-glass")' }} /> <div className="pointer-events-none z-10 "> {children} </div> <GlassFilter /> </Comp> </> ) } function GlassFilter() { return ( <svg className="hidden"> <defs> <filter id="container-glass" x="0%" y="0%" width="100%" height="100%" colorInterpolationFilters="sRGB" > {/* Generate turbulent noise for distortion */} <feTurbulence type="fractalNoise" baseFrequency="0.05 0.05" numOctaves="1" seed="1" result="turbulence" /> {/* Blur the turbulence pattern slightly */} <feGaussianBlur in="turbulence" stdDeviation="2" result="blurredNoise" /> {/* Displace the source graphic with the noise */} <feDisplacementMap in="SourceGraphic" in2="blurredNoise" scale="70" xChannelSelector="R" yChannelSelector="B" result="displaced" /> {/* Apply overall blur on the final result */} <feGaussianBlur in="displaced" stdDeviation="4" result="finalBlur" /> {/* Output the result */} <feComposite in="finalBlur" in2="finalBlur" operator="over" /> </filter> </defs> </svg> ); } type ColorVariant = | "default" | "primary" | "success" | "error" | "gold" | "bronze"; interface MetalButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { variant?: ColorVariant; } const colorVariants: Record< ColorVariant, { outer: string; inner: string; button: string; textColor: string; textShadow: string; } > = { default: { outer: "bg-gradient-to-b from-[#000] to-[#A0A0A0]", inner: "bg-gradient-to-b from-[#FAFAFA] via-[#3E3E3E] to-[#E5E5E5]", button: "bg-gradient-to-b from-[#B9B9B9] to-[#969696]", textColor: "text-white", textShadow: "[text-shadow:_0_-1px_0_rgb(80_80_80_/_100%)]", }, primary: { outer: "bg-gradient-to-b from-[#000] to-[#A0A0A0]", inner: "bg-gradient-to-b from-primary via-secondary to-muted", button: "bg-gradient-to-b from-primary to-primary/40", textColor: "text-white", textShadow: "[text-shadow:_0_-1px_0_rgb(30_58_138_/_100%)]", }, success: { outer: "bg-gradient-to-b from-[#005A43] to-[#7CCB9B]", inner: "bg-gradient-to-b from-[#E5F8F0] via-[#00352F] to-[#D1F0E6]", button: "bg-gradient-to-b from-[#9ADBC8] to-[#3E8F7C]", textColor: "text-[#FFF7F0]", textShadow: "[text-shadow:_0_-1px_0_rgb(6_78_59_/_100%)]", }, error: { outer: "bg-gradient-to-b from-[#5A0000] to-[#FFAEB0]", inner: "bg-gradient-to-b from-[#FFDEDE] via-[#680002] to-[#FFE9E9]", button: "bg-gradient-to-b from-[#F08D8F] to-[#A45253]", textColor: "text-[#FFF7F0]", textShadow: "[text-shadow:_0_-1px_0_rgb(146_64_14_/_100%)]", }, gold: { outer: "bg-gradient-to-b from-[#917100] to-[#EAD98F]", inner: "bg-gradient-to-b from-[#FFFDDD] via-[#856807] to-[#FFF1B3]", button: "bg-gradient-to-b from-[#FFEBA1] to-[#9B873F]", textColor: "text-[#FFFDE5]", textShadow: "[text-shadow:_0_-1px_0_rgb(178_140_2_/_100%)]", }, bronze: { outer: "bg-gradient-to-b from-[#864813] to-[#E9B486]", inner: "bg-gradient-to-b from-[#EDC5A1] via-[#5F2D01] to-[#FFDEC1]", button: "bg-gradient-to-b from-[#FFE3C9] to-[#A36F3D]", textColor: "text-[#FFF7F0]", textShadow: "[text-shadow:_0_-1px_0_rgb(124_45_18_/_100%)]", }, }; const metalButtonVariants = ( variant: ColorVariant = "default", isPressed: boolean, isHovered: boolean, isTouchDevice: boolean, ) => { const colors = colorVariants[variant]; const transitionStyle = "all 250ms cubic-bezier(0.1, 0.4, 0.2, 1)"; return { wrapper: cn( "relative inline-flex transform-gpu rounded-md p-[1.25px] will-change-transform", colors.outer, ), wrapperStyle: { transform: isPressed ? "translateY(2.5px) scale(0.99)" : "translateY(0) scale(1)", boxShadow: isPressed ? "0 1px 2px rgba(0, 0, 0, 0.15)" : isHovered && !isTouchDevice ? "0 4px 12px rgba(0, 0, 0, 0.12)" : "0 3px 8px rgba(0, 0, 0, 0.08)", transition: transitionStyle, transformOrigin: "center center", }, inner: cn( "absolute inset-[1px] transform-gpu rounded-lg will-change-transform", colors.inner, ), innerStyle: { transition: transitionStyle, transformOrigin: "center center", filter: isHovered && !isPressed &&
----------------------------------------
===================================================
=== REFS: DATAGRID ===
==================================================
QUERY: DataGrid
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.755
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.755
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: FOOTER ===
==================================================
QUERY: footer columns links bottom social bottom-bar
CONTEXT (2 chunks):
============================================================

[1] source=www.landingfolio.com  tag=footer  score=0.754
## Put links to your social media in your footer

The footer is where information goes that is relevant across the whole website. Your social media is one of these things... Read more
----------------------------------------

[2] source=freefrontend.com  tag=footer  score=0.672
11vw; letter-spacing: -0.8vw; @media all and (max-width: 768px) { margin: 0 0 6vw; font-size: 18vw; } } .col__content-wrap { display: flex; justify-content: flex-end; @media all and (max-width: 768px) { flex-direction: column; } } .col__content-txt { max-width: 22vw; order: 2; margin-left: 32px; @media all and (max-width: 768px) { order: 1; max-width: 40vw; margin: 0 0 10vw 10vw; } } .slide-link { position: relative; order: 1; display: flex; justify-content: flex-end; width: 75px; height: 53px; > * { pointer-events: none; } @media all and (max-width: 768px) { order: 2; align-self: flex-end; } } .slide-link__circ { width: 53px; height: 53px; border-radius: 50%; border: 1px solid var(--dark); } .slide-link__line { position: absolute; top: 25px; left: 0; width: 64px; height: 3px; background: var(--dark); } .line { overflow: hidden; &:nth-of-type(even) { margin-top: -1vw; } } .line__inner { display: block; } .slide__scroll-link { position: absolute; right: -113px; bottom: 3.5vw; display: block; width: 140px; height: 140px; background: var(--dark); overflow: hidden; @media all and (max-width: 768px) { display: none; } } .slide__scroll-line { position: absolute; left: 26px; bottom: 0; width: 1px; height: 100%; } .slide--0 { .slide__scroll-line { background: #C0D7D8; } } .slide--1 { .slide__scroll-line { background: #D8C0C0; } } .slide--2 { .slide__scroll-line { background: #CDD5E0; } } .slide--3 { .slide__scroll-line { background: #F3D3B0; } } .slide--4 { .slide__scroll-line { background: #F8E9E6; } } .slide--5 { .slide__scroll-line { background: #D1E2EC; } } .slide--6 { .slide__scroll-line { background: #D7CEC5; } } /* Column Image */ .col__image-wrap { position: absolute; left: 0; // top: 50%; // transform: translateY(-50%); width: 100%; height: 160vh; } .img { object-fit: cover; width: 100%; height: 100%; } /* Footer */ .footer { display: flex; align-items: center; justify-content: center; flex-direction: column; background: #cecece; } .footer__link { font-size: 5vw; color: var(--dark); text-decoration: none; font-family: 'Cinzel', serif; } .footer__link-top { position: absolute; left: 50%; bottom: 100px; transform: translateX(-50%); display: flex; align-items: center; justify-content: center; width: 100px; height: 100px; background: var(--dark); font-size: 18px; color: white; text-decoration: none; font-family: 'Cinzel', serif; } .footer__link-top-line { position: absolute; top: -50px; left: 50%; width: 1px; height: 50px; background: var(--dark); } .footer__copyright { position: absolute; left: 50%; bottom: 24px; transform: translateX(-50%); } TSX (React) gsap.registerPlugin(ScrollTrigger); gsap.registerPlugin(ScrollToPlugin); gsap.registerPlugin(SplitText); gsap.registerPlugin(ScrollSmoother); console.clear(); select = e => document.querySelector(e); selectAll = e => document.querySelectorAll(e); const stage = select('.stage'); const slides = selectAll(".slide"); const links = selectAll(".slide__scroll-link"); const titles = selectAll('.col__content-title'); const introTitle = new SplitText('.intro__title', {type: "lines", linesClass: "intro-line"}); const splitTitles = new SplitText(titles, {type: "lines, chars", linesClass: "line", charsClass: "char", position: "relative" }); let slideID = 0; const smoother = ScrollSmoother.create({ smooth: 2, effects: true, // normalizeScroll: true, smoothTouch: 0.1, }); function initHeader() { // animate the logo and fake burger button into place let tl = gsap.timeline({delay: 0.5}); tl.from('.logo', { y: -40, opacity: 0, duration: 2, ease: 'power4' }) .from('.nav-btn__svg rect', { scale: 0, transformOrigin: "center right", duration: 0.6, ease: 'power4', stagger: 0.1 }, 0.6) .to('.nav-rect', { scale: 0.8, transformOrigin: "center left", duration: 0.4, ease: 'power2', stagger: 0.1 }, "-=0.6") // create mouse animations for the faux burger button let navBtn = select('.nav-btn'); navBtn.addEventListener("mouseover", (e) => { gsap.to('.nav-rect', { scaleX: 1, transformOrigin: "top left", duration: 0.4, ease: "power4" }); }); navBtn.addEventListener("mouseout", (e) => { gsap.to('.nav-rect', { scaleX: 0.8, transformOrigin: "top left", duration: 0.6, ease: "power4" }); }); } function initIntro() { // animate the intro elements into place let tl = gsap.timeline({delay: 1.2}); tl.from('.intro-line', { // x: 100, y: 400, ease: 'power4', duration: 3 }) .from('.intro__txt', { x: -100, opacity: 0, ease: 'power4', duration: 3 }, 0.7) .from('.intro__img--1', { // x: -50, y: 50, opacity: 0, ease: 'power2', duration: 10 }, 1) .from('.intro__img--2', { // x: 50, y: -50, opacity: 0, ease: 'power2', duration: 10 }, 1); // set
----------------------------------------
===================================================
=== REFS: FEATURESSECTION ===
==================================================
QUERY: FeaturesSection
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.775
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.774
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: PRICINGPREVIEW ===
==================================================
QUERY: PricingPreview
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.776
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.776
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: CHARTWIDGET ===
==================================================
QUERY: ChartWidget
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.777
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.777
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: SIDEBAR ===
==================================================
QUERY: Sidebar
CONTEXT (2 chunks):
============================================================

[1] source=21dev  tag=forms  score=0.804
const SidebarContent = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => { return ( <div ref={ref} data-sidebar="content" className={cn( "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden", className )} {...props} /> ) }) SidebarContent.displayName = "SidebarContent" const SidebarGroup = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => { return ( <div ref={ref} data-sidebar="group" className={cn("relative flex w-full min-w-0 flex-col p-2", className)} {...props} /> ) }) SidebarGroup.displayName = "SidebarGroup" const SidebarGroupLabel = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> & { asChild?: boolean } >(({ className, asChild = false, ...props }, ref) => { const Comp = asChild ? Slot : "div" return ( <Comp ref={ref} data-sidebar="group-label" className={cn( "duration-200 flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium text-sidebar-foreground/70 outline-none ring-sidebar-ring transition-[margin,opacity] ease-linear focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0", "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0", className )} {...props} /> ) }) SidebarGroupLabel.displayName = "SidebarGroupLabel" const SidebarGroupAction = React.forwardRef< HTMLButtonElement, React.ComponentProps<"button"> & { asChild?: boolean } >(({ className, asChild = false, ...props }, ref) => { const Comp = asChild ? Slot : "button" return ( <Comp ref={ref} data-sidebar="group-action" className={cn( "absolute right-3 top-3.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0", // Increases the hit area of the button on mobile. "after:absolute after:-inset-2 after:md:hidden", "group-data-[collapsible=icon]:hidden", className )} {...props} /> ) }) SidebarGroupAction.displayName = "SidebarGroupAction" const SidebarGroupContent = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => ( <div ref={ref} data-sidebar="group-content" className={cn("w-full text-sm", className)} {...props} /> )) SidebarGroupContent.displayName = "SidebarGroupContent" const SidebarMenu = React.forwardRef< HTMLUListElement, React.ComponentProps<"ul"> >(({ className, ...props }, ref) => ( <ul ref={ref} data-sidebar="menu" className={cn("flex w-full min-w-0 flex-col gap-1", className)} {...props} /> )) SidebarMenu.displayName = "SidebarMenu" const SidebarMenuItem = React.forwardRef< HTMLLIElement, React.ComponentProps<"li"> >(({ className, ...props }, ref) => ( <li ref={ref} data-sidebar="menu-item" className={cn("group/menu-item relative", className)} {...props} /> )) SidebarMenuItem.displayName = "SidebarMenuItem" const sidebarMenuButtonVariants = cva( "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-md p-2 text-left text-sm outline-none ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-[[data-sidebar=menu-action]]/menu-item:pr-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:!size-8 group-data-[collapsible=icon]:!p-2 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0", { variants: { variant: { default: "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground", outline: "bg-background shadow-[0_0_0_1px_hsl(var(--sidebar-border))] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_hsl(var(--sidebar-accent))]", }, size: { default: "h-8 text-sm", sm: "h-7 text-xs", lg: "h-12 text-sm group-data-[collapsible=icon]:!p-0", }, }, defaultVariants: { variant: "default", size: "default", }, } ) const SidebarMenuButton = React.forwardRef< HTMLButtonElement, React.ComponentProps<"button"> & { asChild?: boolean isActive?: boolean tooltip?: string | React.ComponentProps<typeof TooltipContent> } & VariantProps<typeof sidebarMenuButtonVariants> >( ( { asChild = false, isActive = false, variant = "default", size = "default", tooltip, className, ...props }, ref ) => { const Comp = asChild ? Slot : "button" const { isMobile, state } = useSidebar() const button = ( <Comp ref={ref} data-sidebar="menu-button" data-size={size} data-active={isActive} className={cn(sidebarMenuButtonVariants({ variant, size }), className)} {...props} /> ) if (!tooltip) { return button } if (typeof tooltip === "string") { tooltip = { children: tooltip, } } return ( <Tooltip> <TooltipTrigger asChild>{button}</TooltipTrigger> <TooltipContent side="right" align="center" hidden={state !== "collapsed" || isMobile} {...tooltip} /> </Tooltip> ) } ) SidebarMenuButton.displayName = "SidebarMenuButton" const SidebarMenuAction = React.forwardRef< HTMLButtonElement, React.ComponentProps<"button"> & { asChild?: boolean showOnHover?: boolean } >(({ className, asChild = false, showOnHover = false, ...props }, ref) => { const Comp = asChild ? Slot : "button" return ( <Comp ref={ref} data-sidebar="menu-action" className={cn( "absolute right-1 top-1.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 peer-hover/menu-button:text-sidebar-accent-foreground [&>svg]:size-4 [&>svg]:shrink-0", // Increases the hit area of the button on mobile. "after:absolute after:-inset-2 after:md:hidden", "peer-data-[size=sm]/menu-button:top-1", "peer-data-[size=default]/menu-button:top-1.5", "peer-data-[size=lg]/menu-button:top-2.5", "group-data-[collapsible=icon]:hidden", showOnHover && "group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 peer-data-[active=true]/menu-button:text-sidebar-accent-foreground md:opacity-0", className )} {...props} /> ) }) SidebarMenuAction.displayName = "SidebarMenuAction" const SidebarMenuBadge = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => ( <div ref={ref} data-sidebar="menu-badge" className={cn( "absolute right-1 flex h-5 min-w-5 items-center justify-center rounded-md px-1 text-xs font-medium tabular-nums text-sidebar-foreground
----------------------------------------

[2] source=21dev  tag=forms  score=0.800
Sidebar = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> & { side?: "left" | "right" variant?: "sidebar" | "floating" | "inset" collapsible?: "offcanvas" | "icon" | "none" } >( ( { side = "left", variant = "sidebar", collapsible = "offcanvas", className, children, ...props }, ref ) => { const { isMobile, state, openMobile, setOpenMobile } = useSidebar() if (collapsible === "none") { return ( <div className={cn( "flex h-full w-[--sidebar-width] flex-col bg-sidebar text-sidebar-foreground", className )} ref={ref} {...props} > {children} </div> ) } if (isMobile) { return ( <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}> <SheetContent data-sidebar="sidebar" data-mobile="true" className="w-[--sidebar-width] bg-sidebar p-0 text-sidebar-foreground [&>button]:hidden" style={ { "--sidebar-width": SIDEBAR_WIDTH_MOBILE, } as React.CSSProperties } side={side} > <div className="flex h-full w-full flex-col">{children}</div> </SheetContent> </Sheet> ) } return ( <div ref={ref} className="group peer hidden md:block text-sidebar-foreground" data-state={state} data-collapsible={state === "collapsed" ? collapsible : ""} data-variant={variant} data-side={side} > {/* This is what handles the sidebar gap on desktop */} <div className={cn( "duration-200 relative h-svh w-[--sidebar-width] bg-transparent transition-[width] ease-linear", "group-data-[collapsible=offcanvas]:w-0", "group-data-[side=right]:rotate-180", variant === "floating" || variant === "inset" ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4))]" : "group-data-[collapsible=icon]:w-[--sidebar-width-icon]" )} /> <div className={cn( "duration-200 fixed inset-y-0 z-10 hidden h-svh w-[--sidebar-width] transition-[left,right,width] ease-linear md:flex", side === "left" ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]" : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]", // Adjust the padding for floating and inset variants. variant === "floating" || variant === "inset" ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4)_+2px)]" : "group-data-[collapsible=icon]:w-[--sidebar-width-icon] group-data-[side=left]:border-r group-data-[side=right]:border-l", className )} {...props} > <div data-sidebar="sidebar" className="flex h-full w-full flex-col bg-sidebar group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:border-sidebar-border group-data-[variant=floating]:shadow" > {children} </div> </div> </div> ) } ) Sidebar.displayName = "Sidebar" const SidebarTrigger = React.forwardRef< React.ElementRef<typeof Button>, React.ComponentProps<typeof Button> >(({ className, onClick, ...props }, ref) => { const { toggleSidebar } = useSidebar() return ( <Button ref={ref} data-sidebar="trigger" variant="ghost" size="icon" className={cn("h-7 w-7", className)} onClick={(event) => { onClick?.(event) toggleSidebar() }} {...props} > <PanelLeft /> <span className="sr-only">Toggle Sidebar</span> </Button> ) }) SidebarTrigger.displayName = "SidebarTrigger" const SidebarRail = React.forwardRef< HTMLButtonElement, React.ComponentProps<"button"> >(({ className, ...props }, ref) => { const { toggleSidebar } = useSidebar() return ( <button ref={ref} data-sidebar="rail" aria-label="Toggle Sidebar" tabIndex={-1} onClick={toggleSidebar} title="Toggle Sidebar" className={cn( "absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] hover:after:bg-sidebar-border group-data-[side=left]:-right-4 group-data-[side=right]:left-0 sm:flex", "[[data-side=left]_&]:cursor-w-resize [[data-side=right]_&]:cursor-e-resize", "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize", "group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full group-data-[collapsible=offcanvas]:hover:bg-sidebar", "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2", "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2", className )} {...props} /> ) }) SidebarRail.displayName = "SidebarRail" const SidebarInset = React.forwardRef< HTMLDivElement, React.ComponentProps<"main"> >(({ className, ...props }, ref) => { return ( <main ref={ref} className={cn( "relative flex min-h-svh flex-1 flex-col bg-background", "peer-data-[variant=inset]:min-h-[calc(100svh-theme(spacing.4))] md:peer-data-[variant=inset]:m-2 md:peer-data-[state=collapsed]:peer-data-[variant=inset]:ml-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow", className )} {...props} /> ) }) SidebarInset.displayName = "SidebarInset" const SidebarInput = React.forwardRef< React.ElementRef<typeof Input>, React.ComponentProps<typeof Input> >(({ className, ...props }, ref) => { return ( <Input ref={ref} data-sidebar="input" className={cn( "h-8 w-full bg-background shadow-none focus-visible:ring-2 focus-visible:ring-sidebar-ring", className )} {...props} /> ) }) SidebarInput.displayName = "SidebarInput" const SidebarHeader = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => { return ( <div ref={ref} data-sidebar="header" className={cn("flex flex-col gap-2 p-2", className)} {...props} /> ) }) SidebarHeader.displayName = "SidebarHeader" const SidebarFooter = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => { return ( <div ref={ref} data-sidebar="footer" className={cn("flex flex-col gap-2 p-2", className)} {...props} /> ) }) SidebarFooter.displayName = "SidebarFooter" const SidebarSeparator = React.forwardRef< React.ElementRef<typeof Separator>, React.ComponentProps<typeof Separator> >(({ className, ...props }, ref) => { return ( <Separator ref={ref} data-sidebar="separator" className={cn("mx-2 w-auto bg-sidebar-border", className)} {...props} /> ) }) SidebarSeparator.displayName = "SidebarSeparator" const SidebarContent = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => { return ( <div ref={ref} data-sidebar="content" className={cn( "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden", className )} {...props} /> ) }) SidebarContent.displayName = "SidebarContent" const SidebarGroup = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> >(({ className, ...props }, ref) => { return ( <div ref={ref} data-sidebar="group" className={cn("relative flex w-full min-w-0 flex-col p-2", className)} {...props} /> ) }) SidebarGroup.displayName = "SidebarGroup" const SidebarGroupLabel = React.forwardRef< HTMLDivElement, React.ComponentProps<"div"> & { asChild?: boolean } >(({ className,
----------------------------------------
===================================================
=== REFS: USERMENU ===
==================================================
QUERY: UserMenu
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.757
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.756
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: CTASECTION ===
==================================================
QUERY: CTASection
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.801
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.801
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------
===================================================
=== REFS: NAVBAR ===
==================================================
QUERY: navbar navigation link header top sticky
CONTEXT (3 chunks):
============================================================

[1] source=freefrontend.com  tag=navbar  score=0.691
figure { all: unset; } } @layer base.app { body { background: black; } } @layer base.containers { .Navbar { min-block-size: var(--nav-block-size); justify-items: center; padding-inline: var(--size-fluid-3); background-color: black; } .Menu { @media (width < 1024px) { position: fixed; inset-inline: 0; inset-block-end: 0; block-size: var(--nav-block-size); overflow-x: auto; .ItemContent { display: none; } } @media (width >= 768px) { .NavIcon { display: none; } } @media (width < 768px) { .NavLink:hover { text-decoration: none; } .NavLinkTitle { display: none; } } } .NavItem { block-size: 100%; position: relative; } .ItemContent { background-color: white; border-radius: var(--radius-3); box-shadow: var(--shadow-4); inline-size: max(100%, 370px); inset-block-start: var(--nav-block-size); opacity: 0; padding: var(--size-8); position: absolute; transition: 0.2s ease; visibility: hidden; z-index: var(--layer-3); a { color: black; text-decoration: none; display: flex; justify-content: space-between; gap: var(--size-5); transition: 0.2s ease; &::after { font-family: 'Inter', sans-serif; content: '\2191'; font-weight: bold; color: var(--brand); display: inline-flex; rotate: 90deg; opacity: 0; transform: translateY(10px); transition: 0.2s ease; } &:is(:focus-visible, :hover) { color: var(--brand); &::after { opacity: 1; transform: translateY(0px); } } } .NavItem:hover & { visibility: visible; opacity: 1; } .NavItem:focus-within & { visibility: visible; opacity: 1; } } .Main { grid-template-rows: 1fr min-content; :is(img, picture) { object-fit: cover; block-size: 100%; inline-size: 100%; background: var(--gradient-8); } } .CarouselWrapper { overflow-x: hidden; } .Carousel { animation: slide 20s cubic-bezier(0.77, 0, 0.18, 1) forwards infinite; > figure { inline-size: 100dvi; block-size: calc(100dvb - var(--nav-block-size) - var(--size-9)); overflow: hidden; } } footer { block-size: var(--size-9); @media (width < 1024px) { display: none; } } } @layer base.components { .Logo { inline-size: var(--size-11); margin: 0; padding: 0; } .NavLink { padding-inline: var(--size-4); block-size: 100%; color: white; background-color: inherit; font-size: var(--font-size-2); text-decoration-color: currentColor; font-weight: var(--font-weight-6); text-underline-offset: 1ex; @media (width > 1024px) { :is(.NavItem:focus-within, .NavItem:hover) & { text-decoration: underline; color: var(--brand); } } } .ButtonLink { color: white; background: var(--gradient-21); font-size: var(--font-size-2); font-weight: var(--font-weight-6); padding: var(--size-relative-2) var(--size-relative-5); border-radius: var(--radius-4); text-decoration: none; transition: filter 0.2s ease; &:hover { filter: contrast(200%); } } .ItemTitle { color: var(--brand); } .NavIcon { font-size: var(--font-size-5); font-weight: var(--font-weight-4); .NavLink:focus & { color: var(--brand); } } .CodePen { padding-inline: var(--size-fluid-3); block-size: 100%; } } @keyframes slide { 20% { transform: translateX(-100%); } 40% { transform: translateX(-200%); } 60% { transform: translateX(-300%); } 80% { transform: translateX(-400%); } 100% { transform: translateX(-500%); } } [60] Interactive 3D Workspace Diorama URL : https://freefrontend.com/code/interactive-3d-workspace-diorama-2026-02-16/ By : anon Tags : HTML36, CSS282, JavaScript218, Bootstrap65, Tailwind CSS78, html canvas api HTML <canvas class="webgl"></canvas> <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r124/three.min.js"></script> <script src="https://unpkg.com/three@0.126.0/examples/js/loaders/GLTFLoader.js"></script> <script src="https://unpkg.com/three@0.126.0/examples/js/controls/OrbitControls.js"></script> CSS *, *::after, *::before { margin: 0; padding: 0; box-sizing: border-box; outline: none; } body{ overflow: hidden; background-color: #383B50;; cursor: grab; } .webgl{ position: fixed; top: 0; left: 0; } TSX (React) const canvas = document.querySelector('.webgl') const scene = new THREE.Scene() const textureLoader = new THREE.TextureLoader() const sizes = { width: window.innerWidth, height: window.innerHeight } // Base camera const camera = new THREE.PerspectiveCamera(30, sizes.width / sizes.height, 0.1, 100) camera.position.x = 18 camera.position.y = 10 camera.position.z = 20 scene.add(camera) // Controls const controls = new THREE.OrbitControls(camera, canvas) controls.enableDamping = true controls.enableZoom = true controls.enablePan = false controls.minDistance = 10 controls.maxDistance = 20 controls.minPolarAngle = Math.PI / 4 controls.maxPolarAngle = Math.PI / 2.25 controls.minAzimuthAngle = - Math.PI / 16 controls.maxAzimuthAngle = Math.PI / 2 // Renderer const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true }) renderer.setSize(sizes.width, sizes.height) renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)) renderer.outputEncoding = THREE.sRGBEncoding // Materials const bakedTexture = textureLoader.load('https://rawcdn.githack.com/ricardoolivaalonso/ThreeJS-Room01/98fd8d7909308ec03a596928a394bb25ed9239f1/baked.jpg') bakedTexture.flipY = false bakedTexture.encoding = THREE.sRGBEncoding const bakedMaterial = new THREE.MeshBasicMaterial({ map: bakedTexture, side: THREE.DoubleSide, }) //Loader const loader = new THREE.GLTFLoader() loader.load('https://rawcdn.githack.com/ricardoolivaalonso/ThreeJS-Room01/98fd8d7909308ec03a596928a394bb25ed9239f1/THREEJS2.glb', (gltf) => { const model = gltf.scene model.traverse( child => child.material = bakedMaterial ) scene.position.set(0,-2,0) scene.add(model) }, ( xhr ) => { console.log( (
----------------------------------------

[2] source=freefrontend.com  tag=navbar  score=0.686
0.15); } .nav-link.active { background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1)); color: white; box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3), 0 4px 12px rgba(0, 0, 0, 0.1); } .nav-icon { width: 16px; height: 16px; fill: currentColor; transition: transform 0.3s ease; } .nav-link:hover .nav-icon { transform: scale(1.1); } /* MOBILE MENU TOGGLE */ .mobile-toggle { display: none; background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer; padding: 8px; border-radius: 50%; transition: all 0.3s ease; z-index: 1001; position: relative; flex-shrink: 0; } .mobile-toggle:hover { background: rgba(255, 255, 255, 0.1); transform: scale(1.1); } .hamburger { display: flex; flex-direction: column; gap: 4px; width: 24px; height: 18px; justify-content: center; } .hamburger span { width: 24px; height: 2px; background: white; border-radius: 2px; transition: all 0.3s ease; display: block; } .mobile-toggle.active .hamburger span:nth-child(1) { transform: rotate(45deg) translate(6px, 6px); } .mobile-toggle.active .hamburger span:nth-child(2) { opacity: 0; transform: translateX(-20px); } .mobile-toggle.active .hamburger span:nth-child(3) { transform: rotate(-45deg) translate(6px, -6px); } /* CTA BUTTON */ .cta-button { background: linear-gradient(135deg, #ff6b6b, #ee5a52); color: white; text-decoration: none; padding: 10px 20px; border-radius: 25px; font-weight: 600; font-size: 0.9rem; box-shadow: 0 8px 20px rgba(255, 107, 107, 0.3); transition: all 0.3s ease; white-space: nowrap; margin-left: 5px; } .cta-button:hover { transform: translateY(-1px); box-shadow: 0 10px 20px rgba(255, 107, 107, 0.4); }/* MOBILE RESPONSIVE */ @media (max-width: 992px) { .navbar-container { top: 20px; width: calc(100% - 30px); } .navbar { padding: 12px 20px; position: relative; } .mobile-toggle { display: flex !important; align-items: center; justify-content: center; } /* Hide desktop navigation on mobile */ .navbar-nav { display: none; } .brand-text { font-size: 1.2rem; } } /* Mobile Menu Overlay */ .mobile-menu-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(0, 0, 0, 0.8); backdrop-filter: blur(10px); z-index: 1500; opacity: 0; visibility: hidden; transition: all 0.3s ease; } .mobile-menu-overlay.active { opacity: 1; visibility: visible; } /* Mobile Menu Container */ .mobile-menu { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); z-index: 1600; transform: translateY(-100%); transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94); overflow-y: auto; } .mobile-menu.active { transform: translateY(0); } /* Mobile Menu Header */ .mobile-menu-header { display: flex; justify-content: space-between; align-items: center; padding: 30px 30px 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); } .mobile-menu-brand { display: flex; align-items: center; gap: 12px; text-decoration: none; color: white; font-weight: 700; font-size: 1.4rem; } .mobile-menu-close { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; padding: 8px; border-radius: 50%; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; } .mobile-menu-close:hover { background: rgba(255, 255, 255, 0.1); transform: scale(1.1); } /* Mobile Menu Navigation */ .mobile-menu-nav { padding: 40px 30px; list-style: none; } .mobile-menu-item { margin-bottom: 8px; } .mobile-menu-link { display: flex; align-items: center; gap: 16px; padding: 20px 24px; text-decoration: none; color: rgba(255, 255, 255, 0.9); font-weight: 500; font-size: 1.1rem; border-radius: 20px; transition: all 0.3s ease; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 12px; } .mobile-menu-link:hover, .mobile-menu-link.active { background: rgba(255, 255, 255, 0.15); color: white; transform: translateX(8px); border-color: rgba(255, 255, 255, 0.2); } .mobile-menu-icon { width: 24px; height: 24px; fill: currentColor; } .mobile-cta { margin: 30px 30px 40px; } .mobile-cta-button { display: block; width: 100%; background: linear-gradient(135deg, #ff6b6b, #ee5a52); color: white; text-decoration: none; padding: 20px; border-radius: 20px; font-weight: 600; font-size: 1.1rem; text-align: center; box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3); transition: all 0.3s ease; } .mobile-cta-button:hover { transform: translateY(-2px); box-shadow: 0 15px 40px rgba(255, 107, 107, 0.4); } @media (max-width: 768px) { .navbar-container { width: calc(100% - 30px); } } @media (max-width: 480px) { .navbar-container { width: calc(100% - 20px); top: 15px; }
----------------------------------------

[3] source=freefrontend.com  tag=navbar  score=0.676
padding: 25px; } .fancy-nav__close-btn { width: 30px; height: 30px; margin-bottom: 25px; transform: translateY(-30px); opacity: 0; &:before, &:after { width: 130%; height: 5px; } &:before { left: 3px; } &.is-visible { @include transition-mix($delay: 0.2s); transform: translateY(0); opacity: 1; visibility: visible; } } } @media (min-width: 1400px) { .fancy-nav__item { width: 25%; height: 100%; &:not(:last-child) { border-right: 2px solid $border-color--light; } &:not(:nth-last-child(-n + 2)) { border-bottom: none; } } .fancy-nav__item-details { padding: 40px; } .fancy-nav__tab-title { font-size: 2rem; } .fancy-nav__tab { padding: 40px; } .fancy-nav__close-btn { margin-bottom: 40px; } .fancy-nav__tab-description { padding: 40px; } } TSX (React) // https://github.com/nat-davydova/fancy-navigation-block const DOM = { item: ".fancy-nav__item", itemList: ".fancy-nav__list", images: ".fancy-nav__img", tabList: ".fancy-nav__tabs", tab: ".fancy-nav__tab", tabCloseBtn: ".fancy-nav__close-btn", tabImg: ".fancy-nav__tab-img", tabDescr: ".fancy-nav__tab-description", isVisible: "is-visible" }; const fancyItemList = document.querySelector(DOM.itemList); const fancyItems = document.querySelectorAll(DOM.item); const fancyTabList = document.querySelector(DOM.tabList); const fancyTabs = document.querySelectorAll(DOM.tab); function openFancyTab(currentIndex) { fancyTabList.classList.add(DOM.isVisible); const currentTab = fancyTabs[currentIndex]; currentTab.classList.add(DOM.isVisible); addAnimationClassesOnTabOpen(currentTab); } function closeFancyTab(currentIndex) { fancyTabList.classList.remove(DOM.isVisible); const currentTab = fancyTabs[currentIndex]; currentTab.classList.remove(DOM.isVisible); removeAnimationClassesOnTabClose(currentTab); } function addAnimationClassesOnTabOpen(currentTab) { const currentTabCloseBtn = currentTab.querySelector(DOM.tabCloseBtn); currentTabCloseBtn.classList.add(DOM.isVisible); const currentTabImg = currentTab.querySelector(DOM.tabImg); currentTabImg.classList.add(DOM.isVisible); const currentTabDescr = currentTab.querySelector(DOM.tabDescr); currentTabDescr.classList.add(DOM.isVisible); } function removeAnimationClassesOnTabClose(currentTab) { const currentTabCloseBtn = currentTab.querySelector(DOM.tabCloseBtn); currentTabCloseBtn.classList.remove(DOM.isVisible); const currentTabImg = currentTab.querySelector(DOM.tabImg); currentTabImg.classList.remove(DOM.isVisible); const currentTabDescr = currentTab.querySelector(DOM.tabDescr); currentTabDescr.classList.remove(DOM.isVisible); } function getCurrentElemIndex(list, item) { const currentIndex = Array.from(list).indexOf(item); return currentIndex; } function changeMainImage(currentIndex) { const fancyImgs = document.querySelectorAll(DOM.images); fancyImgs.forEach((imgElem, index) => { imgElem.style.opacity = 0; if (index === currentIndex) { imgElem.style.opacity = 1; } }); } fancyItemList.addEventListener("mouseover", (event) => { const target = event.target; if (target.closest(DOM.item)) { const currentFancyItemIndex = getCurrentElemIndex( fancyItems, target.closest(DOM.item) ); changeMainImage(currentFancyItemIndex); } }); fancyItemList.addEventListener("click", (event) => { const target = event.target; if (target.closest(DOM.item)) { const currentFancyItemIndex = getCurrentElemIndex( fancyItems, target.closest(DOM.item) ); openFancyTab(currentFancyItemIndex); } }); fancyTabList.addEventListener("click", (event) => { const target = event.target; if (target.closest(DOM.tabCloseBtn)) { const currentFancyItemIndex = getCurrentElemIndex( fancyTabs, target.closest(DOM.tab) ); closeFancyTab(currentFancyItemIndex); } }); [118] Mouse-Tracking Linear Shine Button URL : https://freefrontend.com/code/mouse-tracking-linear-shine-button-2026-02-04/ By : anon Tags : HTML36, CSS282, JavaScript218, Bootstrap65, Tailwind CSS78, tailwind buttons, css gradient, css radial gradient, css mix blend mode HTML <div id="root"></div> CSS body { background-color: #000; } .shine { background-image: repeating-linear-gradient( 125deg, transparent 0%, transparent 15%, #fff4 25%, transparent 35%, transparent 50% ); background-size: 200%; background-position: calc(var(--mx) + 20%) var(--my); } .glow { background-image: radial-gradient( 100% 50% at calc(50% - var(--mx)) 0%, #fff4 0%, transparent 80% ), radial-gradient( 100% 50% at calc(var(--mx) + 50%) 100%, #fff4 0%, transparent 80% ) } TSX (React) import React, { useRef, useState } from "https://esm.sh/react@18.2.0"; import ReactDOM from "https://esm.sh/react-dom@18.2.0"; function App() { return (React.createElement("div", { className: "w-screen h-screen flex items-center justify-center text-white" }, React.createElement(Button, null))); } function Button() { const buttonRef = useRef(null); const [mouseX, setMouseX] = useState(0.5); const [mouseY, setMouseY] = useState(0.5); const mouseMove = (e) => { const rect = buttonRef.current.getBoundingClientRect(); setMouseX((e.clientX - rect.left) / rect.width); setMouseY((e.clientY - rect.top) / rect.height); }; return (React.createElement("button", { ref: buttonRef, onPointerMove: mouseMove, className: "group relative py-3.5 px-7 rounded-[20px] bg-zinc-800 overflow-hidden" }, React.createElement("div", { className: "absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300", style: { "--mx": `${mouseX * 100}%`, "--my": `${mouseY * 100}%` } }, React.createElement("div", { className: "absolute inset-0 glow" }), React.createElement("div", { className: "absolute inset-0 shine mix-blend-screen" })), React.createElement("div", { className: "absolute inset-0.5 rounded-[18px] bg-zinc-900/75" }), React.createElement("div", { className: "relative text-zinc-300 group-hover:text-zinc-50 transition-colors duration-100" }, "Shiny Button"))); } const root = ReactDOM.createRoot(document.getElementById("root")); root.render(React.createElement(App, null)); [119] Scroll-Driven Image Swapper URL : https://freefrontend.com/code/scroll-driven-image-swapper-2026-02-04/ By : anon Tags : HTML36, CSS282, JavaScript218, Bootstrap65, Tailwind CSS78, js scroll effects, js gallery, js parallax, css gradient, css scroll driven, css mix blend mode HTML <header> <h1><span>All-New</span>CSS Pro</h1> <h2>Scroll-driven crossfades</h2> </header> <main> <section> <div class="image-box"> <div class="swapper"> <div class="progress"> <div><div></div></div> <div><div></div></div> </div> <div class="caption"> <h2>Tiny amounts of CSS</h2> <p>Scroll-driven animations give you the ability to
----------------------------------------
===================================================
=== REFS: HEROSECTION ===
==================================================
QUERY: HeroSection
CONTEXT (2 chunks):
============================================================

[1] source=21dev  tag=animations  score=0.771
} [454] Hero URL : https://21st.dev/community/components/hero CSS https://cdn.21st.dev/user_Codehagen/hero.compiled.css TSX (React) "use client"; import { motion } from "framer-motion"; import { buttonVariants } from "@/components/ui/button"; import { cn } from "@/lib/utils"; import Link from "next/link"; import HeroBadge from "@/components/ui/hero-badge"; const ease = [0.16, 1, 0.3, 1]; interface HeroContentProps { title: string; titleHighlight?: string; description: string; primaryAction?: { href: string; text: string; icon?: React.ReactNode; }; secondaryAction?: { href: string; text: string; icon?: React.ReactNode; }; } function HeroContent({ title, titleHighlight, description, primaryAction, secondaryAction, }: HeroContentProps) { return ( <div className="flex flex-col space-y-4"> <motion.h1 className="text-4xl font-bold tracking-tight sm:text-6xl lg:text-7xl xl:text-8xl" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, ease }} > {title}{" "} {titleHighlight && ( <span className="text-primary">{titleHighlight}</span> )} </motion.h1> <motion.p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-xl sm:leading-8" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1, duration: 0.8, ease }} > {description} </motion.p> <motion.div className="flex flex-col sm:flex-row gap-4 pt-4" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2, duration: 0.8, ease }} > {primaryAction && ( <Link href={primaryAction.href} className={cn( buttonVariants({ size: "lg" }), "gap-2 w-full sm:w-auto justify-center" )} > {primaryAction.icon} {primaryAction.text} </Link> )} {secondaryAction && ( <Link href={secondaryAction.href} className={cn( buttonVariants({ variant: "outline", size: "lg" }), "gap-2 w-full sm:w-auto justify-center" )} > {secondaryAction.icon} {secondaryAction.text} </Link> )} </motion.div> </div> ); } interface HeroProps { pill?: { href?: string; text: string; icon?: React.ReactNode; endIcon?: React.ReactNode; variant?: "default" | "outline" | "ghost"; size?: "sm" | "md" | "lg"; className?: string; }; content: HeroContentProps; preview?: React.ReactNode; } const Hero = ({ pill, content, preview }: HeroProps) => { return ( <div className="container relative overflow-hidden"> <div className="flex min-h-[calc(100vh-64px)] flex-col lg:flex-row items-center py-8 px-4 md:px-8 lg:px-12"> <div className="flex flex-col gap-4 w-full lg:max-w-2xl"> {pill && <HeroBadge {...pill} />} <HeroContent {...content} /> </div> {preview && ( <div className="w-full lg:max-w-xl lg:pl-16 mt-12 lg:mt-0"> {preview} </div> )} </div> </div> ); }; export { Hero }; [455] Features 4 URL : https://21st.dev/community/components/features-4 TSX (React) import { Cpu, Fingerprint, Pencil, Settings2, Sparkles, Zap } from 'lucide-react' export function Features() { return ( <section className="py-12 md:py-20"> <div className="mx-auto max-w-5xl space-y-8 px-6 md:space-y-16"> <div className="relative z-10 mx-auto max-w-xl space-y-6 text-center md:space-y-12"> <h2 className="text-balance text-4xl font-medium lg:text-5xl">The foundation for creative teams management</h2> <p>Lyra is evolving to be more than just the models. It supports an entire to the APIs and platforms helping developers and businesses innovate.</p> </div> <div className="relative mx-auto grid max-w-2xl lg:max-w-4xl divide-x divide-y border *:p-12 sm:grid-cols-2 lg:grid-cols-3"> <div className="space-y-3"> <div className="flex items-center gap-2"> <Zap className="size-4" /> <h3 className="text-sm font-medium">Faaast</h3> </div> <p className="text-sm">It supports an entire helping developers and innovate.</p> </div> <div className="space-y-2"> <div className="flex items-center gap-2"> <Cpu className="size-4" /> <h3 className="text-sm font-medium">Powerful</h3> </div> <p className="text-sm">It supports an entire helping developers and businesses.</p> </div> <div className="space-y-2"> <div className="flex items-center gap-2"> <Fingerprint className="size-4" /> <h3 className="text-sm font-medium">Security</h3> </div> <p className="text-sm">It supports an helping developers businesses.</p> </div> <div className="space-y-2"> <div className="flex items-center gap-2"> <Pencil className="size-4" /> <h3 className="text-sm font-medium">Customization</h3> </div> <p className="text-sm">It supports helping developers and businesses innovate.</p> </div> <div className="space-y-2"> <div className="flex items-center gap-2"> <Settings2 className="size-4" /> <h3 className="text-sm font-medium">Control</h3> </div> <p className="text-sm">It supports helping developers and businesses innovate.</p> </div> <div className="space-y-2"> <div className="flex items-center gap-2"> <Sparkles className="size-4" /> <h3 className="text-sm font-medium">Built for AI</h3> </div> <p className="text-sm">It supports helping developers and businesses innovate.</p> </div> </div> </div> </section> ) } [456] Faq Section URL : https://21st.dev/community/components/faq-section CSS https://cdn.21st.dev/user_tommyjepsen/faq-section.compiled.css TSX (React) import { Check, PhoneCall } from "lucide-react"; import { Badge } from "@/components/ui/badge"; import { Accordion, AccordionContent, AccordionItem, AccordionTrigger, } from "@/components/ui/accordion"; import { Button } from "@/components/ui/button"; function FAQ() { return ( <div className="w-full py-20 lg:py-40"> <div className="container mx-auto"> <div className="grid lg:grid-cols-2
----------------------------------------

[2] source=21dev  tag=effects  score=0.765
{ hidden: { opacity: 0, filter: 'blur(12px)', y: 12, }, visible: { opacity: 1, filter: 'blur(0px)', y: 0, transition: { type: 'spring', bounce: 0.3, duration: 1.5, }, }, }, } export function HeroSection() { return ( <> <HeroHeader /> <main className="overflow-hidden"> <section> <div className="relative pt-24"> <div className="absolute inset-0 -z-10 size-full [background:radial-gradient(125%_125%_at_50%_100%,transparent_0%,var(--background)_75%)]"></div> <div className="mx-auto max-w-5xl px-6"> <div className="sm:mx-auto lg:mr-auto"> <AnimatedGroup variants={{ container: { visible: { transition: { staggerChildren: 0.05, delayChildren: 0.75, }, }, }, ...transitionVariants, }} > <h1 className="mt-8 max-w-2xl text-balance text-5xl font-medium md:text-6xl lg:mt-16"> Build and Ship 10x faster with NS </h1> <p className="mt-8 max-w-2xl text-pretty text-lg"> Tailwindcss highly customizable components for building modern websites and applications that look and feel the way you mean it. </p> <div className="mt-12 flex items-center gap-2"> <div key={1} className="bg-foreground/10 rounded-[14px] border p-0.5"> <Button asChild size="lg" className="rounded-xl px-5 text-base"> <Link href="#link"> <span className="text-nowrap">Start Building</span> </Link> </Button> </div> <Button key={2} asChild size="lg" variant="ghost" className="h-[42px] rounded-xl px-5 text-base"> <Link href="#link"> <span className="text-nowrap">Request a demo</span> </Link> </Button> </div> </AnimatedGroup> </div> </div> <AnimatedGroup variants={{ container: { visible: { transition: { staggerChildren: 0.05, delayChildren: 0.75, }, }, }, ...transitionVariants, }}> <div className="relative -mr-56 mt-8 overflow-hidden px-2 sm:mr-0 sm:mt-12 md:mt-20"> <div aria-hidden className="bg-gradient-to-b to-background absolute inset-0 z-10 from-transparent from-35%" /> <div className="inset-shadow-2xs ring-background dark:inset-shadow-white/20 bg-background relative mx-auto max-w-5xl overflow-hidden rounded-2xl border p-4 shadow-lg shadow-zinc-950/15 ring-1"> <img className="bg-background aspect-15/8 relative hidden rounded-2xl dark:block" src="https://tailark.com/_next/image?url=%2Fmail2.png&w=3840&q=75" alt="app screen" width="2700" height="1440" /> <img className="z-2 border-border/25 aspect-15/8 relative rounded-2xl border dark:hidden" src="https://tailark.com/_next/image?url=%2Fmail2-light.png&w=3840&q=75" alt="app screen" width="2700" height="1440" /> </div> </div> </AnimatedGroup> </div> </section> <section className="bg-background pb-16 pt-16 md:pb-32"> <div className="group relative m-auto max-w-5xl px-6"> <div className="absolute inset-0 z-10 flex scale-95 items-center justify-center opacity-0 duration-500 group-hover:scale-100 group-hover:opacity-100"> <Link href="/" className="block text-sm duration-150 hover:opacity-75"> <span> Meet Our Customers</span> <ChevronRight className="ml-1 inline-block size-3" /> </Link> </div> <div className="group-hover:blur-xs mx-auto mt-12 grid max-w-2xl grid-cols-4 gap-x-12 gap-y-8 transition-all duration-500 group-hover:opacity-50 sm:gap-x-16 sm:gap-y-14"> <div className="flex"> <img className="mx-auto h-5 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/nvidia.svg" alt="Nvidia Logo" height="20" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-4 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/column.svg" alt="Column Logo" height="16" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-4 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/github.svg" alt="GitHub Logo" height="16" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-5 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/nike.svg" alt="Nike Logo" height="20" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-5 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/lemonsqueezy.svg" alt="Lemon Squeezy Logo" height="20" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-4 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/laravel.svg" alt="Laravel Logo" height="16" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-7 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/lilly.svg" alt="Lilly Logo" height="28" width="auto" /> </div> <div className="flex"> <img className="mx-auto h-6 w-fit dark:invert" src="https://html.tailus.io/blocks/customers/openai.svg" alt="OpenAI Logo" height="24" width="auto" /> </div> </div> </div> </section> </main> </> ) } const menuItems = [ { name: 'Features', href: '#link' }, { name: 'Solution', href: '#link' }, { name: 'Pricing', href: '#link' }, { name: 'About', href: '#link' }, ] export const HeroHeader = () => { const [menuState, setMenuState] = React.useState(false) const [scrolled, setScrolled] = React.useState(false) const { scrollYProgress } = useScroll() React.useEffect(() => { const unsubscribe = scrollYProgress.on('change', (latest) => { setScrolled(latest > 0.05) }) return () => unsubscribe() }, [scrollYProgress]) return ( <header> <nav data-state={menuState && 'active'} className={cn('group fixed z-20 w-full border-b transition-colors duration-150', scrolled && 'bg-background/50 backdrop-blur-3xl')}> <div className="mx-auto max-w-5xl px-6 transition-all duration-300"> <div className="relative flex flex-wrap items-center justify-between gap-6 py-3 lg:gap-0 lg:py-4"> <div className="flex w-full items-center justify-between gap-12 lg:w-auto"> <Link href="/" aria-label="home" className="flex items-center space-x-2"> <Logo /> </Link> <button onClick={() => setMenuState(!menuState)} aria-label={menuState == true ? 'Close Menu' : 'Open Menu'} className="relative z-20 -m-2.5 -mr-4 block cursor-pointer p-2.5 lg:hidden"> <Menu className="group-data-[state=active]:rotate-180 group-data-[state=active]:scale-0 group-data-[state=active]:opacity-0 m-auto size-6 duration-200" /> <X className="group-data-[state=active]:rotate-0 group-data-[state=active]:scale-100 group-data-[state=active]:opacity-100 absolute inset-0 m-auto size-6 -rotate-180 scale-0 opacity-0 duration-200" /> </button> <div className="hidden lg:block"> <ul className="flex gap-8 text-sm"> {menuItems.map((item, index) => ( <li key={index}> <Link href={item.href}
----------------------------------------
===================================================
=== REFS: TESTIMONIALSSECTION ===
==================================================
QUERY: TestimonialsSection
CONTEXT (2 chunks):
============================================================

[1] source=templates  tag=cards  score=0.771
## Tailwind CSS Dashboard Templates for Your Projects

Explore top Tailwind CSS dashboard templates that cater to various project needs, from enterprise solutions to budget-friendly options.

Sunday, February 9, 2025 Build Beautiful GUIs With Reactjs Explore how ReactJS simplifies UI development with reusable components, efficient data management, and powerful styling options for modern applications. READ MORE

Explore how ReactJS simplifies UI development with reusable components, efficient data management, and powerful styling options for modern applications.

Tuesday, December 24, 2024 Best Graphic Design Tools for 2025 Best Graphic Design Tools for 2025 READ MORE

Wednesday, September 4, 2024 10 Best Vue 3 UI Component Libraries 2024 Explore the top 10 Vue 3 UI component libraries of 2024 to enhance your projects with versatile and customizable options. READ MORE
----------------------------------------

[2] source=floatui.com  tag=cards  score=0.771
## Tailwind CSS Dashboard Templates for Your Projects

Explore top Tailwind CSS dashboard templates that cater to various project needs, from enterprise solutions to budget-friendly options.

Sunday, February 9, 2025 Build Beautiful GUIs With Reactjs Explore how ReactJS simplifies UI development with reusable components, efficient data management, and powerful styling options for modern applications. READ MORE

Explore how ReactJS simplifies UI development with reusable components, efficient data management, and powerful styling options for modern applications.

Tuesday, December 24, 2024 Best Graphic Design Tools for 2025 Best Graphic Design Tools for 2025 READ MORE

Wednesday, September 4, 2024 10 Best Vue 3 UI Component Libraries 2024 Explore the top 10 Vue 3 UI component libraries of 2024 to enhance your projects with versatile and customizable options. READ MORE
----------------------------------------
===================================================
=== REFS: BENEFITSSECTION ===
==================================================
QUERY: BenefitsSection
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.778
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[7]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[8]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[9]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

[2] source=templates  tag=cards  score=0.778
## Responsive SVG UI Components: How-To Guide

Learn how to create scalable SVG UI components that adapt to any screen size, ensuring fast loading and crisp graphics across devices.

[12]  Tailwind UI Free
URL  : https://floatui.com/tailwind-ui-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates built on top of React/Nextjs with Tailwind CSS. It offers several benefits for web development, including:

Consistent and polished designs: Float UI provides a cohesive set of components with a unified visual language, ensuring consistency in design and enhancing the overall user experience.

Increased productivity: With Float UI's intuitive customizable styles, developers can work more efficiently, iterate quickly, and focus on implementing business logic and user interactions.

Lightweight and performant: Float UI is designed to prioritize performance without sacrificing functionality. The library is optimized for speed and efficiency, enabling faster load times and smooth interactions, resulting in a snappy and delightful user experience.

Saves development time and effort: Float UI's extensive collection of pre-designed components significantly reduces the time and effort required for visual design, allowing developers to focus on implementing business logic.

Extensible: Float UI is not only powerful out of the box but also highly extensible. Developers can extend its functionality with custom modifiers and integrate it with other libraries.

Overall, Float UI is a versatile and powerful tool for creating dynamic, responsive, and engaging web interfaces. It is free, open-source, and backed by a helpful community support.

Float UI offer components created with React, Vue.js, Svelte, HTML, and Alpine.js. Additionally, we leverage the following libraries for interactive components:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.

[13]  Tailwind Templates
URL  : https://floatui.com/tailwind-templates

  CODE 
absolute inset-x-0 mx-auto duration-500 top-0 -translate-x-32 sm:-translate-x-10 w-full sm:w-[653px]

M229.488 -100.921L557.588 270.669L419.698 348.86L95.3076 17.5558L229.488 -100.921Z

mt-32 space-y-7 divide-y divide-zinc-800 gap-14 grid-cols-2 lg:grid lg:space-y-0 lg:divide-y-0

[14]  Tailwind Components Free
URL  : https://floatui.com/tailwind-components-free

  CODE 
Best shadcn/ui blocks and components for your next project.

At Float UI, we believe in making web development faster and more accessible for everyone. Explore our collection of handcrafted, open-source Tailwind CSS components that you can use in your projects without any cost.

Float UI is a collection of modern UI components and website templates, built on top of React/Nextjs with Tailwind CSS, the components are beautiful designed, expertly crafted, allow you to build beautiful websites.

First, Float UI is fully free, and open source, you don't need to pay anything to use it, and we are working on it full-time, so we'll keep improving, and adding more UIs, the second thing if you re working on a large project that requires a high level of UI customization or you find yourself repeating the same UI patterns across projects, consider creating an internal UI library, and in this case Float UI is a great choice. You should definitely use it.

We Provide Support for Components Developed Using React, Vue.js, Svelte, HTML, and Alpine.js.
And for the interactive components we use the following Libraries:

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

Unstyled, accessible components for building high quality design systems and web apps in Vue.

An open-source Svelte library for building high-quality, accessible design systems and web apps.

Alpine is a rugged, minimal tool for composing behavior directly in your markup.
----------------------------------------

### FINAL INSTRUCTION:
Generate clean, modular React components. Every AST node MUST have a corresponding file. No monolithic files. No arbitrary wrappers. Direct Tailwind injection.
