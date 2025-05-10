import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';

function Header({ isLoggedIn, userEmail, onLogout }) {
  const navigate = useNavigate();

  return (
    <header className="header">
      <div className="header-left">
        <Link to="/" className="logo">🎬 MovieVerse</Link>
        <nav className="nav-links">
          <Link to="/">영화</Link>
          <Link to="/board">게시판</Link>
          {/* 향후 마이페이지 추가 가능 */}
        </nav>
      </div>

      <div className="header-right">
        {isLoggedIn ? (
          <>
            <span className="welcome">👤 {userEmail}님</span>
            <button className="btn" onClick={onLogout}>로그아웃</button>
          </>
        ) : (
          <>
            <button className="btn" onClick={() => navigate('/auth', { state: { mode: 'login' } })}>
              로그인
            </button>
            <button className="btn" onClick={() => navigate('/auth', { state: { mode: 'register' } })}>
              회원가입
            </button>
          </>
        )}
      </div>
    </header>
  );
}

export default Header;