import React from 'react';
import { Navigate } from 'react-router-dom';

/**
 * PrivateRoute: 로그인된 사용자만 접근 가능한 보호 라우트
 * - 로그인 상태일 경우 children을 렌더링
 * - 그렇지 않으면 /auth 페이지로 리디렉션
 */
function PrivateRoute({ isLoggedIn, children }) {
  return isLoggedIn ? children : <Navigate to="/auth" replace />;
}

export default PrivateRoute;