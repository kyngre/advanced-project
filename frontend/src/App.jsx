import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import Header from './components/Header.jsx';
import AuthPage from './pages/AuthPage.jsx';
import PrivateRoute from './routes/PrivateRoute.jsx';
import MoviesPage from './pages/MoviesPage.jsx';
import MovieDetailPage from './pages/MovieDetailPage.jsx';
import SubscribePage from './pages/SubscribePage.jsx';
import ProfilePage from './pages/ProfilePage.jsx';
import { ClipLoader } from 'react-spinners';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userEmail, setUserEmail] = useState('');
  const [authReady, setAuthReady] = useState(false);

  const initializeAuth = () => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      try {
        const decoded = jwtDecode(token);
        setIsLoggedIn(true);
        setUserEmail(decoded.email);
      } catch {
        setIsLoggedIn(false);
        setUserEmail('');
      }
    } else {
      setIsLoggedIn(false);
      setUserEmail('');
    }
    setAuthReady(true);
  };

  useEffect(() => {
    initializeAuth();
  }, []);

  return (
    <Router>
      {/* ✅ 로그인 여부 확인 후 Header 렌더링 */}
      {authReady && (
        <Header
          isLoggedIn={isLoggedIn}
          userEmail={userEmail}
          onLogout={() => {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            setIsLoggedIn(false);
            setUserEmail('');
          }}
        />
      )}

      {/* ✅ 로그인 여부 확인 전엔 전체 로딩 화면 */}
      {!authReady ? (
        <div style={{
          height: '100vh',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          backgroundColor: '#141414',
          flexDirection: 'column',
          color: 'white',
        }}>
          <ClipLoader color="#e50914" size={60} />
          <p style={{ marginTop: '1rem', fontSize: '1.1rem' }}>잠시만 기다려주세요...</p>
        </div>
      ) : (
        <Routes>
          <Route path="/" element={<MoviesPage />} />
          <Route
            path="/reviews"
            element={
              <PrivateRoute isLoggedIn={isLoggedIn}>
                <div style={{ padding: '2rem', color: 'white' }}>
                  📝 리뷰 페이지입니다 (로그인한 사용자만 볼 수 있습니다)
                </div>
              </PrivateRoute>
            }
          />
          <Route path="/auth" element={<AuthPage onLoginSuccess={initializeAuth} />} />
          <Route path="/movies/:id" element={<MovieDetailPage />} />
          <Route path="/subscribe" element={<SubscribePage />} />
          <Route
            path="/profile"
            element={
              <PrivateRoute isLoggedIn={isLoggedIn}>
                <ProfilePage />
              </PrivateRoute>
            }
          />
        </Routes>
      )}
    </Router>
  );
}

export default App;