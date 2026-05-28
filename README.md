# axis-consent — AXIS 시스템 사용 동의서

> GST AX본부 DX팀 · 협력사 작업자 교육 입장용 디지털 동의서
> AXIS-OPS / AXIS-VIEW 시스템 사용에 관한 「개인정보 보호법」 기반 사전 동의 수집

axis-manual과 **분리 운영**되는 독립 사이트. 인증 미들웨어 없이 누구나 QR로 접근 가능.

---

## 🏗️ 구조

```
axis-consent/
├── index.html          # 동의 폼 (Netlify Forms + 자필 서명 캔버스)
├── thank-you.html      # 제출 완료 페이지
├── netlify.toml        # Netlify 배포 설정 (빌드 X, 정적 publish)
├── README.md           # 이 파일
└── .gitignore
```

**기술 스택**: 정적 HTML + Vanilla JS · 외부 의존성 0 · 빌드 도구 X

---

## 🚀 배포

### 옵션 A. Netlify Drop (가장 빠름, 일회성)

1. https://app.netlify.com/drop 접속
2. `axis-consent/` 폴더 통째로 drag & drop
3. 사이트 생성 + URL 발급 (예: `random-name-12345.netlify.app`)
4. Site settings → Change site name → `axis-consent` 등 의미 있는 이름으로

### 옵션 B. Git 연동 (운영 권장)

```bash
cd ~/Desktop/GST/axis-consent
git init
git add .
git commit -m "Initial: AXIS 동의서 v1.0.0"

# GitHub repo 신규 생성 후
git remote add origin https://github.com/<org>/axis-consent.git
git push -u origin main
```

그 다음 Netlify:
1. https://app.netlify.com/start → Import from Git
2. GitHub repo 선택
3. Build settings (이미 netlify.toml에 정의됨, 기본값 그대로)
4. Deploy

### 옵션 C. Netlify CLI

```bash
npm install -g netlify-cli
cd ~/Desktop/GST/axis-consent
netlify deploy --prod --dir=.
```

---

## 📬 Netlify Forms 활성화 확인

배포 후 Netlify 대시보드 → **Forms** 탭에서 `consent` 폼이 자동 인식되었는지 확인.

만약 안 보이면:
- Site settings → Forms → "Form detection" 활성화
- index.html의 `<form data-netlify="true">` 속성 확인

### 응답 확인

- Netlify 대시보드 → Forms → `consent` → 제출 목록
- 각 제출에는 `signature` 필드에 자필 서명 PNG (base64 data URL)이 포함됨
- CSV 내보내기: Forms 탭의 "Export" 버튼

### 알림 설정 (선택)

Site settings → Forms → Notifications:
- 새 제출 시 이메일 발송 (DX팀 메일 주소)
- Slack/Outgoing webhook 가능

---

## 🔗 QR 코드 재생성

새 URL이 확정되면 (예: `https://axis-consent.netlify.app`) QR 이미지를 재생성:

```bash
# axis-consent와 같은 부모 폴더 ~/Desktop/GST/ 에 gen_qr.py가 있음
cd ~/Desktop/GST
python3 gen_qr.py "https://axis-consent.netlify.app/"
```

생성된 `AXIS_동의서_QR.png` 를 입구용 A4 포스터(`AXIS_동의서_QR_포스터.html`)에 반영.

---

## 🔒 보안 / 운영 정책

- **공개 접근**: 인증 없이 누구나 폼 작성 가능 (의도된 설계)
- **수집 데이터**: 성명·소속·역할·이메일·교육 회차·교육 일자·동의 3종·자필 서명
- **수집 항목 변경 시**: 「개인정보 보호법」 기반이므로 법무·인사팀 검토 필수
- **응답 보관**: Netlify Forms 기본 100 submissions/월 무료. 운영 안정화 후 Pro 플랜 또는 Webhook으로 자사 DB 연동 검토
- **자필 서명 데이터**: base64 PNG 형태. 응답당 ~10-30KB

---

## 📅 갱신 이력

| 버전 | 일자 | 변경 |
|---|---|---|
| v1.0.0 | 2026-05-28 | 초기 배포 — 4종 → 3종 필수 동의(개인정보 수집·제3자 제공·시스템 이용) + 자필 서명 캔버스 |

---

## 관련 문서 (외부)

- `~/Desktop/GST/AXIS_시스템_사용_및_교육_참여_동의서_v0.3_초안.docx` — 종이 보관용 양식
- `~/Desktop/GST/AXIS_동의서_QR_포스터.pdf` — 교육 입구용 A4 포스터
- `~/Desktop/GST/AXIS_동의서_QR.png` — QR 이미지 (PNG)
- `~/Desktop/GST/gen_qr.py` — QR 재생성 스크립트
- `~/Desktop/GST/axis-manual/` — 매뉴얼 사이트 (분리 운영)
