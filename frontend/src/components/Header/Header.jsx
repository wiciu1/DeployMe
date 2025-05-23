import {Link, useLocation} from 'react-router-dom';
import { useState } from 'react';
import "./Header.css";
import {useAuth} from "../AuthContext.jsx";

const Header = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();
  const toggleMenu = () => setIsOpen(!isOpen);
  const closeMenu = () => {
      setIsOpen(false);
      window.scrollTo({top: 0, behavior: 'smooth'});
  }

  const activeLinkStyle = {
      color: '#17994c',
      fontWeight: "bold",
  };
  const {isAuthenticated} = useAuth();

    if (isAuthenticated === null) {
    return null;
  }

  if (['/login', '/register'].includes(location.pathname)) {
    return null;
  }
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark sticky-top px-4 custom-navbar">
      <Link className="navbar-brand d-flex align-items-center gap-2" to="/" onClick={closeMenu}>
        <img src="/images/logo.png" alt="DeployMe logo" className="logo" />
      </Link>

      <button
        className="navbar-toggler"
        type="button"
        onClick={toggleMenu}
      >
        <span className="navbar-toggler-icon"></span>
      </button>

      <div className={`collapse navbar-collapse ${isOpen ? 'show' : ''}`} id="navbarNav">
        <div className="d-flex justify-content-between w-100 flex-column flex-lg-row">

          {isAuthenticated && (
          <ul className="navbar-nav gap-2">
            <li className="nav-item">
              <Link className="nav-link" to="/" onClick={closeMenu} style={location.pathname === '/' ? activeLinkStyle : {}}>Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/template2" onClick={closeMenu} style={location.pathname === '/stats' ? activeLinkStyle : {}}>Statistics</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/template3" onClick={closeMenu} style={location.pathname === '/template' ? activeLinkStyle : {}}>template</Link>
            </li>
          </ul>
        )}

        <ul className="navbar-nav gap-2 ms-lg-auto mt-3 mt-lg-0">
          {isAuthenticated ? (
            <li className="nav-item">
              <Link
                className="btn btn-success"
                to="/logout"
                onClick={closeMenu}
              >
                Logout
              </Link>
            </li>
          ) : (
            <>
              <li className="nav-item">
                <Link
                  className="btn btn-outline-light"
                  to="/login"
                  onClick={closeMenu}
                >
                  Log in
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className="btn btn-success"
                  to="/register"
                  onClick={closeMenu}
                >
                  Sign up
                </Link>
              </li>
            </>
          )}
        </ul>
        </div>
      </div>
    </nav>
  );
};

export default Header;
