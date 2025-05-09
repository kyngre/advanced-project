import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/api', // Django 서버 주소
  headers: {
    'Content-Type': 'application/json',
  },
});

// ✅ 모든 요청 전에 토큰을 자동으로 붙이기
instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default instance;