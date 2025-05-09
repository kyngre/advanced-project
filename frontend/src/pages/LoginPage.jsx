import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from '../api/axios.js';

function LoginPage({ onLoginSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/token/', { email, password });
      localStorage.setItem('accessToken', res.data.access);
      alert('로그인 성공!');
      onLoginSuccess();        // ✅ 부모에게 로그인 상태 갱신 요청
      navigate('/');           // ✅ 홈으로 이동
    } catch (err) {
      alert('로그인 실패');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>🔐 로그인</h2>
      <form onSubmit={handleLogin}>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <br />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <br />
        <button type="submit">로그인</button>
      </form>
    </div>
  );
}

export default LoginPage;