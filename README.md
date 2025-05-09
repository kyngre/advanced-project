# 🎬 영화 리뷰 플랫폼

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-REST--Framework-green)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)
![Stack](https://img.shields.io/badge/Stack-Fullstack-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

> 사용자들이 영화를 검색하고, 리뷰를 작성하고, 커뮤니티에서 소통할 수 있는 웹 애플리케이션입니다.

---

## 📑 목차

- [🔧 주요 기능](#-주요-기능)
- [🗂 기술 스택](#-기술-스택)
- [📁 프로젝트 구조](#-프로젝트-구조-백엔드-기준-예시)
- [🚀 실행 방법](#-실행-방법)
- [🔐 JWT 인증 사용법](#-jwt-인증-사용법-swagger에서)
- [📜 변경 로그](#-변경-로그)
- [🛠 향후 계획](#-향후-계획)
- [📊 프로젝트 일정 (Gantt Chart)](#-프로젝트-일정-gantt-chart)
- [📄 라이선스](#-라이선스)
- [🙌 기여 방법](#-기여-방법)
- [👥 기여자들](#-기여자들)

---

## 🔧 주요 기능

### ✅ backend

- [🔧 백엔드 주요 기능](./backend/README.md)

---

## 🗂 기술 스택

| 구분       | 기술 |
|------------|------|
| **Backend** | Django, Django REST Framework, SimpleJWT |
| **Frontend** | React (예정) |
| **DB**      | PostgreSQL or SQLite |
| **Docs**    | Swagger (drf-yasg) |
| **Auth**    | JWT (Access/Refresh Token) |
| **DevOps**  | GitHub, Docker (예정) |

---

## 📁 프로젝트 구조 (백엔드 기준 예시)

```
backend/
├── config/                     # Django 프로젝트 설정 폴더
│   ├── settings.py             # 전체 설정
│   ├── urls.py                 # 전역 URL 라우팅
│   └── wsgi.py / asgi.py       # 배포용 설정
│
├── users/                      # 사용자 앱
│   ├── models.py               # 사용자 모델 (AbstractUser 확장 가능)
│   ├── views.py                # 회원가입, 프로필, 구독 API
│   ├── serializers.py
│   ├── urls.py
│   └── permissions.py
│
├── movies/                     # 영화 앱
│   ├── models.py               # 영화 + OTT ManyToMany
│   ├── views.py                # 조회, 등록, 정렬 등
│   ├── serializers.py
│   └── urls.py
│
├── reviews/                    # 리뷰 + 댓글 + 좋아요
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── urls.py
│
├── ott/                        # OTT 플랫폼 (넷플릭스 등)
│   ├── models.py
│   ├── serializers.py
│   └── urls.py
|
├── board/                      # 게시판 앱
│   ├── models.py               
│   ├── views.py                # 작성, 삭제 등등
│   ├── serializers.py
│   └── urls.py
│
├── manage.py                   # Django 실행 파일
├── requirements.txt            # 패키지 목록
└── db.sqlite3 (또는 PostgreSQL 사용 가능)
```

---

## 🚀 실행 방법

### 1. 가상환경 설치 및 패키지 설치

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 마이그레이션 및 서버 실행

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 3. Swagger 접속

```
http://localhost:8000/swagger/
```

---

## 🔐 JWT 인증 사용법 (Swagger에서)

1. `/api/token/`에서 access, refresh 토큰 발급
2. Swagger 우측 상단 **Authorize** 클릭
3. `Bearer <access_token>` 형식으로 입력 후 인증
4. 인증 후 Swagger에서 각 API를 테스트할 수 있습니다.

**예시**:
- **Access Token 발급 후**: `Bearer <your_access_token>`을 사용하여 요청에 인증을 추가합니다.

---
## 📜 변경 로그

### v1.0.0 (2025-05-05)
- 영화 등록, 목록 조회, 수정, 삭제 기능 구현
- JWT 인증 시스템 추가
- Swagger UI를 통한 API 테스트 기능 구현

### v0.9.0 (2025-04-28)
- 기본 영화 모델과 OTT 연결 기능 구현

---

## 🛠 향후 계획

- React 기반 프론트엔드 연동
- Django Admin 페이지 커스터마이징
- Docker 배포 자동화

---

## 📊 프로젝트 일정 (Gantt Chart)

![Gantt Chart](docs/images/ganttchart.png)

위 이미지는 프로젝트의 주요 일정과 마일스톤을 시각적으로 보여줍니다. 각 단계는 다음과 같이 구성되어 있습니다:
1. **기능 설계 및 백엔드 개발**: API 설계 및 Django 기반 백엔드 구현.
2. **프론트엔드 개발**: React를 사용한 사용자 인터페이스 개발.
3. **통합 테스트 및 디버깅**: 백엔드와 프론트엔드 연동 테스트.
4. **배포 및 유지보수**: Docker를 활용한 배포 및 지속적인 업데이트.

---

## 📄 라이선스
 - 이 프로젝트는 MIT 라이선스를 따릅니다.

---

## 🙌 기여 방법

1. 이 저장소를 fork 합니다.
2. 새로운 브랜치를 만듭니다 (`git checkout -b feature/my-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add my feature'`)
4. PR을 보냅니다!

---

## 👥 기여자들

이 프로젝트에 기여해 주신 분들:

- [@slimshady913](https://github.com/slimshady913) - 주요 기능 개발, 문서화 및 테스트, 디자인 및 UI 개선
- [@kyngre](https://github.com/kyngre) - 라이센스 업데이트

기여해 주셔서 감사합니다! 😊

---