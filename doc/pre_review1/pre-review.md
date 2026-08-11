PASS
평가 항목 #1
근거
README.md > 'python --version # 또는 python3 --version'
잘한 점
README에 Python 버전 확인 명령이 명시되어 있음
부족한 점
실행 스크린샷(명령 출력)은 없음
보완
python --version 출력 스크린샷을 추가 제출하세요
PASS
평가 항목 #2
근거
README.md > 'git --version'
잘한 점
Git 버전 확인 명령을 문서화함
부족한 점
git config 출력 스크린샷은 미제출
보완
git --version과 git config 출력 캡처를 첨부하세요
FAIL
평가 항목 #3
부족한 점
저장소의 실제 GitHub URL이 문서/파일에 없음
보완
공개 저장소 URL을 README나 제출물에 명시하세요
FAIL
평가 항목 #4
부족한 점
샘플 repo clone 실행 로그(출력/스크린샷)가 없음
보완
git clone 실행 화면 또는 터미널 로그 캡처를 제출하세요
PASS
평가 항목 #5
근거
prompt-manager/main.py > '메뉴를 선택하세요: '
잘한 점
메뉴 출력과 사용자 입력(숫자 비교) 흐름이 구현되어 있음
부족한 점
메뉴 선택 동작의 실행 캡처는 없음
보완
메뉴 선택 인터랙션 스크린샷을 추가 제출하세요
PASS
평가 항목 #6
근거
prompt-manager/main.py > 'def add_prompt():'
잘한 점
add_prompt 함수로 등록 로직이 분리되어 구현되어 있음
부족한 점
중복 제목 처리 등 등록 정책은 없음
보완
등록 시 중복 검사 정책을 문서화하거나 안내문을 추가하세요
PASS
평가 항목 #7
근거
prompt-manager/main.py > 'def show_by_category():'
잘한 점
카테고리 필터 함수가 별도 구현되어 있음
부족한 점
대소문자나 유사 카테고리 매핑 규칙은 없음
보완
카테고리 입력의 대소문자/유사명 처리 방안을 문서로 보완하세요
PASS
평가 항목 #8
근거
prompt-manager/main.py > "if keyword in p['title'].lower() or keyword in p['content'].lower()"
잘한 점
제목/내용 대상으로 부분문자열 검색이 구현되어 있음
부족한 점
정규화(토큰화)나 언어별 처리 설명은 없음
보완
검색 방식의 장단점(부분문자열 vs 정규표현식)을 간단히 문서화하세요
PASS
평가 항목 #9
근거
prompt-manager/main.py > "prompts[idx]['favorite'] = not prompts[idx]['favorite']"
잘한 점
즐겨찾기 토글 로직이 명확히 구현되어 있음
부족한 점
즐겨찾기 추가/삭제 이력(로그) 저장은 없음
보완
토글 동작의 사용자 피드백(예: 상태 변경 로그)을 보강하세요
FAIL
평가 항목 #10
부족한 점
브랜치 생성/병합을 입증하는 git log/graph 실행 결과가 없음
보완
git log --oneline --graph 출력 스크린샷을 제출하세요
PASS
평가 항목 #11
근거
README.md > '# 코디세이 2단계 미션: 프롬프트 매니저 (Prompt Manager)'
잘한 점
상세한 README가 존재하며 실행방법과 기능을 정리함
부족한 점
원격 저장소 링크와 실제 커밋 스냅샷은 없음
보완
README에 저장소 URL과 커밋/브랜치 요약을 추가하세요
PASS
평가 항목 #12
근거
prompt-manager/main.py > 'def show_menu():'
잘한 점
기능별로 함수(예: show_menu)가 분리되어 구현되어 있음
부족한 점
각 함수의 역할·입출력 명세 문서는 부족함
보완
주요 함수별 짧은 설명(한 줄)을 README나 코드 주석에 추가하세요
PASS
평가 항목 #13
근거
prompt-manager/main.py > 'prompts = ['
잘한 점
프롬프트가 리스트 내 딕셔너리 구조로 명확히 정의되어 있음
부족한 점
데이터 구조 선택 이유(장단점)는 문서화되어 있지 않음
보완
왜 list-of-dict를 선택했는지 간단한 근거를 README에 기재하세요
PASS
평가 항목 #14
근거
prompt-manager/main.py > '오류: 제목은 필수입니다.'
잘한 점
입력 빈값 검증과 숫자 입력 예외처리가 코드에 구현됨
부족한 점
입력 허용 범위나 형식 규칙 문서는 부족함
보완
입력 규칙(최대 길이, 허용 문자 등)을 문서로 정리하세요
PASS
평가 항목 #15
근거
README.md > '커밋 규칙: 각 기능 단위별로 의미 있는 커밋 메시지 작성 (최소 10개 이상 커밋 달성).''
잘한 점
기능 단위 커밋 기준을 문서에서 명시하고 있음
부족한 점
실제 커밋 로그(예: git log 스냅샷)는 제출되지 않음
보완
주요 커밋 메시지 예시 또는 git log 스크린샷을 첨부하세요
FAIL
평가 항목 #16
부족한 점
리스트·딕셔너리 선택의 장단점(설계 근거) 설명이 없음
보완
데이터구조 선택 이유와 대안의 장단점을 README에 서술하세요
FAIL
평가 항목 #17
부족한 점
while 반복 설계 이유(종료 조건 등)에 대한 명시적 설명이 없음
보완
메인 루프 설계 이유와 종료 조건을 문서로 보완하세요
PASS
평가 항목 #18
근거
prompt-manager/main.py > "if keyword in p['title'].lower() or keyword in p['content'].lower()"
잘한 점
검색이 부분문자열 검사 방식으로 구현되어 있음을 코드로 확인함
부족한 점
검색 성능/정확도 개선 방안 설명은 없음
보완
부분문자열 방식의 한계와 개선 방향(토큰화 등)을 간단히 추가하세요
PASS
평가 항목 #19
근거
README.md > '브랜치 활용 전략: 기능 개발 브랜치(`feature/list-prompts`)를 생성, 체크아웃(`checkout`), 병합(`merge`)하여 코드 이력을 체계적으로 관리.'
잘한 점
브랜치 분리·병합 목적(코드 이력 관리)을 문서에서 설명함
부족한 점
브랜치 명세·병합 규칙(컨벤션)은 구체화되어 있지 않음
보완
브랜치 네이밍·병합 기준을 간단히 명시하세요
PASS
평가 항목 #20
근거
prompt-manager/main.py > "DATA_FILE = 'prompts.json'"
잘한 점
JSON 파일 기반 영속화가 코드와 문서에 구현·명시되어 있음
부족한 점
대체 파일 형식(예: CSV, DB) 비교 제안은 없음
보완
영속화 형식 선택 이유와 확장 방안을 README에 덧붙이세요
FAIL
평가 항목 #21
부족한 점
동명(중복), 충돌, 카테고리 충돌 처리 규칙이 구현·문서화되어 있지 않음
보완
동명/충돌 처리 규칙(예: 자동 접미사, 확인 프롬프트)을 문서화하거나 코드에 반영하세요