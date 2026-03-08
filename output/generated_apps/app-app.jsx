Here is the complete React component file:

import React, { useState } from 'react';

function Navbar() {
  const [open, setOpen] = useState(false);
  const items = [
    { label: "Home", link: "/" },
    { label: "About", link: "/about" },
    { label: "Contact", link: "/contact" }
  ];
  const socialItems = [
    { label: "GitHub", link: "https://github.com" },
    { label: "LinkedIn", link: "https://www.linkedin.com" },
    { label: "Twitter", link: "https://twitter.com" }
  ];

  return (
    <div className="bg-slate-50">
      <nav
        className="
          flex 
          justify-between 
          py-4 
          px-6 
          sm:py-6 
          sm:px-8 
          md:py-8 
          md:px-12 
          lg:py-12 
          lg:px-16 
          xl:py-20 
          xl:px-24
        "
      >
        <div className="flex items-center">
          <a href="#" className="text-slate-900 font-bold">Logo</a>
        </div>
        <button
          className="
            flex 
            justify-center 
            items-center 
            w-full 
            sm:w-auto 
            md:hidden 
            lg:block 
            xl:invisible
          "
          aria-label={open ? 'Close menu' : 'Open menu'}
          aria-expanded={open}
          aria-controls="staggered-menu-panel"
          onClick={() => setOpen(!open)}
        >
          <span className="
            flex 
            justify-center 
            items-center 
            w-full 
            h-12 
            sm:h-10 
            md:w-auto 
            lg:h-14
          ">
            <svg
              xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
              fill="none" stroke="currentColor"
              strokeWidth={2}
              className="
                flex 
                justify-center 
                items-center 
                w-6 
                h-6 
                sm:w-5 
                sm:h-5 
                md:w-7 
                lg:w-8
              "
            >
              <path d="M3 11V20h3" />
              <path d="M21 13.172a9 9 0 0 1-2.945 0l-6.884 1.623a1 1 0 0 0 .66-.165L16 10l5 1v3z" />
            </svg>
          </span>
        </button>

        <div
          className="
            hidden 
            md:block 
            lg:flex 
            xl:invisible 
            self-center 
            justify-self-start 
            w-full 
            sm:w-auto 
            md:w-2/5 
            lg:w-1/3 
            xl:w-1/4
          "
        >
          <ul className="flex flex-col">
            {items.map((item, index) => (
              <li key={index} className="mb-2 last:mb-0">
                <a href={item.link} className="text-slate-900 hover:text-indigo-500 transition duration-300 ease-in-out">
                  {item.label}
                </a>
              </li>
            ))}
          </ul>

          <div
            className="
              hidden 
              md:block 
              lg:flex 
              xl:invisible 
              self-center 
              justify-self-start 
              w-full 
              sm:w-auto 
              md:w-2/5 
              lg:w-1/3 
              xl:w-1/4
            "
          >
            <ul className="flex flex-col">
              {socialItems.map((item, index) => (
                <li key={index} className="mb-2 last:mb-0">
                  <a href={item.link} className="text-slate-900 hover:text-indigo-500 transition duration-300 ease-in-out">
                    {item.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

        </div>
      </nav>
    </div>
  );
}

export default Navbar;

This file creates a simple navbar component with logo, navigation links, and social media links. The navbar is responsive and changes its layout based on the screen size.

The `useState` hook is used to create a state variable `open` that tracks whether the menu is open or not. When the button is clicked, the state is toggled.

The navbar's styles are based on the Tailwind CSS framework.