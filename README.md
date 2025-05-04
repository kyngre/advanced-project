# 🎬 영화 리뷰 플랫폼

> 사용자들이 영화를 검색하고, 리뷰를 작성하고, 커뮤니티에서 토론할 수 있는 웹 애플리케이션입니다.

---

## 🔧 주요 기능

### ✅ 사용자 기능
- JWT 기반 회원가입 및 로그인
- 프로필 조회 및 OTT 구독 설정
- 토큰 기반 인증 시스템

### ✅ 영화 기능
- 영화 등록, 목록 조회, 상세 보기, 수정/삭제
- 영화 정렬 기능 (평점, 개봉일, 제목 등)
- OTT 플랫폼과의 다대다 연결

### ✅ 리뷰 및 커뮤니티
- 영화별 리뷰 작성 및 조회
- 리뷰 평점(1~5점) 및 좋아요 기능
- 댓글 등록 및 삭제 (작성자만 삭제 가능)
- 리뷰별 평점 평균 자동 계산

### ✅ Swagger 문서화
- API 자동 문서화 (drf-yasg)
- 한글 설명 제공
- `/swagger/` 경로에서 테스트 가능

---

## 🗂 기술 스택

| 구분       | 기술 |
|------------|------|
| **Backend** | Django, Django REST Framework, SimpleJWT |
| **Frontend** | React (예정) |
| **DB**      | PostgreSQL or SQLite (개발 단계) |
| **Docs**    | Swagger (drf-yasg) |
| **Auth**    | JWT (Access/Refresh Token) |
| **DevOps**  | GitHub, Docker (예정) |

---

## 📁 프로젝트 구조 (백엔드 기준)

backend/
├── users/ # 사용자 기능 (회원가입, 프로필, 구독)
├── movies/ # 영화 모델 및 API
├── reviews/ # 리뷰, 댓글, 좋아요
├── ott/ # OTT 플랫폼 관리
├── config/ # 프로젝트 설정
├── manage.py