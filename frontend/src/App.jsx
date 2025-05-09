import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import Header from './components/Header.jsx';
import AuthPage from './pages/AuthPage.jsx';
import PrivateRoute from './routes/PrivateRoute.jsx';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userEmail, setUserEmail] = useState('');

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
          setIsLoggedIn(false);
          setUserEmail('');
        }}
      />

      <Routes>
        <Route path="/auth" element={<AuthPage onLoginSuccess={initializeAuth} />} />

        <Route
          path="/"
          element={
            <PrivateRoute isLoggedIn={isLoggedIn}>
              <div style={{ padding: '2rem', color: 'white' }}>
                🎬 홈입니다 (로그인한 사용자만 볼 수 있습니다)
              </div>
            </PrivateRoute>
          }
        />

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
      </Routes>
    </Router>
  );
}

export default App;