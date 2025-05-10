import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from '../api/axios';
import './Header.css';

function Header({ isLoggedIn, onLogout }) {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const res = await axios.get('/users/profile/');
        setUsername(res.data.username);
      } catch (err) {
        console.error('프로필 정보를 불러오지 못했습니다:', err);
      }
    };

    if (isLoggedIn) {
      fetchProfile();
    } else {
      setUsername('');
    }
  }, [isLoggedIn]);

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
            <span className="welcome">👤 {username ? `${username}님` : '사용자님'}</span>
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