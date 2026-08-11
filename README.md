# 코디세이 2단계 미션: 프롬프트 매니저 (Prompt Manager)

> **Python 3.10+** 및 **Git/GitHub** 환경 실습을 위한 콘솔 기반 AI 프롬프트 관리 프로그램입니다.

---

## 🚀 1. 프로젝트 학습 목표

GenAI 활용에 필수적인 프롬프트(텍스트 요약, 이미지 생성, 페르소나 부여 등)를 체계적으로 관리, 분류, 검색, 탐색하는 프로그램입니다.

### 주요 학습 달성 목표
- **VSCode & Python**: Python 3.10 이상 개발 환경 구축 및 함수 기반 모듈화 파이썬 프로그래밍 구현.
- **Git & GitHub 필수 명령어**: Version Control System(VCS)의 원리를 이해하고 필수 명령어 8종 실습 완료.
- **브랜치 활용 전략**: 기능 개발 브랜치(`feature/list-prompts`)를 생성, 체크아웃(`checkout`), 병합(`merge`)하여 코드 이력을 체계적으로 관리.

---

## 🛠 2. 개발 환경 구축 (Development Environment)

* **Editor**: Visual Studio Code (VSCode)
  * Extensions: Python Extension, Korean Language Pack
* **Language**: Python 3.10 이상
* **VCS**: Git 2.x / GitHub

### 개발 환경 점검 및 Git 초기 설정 명령어
```bash
# 1. Python 버전 확인 (3.10 이상 필수)
python --version   # 또는 python3 --version

# 2. Git 버전 확인 및 기본 설정
git --version
git config --global user.name "사용자 이름"
git config --global user.email "사용자 이메일"
git config --global init.defaultBranch main
```

---

## 💡 3. 구현된 주요 기능 및 카테고리 분류

### 핵심 기능 (Phase 3 & 4)
1. **프롬프트 추가**: 제목, 내용, 카테고리를 입력받아 새로운 프롬프트를 저장합니다.
2. **프롬프트 목록 보기**: 전체 프롬프트 번호, 즐겨찾기 상태(⭐), 카테고리, 제목을 출력합니다.
3. **카테고리별 보기**: 특정 카테고리를 입력받아 해당 카테고리의 프롬프트만 필터링합니다.
4. **프롬프트 검색**: 제목이나 내용에 특정 키워드가 포함된 프롬프트를 검색합니다.
5. **프롬프트 상세 보기**: 프롬프트 번호를 입력받아 구분선과 함께 전체 내용을 출력하고 **조회수를 1 증가**시킵니다.
6. **즐겨찾기 토글**: 프롬프트 번호로 즐겨찾기(⭐) 상태를 켜거나 끕니다.
7. **즐겨찾기 목록 보기**: 즐겨찾기에 등록된 프롬프트만 모아서 출력합니다.

### 보너스 기능 (Phase 5)
8. **Markdown 내보내기**: `prompts.json` 데이터를 읽어 각 카테고리별로 `.md` 파일을 생성하여 내보냅니다.
9. **인기 프롬프트 (조회수순)**: 조회수가 높은 순서대로 상위 5개의 프롬프트를 출력합니다.
10. **프롬프트 수정**: 기존 프롬프트의 제목, 내용, 카테고리를 변경합니다.
11. **프롬프트 삭제**: 특정 프롬프트를 목록에서 삭제합니다.
12. **JSON 영속화**: `prompts.json`을 사용하여 데이터를 저장하고 로드합니다. 프로그램이 종료되어도 데이터가 유지됩니다.

### 세부 카테고리 분류
- **텍스트 요약/작성**: 블로그 포스팅, 기사 요약, 이메일 초안 작성 등
- **이미지 생성**: Midjourney, DALL-E 등 이미지 생성기용 프롬프트
- **코딩 보조**: 코드 리뷰, 리팩토링, 버그 수정 프롬프트
- **업무 자동화**: 회의록 요약, 데이터 분석, 반복 업무 자동화 프롬프트
- **멀티미디어**: 영상 생성, 오디오 스크립트 작성 등

---

## 📋 4. 데이터 구조 및 기본 데이터

### 데이터 구조 (List of Dict)
초기 데이터는 다음과 같이 딕셔너리의 리스트 형태로 구성됩니다.
```python
prompts = [
    {
        "title": "회의록 요약 코치 (Few-shot & Persona)",
        "content": "[역할(Persona)]\n너는 20년 경력의 'SW 품질 컨설팅 전문 프로젝트 매니저' 역할을 수행하는 AI 업무 코치야.\n\n[목표(Objective)]\n제공되는 회의 녹취록이나 메모를 분석하여, 명확한 결정사항과 Action Item을 도출하고 사내 공유용 템플릿에 맞춰 요약본을 작성한다.\n\n[작업 원칙 및 안전장치]\n1. 추측성 표현을 절대 금지하며, 원문에 없는 내용은 절대 지어내지 않는다.\n2. 사실/수치/정책/일정과 관련된 내용 중 근거가 부족하거나 모호한 부분은 임의로 작성하지 말고 반드시 \"확인 필요\" 항목으로 별도 분류한다.",
        "category": "업무자동화",
        "favorite": True,
        "views": 0
    },
    {
        "title": "시네마틱 영상 생성 (Google Veo 3.1)",
        "content": "[Scene 01: 무채색의 일상]\nCinematic bust shot of a 20-year-old Asian Gen Z youth with short black hair, wearing a black oversized streetwear hoodie, standing in a dull, monochrome gray subway station. The youth is bored and expressionless, blinks slowly, and lets out a subtle sigh, dropping their shoulders slightly. The camera has a very slight handheld shake. Flat, diffuse lighting, muted monochrome color palette, highly detailed, photorealistic, shot on 35mm lens.",
        "category": "멀티미디어",
        "favorite": True,
        "views": 0
    },
    {
        "title": "고객 피드백 실시간 JSON 분석",
        "content": "당신은 고객의 피드백을 실시간으로 분석하는 전문 AI 어시스턴트입니다.\n사용자가 제공한 피드백 텍스트를 분석하여 아래 세 가지 항목을 도출하고, 반드시 유효한 JSON 형식으로만 응답해 주세요.\n\n1. summary: 피드백의 핵심 내용을 파악하여 1문장으로 요약\n2. sentiment: 감정 판별 (Positive / Negative / Neutral)\n3. urgency: 긴급도 판별 (High / Low)",
        "category": "데이터분석",
        "favorite": False,
        "views": 0
    }
]
```

---

## ▶️ 5. 프로그램 실행 방법 (How to Run)

### 저장소 복제 (Clone)
```bash
git clone <GitHub-저장소-URL>
cd prompt-manager
```

### 프로그램 실행
```bash
python main.py
```

---

## 🌿 6. Git 8대 필수 명령어 활용 요약 및 커밋 이력

### 필수 Git 8대 명령어 실습 내역
| 명령어 | 프로젝트 내 활용 내용 |
|---|---|
| `git init` | 저장소 생성 및 초기화 실습 (현재 최상위 경로 기준) |
| `git add` | 작업한 `main.py` 및 각종 파일들을 스테이징 영역에 추가 |
| `git commit` | 기능 구현 단계별로 의미 있는 커밋 메시지와 함께 변경사항 기록 |
| `git push` | 로컬 커밋 이력을 원격 저장소에 업로드 |
| `git pull` | 원격 저장소의 최신 변경 이력을 로컬로 병합 |
| `git checkout` | `feature/list-prompts` 브랜치로 분기 및 `main` 브랜치 복귀 |
| `git clone` | 샘플 저장소 복제 실습 |
| `git merge` | 목록 보기 기능이 완성된 브랜치를 `main` 브랜치에 병합 |

### 브랜치 작업 및 커밋 이력
- **브랜치 분기**: 목록 출력 기능 개발 시 `feature/list-prompts` 브랜치를 생성(`checkout`)하여 작업 후, `main` 브랜치로 병합(`merge`)하여 코드 이력을 관리했습니다.
- **커밋 규칙**: 각 기능 단위별로 의미 있는 커밋 메시지 작성 (최소 10개 이상 커밋 달성).

```bash
# 브랜치 병합 및 커밋 이력 확인 명령어
git log --oneline --graph
```

---

## 💻 7. 프로그램 실행 화면 예시
```plaintext
==============================
프롬프트 관리자
==============================
1. 프롬프트 추가
2. 프롬프트 목록 보기
3. 카테고리별 보기
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 토글
7. 즐겨찾기 목록 보기
8. Markdown 내보내기
9. 인기 프롬프트 (조회수순)
10. 프롬프트 수정
11. 프롬프트 삭제
0. 종료
==============================
메뉴를 선택하세요: 2

--- 프롬프트 목록 ---
[1] ⭐ [업무자동화] 회의록 요약 코치 (Few-shot & Persona)
[2] ⭐ [멀티미디어] 시네마틱 영상 생성 (Google Veo 3.1)
[3]    [데이터분석] 고객 피드백 실시간 JSON 분석
[4]    [데이터분석] IT 뉴스 기사 자동 요약 및 분류
```

---

## ✅ 8. 최종 결과물 체크리스트
- [x] GitHub 저장소 URL: 공개(Public) 권한 설정
- [x] 개발 환경 설정 스크린샷: VSCode, Python 3.10+ 버전, Git config 설정 화면
- [x] 프로그램 실행 결과 스크린샷: 메뉴, 프롬프트 추가, 목록, 검색, 상세 보기, 즐겨찾기 실행 화면
- [x] Git 로그 스크린샷: `git log --oneline --graph` 실행 화면 (최소 10개 커밋 및 브랜치 병합 내역 포함)