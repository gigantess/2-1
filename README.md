# 코디세이 2단계 미션: 프롬프트 매니저 (Prompt Manager)

> **Python 3.10+** 및 **Git/GitHub** 환경 실습을 위한 콘솔 기반 AI 프롬프트 관리 프로그램입니다.
> 🔗 **저장소 URL**: [https://github.com/your-username/step2-prompt-manager](https://github.com/your-username/step2-prompt-manager) (예시 URL)

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

## 💡 3. 구현된 주요 기능 및 아키텍처

### 3.1 핵심 기능 (Phase 3 & 4)
1. **프롬프트 추가**: 제목, 내용, 카테고리를 입력받아 새로운 프롬프트를 저장합니다. (동일 제목 중복 방지 및 입력값 정규화 적용)
2. **프롬프트 목록 보기**: 전체 프롬프트 번호, 즐겨찾기 상태(⭐), 카테고리, 제목을 출력합니다.
3. **카테고리별 보기**: 특정 카테고리를 입력받아 해당 카테고리의 프롬프트만 필터링합니다.
4. **프롬프트 검색**: 제목이나 내용에 특정 키워드가 포함된 프롬프트를 검색합니다.
5. **프롬프트 상세 보기**: 프롬프트 번호를 입력받아 구분선과 함께 전체 내용을 출력하고 **조회수를 1 증가**시킵니다.
6. **즐겨찾기 추가/삭제**: 프롬프트 번호로 즐겨찾기(⭐) 상태를 추가하거나 해제합니다.
7. **즐겨찾기 목록 보기**: 즐겨찾기에 등록된 프롬프트만 모아서 출력합니다.

### 3.2 보너스 기능 (Phase 5)
8. **Markdown 내보내기**: `prompts.json` 데이터를 읽어 각 카테고리별로 `.md` 파일을 생성하여 내보냅니다.
9. **인기 프롬프트 (조회수순)**: 조회수가 높은 순서대로 상위 5개의 프롬프트를 출력합니다.
10. **프롬프트 수정**: 기존 프롬프트의 제목, 내용, 카테고리를 변경합니다.
11. **프롬프트 삭제**: 특정 프롬프트를 목록에서 삭제합니다.
12. **JSON 영속화**: `prompts.json`을 사용하여 데이터를 저장하고 로드합니다.

### 3.3 아키텍처 및 설계 원칙
- **메인 루프 설계**: `while True` 무한 루프를 통해 사용자가 명시적으로 `0`을 입력해 종료(`break`)하기 전까지 계속해서 인터랙션을 유지하도록 설계하여 프로그램의 연속성을 보장합니다.
- **입력 정규화 규칙**:
  - 모든 문자열 입력은 앞뒤 공백을 제거(`strip()`)하여 빈 값 입력을 방지합니다.
  - 카테고리명은 검색 및 그룹화의 일관성을 위해 대소문자를 구분하지 않고 관리되도록 설계되었습니다.
- **검색 알고리즘 한계 및 개선 방향**:
  - 현재는 파이썬의 `in` 연산자를 활용한 단순 부분문자열 검색을 사용합니다. 이는 구현이 단순하고 리소스 소모가 적다는 장점이 있습니다.
  - 하지만 한글 특성상 조사가 포함되거나 띄어쓰기가 일치하지 않으면 검색에 실패할 수 있습니다. 향후 **정규표현식(Regex)** 패턴 검색이나 **형태소 분석기를 도입한 N-gram 토큰화** 방식을 적용하여 검색 품질을 고도화할 수 있습니다.

---

## 📋 4. 데이터 구조 및 설계 근거

### 4.1 데이터 구조 (List of Dict) 선택 이유
프롬프트 데이터는 **리스트 안의 딕셔너리(`list-of-dict`)** 형태로 구성됩니다.
- **장점**: 파이썬에서 다루기 가장 직관적이며 JSON 형식과 1:1로 깔끔하게 매핑됩니다. 데이터 순회 및 조작이 간편합니다.
- **대안 비교**: 클래스(Object) 기반 방식이나 관계형 DB(SQLite 등)를 도입하기에는 현재 프로그램의 복잡도와 데이터 규모가 크지 않아 오버엔지니어링이 될 수 있다고 판단했습니다.

### 4.2 JSON 영속화 선택 이유
- JSON 형식은 CSV 형식에 비해 여러 줄(Multi-line)로 구성된 텍스트 데이터(`content`)를 계층적이고 안전하게 보관하는 데 훨씬 유리합니다.
- 향후 프롬프트 데이터가 수만 건 단위로 방대해진다면 파일 기반의 JSON 대신 로컬 DB(SQLite)나 외부 NoSQL DB 형식으로 확장하는 방안을 고려해볼 수 있습니다.

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

## 🌿 6. Git 8대 필수 명령어 및 브랜치 전략

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

### 브랜치 네이밍 및 병합 규칙 (Convention)
- **기능 개발**: 새로운 기능은 반드시 `feature/기능명` 브랜치를 생성하여 작업합니다.
- **버그 수정**: 오류 수정은 `fix/이슈명` 형태로 관리합니다.
- **병합 원칙**: 개별 브랜치에서 기능 구현과 테스트가 모두 완료되면 `main` 브랜치로 `merge`하여 코드 이력을 보호하고 체계적으로 관리합니다.

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
6. 즐겨찾기 추가/삭제
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