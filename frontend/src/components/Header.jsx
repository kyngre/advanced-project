import React from 'react';

function Header({ isLoggedIn, userEmail, onLogout }) {
  return (
    <header style={{ padding: '1rem', backgroundColor: '#eee' }}>
      {isLoggedIn ? (
        <>
          <span>👤 {userEmail}님 환영합니다</span>
          <button onClick={onLogout} style={{ marginLeft: '1rem' }}>로그아웃</button>
        </>
      ) : (
        <span>로그인해주세요</span>
      )}
    </header>
  );
}

export default Header;