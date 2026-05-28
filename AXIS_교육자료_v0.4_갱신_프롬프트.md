# 프롬프트 — AXIS 교육 자료 v0.4 갱신

> VSCode 터미널 Claude Code 전용. 이 파일 전체를 복사해서 Claude Code에 붙여넣고 시작.
> 작성자: Cowork Claude · 2026-05-28

---

## 🎯 목표

`~/Desktop/GST/` 하위의 교육 자료 2종을 **현 시점 사실 정합 + 분리된 사이트 구조**에 맞게 갱신.

- `AXIS_교육_슬라이드_v0.3.html` → **`AXIS_교육_슬라이드_v0.4.html`** 새 파일로 저장 (원본 보존)
- `AXIS_교육_진행스크립트_v0.1_초안.md` → **`AXIS_교육_진행스크립트_v0.2.md`** 새 파일로 저장 (원본 보존)

---

## 📂 작업 환경 (경로 확정)

```
~/Desktop/GST/
├── AXIS_교육_슬라이드_v0.3.html         ← 원본 (참조용, 수정 X)
├── AXIS_교육_진행스크립트_v0.1_초안.md   ← 원본 (참조용, 수정 X)
├── AXIS_교육_자료_v0.2.html             ← 단일 페이지 형식 (참고만, 채택 안 됨)
├── AXIS_교육자료_v0.4_갱신_프롬프트.md  ← 이 파일
│
├── axis-manual/                         ← 매뉴얼 사이트 (인증 잠금, v1.9.0+)
│   ├── operator/
│   ├── manager/
│   ├── admin/
│   ├── reference/
│   └── netlify/edge-functions/auth.ts   ← JWT 인증 미들웨어
│
└── axis-consent/                        ← 동의서 사이트 (공개, 신규)
    ├── index.html
    ├── thank-you.html
    └── netlify.toml
```

---

## 🧭 배경 컨텍스트 (Claude Code가 알아야 할 것)

### 1. 교육 운영 개요

- **대상**: 협력사 작업자 (MECH 오전 / ELEC 오후 회차)
- **장소·시간**: 강당 60분
- **형식**: 강사 시연 + 작업자 관람 (실습 X)
- **상태**: 전원 가입 완료 — 신규 입사자만 신규 가입
- **핵심 메시지**: "여러분의 작업이 더 잘 드러나고, GST는 더 정확한 일정을 드릴 수 있습니다"

### 2. axis-manual 현재 상태 (v1.10.0 · 기준 OPS v2.19.11 · VIEW v1.49.1)

v0.3 슬라이드 작성 이후 다음이 누적되었음 — 슬라이드에 반영 필요:

- **v1.2.0**: Manager 페이지 완성 (force-close · manager-delegation)
- **v1.3.0**: Admin Section A 권한 영역 (inactive-users · permissions)
- **v1.4.0** 🔒: **JWT 인증 미들웨어** (Netlify Edge Function) 도입
  - 매뉴얼 사이트 URL 직접 접근 시 401 차단
  - OPS 앱 또는 VIEW의 [📖 매뉴얼] 버튼으로만 진입 가능
  - 폰트·아이콘·robots.txt만 우회 예외
- **v1.5.0**: Admin Section B (checklist-management · qr-etl)
- **v1.6.0**: Admin Section C (factory-dashboard · production)
- **v1.7.0**: Admin Section D (analytics) — **매뉴얼 100% 완성**
- **v1.8.0**: admin 페이지 전수 정정 + **material-master · missing-close 신규**
  - 자재 마스터 수치 정정: **185 자재 · 1,626 BOM** (이전 186/1,640은 placeholder)
  - 4역할 모델 정립 (admin / GST 매니저 / 협력사 매니저 / GST 작업자)
  - 알람 enum 정정 — 22종 전수 (ELEC_INSPECTION_COMPLETE→ELEC_COMPLETE, WORKER_REGISTERED 제거 등)
- **v1.9.0**: 버전 관리 시스템 도입 (VersionBanner · `.vitepress/versions.ts`)
  - 페이지 상단 자동 배너 — 매뉴얼·OPS·VIEW 버전 + 정합 확인일 표시
- **v1.10.0** (최신, 2026-05-28): OPS Sprint 79 통합
  - 신규 페이지: `operator/si-finishing.md` (SI 마무리공정 3 Tab — GST 전용)
  - 신규 페이지: `manager/admin-options.md` (OPS app 안의 admin 옵션 화면)
  - **출하 미처리 자동 이메일 알림** (매일 07:30 KST, default OFF)
  - alert-types § 6 이메일 알림 신규 섹션

매뉴얼 사이드바 최신 구조 (config.ts L70~133 참고):

```
operator/
  · 시작하기 · 로그인·권한 · QR 스캔 · Task 작업 흐름
  · 릴레이·일시정지 · 체크리스트 (TM·ELEC·MECH)
  · SI 마무리공정 (GST 인원, Sprint 79~)   ← v1.10.0 신규
  · 알림 받기 · 출퇴근 (협력사)

manager/
  · 시작하기 · 미종료 작업 관리 · 강제 종료
  · 매니저 권한 위임
  · OPS 관리자 옵션 (GST 인원)              ← v1.10.0 신규

admin/  (Dashboard / Management / Analysis 3카테고리)
  · 공장 대시보드 · 생산 관리
  · QR·ETL 변경 이력 · 체크리스트 관리 · 자재 마스터 · 권한 관리 · 비활성 사용자
  · 종료 누락 분석 · 사용자 분석

reference/
  · 알람 유형 · 버전 이력 · 용어집 · 협력사·공정 매핑
```

**참고: 사이드바 검증 절차**

Claude Code가 작업 시작 전에 다음을 한 번 확인하면 추측 오류 방지:

```bash
cat ~/Desktop/GST/axis-manual/.vitepress/config.ts | sed -n '70,133p'
cat ~/Desktop/GST/axis-manual/.vitepress/versions.ts
```

### 3. axis-consent 분리 운영 (신규)

기존 `axis-manual/public/consent.html` (실제로 push 안 됐음) → **별도 사이트로 분리**:

- 위치: `~/Desktop/GST/axis-consent/`
- 파일: `index.html` (폼) · `thank-you.html` (제출 완료) · `netlify.toml` · `README.md`
- 인증 미들웨어 **없음** — 공개 접근 가능
- Netlify Forms 통합 (`data-netlify="true"`)
- 자필 서명 캔버스 (HTML5 canvas, touch + mouse)
- 동의 항목 3종 필수 (개인정보 수집·제3자 제공·시스템 이용)
- URL은 **아직 미확정** — 사용자가 git/Netlify 설정 중. placeholder로 `[axis-consent URL]` 사용

### 4. 알람 명세 정정 완료 (v1.x 누적)

`axis-manual/reference/alert-types.md`가 v1.x로 대대적 정정됨 — **22종 (DB enum 24종 중 미사용 2종 제외)**:

| 카테고리 | 알람 |
|---|---|
| 작업자 본인 | TASK_REMINDER · SHIFT_END_REMINDER · BREAK_TIME_PAUSE · BREAK_TIME_END · WORKER_APPROVED · WORKER_REJECTED |
| 이상 감지 (매니저) | PROCESS_READY · DURATION_EXCEEDED · REVERSE_COMPLETION · UNFINISHED_AT_CLOSING |
| 매니저 에스컬레이션 | TASK_ESCALATION · TASK_NOT_STARTED · RELAY_ORPHAN · CHECKLIST_DONE_TASK_OPEN · ORPHAN_ON_FINAL |
| 공정 흐름·체크리스트 | TMS_TANK_COMPLETE · TANK_DOCKING_COMPLETE · ELEC_COMPLETE · CHECKLIST_TM_READY · CHECKLIST_MECH_READY · CHECKLIST_ISSUE |
| 시스템 | WORKER_DEACTIVATION_REQUEST |

v0.3 슬라이드에서 알람 표에 잘못 적힌 정보가 있을 수 있음 — 위 정합으로 정정.

---

## ✏️ 갱신해야 할 항목 (상세)

### A. 슬라이드 갱신 (`AXIS_교육_슬라이드_v0.4.html`)

#### A-1. 메타데이터

- 푸터·표지의 버전 라벨 `v0.3` → `v0.4`
- 표지의 갱신일을 오늘 날짜로 (예: `2026-05-28`)

#### A-2. 회차 안내 슬라이드 (현재 §7)

기존 카드 그대로 유지. 단 MECH 강조 영역 한 줄 보강:

- 변경 전: "신규 MECH 체크리스트 73항목 / 20그룹"
- 변경 후: "신규 MECH 체크리스트 73항목 + 자재 마스터(VIEW 등록) 연동"

#### A-3. 본인 카테고리 심화 슬라이드 (현재 §10)

MECH 회차 강조 포인트에서 다음 추가:
- "자재 마스터 SELECT — VIEW [자재 마스터] 페이지에서 등록 가능 (Sprint 66~)"

ELEC 회차는 변경 없음.

#### A-4. 자주 발생 문제 슬라이드 (현재 §11)

**최상단에 추가** (가장 자주 발생 가능성 큼):

| 구분 | 증상 | 해결 |
|---|---|---|
| 공통 | 매뉴얼 사이트 URL 직접 접근 시 "🔒 접근 제한" 표시 | OPS 앱 또는 VIEW의 [📖 매뉴얼] 버튼으로 진입 |

기존 7행은 그대로 유지.

#### A-5. 사후 자료 슬라이드 (현재 §14)

**대대적 갱신** — 매뉴얼 접근 방식이 변경됨:

```
[REFERENCE · 01] AXIS 매뉴얼 사이트
  - "OPS 앱 또는 VIEW의 [📖 매뉴얼] 버튼으로 진입 (인증 필요)"
  - URL 직접 입력은 차단됨을 명시
  - 매뉴얼은 v1.9.0 기준 100% 완성 — operator/manager/admin/reference 모두 작성

[REFERENCE · 02] FAQ 페이지
  - 매뉴얼 사이트 내 /faq 경로 — 동일하게 인증 필요
```

**새로 추가할 영역** (REFERENCE · 03 또는 별 슬라이드):

```
[NEW HIRE · 가입 + 동의서]
  - 신규 입사자: 본인 단말에서 가입 → 협력사 매니저 승인
  - 교육 입장 동의서: 입구 QR로 axis-consent 사이트 진입
  - URL placeholder: [axis-consent URL] — 사용자가 확정 후 교체
  - 1~2분 / 자필 서명 / 자동 제출
```

#### A-6. Q&A 마지막 슬라이드 (현재 §15)

신규 입사자 callout 유지하되 문구 정정:
- "동의서 미제출자는 입구에서 제출" → "동의서 미제출자는 입구 QR 코드로 즉시 제출"

#### A-7. 디자인 톤 (절대 변경 X)

- DM Sans + JetBrains Mono 폰트 그대로
- 색상 토큰 변경 X
- **박스 엣지에 굵은 컬러 보더 금지** — 색상은 텍스트·뱃지·dot에만 사용
- section-num 검정 사각형 뱃지 패턴 유지
- 카드는 `1px solid var(--g200)` 얇은 회색만
- 슬라이드 4번 (Key Message) 만 dark 배경 유지

#### A-8. 슬라이드 추가 시 주의

만약 §14 사후 자료를 1장으로 못 담아 2장으로 분리하면 — JS의 `slides.length` 자동 인식이라 코드 수정 불필요. 단 counter 표시 `/15`가 `/16`으로 자동 변경되는지 확인.

---

### B. 진행 스크립트 갱신 (`AXIS_교육_진행스크립트_v0.2.md`)

#### B-1. 메타데이터

- 상단 버전 `v0.1 초안` → `v0.2`
- 마지막 갱신일 오늘 날짜로

#### B-2. §6 "어디서 더 찾나" 부분

기존 "매뉴얼 사이트 + FAQ" 안내에 다음 추가:

```
- 매뉴얼 사이트는 보안 정책으로 OPS 앱 또는 VIEW를 통해서만 접근 가능합니다.
  앱 홈에서 [📖 매뉴얼] 버튼을 누르면 자동 인증되어 진입합니다.
- 동의서 미제출 시 입구 QR로 즉시 제출 가능합니다 (axis-consent 사이트).
```

#### B-3. §7 "기억할 5가지" 강조 멘트 보강 (5번 항목)

기존:
> 막히면 매뉴얼 사이트 + FAQ — 그 다음 협력사 매니저, 그래도 안 풀리면 GST AX팀

→ 변경:
> 막히면 OPS 앱의 [📖 매뉴얼] 버튼 + FAQ — 그 다음 협력사 매니저, 그래도 안 풀리면 GST AX팀

#### B-4. 강사 사전 점검 체크리스트 (마지막 섹션)

다음 항목 추가:

- [ ] axis-consent URL 입력된 QR 포스터 입구 비치 확인
- [ ] Netlify Forms 응답 알림 받을 DX팀 이메일 설정 확인
- [ ] OPS 앱·VIEW의 [📖 매뉴얼] 버튼 정상 작동 확인 (강사 사전 테스트)

---

## 🔍 검증 단계 (작업 완료 후 실행)

### 1. 슬라이드 v0.4 브라우저 검증

```bash
open ~/Desktop/GST/AXIS_교육_슬라이드_v0.4.html
```

확인:
- 모든 슬라이드 좌우 화살표로 이동 가능
- F 키로 풀스크린 토글
- 마우스 클릭(좌/우 절반)으로 이동
- 우측 하단 counter `n / 총개수` 정확 표시
- 다크 모드 미디어 쿼리 정상 (system 다크 모드일 때)

### 2. 모바일/태블릿 반응형

Chrome DevTools → Device Toolbar:
- iPhone SE (375px)
- iPad (768px)
- Desktop (1280px)

### 3. 인쇄 미리보기

`Cmd+P` → A4 portrait → 각 슬라이드가 별도 페이지로 분리되는지 확인

### 4. 스크립트 v0.2 마크다운 렌더

VSCode → Preview (Cmd+K V) 로 렌더 확인

### 5. 사실 정합성 더블 체크

다음 파일들을 grep 해서 v0.4 슬라이드 내용이 정합한지 검증:

```bash
# 알람 22종 정합
grep -c "^|" ~/Desktop/GST/axis-manual/reference/alert-types.md

# 매뉴얼 사이드바 최신 구조
cat ~/Desktop/GST/axis-manual/.vitepress/config.ts | grep -A 1 "text:"

# JWT 인증 우회 예외 목록
grep -A 5 "pathname ===" ~/Desktop/GST/axis-manual/netlify/edge-functions/auth.ts
```

---

## 📋 진행 절차 추천

1. **읽기 우선** (10분)
   - `AXIS_교육_슬라이드_v0.3.html` 전체 읽기
   - `AXIS_교육_진행스크립트_v0.1_초안.md` 전체 읽기
   - `axis-manual/.vitepress/config.ts` 사이드바 구조 확인
   - `axis-manual/netlify/edge-functions/auth.ts` 인증 우회 정책 확인

2. **계획 정리** (5분)
   - 변경 영역 매핑 (위 A-1 ~ A-8, B-1 ~ B-4)
   - 새 슬라이드 추가 필요 여부 결정 (§14 분리 vs 통합)
   - 사용자에게 확인이 필요한 결정 사항이 있으면 작업 시작 전에 질문

3. **새 파일 작성** (30~40분)
   - `cp AXIS_교육_슬라이드_v0.3.html AXIS_교육_슬라이드_v0.4.html`
   - `cp AXIS_교육_진행스크립트_v0.1_초안.md AXIS_교육_진행스크립트_v0.2.md`
   - 두 새 파일에 각각 갱신 적용 (원본은 그대로)

4. **검증** (15분)
   - 위 "검증 단계" 5개 실행

5. **변경 요약 보고** (5분)
   - 작업한 슬라이드/스크립트의 변경 항목 요약
   - 사용자가 추가로 결정해야 할 사항 (예: §14 분리할지) 정리
   - 잠재적 이슈 (예: counter `/15` → `/16` 변경) 안내

---

## ⚠️ 결정 보류 → 사용자에게 질문할 사항

다음은 작업 진행 중 또는 시작 전에 사용자(Twin파파)에게 확인하면 좋은 항목입니다:

1. **§14 분리 여부** — 사후 자료 슬라이드를 1장으로 통합할지 vs 2장(매뉴얼+동의서)으로 분리할지
2. **axis-consent URL 확정 여부** — 이미 결정됐다면 placeholder 대신 실 URL 박기
3. **JWT 인증 안내 강도** — 작업자 입장에서 "URL 직접 접근 안 됨" 메시지를 강조할지 vs "OPS의 매뉴얼 버튼 사용"만 안내할지
4. **버전 관리 시스템(v1.9.0) 언급 여부** — 작업자가 본인 OPS 버전과 매뉴얼 버전 매칭하는 안내를 별도 슬라이드로 만들지 vs 생략할지

질문이 명확하면 1번부터 순서대로 확인 후 진행 권장.

---

## 🎁 보너스 (시간 여유 시)

- v0.3 슬라이드의 `[매뉴얼 URL — Netlify 배포 주소 삽입]` placeholder는 현재 axis-manual 실 URL로 교체 가능 (사용자에게 확인)
- 슬라이드 7번 회차 안내에 OPS 앱 버전 권장 사항 (v2.12.2+) 작은 글씨로 추가 가능
- 스크립트의 강사 보조 메모에 "v1.9.0 버전 매칭 시연" 한 줄 추가 가능

---

## 🧪 디자인 시스템 토큰 참고 (CSS 변수)

slide v0.3에 이미 정의되어 있으니 그대로 활용:

```css
:root {
  --c: #2A2D35;           /* 본문 텍스트 (다크 그레이) */
  --st: #8B90A0;          /* 보조 텍스트 */
  --a: #6366F1;           /* 액센트 / MECH 카테고리 */
  --a-light: #EEF2FF;     /* 액센트 배경 */
  --bg: #FAFAFA;          /* 페이지 배경 */
  --white: #FFFFFF;
  --g100: #F5F5F7;        /* 카드 배경 (보조) */
  --g200: #E5E7EB;        /* 카드 보더 */
  --g400: #9CA3AF;
  --g500: #6B7280;
  --g700: #374151;
  --green: #059669;       /* OPS / 성공 */
  --green-bg: #ECFDF5;
  --blue: #0070F3;        /* VIEW / ELEC 카테고리 */
  --blue-bg: #EFF6FF;
  --amber: #D97706;       /* 경고 */
  --amber-bg: #FFFBEB;
  --red: #DC2626;         /* LIVE 시연 / 위험 */
  --red-bg: #FEF2F2;
}
```

폰트:
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
font-family: 'DM Sans', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
```

---

## ✅ 완료 기준

- [ ] `AXIS_교육_슬라이드_v0.4.html` 작성 완료 (원본 v0.3 보존)
- [ ] `AXIS_교육_진행스크립트_v0.2.md` 작성 완료 (원본 v0.1 보존)
- [ ] 브라우저 검증 5종 모두 통과
- [ ] 변경 요약 보고 작성
- [ ] 사용자 추가 결정 사항 (있다면) 정리
