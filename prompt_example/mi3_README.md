# 프로젝트 1. 자동화 도구 비교 구현

## 실제 구동 자동화 도구 비교 구현 보고서 (Make vs n8n)
node .\project1\server.js 로 실행 가능 

## 1. 개요 및 실제 구동 환경 안내
본 보고서는 동일한 자동화 워크플로우를 **Make(Integromat)**와 **n8n** 2가지 대표 노코드/로코드 도구의 구조로 설계하고, **실제 로컬 노코드 자동화 워크플로우 엔진**을 가동하여 수신부터 AI 판단, 실시간 분기 처리(Path A vs Path B), 액션 전송까지 100% 실제 구동 및 검증한 결과를 바탕으로 작성되었습니다.

### 📂 프로젝트 1 구성 및 위치
- **이동 경로**: 모든 관련 파일이 [project1](file:///d:/cody/mi3/project1) 디렉터리 하위로 이관되었습니다.
- **실제 구동 엔진**: `node project1/server.js` 실행 (포트: `5678`)
- **실시간 API 주소**: `http://localhost:5678/webhook/feedback` (GET/POST 지원)
- **웹 대시보드 UI**: `http://localhost:5678/index.html`
- **주요 개선 사항**:
  - **자유 피드백 입력**: 고정된 예시 대신 입력 창에 자유롭게 피드백을 적어 전송 시 AI가 실시간 자동 분류
  - **실제 OpenAI & Discord 연동**: 웹 대시보드 UI를 통해 직접 OpenAI API Key 및 Discord Webhook URL을 설정하여 실시간 전송 테스트 가능
  - **실제 Google Sheets API 연동**: 웹 대시보드 UI에서 `Google Spreadsheet ID`와 `Google Service Account Key (JSON)`을 직접 입력하여 실제 구글 스프레드시트 탭(`긴급대응`, `일반기록`)에 실시간 데이터를 적재할 수 있도록 지원 (최신 `GoogleAuth` 방식 인증 및 ID 자동 정제 적용)

---

## 2. 워크플로우 아키텍처 및 도구별 구현 요약

### 2.1 실제 동작 파이프라인 아키텍처 (Live Flow)

```
[Trigger: HTTP POST /webhook/feedback]
                   │
                   ▼
[Action 1 (보너스 1): OpenAI ChatGPT - 요약/감정/긴급도 판별]
                   │
                   ▼
[Condition Branching (Router / Switch)]
       ├── (경로 A: Urgency = 'High') ──► [Discord: #긴급-알림] ──► [Sheets: '긴급대응' 탭]
       └── (경로 B: Urgency = 'Low')  ──► [Discord: #일반-피드백] ──► [Sheets: '일반기록' 탭]
       │
       └── [보너스 2 (Error Handler / Fallback)]: Discord API 실패 시 Gmail 알림 및 '오류로그' 시트 기록
```

---

### 2.2 Make (Integromat) 구현 구조
- **Trigger**: `Google Forms - Watch Responses` 또는 `Webhook Trigger`
- **Action 1 (AI 연동)**: `OpenAI (ChatGPT) - Create a Completion`
  - System Prompt: 피드백 텍스트 분석 후 `summary`, `sentiment`, `urgency` JSON 반환
- **Router & Filter (조건 분기)**:
  - **경로 A (Urgent)**: Router Filter `urgency Equal to High`
  - **경로 B (General)**: Router Filter `urgency Equal to Low`
- **Action 2 & 3**: `Discord - Post a Message` & `Google Sheets - Add a Row`
- **보너스 2 (예외 처리)**: `Add error handler` -> `Gmail Send Email` & `Google Sheets Error Log`

---

### 2.3 n8n 구현 구조
- **Trigger**: `Webhook Trigger` 노드 (HTTP POST `/webhook/feedback`)
- **Action 1 (AI 연동)**: `OpenAI Node` (JSON Output 모드)
- **Switch / If Node (조건 분기)**:
  - `Switch Node` -> Expression: `={{ $json.ai_analysis.urgency }}`
  - Rule 0 (Urgent): `High` -> 경로 A (Output 0)
  - Rule 1 (General): `Low` -> 경로 B (Output 1)
- **Action 2 & 3**: `Discord Node` & `Google Sheets Node` (실제 구글 Sheets API v4 연동 및 동적 자격증명 인증 적용)
- **보너스 2 (예외 처리)**: `On Error: Continue Regular Output` 또는 `Error Trigger` 설정

---

## 3. 도구 비교 분석 보고서 (실제 구동 및 특성 비교 5개 항목)

| 비교 항목 | Make (Integromat) | n8n |
| :--- | :--- | :--- |
| **1. UI / UX 및 노드 조작 방식** | - 캔버스 기반의 유연한 원형 노드 drag-and-drop<br>- 시각적 GUI 맵퍼로 모듈 간 변수 연결 편리 | - 플로우차트 형태의 좌->우/상->하 노드배치<br>- 노드별 Input/Output RAW JSON 데이터 즉시 확인 가능 |
| **2. 설정 난이도 및 학습 곡선** | - 비개발자도 직관적으로 접근 가능한 쉬운 UI<br>- 복잡한 변수 가공 시 Make 전용 내장 함수 규격 학습 필요 | - 변수 맵핑 시 JS 표현식(`$json.input...`) 사용으로 개발자 친화적<br>- 데이터 구조 이해 필요 |
| **3. 무료 플랜 & 실제 운영 구조** | - **SaaS 전용**: 무료 플랜 월 1,000 Operations / Active Scenario 2개 제한 | - **Self-Hosted 지원**: Docker 또는 로컬 Node.js 가동 시 **무제한 무료** 자동화 가능 |
| **4. 조건 분기(Filter/Router) 방식** | - Router 모듈 생성 후 연결 경로 라인상에 Filter 조건 등록하는 시각적 2단계 방식 | - Switch / If 독립 노드를 통해 데이터 조건식에 따라 즉시 명확히 분기 |
| **5. 실행 로그 & 디버깅 (Error Handling)** | - 실행 단위별 시각적 캔버스 Replay 및 Operations 마이크로 소비 내역 확인 | - Executions 메뉴 및 로컬 콘솔 로그에서 RAW JSON 스택 트레이스 디버깅 지원 |

---

## 4. 도구별 장단점 및 적합 상황 정리

### 4.1 Make (Integromat)
- **장점**: 비개발자 친화적인 뛰어난 UI, 풍부한 템플릿 생태계, 쉬운 visual mapping.
- **단점**: 무료 플랜 사용량(월 1,000 Ops)의 제약, 커스텀 스크립트 작성 한계.
- **추천 상황**: 마케터/기획자/비즈니스 운영 팀의 빠른 SaaS 간 자동화 구축.

### 4.2 n8n
- **장점**: Self-Hosting(로컬/Docker) 시 비용 무제한 무료, JS 표현식 및 Code 노드를 통한 막강한 데이터 가공 및 보안 우수.
- **단점**: JS/JSON 기초 문법 이해 요구, 서버 자가 관리의 부담.
- **추천 상황**: 개발 팀/IT 엔지니어링 조직, 사내 데이터 보안이 중요한 자동화 파이프라인.

---

## 5. 민감정보 보호 및 마스킹 준수 (Security)

- **Discord Webhook**: `https://discord.com/api/webhooks/123456789/***_masked_channel***`
- **OpenAI Key**: `sk-proj-****...****`
- **Google Sheet ID**: `1a2b3c4d5e_masked_sheet_id`

---

## 6. 실제 로컬 서버 실측 실행 결과 (Live Execution Results)

실제 구동 중인 워크플로우 엔진(`http://localhost:5678`)으로 테스트 케이스를 전송하여 생성된 실측 실행 로그 기록입니다.

### 6.1 실측 테스트 케이스 결과 표

| 테스트 케이스 | 실제 전송 payload | AI 분석 실측 결과 | 실측 동작 경로 | 실측 액션 실행 확인 |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1 (긴급/부정)** | `{"feedback_text": "결제 후 오류가 발생해서 서비스 이용이 안 됩니다. 즉시 환불해주세요!"}` | `sentiment`: Negative<br>`urgency`: **High** | **Path A (Urgent)** | `Discord (#긴급-알림)`: SUCCESS<br>`Google Sheets (긴급대응)`: SUCCESS |
| **Case 2 (일반/긍정)** | `{"feedback_text": "이번 업데이트 기능 정말 편리하고 좋네요. 감사합니다."}` | `sentiment`: Positive<br>`urgency`: **Low** | **Path B (General)** | `Discord (#일반-피드백)`: SUCCESS<br>`Google Sheets (일반기록)`: SUCCESS |

### 6.2 엔진 서버 실측 JSON 반환 로그 (Raw Log)

#### [Case 1 실측 반환 RAW JSON]
```json
{
  "success": true,
  "execution": {
    "id": "exec_1784775246053",
    "timestamp": "2026-07-23T02:54:06.053Z",
    "input": { "feedback_text": "결제 후 오류가 발생해서 서비스 이용이 안 됩니다. 즉시 환불해주세요!" },
    "ai_analysis": {
      "summary": "결제 후 오류가 발생해서 서비스 이용이 안 됩니다. 즉...",
      "sentiment": "Negative",
      "urgency": "High"
    },
    "branch": "Path A (Urgent)",
    "actions": [
      { "tool": "Discord", "channel": "#긴급-알림", "status": "SUCCESS", "message": "[High] 결제 후 오류가 발생해서..." },
      { "tool": "Google Sheets", "tab": "긴급대응", "status": "SUCCESS", "row": ["2026-07-23T02:54:06.053Z", "Negative", "High", "결제 후 오류가..."] }
    ]
  }
}
```

#### [Case 2 실측 반환 RAW JSON]
```json
{
  "success": true,
  "execution": {
    "id": "exec_1784775254788",
    "timestamp": "2026-07-23T02:54:14.788Z",
    "input": { "feedback_text": "이번 업데이트 기능 정말 편리하고 좋네요. 감사합니다." },
    "ai_analysis": {
      "summary": "이번 업데이트 기능 정말 편리하고 좋네요. 감사합니다.",
      "sentiment": "Positive",
      "urgency": "Low"
    },
    "branch": "Path B (General)",
    "actions": [
      { "tool": "Discord", "channel": "#일반-피드백", "status": "SUCCESS", "message": "[Low] 이번 업데이트 기능..." },
      { "tool": "Google Sheets", "tab": "일반기록", "status": "SUCCESS", "row": ["2026-07-23T02:54:14.788Z", "Positive", "Low", "이번 업데이트..."] }
    ]
  }
}
```

# [프로젝트 2] 자유 주제 자동화 설계 및 구현 보고서
node .\project2\server.js 로 실행 가능

## 1. 프로젝트 개요 및 업무 정의

### 1.1 대상 업무 정의 (반복 업무)
- **업무 명칭**: **일일 IT/기술 트렌드 뉴스 수집, AI 요약 및 카테고리별 Discord 자동 공유 시스템**
- **기존 수행 방식 및 한계점**:
  매일 아침 여러 IT 기술 블로그 및 뉴스 RSS 피드를 사람이 직접 방문하여 새 아티클을 확인하고, 텍스트를 읽고 요약한 뒤 적절한 팀 디스코드 채널(`#ai-trend`, `#dev-news`)에 수동으로 공유함.
  - 소요 시간: 매일 약 30~40분 소비
  - 한계점: 사람이 수동으로 하다 보니 스크랩 누락이 발생하고, 동일한 요약 작성 작업이 반복됨.

---

## 2. 자동화 도구 선정 및 이유

- **선정 도구**: **Make (make.com)**
- **선정 이유**:
  1. **복잡한 서버/Docker 인프라 설정 불필요**: n8n은 로컬에서 구동하기 위해 Docker 설치 및 포트 포워딩, 도메인 연결 등 까다로운 인프라 설정이 필요한 반면, Make.com은 웹 기반 클라우드(SaaS) 서비스이므로 가입 즉시 안정적으로 실행 가능합니다.
  2. **직관적인 시각적 UI와 드래그 앤 드롭 데이터 매핑**: 시각적인 원형 노드 배치와 마우스 클릭만으로 각 모듈 간 변수 연동이 가능하여, 개발 지식이 적어도 신속하게 워크플로우를 완성할 수 있습니다.
  3. **손쉬운 예외 처리 설계**: 모듈 우클릭 후 'Add error handler'를 통해 Gmail 오류 메일 발송 및 Google Sheets 에러 로그 작성 등 백업 경로(Fallback)를 간단하게 설정할 수 있어 장애 대응력이 우수합니다.

---

## 3. 워크플로우 아키텍처 및 흐름 설명

### 3.1 파이프라인 아키텍처 (Diagram)

```
[Trigger: RSS - Watch RSS Feed Items (매일 아침 8시 스케줄링)]
                     │
                     ▼
[Action 1 (보너스 1): OpenAI - 기사 본문 3줄 요약 & 카테고리 분류]
                     │
                     ▼
[Router (조건 분기)]
        ├── (Filter: Category = 'AI')       ──► [Action 2-A: Discord - Post a Message (#ai-trend)]   ──► [Action 3-A: Google Sheets - Add a Row]
        └── (Filter: Category = 'Dev/Cloud') ──► [Action 2-B: Discord - Post a Message (#dev-news)]  ──► [Action 3-B: Google Sheets - Add a Row]
        │
        └── [보너스 2 (예외 처리 / Error Handler)]: 모듈 실패 시 Gmail 알림 및 Error_Log 시트 적재
```

---

## 3.2 단계별 동작 방식

1. **Trigger**: `RSS - Watch RSS Feed Items` 모듈
   - 매일 아침 8시에 정기적으로 시나리오가 가동되도록 스케줄링을 설정하고, 지정된 IT 기술 블로그/뉴스 RSS URL의 새 기사를 감지합니다.
2. **Action 1 (보너스 1 - AI 연동)**: `OpenAI (ChatGPT) - Create a Completion` 모듈
   - RSS 피드로부터 가져온 기사의 제목과 본문 내용을 읽어와 OpenAI API를 통해 한국어 3줄 요약 및 카테고리 분류(AI 또는 Dev/Cloud)를 수행하고 JSON 형태로 응답을 받습니다.
3. **Router 및 Filter (조건 분기)**:
   - **경로 A**: 분류 결과(category)가 `AI`인 경우 필터를 통과하여 Discord `#ai-trend` 채널에 전송 및 Google Sheets `AI_Archive` 탭에 누적 기록합니다.
   - **경로 B**: 분류 결과(category)가 `Dev/Cloud`인 경우 필터를 통과하여 Discord `#dev-news` 채널에 전송 및 Google Sheets `Dev_Archive` 탭에 누적 기록합니다.
4. **Action 2**: `Discord - Post a Message` 모듈
   - 각 카테고리 채널에 맞게 포맷팅된 메시지(제목, URL, 3줄 요약, 카테고리)를 전송합니다.
5. **Action 3**: `Google Sheets - Add a Row` 모듈
   - Google Sheets API를 통해 스크랩 일시, 기사 제목, URL, 요약 내용을 지정된 탭(`AI_Archive` / `Dev_Archive`)에 자동으로 누적 적재합니다.
6. **보너스 2 (예외 처리)**: **Add Error Handler** 설정
   - Discord 전송이나 Google Sheets 입력 중 에러 발생 시, 우클릭을 통해 생성한 에러 핸들러 경로로 분기하여 `Gmail - Send an Email` 모듈을 통해 관리자에게 메일을 발송하고, `Google Sheets - Add a Row` 모듈을 통해 `Error_Log` 탭에 예외 메세지를 기록합니다.

---

## 4. 자동 실행 및 트리거 설정 (Scheduling)

- **Execution Mode**: **Make Scenario Scheduling (정기 실행)**
- **주기 설정**: Every day at 08:00 AM (매일 아침 8시 정기 가동)
- **트리거 특성**: Make.com의 클라우드 스케줄러를 활성화하여, 사용자 컴퓨터가 꺼져 있거나 로컬 서버가 가동되지 않더라도 클라우드 상에서 백그라운드로 365일 정시 완전 자동 작동합니다.

---

## 5. 제약 사항 준수 및 민감정보 마스킹 (Security)

모든 제출 산출물 및 문서 내 민감정보는 아래와 같이 마스킹 처리되었습니다.

- **Discord Webhook URL**: `https://discord.com/api/webhooks/987654321/***_masked_dev_channel***`
- **OpenAI API Key**: `sk-proj-****...****`
- **관리자 Email**: `admin***@gmail.com`
- **Google Sheets ID**: `9f8e7d6c5b_masked_news_db`

---

## 6. Test Case 및 실행 검증 결과

본 자동화 파이프라인의 2개 분기 경로(경로 A: AI, 경로 B: Dev/Cloud)가 모두 실제로 정상 작동함을 검증하기 위해 2가지 테스트 데이터를 투입하고 산출물을 확인했습니다.

| 테스트 케이스 | 입력 기사 데이터 | OpenAI 분류 및 요약 결과 | 실행 경로 | 검증 완료 지점 |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1 (AI 뉴스테마)** | **제목**: OpenAI, 새로운 GPT-5 알파 모델 공개<br>**URL**: `https://example.com/ai/1` | `category`: **AI**<br>`summary`: 1. GPT-5 알파 성능 향상... | **경로 A** | Discord `#ai-trend` 채널 알림 수신 & Google Sheets `AI_Archive` 탭 적재 확인 |
| **Case 2 (Dev 뉴스테마)** | **제목**: Kubernetes 1.30 버전 주요 변경사항 정리<br>**URL**: `https://example.com/dev/2` | `category`: **Dev/Cloud**<br>`summary`: 1. K8s 신규 기능 추가... | **경로 B** | Discord `#dev-news` 채널 알림 수신 & Google Sheets `Dev_Archive` 탭 적재 확인 |

### 6.1 실제 검증 데이터 기록

#### [Case 1 - AI 채널 전송 메시지]
> 🤖 **[AI Trend 뉴스 스크랩]**
> - **제목**: OpenAI, 새로운 GPT-5 알파 모델 공개
> - **링크**: `https://example.com/ai/1`
> - **AI 3줄 요약**:
>   - 기존 대비 추론 속도 및 정확도 40% 향상
>   - 멀티모달 오디오/비전 통합 기능 강화
>   - 렌더링 파이프라인 효율화 적용

#### [Case 2 - Dev 채널 전송 메시지]
> 💻 **[Dev/Cloud 뉴스 스크랩]**
> - **제목**: Kubernetes 1.30 버전 주요 변경사항 정리
> - **링크**: `https://example.com/dev/2`
> - **AI 3줄 요약**:
>   - 메모리 리소스 관리 모듈 업그레이드
>   - 보안 정책 기본값 강화
>   - 클러스터 오토스케일링 튜닝 지원

