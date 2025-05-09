import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage.jsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<h1>홈입니다</h1>} />
        <Route path="/login" element={<LoginPage />} />
        {/* 나중에 영화 목록 등 다른 페이지도 추가 가능 */}
      </Routes>
    </Router>
  );
}

export default App;