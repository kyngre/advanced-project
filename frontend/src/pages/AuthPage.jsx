import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import axios from '../api/axios';
import './AuthPage.css';
import { ClipLoader } from 'react-spinners';

/**
 * AuthPage: 로그인 / 회원가입 통합 페이지
 * - mode 상태에 따라 화면 전환
 * - 로그인 성공 시 메인으로 이동
 * - 회원가입 성공 시 구독 선택 페이지로 이동
 */
function AuthPage({ onLoginSuccess }) {
  const navigate = useNavigate();
  const location = useLocation();

  // 🔧 상태 정의
  const [mode, setMode] = useState(location.state?.mode === 'register' ? 'register' : 'login');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [loading, setLoading] = useState(false);

  // 🔄 페이지 이동에 따른 모드 갱신
  useEffect(() => {
    const nextMode = location.state?.mode;
    if (nextMode === 'register' || nextMode === 'login') {
      setMode(nextMode);
      setErrorMessage('');
    }
  }, [location.key]);

  // 🚀 로그인 또는 회원가입 처리
  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage('');
    setLoading(true);

    try {
      if (mode === 'login') {
        const res = await axios.post('/token/', { email, password });
        localStorage.setItem('accessToken', res.data.access);
        localStorage.setItem('refreshToken', res.data.refresh);
        onLoginSuccess?.();
        navigate('/');
      } else {
        await axios.post('/users/register/', { email, username, password });
        const res = await axios.post('/token/', { email, password });
        localStorage.setItem('accessToken', res.data.access);
        localStorage.setItem('refreshToken', res.data.refresh);
        onLoginSuccess?.();
        navigate('/subscribe'); // ✅ 회원가입 후 구독 설정 페이지로 이동
      }

      setEmail('');
      setUsername('');
      setPassword('');
    } catch (err) {
      const defaultMessage = mode === 'login' ? '로그인에 실패하였습니다.' : '회원가입에 실패하였습니다.';
      const detail =
        err.response?.data?.detail ||
        err.response?.data?.username?.[0] ||
        err.response?.data?.email?.[0] ||
        err.response?.data?.password?.[0] ||
        '';
      setErrorMessage(`${defaultMessage} ${detail}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      {/* 🔃 로딩 스피너 */}
      {loading && (
        <div className="fullscreen-loading">
          <ClipLoader color="#e50914" size={60} />
          <p className="loading-text">잠시만 기다려주세요...</p>
        </div>
      )}

      {/* 🔐 로그인 또는 회원가입 폼 */}
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

        {/* ❗ 에러 메시지 */}
        {errorMessage && (
          <p className="error-message">{errorMessage}</p>
        )}

        {/* 🔁 로그인 / 회원가입 모드 전환 */}
        <p className="toggle-text">
          {mode === 'login' ? '아직 회원이 아니신가요?' : '이미 계정이 있으신가요?'}{' '}
          <span
            onClick={() => {
              const nextMode = mode === 'login' ? 'register' : 'login';
              setMode(nextMode);
              setErrorMessage('');
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