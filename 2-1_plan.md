# 코디세이 2단계 미션: Python & Git 기초 - Git과 함께하는 Python 첫 발자국

코디세이 2단계 미션 "Python & Git 기초: Git과 함께하는 Python 첫 발자국" 수행을 위한 단계별 실행 계획입니다.
모든 요구사항(Python 3.10+, 필수 Git 명령어 8종, 10개 이상의 커밋, 브랜치 병합, README.md, 제출 산출물)을 누락 없이 반영하여 구성했습니다.

---

## 1. 단계별 로드맵 개요

1.  **Phase 1: 개발 환경 구축 및 설정**
    *   VSCode, Python 3.10+, Git 환경 점검 및 캡처.
    *   개발 도구를 설치 및 설정하고, 제출용 환경 스크린샷을 확보합니다.
2.  **Phase 2: Git 저장소 초기화 및 기본 실습**
    *   Git 8대 명령어 실습 및 초기 파일 세팅.
    *   샘플 저장소 Clone 실습부터 로컬/원격 저장소 연결, 첫 Push까지 수행합니다.
3.  **Phase 3: 기본 프로그램 구조 및 초기 데이터 설계**
    *   메인 루프 및 기본 프롬프트 데이터(리스트/딕셔너리) 구현.
    *   기본 데이터(최소 3개)를 구성하고 메뉴 및 메인 루프를 함수 단위로 설계합니다.
4.  **Phase 4: 기능별 단계적 개발 및 Git 브랜치 전략**
    *   브랜치 작업, 기능 구현 및 10개 이상 커밋 달성.
    *   목록 보기 기능은 브랜치에서 작성 후 Merge하며, 제약사항에 맞춰 커밋을 쌓아갑니다.
5.  **Phase 5: 보너스 기능 구현 (선택)**
    *   JSON 영속화, CRUD 및 조회수 정렬.
    *   파일 입출력(JSON/MD) 및 프롬프트 수정/삭제, 조회수 관리 기능을 추가합니다.
6.  **Phase 6: 최종 검증 및 제출물 준비**
    *   `git log` 확인, 실행 스크린샷 및 `README.md` 점검.
    *   모든 제출용 스크린샷을 캡처하고 GitHub 저장소 URL을 준비합니다.

---

## 2. 세부 실행 계획

### Phase 1: 개발 환경 구축 및 설정 (제출용 스크린샷 획득)

#### VSCode 환경 설정
- VSCode 실행 후 Python 확장(Extension) 및 Korean Language Pack 설치.
- VSCode 왼쪽 아래 계정 아이콘을 클릭하여 GitHub 계정 로그인 및 연동 확인.

#### Python 및 Git 버전 점검
- 터미널 실행 후 Python 버전 확인 (3.10 이상 필수):
```bash
python --version  # 또는 python3 --version
```
- 간단한 `hello.py` 작성 및 실행: `print("Hello")`
- Git 버전 확인 및 사용자 정보/기본 브랜치 설정:
```bash
git --version
git config --global user.name "사용자 이름"
git config --global user.email "사용자 이메일"
git config --global init.defaultBranch main
```
- **[제출물 1 확보]** 개발 환경 설정 스크린샷 캡처 (VSCode, Python 버전, Git 설정 출력 화면 포함).

### Phase 2: Git 저장소 초기화 및 필수 명령어 실습

#### Git Clone 실습 및 삭제
- 공개 샘플 저장소를 내려받아 구조와 로그를 확인한 뒤 삭제 (`clone` 명령어 조건 충족):
```bash
git clone https://github.com/octocat/Spoon-Knife.git sample_repo
cd sample_repo && git log --oneline
cd .. && rm -rf sample_repo
```

#### 프로젝트 저장소 생성 및 초기화
- 프로젝트 폴더 생성 및 이동: `mkdir prompt-manager && cd prompt-manager`
- GitHub에서 새 원격 저장소(`prompt-manager`) 생성.
- 로컬 저장소 초기화 (`init` 명령어 조건 충족):
```bash
git init
```

#### 기초 파일 생성 및 첫 커밋/푸시
- `.gitignore` 파일 작성 (Python 캐시 파일 제외): `__pycache__/`, `*.pyc`
- `README.md` 파일 생성 및 기본 제목 작성.
- **[Commit 1]** 첫 커밋 수행 및 원격 저장소 연결/푸시 (`add`, `commit`, `push` 조건 충족):
```bash
git add .
git commit -m "docs: Initial commit with README and gitignore"
git remote add origin <GitHub-저장소-URL>
git push -u origin main
```
- **[Pull 실습]** 원격 반영 확인 후 `git pull` 실행 (`pull` 조건 충족).

### Phase 3 & 4: Python 구현 및 Git 커밋 매핑 (최소 10개 커밋 달성)

각 기능 구현 시 모듈화(함수 분리)를 적용하며, 의미 있는 기능 단위로 커밋을 진행합니다.

| 단계 | 구현 기능 및 파이썬 코드 요소 | 실행할 Git 명령어 | 커밋 메시지 (의미 있는 커밋 예시) |
|---|---|---|---|
| **Step 3.1** | `main.py` 생성 및 기본 프롬프트 데이터(3개 이상) 정의<br>• 구조: `list` 내 `dict` (`title`, `content`, `category`, `favorite`) | `git add main.py`<br>`git commit` | **[Commit 2]** `feat: Add initial prompt dataset` |
| **Step 3.2** | 메뉴 출력 함수 `show_menu()` 및 메인 루프 구현<br>• 잘못된 입력 예외처리 및 `0. 종료` 제어 | `git add main.py`<br>`git commit` | **[Commit 3]** `feat: Implement basic menu display and main loop` |
| **Step 4.1** | 프롬프트 추가 기능 `add_prompt()` 구현<br>• 입력값 검증(빈 값 처리) 및 카테고리 선택 기능 | `git add main.py`<br>`git commit` | **[Commit 4]** `feat: Implement prompt addition function with input validation` |
| **Step 4.2** | **[브랜치 분기]** 목록 보기 기능 구현 (`show_list()`)<br>• 모든 프롬프트 번호, 제목, 카테고리, 즐겨찾기(⭐) 출력 | `git checkout -b feature/list-prompts`<br>`git add main.py`<br>`git commit` | **[Commit 5]** `feat: Implement prompt list display function` |
| **Step 4.3** | **[브랜치 병합]** `main` 브랜치 이동 및 병합 | `git checkout main`<br>`git merge feature/list-prompts` | `checkout`, `merge` 명령어 수행 완료 |
| **Step 4.4** | 카테고리별 조회 기능 `show_by_category()` 구현<br>• 카테고리 선택 시 해당 항목만 필터링하여 출력 | `git add main.py`<br>`git commit` | **[Commit 6]** `feat: Implement category filter function` |
| **Step 4.5** | 프롬프트 검색 기능 `search_prompt()` 구현<br>• 키워드 입력받아 제목/내용 포함 여부 검색 | `git add main.py`<br>`git commit` | **[Commit 7]** `feat: Implement prompt search function by keyword` |
| **Step 4.6** | 상세 보기 기능 `show_detail()` 구현<br>• 프롬프트 번호 입력 시 구분선과 함께 전체 내용 출력 | `git add main.py`<br>`git commit` | **[Commit 8]** `feat: Implement prompt detail view function` |
| **Step 4.7** | 즐겨찾기 관리 `toggle_favorite()` & 목록 `show_favorites()` 구현<br>• 즐겨찾기 토글(`True`/`False`) 및 모아보기 | `git add main.py`<br>`git commit` | **[Commit 9]** `feat: Implement favorite toggle and favorite list view functions` |
| **Step 4.8** | `README.md` 최종 작성 및 코드 정리<br>• 프로그램 이름/설명, 실행 방법, 기능 목록, 카테고리 설명 | `git add README.md`<br>`git commit` | **[Commit 10]** `docs: Complete README.md with project overview and user guide` |

### Phase 5: 보너스 기능 구현 (선택 사항)

#### 보너스 1: JSON 영속화 및 Markdown 내보내기
- `json` 모듈 활용: 프로그램 시작 시 `prompts.json` 로드, 종료/추가 시 저장.
- `export_to_markdown()`: 카테고리별 `.md` 파일 출력.
- **[Commit 11]** `feat: Add JSON persistence and Markdown export capabilities`

#### 보너스 2: CRUD(수정/삭제) 및 조회수 정렬
- `edit_prompt()`, `delete_prompt()` 구현.
- 상세 보기(`show_detail`) 시 `views` 카운트 증가 및 Top 목록 조회 기능 구현.
- **[Commit 12]** `feat: Add CRUD edit/delete and view count tracking features`

### Phase 6: 최종 검증 및 제출 산출물 준비

#### 원격 저장소 푸시
```bash
git push origin main
```

#### 제출물 4종 최종 점검
**산출물 체크리스트**
- GitHub 저장소 URL: Public 저장소 권한 확인.
- 개발 환경 설정 스크린샷: VSCode, Python 3.10+ 버전(`python --version`), Git 설정(`git config --list`) 포함.
- 프로그램 실행 결과 스크린샷: 메뉴 화면, 프롬프트 추가, 목록 조회, 검색, 상세 보기, 즐겨찾기 결과 캡처.
- Git 로그 스크린샷: 터미널에서 아래 명령어 실행 결과 캡처 (최소 10개 커밋 및 브랜치 병합 그래프 확인).
```bash
git log --oneline --graph
```

---

## 3. Git 필수 명령어 충족 검증표

| 필수 Git 명령어 | 적용 위치 및 수행 내역 |
|---|---|
| `init` | Phase 2.2 - 로컬 프로젝트 폴더 저장소 초기화 |
| `add` | Phase 2 & 4 - 각 기능 작성 후 스테이징 영역 추가 |
| `commit` | Phase 2 & 4 - 기능 단위별 최소 10회 이상 커밋 수행 |
| `push` | Phase 2.3 & 6.1 - 로컬 내역 원격 저장소(`main`) 상주 반영 |
| `pull` | Phase 2.3 - 원격 저장소 변경 사항 동기화 실습 |
| `checkout` | Phase 4.2 & 4.3 - `feature/list-prompts` 브랜치 이동 및 `main` 복귀 |
| `clone` | Phase 2.1 - 공개 샘플 저장소 다운로드 후 구조 확인 실습 |
| `merge` | Phase 4.3 - `feature/list-prompts` 브랜치를 `main`으로 병합 |