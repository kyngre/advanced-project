import React from 'react';
import { useNavigate } from 'react-router-dom';
import jwt_decode from 'jwt-decode';

function Header() {
  const navigate = useNavigate();
  const token = localStorage.getItem('accessToken');

  let email = null;
  if (token) {
    try {
      const decoded = jwt_decode(token);
      email = decoded.email;
    } catch (e) {
      console.error('토큰 디코딩 오류:', e);
    }
  }

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    alert('로그아웃 되었습니다.');
    navigate('/login');
  };

  return (
    <header style={{ padding: '1rem', backgroundColor: '#f5f5f5', marginBottom: '2rem' }}>
      {email ? (
        <>
          <span>👤 {email}님, 환영합니다.</span>
          <button onClick={handleLogout} style={{ marginLeft: '1rem' }}>로그아웃</button>
        </>
      ) : (
        <span>로그인해주세요</span>
      )}
    </header>
  );
}

export default Header;