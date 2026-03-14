import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu, X } from 'lucide-react';

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <>
      <nav 
        className="fixed top-4 md:top-6 left-1/2 -translate-x-1/2 z-50 bg-white/80 backdrop-blur-md border border-white/20 rounded-full px-4 py-2 md:px-10 md:py-4 shadow-2xl flex items-center justify-between gap-2 md:gap-8 w-[95%] md:w-auto max-w-4xl" 
        data-testid="navbar"
      >
        {/* Logo - Smaller font on mobile */}
        <Link 
          to="/" 
          className="text-xl md:text-3xl font-bold shrink-0" 
          style={{ color: '#F28C1C' }} 
          data-testid="nav-logo"
        >
          SahyadriMates
        </Link>
        
        {/* Desktop Menu - Hidden on mobile */}
        <div className="hidden md:flex items-center gap-6" data-testid="nav-menu">
          <Link to="/tours" className="text-primary hover:text-accent transition-colors font-medium">
            Tours
          </Link>
          <Link to="/tours?category=trek" className="text-primary hover:text-accent transition-colors font-medium">
            Treks
          </Link>
          <Link to="/tours?category=camping" className="text-primary hover:text-accent transition-colors font-medium">
            Camping
          </Link>
        </div>

        <div className="flex items-center gap-1 md:gap-4 ml-auto">
          {/* User Section */}
          

          {/* Mobile Menu Toggle */}
          <button 
            className="md:hidden p-2 text-primary hover:bg-black/5 rounded-full transition-colors"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </nav>

      {/* Mobile Dropdown Overlay */}
      {isMenuOpen && (
        <div className="fixed inset-0 z-40 bg-white/95 backdrop-blur-lg md:hidden flex flex-col items-center justify-center gap-8 pt-20">
          <Link to="/tours" onClick={() => setIsMenuOpen(false)} className="text-2xl font-semibold">Tours</Link>
          <Link to="/tours?category=trek" onClick={() => setIsMenuOpen(false)} className="text-2xl font-semibold">Treks</Link>
          <Link to="/tours?category=camping" onClick={() => setIsMenuOpen(false)} className="text-2xl font-semibold">Camping</Link>
        </div>
      )}
    </>
  );
}
