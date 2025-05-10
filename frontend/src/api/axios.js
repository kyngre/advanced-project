import axios from 'axios';

// 🔧 Axios 인스턴스 생성 (기본 baseURL 설정)
const instance = axios.create({
  baseURL: 'http://localhost:8000/api/', // 배포 시 변경 필요
});

// 🔐 요청 인터셉터: accessToken을 자동으로 Authorization 헤더에 추가
instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// 🔄 응답 인터셉터: accessToken 만료 시 refreshToken으로 갱신 시도
instance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // accessToken이 만료되었고 아직 재시도하지 않은 경우
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refreshToken');
        if (!refreshToken) throw new Error('No refresh token');

        // refreshToken을 이용해 새 accessToken 요청
        const res = await axios.post('http://localhost:8000/api/token/refresh/', {
          refresh: refreshToken,
        });

        // 새 accessToken 저장 및 기존 요청 재시도
        localStorage.setItem('accessToken', res.data.access);
        originalRequest.headers.Authorization = `Bearer ${res.data.access}`;
        return instance(originalRequest);
      } catch (refreshError) {
        // refresh 실패 시 로그아웃 및 로그인 페이지로 이동
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        window.location.href = '/auth';
      }
    }

    return Promise.reject(error);
  }
);

export default instance;