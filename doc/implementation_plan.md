# 프롬프트 매니저 구현 계획 (2-1_plan.md 기반)

`2-1_plan.md` 문서에 명시된 요구사항과 단계별 지침에 따라 `prompt-manager` 폴더 내에 프롬프트 관리자 프로그램을 파이썬으로 구현하고 Git 커밋 기록을 남길 계획입니다.

## User Review Required

- 본 계획은 로컬 저장소에서의 Git 명령어(init, add, commit, branch, merge) 수행과 Python 코드 구현을 자동화하여 진행합니다.
- GitHub 원격 저장소 연동(clone, remote add, push, pull)은 사용자 계정 인증이 필요하므로 AI가 직접 수행할 수 없습니다. 따라서 원격 저장소 관련 명령어는 생략하거나 로컬 커밋으로 대체하여 진행합니다. (필요 시 직접 원격 저장소에 Push 하셔야 합니다.)
- `prompt-manager` 폴더 내에 새로운 Git 저장소를 초기화(`git init`)하여 진행합니다. 상위 폴더(`step2`)가 이미 Git 저장소이므로, 중첩된 Git 저장소가 생성될 수 있습니다. 진행해도 괜찮으신가요?

## Proposed Changes

요구사항에 맞추어 다음 단계를 순차적으로 실행하며 코드를 작성하고 Git 커밋을 기록합니다.

### Phase 2: 기본 설정
- `prompt-manager` 폴더에서 `git init` 수행
- `README.md` 생성 및 `.gitignore` 작성 (Python 캐시 제외)
- 커밋: `docs: Initial commit with README and gitignore`

### Phase 3 & 4: 기능 구현 및 Git 브랜치 전략
- **Step 3.1**: `main.py`에 기본 데이터셋 3개 추가 (커밋: `feat: Add initial prompt dataset`)
- **Step 3.2**: 메인 메뉴 및 프로그램 루프 구현 (커밋: `feat: Implement basic menu display and main loop`)
- **Step 4.1**: 새로운 프롬프트 추가 기능 구현 (커밋: `feat: Implement prompt addition function with input validation`)
- **Step 4.2 & 4.3**: `feature/list-prompts` 브랜치 생성 후 목록 보기 기능 구현, 커밋 후 `main` 브랜치에 병합 (커밋: `feat: Implement prompt list display function` 및 병합 완료)
- **Step 4.4**: 카테고리별 조회 기능 구현 (커밋: `feat: Implement category filter function`)
- **Step 4.5**: 검색 기능 구현 (커밋: `feat: Implement prompt search function by keyword`)
- **Step 4.6**: 상세 보기 기능 구현 (커밋: `feat: Implement prompt detail view function`)
- **Step 4.7**: 즐겨찾기 토글 및 모아보기 기능 구현 (커밋: `feat: Implement favorite toggle and favorite list view functions`)
- **Step 4.8**: `README.md` 최종 작성 (커밋: `docs: Complete README.md with project overview and user guide`)

### Phase 5: 보너스 기능 구현
- **보너스 1**: JSON 영속화 (시작 시 로드, 변경 시 저장) 및 Markdown 내보내기 기능 추가 (커밋: `feat: Add JSON persistence and Markdown export capabilities`)
- **보너스 2**: 프롬프트 수정/삭제(CRUD) 기능 및 조회수 정렬 기능 추가 (커밋: `feat: Add CRUD edit/delete and view count tracking features`)

위 계획에 따라 각 단계별로 코드를 작성하고 커밋을 남기는 스크립트를 작성하여 한 번에 실행하거나, 순차적으로 구현을 진행하겠습니다. 승인해 주시면 즉시 작업을 시작하겠습니다.
