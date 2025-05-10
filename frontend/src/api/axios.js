import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/', // 필요시 배포용 주소로 변경
});

// ✅ 요청 인터셉터: accessToken을 헤더에 자동 첨부
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

// ✅ 응답 인터셉터: accessToken이 만료된 경우 refresh 시도
instance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // access token이 만료되었고 재시도한 적 없는 경우
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refreshToken');
        if (!refreshToken) throw new Error('No refresh token');

        // refresh token으로 access token 재발급 요청
        const res = await axios.post('http://localhost:8000/api/token/refresh/', {
          refresh: refreshToken,
        });

        // 새 access token 저장 및 기존 요청 재시도
        localStorage.setItem('accessToken', res.data.access);
        originalRequest.headers.Authorization = `Bearer ${res.data.access}`;
        return instance(originalRequest);
      } catch (refreshError) {
        // refresh 실패 시 로그아웃 처리
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        window.location.href = '/auth';
      }
    }

    return Promise.reject(error);
  }
);

export default instance;