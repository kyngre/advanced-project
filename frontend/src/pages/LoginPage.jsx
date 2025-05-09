import React, { useState } from 'react';
import axios from '../api/axios.js';

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/token/', {
        email,
        password,
      });

      const { access } = response.data;
      localStorage.setItem('accessToken', access); // ✅ 토큰 저장
      alert('로그인 성공!');
    } catch (error) {
      console.error('로그인 실패:', error);
      alert('이메일 또는 비밀번호가 잘못되었습니다.');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>🔐 로그인</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>이메일:</label><br />
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div style={{ marginTop: '1rem' }}>
          <label>비밀번호:</label><br />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" style={{ marginTop: '1rem' }}>로그인</button>
      </form>
    </div>
  );
}

export default LoginPage;