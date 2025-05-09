import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage.jsx';
import Header from './components/Header.jsx';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/" element={<h2>🎬 홈입니다. 로그인 상태 유지 테스트!</h2>} />
      </Routes>
    </Router>
  );
}

export default App;