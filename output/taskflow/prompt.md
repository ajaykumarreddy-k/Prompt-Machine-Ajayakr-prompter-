# TaskFlow — Frontend Prompt

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
              "Display navigation options"
            ]
          },
          {
            "type": "StatCard",
            "props": [
              {
                "title": "Total Tasks"
              },
              {
                "stats": 100
              }
            ],
            "responsibilities": [
              "Display statistical information about tasks"
            ]
          },
          {
            "type": "ActivityFeed",
            "props": [
              {
                "items": []
              }
            ],
            "responsibilities": [
              "Show recent activities or events"
            ]
          },
          {
            "type": "CreateTaskModal",
            "props": [],
            "responsibilities": [
              "Allow users to create new tasks"
            ]
          },
          {
            "type": "Modals",
            "props": [],
            "responsibilities": [
              "Handle various modal dialogs"
            ]
          },
          {
            "type": "Button",
            "props": [
              {
                "title": "Action"
              }
            ],
            "responsibilities": [
              "Trigger actions or events"
            ]
          },
          {
            "type": "DataGrid",
            "props": [
              {
                "items": []
              }
            ],
            "responsibilities": [
              "Display tabular data"
            ]
          },
          {
            "type": "KanbanColumn",
            "props": [
              {
                "title": "In Progress"
              },
              {
                "items": []
              }
            ],
            "responsibilities": [
              "Show tasks in a column of the Kanban board"
            ]
          },
          {
            "type": "Kanban Board",
            "props": [],
            "responsibilities": [
              "Display and manage tasks on a Kanban board"
            ]
          },
          {
            "type": "TaskDetailModal",
            "props": [
              {
                "task": {}
              }
            ],
            "responsibilities": [
              "Show detailed information about a task"
            ]
          },
          {
            "type": "BoardContainer",
            "props": [],
            "responsibilities": [
              "Contain the Kanban board components"
            ]
          },
          {
            "type": "InputField",
            "props": [
              {
                "placeholder": "Search"
              }
            ],
            "responsibilities": [
              "Allow users to input text for search or filtering"
            ]
          },
          {
            "type": "ChartWidget",
            "props": [
              {
                "data": []
              }
            ],
            "responsibilities": [
              "Display charts or graphs related to data"
            ]
          },
          {
            "type": "UserMenu",
            "props": [],
            "responsibilities": [
              "Provide user-specific actions and options"
            ]
          },
          {
            "type": "TaskCard",
            "props": [
              {
                "task": {}
              }
            ],
            "responsibilities": [
              "Show a card for a specific task"
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
              "Display navigation options"
            ]
          },
          {
            "type": "ChartWidget",
            "props": [
              {
                "data": []
              }
            ],
            "responsibilities": [
              "Display charts or graphs related to analytics data"
            ]
          },
          {
            "type": "DataGrid",
            "props": [
              {
                "items": []
              }
            ],
            "responsibilities": [
              "Show tabular data for analytics"
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
              "Display navigation options"
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
- Navbar: Display navigation options
- StatCard: Display statistical information about tasks
- ActivityFeed: Show recent activities or events
- CreateTaskModal: Allow users to create new tasks
- Modals: Handle various modal dialogs
- Button: Trigger actions or events
- DataGrid: Display tabular data
- KanbanColumn: Show tasks in a column of the Kanban board
- Kanban Board: Display and manage tasks on a Kanban board
- TaskDetailModal: Show detailed information about a task
- BoardContainer: Contain the Kanban board components
- InputField: Allow users to input text for search or filtering
- ChartWidget: Display charts or graphs related to data
- UserMenu: Provide user-specific actions and options
- TaskCard: Show a card for a specific task
- Navbar: Display navigation options
- ChartWidget: Display charts or graphs related to analytics data
- DataGrid: Show tabular data for analytics
- Navbar: Display navigation options

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
  - `src/components/`: ActivityFeed, BoardContainer, Button, ChartWidget, CreateTaskModal, DataGrid, InputField, Kanban Board, KanbanColumn, Modals, Navbar, StatCard, TaskCard, TaskDetailModal, UserMenu
  - `src/App.jsx`: Routing definitions for /, /analytics, /settings

### 5. KNOWLEDGE BASE INTELLIGENCE
===================================================
=== REFS: CREATETASKMODAL ===
==================================================
QUERY: CreateTaskModal
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.746
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

[2] source=templates  tag=cards  score=0.745
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
=== REFS: MODALS ===
==================================================
QUERY: Modals
CONTEXT (2 chunks):
============================================================

[1] source=olayouts  tag=animations  score=0.789
} to { transform: translateX(-100%); } } } @import "tailwindcss"; @theme { --animate-infinite-scroll: infinite-scroll 25s linear infinite; @keyframes infinite-scroll { from { transform: translateX(0); } to { transform: translateX(-100%); } } } [30] Animated Dialog URL : https://www.ui-layouts.com/components/dialog CODE npx uilayouts@latest add dialog npx uilayouts@latest add dialog [31] Media Modals URL : https://www.ui-layouts.com/components/media-modal CODE npx uilayouts@latest add media-modal npx uilayouts@latest add media-modal [32] Linear Card URL : https://www.ui-layouts.com/components/linear-modal CODE npx uilayouts@latest add linear-modal npx uilayouts@latest add linear-modal [33] SKIPPED https://www.ui-layouts.com/components/gallery-modal [34] Responsive Modal URL : https://www.ui-layouts.com/components/responsive-modal CODE npx uilayouts@latest add responsive-modal npx uilayouts@latest add responsive-modal export default function RootLayout({ children, }: Readonly<{ children: React.ReactNode; }>) { return ( <html lang='en'> <body className={poppins.className}> <div vaul-drawer-wrapper=''>{children}</div> </body> </html> ); } export default function RootLayout({ children, }: Readonly<{ children: React.ReactNode; }>) { return ( <html lang='en'> <body className={poppins.className}> <div vaul-drawer-wrapper=''>{children}</div> </body> </html> ); } [35] Directional Drawer URL : https://www.ui-layouts.com/components/directional-drawer CODE npx uilayouts@latest add directional-drawer npx uilayouts@latest add directional-drawer [36] Motion Drawer URL : https://www.ui-layouts.com/components/motion-drawer CODE npx uilayouts@latest add motion-drawer npx uilayouts@latest add motion-drawer (isOpen: boolean) => void { open: string; close: string } { type?: 'spring' | 'tween'; damping?: number; stiffness?: number; duration?: number } { type: 'spring', damping: 25, stiffness: 120 } 'push' | 'merge' | 'stay' [37] Color Picker URL : https://www.ui-layouts.com/components/color-picker CODE npx uilayouts@latest add color-picker npx uilayouts@latest add color-picker (color: string) => void [38] SKIPPED https://www.ui-layouts.com/components/buttons [39] Motion Number URL : https://www.ui-layouts.com/components/motion-number CODE npm install @number-flow/react npm install @number-flow/react [40] Animated Range Slider URL : https://www.ui-layouts.com/components/range-slider CODE npx uilayouts@latest add slider npx uilayouts@latest add slider (value?: number) => ReactNode [41] SKIPPED https://www.ui-layouts.com/components/password [42] Tags Input URL : https://www.ui-layouts.com/components/tags-input CODE npx uilayouts@latest add tags-input npx uilayouts@latest add tags-input React.Dispatch<React.SetStateAction<string[]>> [43] Phone Input URL : https://www.ui-layouts.com/components/phone-input CODE npx uilayouts@latest add phone-input npx uilayouts@latest add phone-input [44] Datetime Picker URL : https://www.ui-layouts.com/components/datetime-picker CODE npx uilayouts@latest add datetime-input npx uilayouts@latest add datetime-input [45] Multi Selector URL : https://www.ui-layouts.com/components/multi-selector CODE npx uilayouts@latest add multi-selector npx uilayouts@latest add multi-selector { label: string; value: string; icon?: React.ComponentType; disable?: boolean; }[] (value: string[]) => void React.RefObject<HTMLButtonElement> [46] File Upload URL : https://www.ui-layouts.com/components/file-upload CODE npx uilayouts@latest add file-upload npx uilayouts@latest add file-upload (value: File[] | null) => void 'horizontal' | 'vertical' 'rtl' | 'ltr' | undefined React.Ref<HTMLDivElement> (index: number) => void Dispatch<SetStateAction<number>> 'horizontal' | 'vertical' 'rtl' | 'ltr' | undefined [47] Animated Globe URL : https://www.ui-layouts.com/components/globe CODE npx uilayouts@latest add globe npx uilayouts@latest add globe [48] Image Ripple Effect URL : https://www.ui-layouts.com/components/image-ripple-effect CODE npm install three @types/three @react-three/fiber @react-three/drei npm install three @types/three @react-three/fiber @react-three/drei const texture = useTexture('/brush.png'); const texture = useTexture('/brush.png'); // change images const texture1 = useTexture('/picture3.jpeg'); const material1 = new THREE.MeshBasicMaterial({ map: texture1 }); const image1 = new THREE.Mesh(geometry, material1); // positining image1.position.x = -0.0 * viewport.width; image1.position.y = 40; image1.position.z = 1; image1.scale.x = viewport.width / 4; image1.scale.y = viewport.width / 3.2; // change images const texture1 = useTexture('/picture3.jpeg'); const material1 = new THREE.MeshBasicMaterial({ map: texture1 }); const image1 = new THREE.Mesh(geometry, material1); // positining image1.position.x = -0.0 * viewport.width; image1.position.y = 40; image1.position.z = 1; image1.scale.x = viewport.width / 4; image1.scale.y = viewport.width / 3.2; function Images(viewport) { const scene = new THREE.Scene(); const camera = new THREE.OrthographicCamera( viewport.width / -2, viewport.width / 2, viewport.height / 2, viewport.height / -2, -1000, 1000 ); camera.position.z = 2; scene.add(camera); const geometry = new THREE.PlaneGeometry(1, 1); const group = new THREE.Group(); // !mark[//images/picture1.jpeg/] red // !mark red const texture1 = useTexture('/images/picture1.jpeg'); const material1 = new THREE.MeshBasicMaterial({ map: texture1 }); const image1 = new THREE.Mesh(geometry, material1); image1.position.x = -0.25 * viewport.width; image1.position.y = 0; image1.position.z = 1; image1.scale.x = viewport.width / 5; image1.scale.y = viewport.width
----------------------------------------

[2] source=floatui.com  tag=cards  score=0.770
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
===================================================
=== REFS: BUTTON ===
==================================================
QUERY: Button
CONTEXT (2 chunks):
============================================================

[1] source=21dev  tag=navbar  score=0.798
onClick={handleButtonClick} className={`px-6 py-4 sm:px-8 sm:py-6 rounded-full border-4 bg-[rgba(63,63,63,1)] border-card text-sm sm:text-base text-white hover:bg-[rgba(63,63,63,0.9)] transition-colors ${buttonClassName}`} > {buttonText} </button> </div> </div> </section> ) } [265] Header 1 URL : https://21st.dev/community/components/header-1 TSX (React) 'use client'; import React from 'react'; import { Button, buttonVariants } from '@/components/ui/button'; import { cn } from '@/lib/utils'; import { MenuToggleIcon } from '@/components/ui/menu-toggle-icon'; import { useScroll } from '@/components/ui/use-scroll'; import { createPortal } from 'react-dom'; export function Header() { const [open, setOpen] = React.useState(false); const scrolled = useScroll(10); const links = [ { label: 'Features', href: '#', }, { label: 'Pricing', href: '#', }, { label: 'About', href: '#', }, ]; React.useEffect(() => { if (open) { document.body.style.overflow = 'hidden'; } else { document.body.style.overflow = ''; } return () => { document.body.style.overflow = ''; }; }, [open]); return ( <header className={cn('sticky top-0 z-50 w-full border-b border-transparent', { 'bg-background/95 supports-[backdrop-filter]:bg-background/50 border-border backdrop-blur-lg': scrolled, })} > <nav className="mx-auto flex h-14 w-full max-w-5xl items-center justify-between px-4"> <div className="hover:bg-accent rounded-md p-2"> <WordmarkIcon className="h-4" /> </div> <div className="hidden items-center gap-2 md:flex"> {links.map((link) => ( <a key={link.label} className={buttonVariants({ variant: 'ghost' })} href={link.href}> {link.label} </a> ))} <Button variant="outline">Sign In</Button> <Button>Get Started</Button> </div> <Button size="icon" variant="outline" onClick={() => setOpen(!open)} className="md:hidden" aria-expanded={open} aria-controls="mobile-menu" aria-label="Toggle menu" > <MenuToggleIcon open={open} className="size-5" duration={300} /> </Button> </nav> <MobileMenu open={open} className="flex flex-col justify-between gap-2"> <div className="grid gap-y-2"> {links.map((link) => ( <a key={link.label} className={buttonVariants({ variant: 'ghost', className: 'justify-start', })} href={link.href} > {link.label} </a> ))} </div> <div className="flex flex-col gap-2"> <Button variant="outline" className="w-full bg-transparent"> Sign In </Button> <Button className="w-full">Get Started</Button> </div> </MobileMenu> </header> ); } type MobileMenuProps = React.ComponentProps<'div'> & { open: boolean; }; function MobileMenu({ open, children, className, ...props }: MobileMenuProps) { if (!open || typeof window === 'undefined') return null; return createPortal( <div id="mobile-menu" className={cn( 'bg-background/95 supports-[backdrop-filter]:bg-background/50 backdrop-blur-lg', 'fixed top-14 right-0 bottom-0 left-0 z-40 flex flex-col overflow-hidden border-y md:hidden', )} > <div data-slot={open ? 'open' : 'closed'} className={cn( 'data-[slot=open]:animate-in data-[slot=open]:zoom-in-97 ease-out', 'size-full p-4', className, )} {...props} > {children} </div> </div>, document.body, ); } export const WordmarkIcon = (props: React.ComponentProps<"svg">) => ( <svg viewBox="0 0 84 24" fill="currentColor" {...props}> <path d="M45.035 23.984c-1.34-.062-2.566-.441-3.777-1.16-1.938-1.152-3.465-3.187-4.02-5.36-.199-.784-.238-1.128-.234-2.058 0-.691.008-.87.062-1.207.23-1.5.852-2.883 1.852-4.144.297-.371 1.023-1.09 1.41-1.387 1.399-1.082 2.84-1.68 4.406-1.816.536-.047 1.528-.02 2.047.054 1.227.184 2.227.543 3.106 1.121 1.277.84 2.5 2.184 3.367 3.7.098.168.172.308.172.312-.004 0-1.047.723-2.32 1.598l-2.711 1.867c-.61.422-2.91 2.008-2.993 2.062l-.074.047-1-1.574c-.55-.867-1.008-1.594-1.012-1.61-.007-.019.922-.648 2.188-1.476 1.215-.793 2.2-1.453 2.191-1.46-.02-.032-.508-.27-.691-.34a5 5 0 0 0-.465-.13c-.371-.09-1.105-.125-1.426-.07-1.285.219-2.336 1.3-2.777 2.852-.215.761-.242 1.636-.074 2.355.129.527.383 1.102.691 1.543.234.332.727.82 1.047 1.031.664.434 1.195.586 1.969.555.613-.023 1.027-.129 1.64-.426 1.184-.574 2.16-1.554 2.828-2.843.122-.235.208-.372.227-.368.082.032 3.77 1.938 3.79 1.961.034.032-.407.93-.696 1.414a12 12 0 0 1-1.051 1.477c-.36.422-1.102 1.14-1.492 1.445a9.9 9.9 0 0 1-3.23 1.684 9.2 9.2 0 0 1-2.95.351M74.441 23.996c-1.488-.043-2.8-.363-4.066-.992-1.687-.848-2.992-2.14-3.793-3.774-.605-1.234-.863-2.402-.863-3.894.004-1.149.176-2.156.527-3.11.14-.378.531-1.171.75-1.515 1.078-1.703 2.758-2.934 4.805-3.524.847-.242 1.465-.332 2.433-.351 1.032-.024 1.743.055 2.48.277l.31.09.007 2.48c.004 1.364 0 2.481-.008 2.481a1 1 0 0 1-.12-.055c-.688-.347-2.09-.488-2.962-.296-.754.167-1.296.453-1.785.945a3.7 3.7 0 0 0-1.043 2.11c-.047.382-.02 1.109.055 1.437a3.4 3.4 0 0 0 .941 1.738c.75.75 1.715 1.102 2.875 1.05.645-.03 1.118-.14 1.563-.366q1.721-.864 2.02-3.145c.035-.293.042-1.266.042-7.957V0H84l-.012 8.434c-.008 7.851-.011 8.457-.054 8.757-.196 1.274-.586 2.25-1.301 3.243-1.293 1.808-3.555 3.07-6.145 3.437-.664.098-1.43.14-2.047.125M9.848 23.574a14 14 0 0 1-1.137-.152c-2.352-.426-4.555-1.781-6.117-3.774-.27-.335-.75-1.05-.95-1.406-1.156-2.047-1.695-4.27-1.64-6.77.047-1.995.43-3.66 1.23-5.316.524-1.086 1.04-1.87 1.793-2.715C4.567 1.72 6.652.535 8.793.171 9.68.02 10.093 0 12.297 0h1.789v5.441l-.961.016c-2.36.04-3.441.215-4.441.719-.836.414-1.278.879-1.895 1.976-.219.399-.535 1.02-.535 1.063 0 .02 1.285.027 3.918.027h3.914v5.113h-3.914c-2.54 0-3.918.008-3.918.028 0 .05.254.597.441.953.344.656.649 1.086 1.051 1.48.668.657 1.356.985 2.445 1.16.645.106 1.274.145 2.61.16l1.285.016v5.442l-2.055-.004a120 120 0 0 1-2.183-.016M16.469 14.715c0-5.504.011-9.04.031-9.29a5.54 5.54 0 0 1 1.527-3.48c.778-.82 1.922-1.457 3.118-1.734C21.915.035 22.422 0 24.39 0h1.652v4.914h-1.426c-1.324 0-1.445.004-1.644.055-.739.191-1.059.699-1.106 1.754l-.015.355h4.191v4.914h-4.184v11.602h-5.39ZM27.023 14.727c0-5.223.012-9.04.028-9.278.129-1.98 1.234-3.68 3.012-4.62.87-.462 1.777-.716 2.851-.802A61 61 0 0 1 34.945 0h1.649v4.914h-1.426c-1.32 0-1.441.004-1.64.055-.739.191-1.063.699-1.106 1.754l-.02.355h4.192v4.914H32.41v11.602h-5.387ZM55.48 15.406V7.22h4.66v1.363c0 1.3.005 1.363.051 1.363.04 0 .075-.054.133-.203.38-.98.969-1.68 1.711-2.031.563-.266 1.422-.43 2.492-.48l.414-.02v4.914l-.414.035c-.738.063-1.597.195-2.058.313-.297.082-.688.28-.875.449-.324.289-.532.703-.625 1.254-.094.547-.098.879-.098 5.144v4.274h-5.39Zm0 0" /> </svg> ); [266] Hero With Group Of Images, Text And Two Buttons URL : https://21st.dev/community/components/hero-with-group-of-images-text-and-two-buttons CSS https://cdn.21st.dev/user_tommyjepsen/hero-with-group-of-images-text-and-two-buttons.compiled.css TSX (React) import { MoveRight, PhoneCall } from "lucide-react"; import { Button } from "@/components/ui/button"; import { Badge } from "@/components/ui/badge"; function Hero() { return ( <div className="w-full py-20 lg:py-40"> <div className="container mx-auto"> <div className="grid grid-cols-1 gap-8 items-center md:grid-cols-2"> <div className="flex gap-4 flex-col"> <div> <Badge variant="outline">We&apos;re live!</Badge> </div> <div
----------------------------------------

[2] source=21dev  tag=effects  score=0.785
asChild?: boolean } const Button = React.forwardRef<HTMLButtonElement, ButtonProps>( ({ className, variant, size, asChild = false, ...props }, ref) => { const Comp = asChild ? Slot : "button" return ( <Comp className={cn(buttonVariants({ variant, size, className }))} ref={ref} {...props} /> ) } ) Button.displayName = "Button" export { Button, buttonVariants, liquidbuttonVariants, LiquidButton } const liquidbuttonVariants = cva( "inline-flex items-center transition-colors justify-center cursor-pointer gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-[color,box-shadow] disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive", { variants: { variant: { default: "bg-transparent hover:scale-105 duration-300 transition text-primary", destructive: "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40", outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground", secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80", ghost: "hover:bg-accent hover:text-accent-foreground", link: "text-primary underline-offset-4 hover:underline", }, size: { default: "h-9 px-4 py-2 has-[>svg]:px-3", sm: "h-8 text-xs gap-1.5 px-4 has-[>svg]:px-4", lg: "h-10 rounded-md px-6 has-[>svg]:px-4", xl: "h-12 rounded-md px-8 has-[>svg]:px-6", xxl: "h-14 rounded-md px-10 has-[>svg]:px-8", icon: "size-9", }, }, defaultVariants: { variant: "default", size: "xxl", }, } ) function LiquidButton({ className, variant, size, asChild = false, children, ...props }: React.ComponentProps<"button"> & VariantProps<typeof liquidbuttonVariants> & { asChild?: boolean }) { const Comp = asChild ? Slot : "button" return ( <> <Comp data-slot="button" className={cn( "relative", liquidbuttonVariants({ variant, size, className }) )} {...props} > <div className="absolute top-0 left-0 z-0 h-full w-full rounded-full shadow-[0_0_6px_rgba(0,0,0,0.03),0_2px_6px_rgba(0,0,0,0.08),inset_3px_3px_0.5px_-3px_rgba(0,0,0,0.9),inset_-3px_-3px_0.5px_-3px_rgba(0,0,0,0.85),inset_1px_1px_1px_-0.5px_rgba(0,0,0,0.6),inset_-1px_-1px_1px_-0.5px_rgba(0,0,0,0.6),inset_0_0_6px_6px_rgba(0,0,0,0.12),inset_0_0_2px_2px_rgba(0,0,0,0.06),0_0_12px_rgba(255,255,255,0.15)] transition-all dark:shadow-[0_0_8px_rgba(0,0,0,0.03),0_2px_6px_rgba(0,0,0,0.08),inset_3px_3px_0.5px_-3.5px_rgba(255,255,255,0.09),inset_-3px_-3px_0.5px_-3.5px_rgba(255,255,255,0.85),inset_1px_1px_1px_-0.5px_rgba(255,255,255,0.6),inset_-1px_-1px_1px_-0.5px_rgba(255,255,255,0.6),inset_0_0_6px_6px_rgba(255,255,255,0.12),inset_0_0_2px_2px_rgba(255,255,255,0.06),0_0_12px_rgba(0,0,0,0.15)]" /> <div className="absolute top-0 left-0 isolate -z-10 h-full w-full overflow-hidden rounded-md" style={{ backdropFilter: 'url("#container-glass")' }} /> <div className="pointer-events-none z-10 "> {children} </div> <GlassFilter /> </Comp> </> ) } function GlassFilter() { return ( <svg className="hidden"> <defs> <filter id="container-glass" x="0%" y="0%" width="100%" height="100%" colorInterpolationFilters="sRGB" > {/* Generate turbulent noise for distortion */} <feTurbulence type="fractalNoise" baseFrequency="0.05 0.05" numOctaves="1" seed="1" result="turbulence" /> {/* Blur the turbulence pattern slightly */} <feGaussianBlur in="turbulence" stdDeviation="2" result="blurredNoise" /> {/* Displace the source graphic with the noise */} <feDisplacementMap in="SourceGraphic" in2="blurredNoise" scale="70" xChannelSelector="R" yChannelSelector="B" result="displaced" /> {/* Apply overall blur on the final result */} <feGaussianBlur in="displaced" stdDeviation="4" result="finalBlur" /> {/* Output the result */} <feComposite in="finalBlur" in2="finalBlur" operator="over" /> </filter> </defs> </svg> ); } type ColorVariant = | "default" | "primary" | "success" | "error" | "gold" | "bronze"; interface MetalButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { variant?: ColorVariant; } const colorVariants: Record< ColorVariant, { outer: string; inner: string; button: string; textColor: string; textShadow: string; } > = { default: { outer: "bg-gradient-to-b from-[#000] to-[#A0A0A0]", inner: "bg-gradient-to-b from-[#FAFAFA] via-[#3E3E3E] to-[#E5E5E5]", button: "bg-gradient-to-b from-[#B9B9B9] to-[#969696]", textColor: "text-white", textShadow: "[text-shadow:_0_-1px_0_rgb(80_80_80_/_100%)]", }, primary: { outer: "bg-gradient-to-b from-[#000] to-[#A0A0A0]", inner: "bg-gradient-to-b from-primary via-secondary to-muted", button: "bg-gradient-to-b from-primary to-primary/40", textColor: "text-white", textShadow: "[text-shadow:_0_-1px_0_rgb(30_58_138_/_100%)]", }, success: { outer: "bg-gradient-to-b from-[#005A43] to-[#7CCB9B]", inner: "bg-gradient-to-b from-[#E5F8F0] via-[#00352F] to-[#D1F0E6]", button: "bg-gradient-to-b from-[#9ADBC8] to-[#3E8F7C]", textColor: "text-[#FFF7F0]", textShadow: "[text-shadow:_0_-1px_0_rgb(6_78_59_/_100%)]", }, error: { outer: "bg-gradient-to-b from-[#5A0000] to-[#FFAEB0]", inner: "bg-gradient-to-b from-[#FFDEDE] via-[#680002] to-[#FFE9E9]", button: "bg-gradient-to-b from-[#F08D8F] to-[#A45253]", textColor: "text-[#FFF7F0]", textShadow: "[text-shadow:_0_-1px_0_rgb(146_64_14_/_100%)]", }, gold: { outer: "bg-gradient-to-b from-[#917100] to-[#EAD98F]", inner: "bg-gradient-to-b from-[#FFFDDD] via-[#856807] to-[#FFF1B3]", button: "bg-gradient-to-b from-[#FFEBA1] to-[#9B873F]", textColor: "text-[#FFFDE5]", textShadow: "[text-shadow:_0_-1px_0_rgb(178_140_2_/_100%)]", }, bronze: { outer: "bg-gradient-to-b from-[#864813] to-[#E9B486]", inner: "bg-gradient-to-b from-[#EDC5A1] via-[#5F2D01] to-[#FFDEC1]", button: "bg-gradient-to-b from-[#FFE3C9] to-[#A36F3D]", textColor: "text-[#FFF7F0]", textShadow: "[text-shadow:_0_-1px_0_rgb(124_45_18_/_100%)]", }, }; const metalButtonVariants = ( variant: ColorVariant = "default", isPressed: boolean, isHovered: boolean, isTouchDevice: boolean, ) => { const colors = colorVariants[variant]; const transitionStyle = "all 250ms cubic-bezier(0.1, 0.4, 0.2, 1)"; return { wrapper: cn( "relative inline-flex transform-gpu rounded-md p-[1.25px] will-change-transform", colors.outer, ), wrapperStyle: { transform: isPressed ? "translateY(2.5px) scale(0.99)" : "translateY(0) scale(1)", boxShadow: isPressed ? "0 1px 2px rgba(0, 0, 0, 0.15)" : isHovered && !isTouchDevice ? "0 4px 12px rgba(0, 0, 0, 0.12)" : "0 3px 8px rgba(0, 0, 0, 0.08)", transition: transitionStyle, transformOrigin: "center center", }, inner: cn( "absolute inset-[1px] transform-gpu rounded-lg will-change-transform", colors.inner, ), innerStyle: { transition: transitionStyle, transformOrigin: "center center", filter: isHovered && !isPressed &&
----------------------------------------
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
=== REFS: KANBANCOLUMN ===
==================================================
QUERY: KanbanColumn
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.760
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

[2] source=templates  tag=cards  score=0.760
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
=== REFS: KANBAN BOARD ===
==================================================
QUERY: Kanban Board
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.769
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

[2] source=templates  tag=cards  score=0.769
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
=== REFS: TASKDETAILMODAL ===
==================================================
QUERY: TaskDetailModal
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.754
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

[2] source=templates  tag=cards  score=0.754
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
=== REFS: BOARDCONTAINER ===
==================================================
QUERY: BoardContainer
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.761
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

[2] source=templates  tag=cards  score=0.761
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
=== REFS: INPUTFIELD ===
==================================================
QUERY: InputField
CONTEXT (2 chunks):
============================================================

[1] source=floatui.com  tag=cards  score=0.765
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

[2] source=templates  tag=cards  score=0.764
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
=== REFS: TASKCARD ===
==================================================
QUERY: TaskCard
CONTEXT (2 chunks):
============================================================

[1] source=21dev  tag=animations  score=0.753
); } const Tab = ({ children, setPosition, }: { children: React.ReactNode; setPosition: any; }) => { const ref = useRef<HTMLLIElement>(null); return ( <li ref={ref} onMouseEnter={() => { if (!ref.current) return; const { width } = ref.current.getBoundingClientRect(); setPosition({ width, opacity: 1, left: ref.current.offsetLeft, }); }} className="relative z-10 block cursor-pointer px-3 py-1.5 text-xs uppercase text-white mix-blend-difference md:px-5 md:py-3 md:text-base" > {children} </li> ); }; const Cursor = ({ position }: { position: any }) => { return ( <motion.li animate={position} className="absolute z-0 h-7 rounded-full bg-black md:h-12" /> ); }; export default NavHeader; [378] Layout Grid URL : https://21st.dev/community/components/layout-grid CSS https://cdn.21st.dev/user_aceternity/layout-grid.compiled.css TSX (React) "use client"; import React, { useState, useRef, useEffect } from "react"; import { AnimatePresence, motion } from "framer-motion"; import { cn } from "@/lib/utils"; import Image from "next/image"; type Card = { id: number; content: JSX.Element | React.ReactNode | string; className: string; thumbnail: string; }; export const LayoutGrid = ({ cards }: { cards: Card[] }) => { const [selected, setSelected] = useState<Card | null>(null); const [lastSelected, setLastSelected] = useState<Card | null>(null); const handleClick = (card: Card) => { setLastSelected(selected); setSelected(card); }; const handleOutsideClick = () => { setLastSelected(selected); setSelected(null); }; return ( <div className="w-full h-full p-10 grid grid-cols-1 md:grid-cols-3 max-w-7xl mx-auto gap-4 relative"> {cards.map((card, i) => ( <div key={i} className={cn(card.className, "")}> <motion.div onClick={() => handleClick(card)} className={cn( card.className, "relative overflow-hidden", selected?.id === card.id ? "rounded-lg cursor-pointer absolute inset-0 h-1/2 w-full md:w-1/2 m-auto z-50 flex justify-center items-center flex-wrap flex-col" : lastSelected?.id === card.id ? "z-40 bg-white rounded-xl h-full w-full" : "bg-white rounded-xl h-full w-full" )} layoutId={`card-${card.id}`} > {selected?.id === card.id && <SelectedCard selected={selected} />} <ImageComponent card={card} /> </motion.div> </div> ))} <motion.div onClick={handleOutsideClick} className={cn( "absolute h-full w-full left-0 top-0 bg-black opacity-0 z-10", selected?.id ? "pointer-events-auto" : "pointer-events-none" )} animate={{ opacity: selected?.id ? 0.3 : 0 }} /> </div> ); }; const ImageComponent = ({ card }: { card: Card }) => { return ( <motion.img layoutId={`image-${card.id}-image`} src={card.thumbnail} height="500" width="500" className={cn( "object-cover object-top absolute inset-0 h-full w-full transition duration-200" )} alt="thumbnail" /> ); }; const SelectedCard = ({ selected }: { selected: Card | null }) => { return ( <div className="bg-transparent h-full w-full flex flex-col justify-end rounded-lg shadow-2xl relative z-[60]"> <motion.div initial={{ opacity: 0, }} animate={{ opacity: 0.6, }} className="absolute inset-0 h-full w-full bg-black opacity-60 z-10" /> <motion.div layoutId={`content-${selected?.id}`} initial={{ opacity: 0, y: 100, }} animate={{ opacity: 1, y: 0, }} exit={{ opacity: 0, y: 100, }} transition={{ duration: 0.3, ease: "easeInOut", }} className="relative px-8 pb-4 z-[70]" > {selected?.content} </motion.div> </div> ); }; [379] Spotlight New URL : https://21st.dev/community/components/spotlight-new TSX (React) "use client"; import React from "react"; import { motion } from "motion/react"; type SpotlightProps = { gradientFirst?: string; gradientSecond?: string; gradientThird?: string; translateY?: number; width?: number; height?: number; smallWidth?: number; duration?: number; xOffset?: number; }; export const Spotlight = ({ gradientFirst = "radial-gradient(68.54% 68.72% at 55.02% 31.46%, hsla(210, 100%, 85%, .08) 0, hsla(210, 100%, 55%, .02) 50%, hsla(210, 100%, 45%, 0) 80%)", gradientSecond = "radial-gradient(50% 50% at 50% 50%, hsla(210, 100%, 85%, .06) 0, hsla(210, 100%, 55%, .02) 80%, transparent 100%)", gradientThird = "radial-gradient(50% 50% at 50% 50%, hsla(210, 100%, 85%, .04) 0, hsla(210, 100%, 45%, .02) 80%, transparent 100%)", translateY = -350, width = 560, height = 1380, smallWidth = 240, duration = 7, xOffset = 100, }: SpotlightProps = {}) => { return ( <motion.div initial={{ opacity: 0, }} animate={{ opacity: 1, }} transition={{ duration: 1.5, }} className="pointer-events-none absolute inset-0 h-full w-full" > <motion.div animate={{ x: [0, xOffset, 0], }} transition={{ duration, repeat: Infinity, repeatType: "reverse", ease: "easeInOut", }} className="absolute top-0 left-0 w-screen h-screen z-40 pointer-events-none" > <div style={{ transform: `translateY(${translateY}px) rotate(-45deg)`, background: gradientFirst, width: `${width}px`, height: `${height}px`,
----------------------------------------

[2] source=floatui.com  tag=cards  score=0.752
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

### FINAL INSTRUCTION:
Generate clean, modular React components. Every AST node MUST have a corresponding file. No monolithic files. No arbitrary wrappers. Direct Tailwind injection.
