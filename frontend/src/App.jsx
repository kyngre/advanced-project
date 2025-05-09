import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import Header from './components/Header.jsx';
import AuthPage from './pages/AuthPage.jsx';

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [userEmail, setUserEmail] = useState('');

    // ✅ 로그인 상태 초기화 함수
    const initializeAuth = () => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            try {
                const decoded = jwtDecode(token);
                setIsLoggedIn(true);
                setUserEmail(decoded.email);
            } catch (e) {
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
                <Route path="/" element={<h2>🎬 홈입니다</h2>} />
            </Routes>
        </Router>
  );
}

export default App;