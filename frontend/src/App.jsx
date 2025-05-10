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

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userEmail, setUserEmail] = useState('');
  const [authReady, setAuthReady] = useState(false); // ✅ 추가

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
    setAuthReady(true); // ✅ 인증 판단 완료
  };

  useEffect(() => {
    initializeAuth();
  }, []);

  return (
    <Router>
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

      {/* ✅ 인증 판단이 완료되었을 때만 라우터 렌더링 */}
      {authReady && (
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