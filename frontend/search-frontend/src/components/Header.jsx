import { useState, useEffect } from 'react';
import './Header.css';
import '../theme.css'; // Adjust the path based on your folder structure
import logo from '../assets/logo.png';

const isLoggedIn = true; // Mock login state
const username = 'JohnDoe';
const profilePic = 'https://i.pravatar.cc/40'; // random avatar

export function Header() {
  const [theme, setTheme] = useState('system');

  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'light') {
      root.setAttribute('data-theme', 'light');
    } else if (theme === 'dark') {
      root.setAttribute('data-theme', 'dark');
    } else {
      root.removeAttribute('data-theme'); // System default
    }
  }, [theme]);

  return (
    <header className="header">
      <div className="logo-section">
        <img src={logo} alt="Search Engine Logo" className="logo" />
        <h2>MySearch</h2>
      </div>

      <div className="header-right">
        {/* ✅ Theme Switch */}
        <div className="theme-switch">
          <button onClick={() => setTheme('light')} title="Light Mode">🌞</button>
          <button onClick={() => setTheme('dark')} title="Dark Mode">🌙</button>
          <button onClick={() => setTheme('system')} title="System Default">🖥️</button>
        </div>

        {/* Auth Section */}
        <div className="auth-section">
          {isLoggedIn ? (
            <div className="user-info">
              <span>{username}</span>
              <img src={profilePic} alt="Profile" className="profile-pic" />
            </div>
          ) : (
            <div>
              <button className="auth-btn">Login</button>
              <button className="auth-btn">Signup</button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
