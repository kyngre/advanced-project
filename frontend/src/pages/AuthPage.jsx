import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import axios from '../api/axios';
import './AuthPage.css';
import { ClipLoader } from 'react-spinners'; // ✅ 스피너 추가

function AuthPage({ onLoginSuccess }) {
  const navigate = useNavigate();
  const location = useLocation();

  const [mode, setMode] = useState(location.state?.mode === 'register' ? 'register' : 'login');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [loading, setLoading] = useState(false); // ✅ 로딩 상태 추가

  useEffect(() => {
    const nextMode = location.state?.mode;
    if (nextMode === 'register' || nextMode === 'login') {
      setMode(nextMode);
      setErrorMessage('');
    }
  }, [location.key]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage('');
    setLoading(true);

    try {
      if (mode === 'login') {
        const res = await axios.post('/token/', { email, password });
        localStorage.setItem('accessToken', res.data.access);
        onLoginSuccess?.();
        navigate('/');
      } else {
        await axios.post('/users/register/', { email, username, password });
        const res = await axios.post('/token/', { email, password });
        localStorage.setItem('accessToken', res.data.access);
        onLoginSuccess?.();
        navigate('/');
      }
    } catch (err) {
      setErrorMessage(mode === 'login' ? '로그인에 실패하였습니다.' : '회원가입에 실패하였습니다.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      {loading ? (
        <div className="loading-box">
          <ClipLoader color="#e50914" size={50} />
          <p style={{ marginTop: '1rem' }}>잠시만 기다려주세요...</p>
        </div>
      ) : (
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

          {errorMessage && (
            <p className="error-message" style={{ color: 'red', marginTop: '0.5rem' }}>
              {errorMessage}
            </p>
          )}

          <p className="toggle-text">
            {mode === 'login' ? '아직 회원이 아니신가요?' : '이미 계정이 있으신가요?'}{' '}
            <span
              onClick={() => {
                const nextMode = mode === 'login' ? 'register' : 'login';
                setMode(nextMode);
                setErrorMessage('');
                navigate('/auth', { state: { mode: nextMode } });
              }}
              style={{ cursor: 'pointer', textDecoration: 'underline' }}
            >
              {mode === 'login' ? '회원가입' : '로그인'}
            </span>
          </p>
        </form>
      )}
    </div>
  );
}

export default AuthPage;