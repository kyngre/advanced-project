# 🎨 Frontend - React

![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react)
![JWT](https://img.shields.io/badge/Auth-JWT-red)
![Style](https://img.shields.io/badge/Style-Netflix--Inspired-black)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> 넷플릭스 스타일 UI를 기반으로 사용자 인증, 영화 리뷰 작성, 게시판 등 기능을 제공하는 React 프론트엔드입니다.

---

## 📑 목차

- [🎨 프로젝트 소개](#-프로젝트-소개)
- [🔧 주요 기능](#-주요-기능)
  - [✅ 사용자 인증 및 상태 관리](#-사용자-인증-및-상태-관리)
  - [✅ 넷플릭스 스타일 UI](#-넷플릭스-스타일-ui)
  - [✅ 보호 라우팅](#-보호-라우팅)
- [💡 기술 스택](#-기술-스택)
- [📁 디렉터리 구조](#-디렉터리-구조)
- [🚀 실행 방법](#-실행-방법)
- [🔐 인증 흐름 요약](#-인증-흐름-요약)
- [🧩 향후 구현 예정 기능](#-향후-구현-예정-기능)
- [📄 연동 백엔드](#-연동-백엔드)

---

## 🔧 주요 기능

### ✅ 사용자 인증 및 상태 관리
- JWT 기반 로그인 / 회원가입 구현
- accessToken을 localStorage에 저장하여 로그인 상태 유지
- 로그인 성공 시 Header에 사용자 이메일 표시
- 로그아웃 시 상태 초기화 및 토큰 삭제

### ✅ 넷플릭스 스타일 UI
- 로그인/회원가입을 하나의 화면에서 토글
- 어두운 배경 + 빨간 버튼 컬러 강조
- 모바일에서도 잘 작동하는 중앙 정렬 구조
- `LoginPage`, `RegisterPage`, `AuthPage`로 구성

### ✅ 보호 라우팅
- 로그인하지 않은 사용자가 접근 시 `/auth`로 리디렉션
- `PrivateRoute.jsx`를 통한 경로 보호 구현
- 예시: `/`, `/reviews`는 로그인한 사용자만 접근 가능

---

## 💡 기술 스택

| 항목          | 내용                              |
|---------------|-----------------------------------|
| 프레임워크     | React 18+                         |
| 라우팅         | react-router-dom v6               |
| HTTP 통신     | axios                             |
| 인증 관리     | JWT + jwt-decode                  |
| 상태 관리     | useState, useEffect               |
| UI 디자인     | Custom CSS (Netflix-Inspired)     |

---

## 📁 디렉터리 구조

```
frontend/
├── public/
│ └── index.html
├── src/
│ ├── api/ # axios 인스턴스
│ │ └── axios.js
│ ├── components/ # Header 컴포넌트 등
│ │ └── Header.jsx
│ ├── pages/ # 페이지 구성
│ │ ├── AuthPage.jsx
│ │ ├── LoginPage.jsx
│ │ ├── RegisterPage.jsx
│ │ └── MovieDetailPage.jsx (예정)
│ ├── routes/ # 보호 라우트
│ │ └── PrivateRoute.jsx
│ ├── App.jsx # 전체 라우터 및 상태 관리
│ └── index.js # 앱 진입점
└── package.json # 종속성 관리
```

---

## 🚀 실행 방법

```bash
cd frontend
npm install
npm start
```

> 기본적으로 `http://localhost:3000`에서 앱이 실행됩니다.  
> `.env` 파일에서 API URL을 지정하지 않은 경우, `axios` 기본 경로는 `/api`로 설정되어 있어 `proxy` 설정을 통해 Django 백엔드와 연결됩니다.

---

## 🔐 인증 흐름 요약

1. `/auth`에서 로그인 또는 회원가입
2. 로그인 성공 시 JWT accessToken을 localStorage에 저장
3. Header에서 이메일 표시 및 보호 페이지 접근 허용
4. 로그아웃 시 토큰 제거 및 상태 초기화

---

## 🧩 향후 구현 예정 기능

- 영화 상세 페이지 및 리뷰 목록/작성 기능
- 리뷰 수정/삭제 및 좋아요 기능
- 게시판 글쓰기 및 댓글 기능
- JWT refresh token 처리 (자동 갱신)
- 반응형 UI 개선 및 페이지 애니메이션 추가

---

## 📄 연동 백엔드

- [🛠 Django REST API 문서 보기](../backend/README.md)

