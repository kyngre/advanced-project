import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import axios from '../api/axios';
import './AuthPage.css';

function AuthPage({ onLoginSuccess }) {
  const navigate = useNavigate();
  const location = useLocation();

  // ✅ location.state를 기반으로 초기 mode 설정
  const [mode, setMode] = useState(location.state?.mode === 'register' ? 'register' : 'login');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // ✅ location 변경될 때마다 mode 재설정
  useEffect(() => {
    const nextMode = location.state?.mode;
    if (nextMode === 'register' || nextMode === 'login') {
      setMode(nextMode);
    }
  }, [location.key]); // location.key를 watch해야 페이지 전환 인식됨

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (mode === 'login') {
        const res = await axios.post('/token/', { email, password });
        localStorage.setItem('accessToken', res.data.access);
        onLoginSuccess?.();
        alert('로그인 성공!');
        navigate('/');
      } else {
        await axios.post('/users/register/', { email, username, password });
        alert('회원가입 성공! 로그인하세요.');
        setMode('login');
        setPassword('');
      }
    } catch (err) {
      alert(`${mode === 'login' ? '로그인' : '회원가입'} 실패`);
    }
  };

  return (
    <div className="auth-container">
      <form className="auth-box" onSubmit={handleSubmit}>
        <h2>{mode === 'login' ? '로그인' : '회원가입'}</h2>

        <input
          type="email"
          placeholder="이메일"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        {mode === 'register' && (
          <input
            type="text"
            placeholder="사용자명"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        )}

        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">{mode === 'login' ? '로그인' : '가입하기'}</button>

        <p className="toggle-text">
          {mode === 'login' ? '아직 회원이 아니신가요?' : '이미 계정이 있으신가요?'}{' '}
          <span
            onClick={() => {
              const nextMode = mode === 'login' ? 'register' : 'login';
              setMode(nextMode);
              navigate('/auth', { state: { mode: nextMode } });
            }}
          >
            {mode === 'login' ? '회원가입' : '로그인'}
          </span>
        </p>
      </form>
    </div>
  );
}

export default AuthPage;