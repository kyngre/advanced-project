import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from '../api/axios.js';
import './LoginPage.css'; // ✅ 스타일 연결

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
      onLoginSuccess();
      navigate('/');
    } catch (err) {
      alert('로그인 실패');
    }
  };

  return (
    <div className="login-container">
      <form className="login-box" onSubmit={handleLogin}>
        <h2>로그인</h2>
        <input type="email" placeholder="이메일 주소" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <input type="password" placeholder="비밀번호" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <button type="submit">로그인</button>
      </form>
    </div>
  );
}

export default LoginPage;