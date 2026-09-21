# Qbasis.One 홈페이지

Astro 정적 사이트입니다. `/`는 한국어, `/en/`은 영어이고, 헤더와 푸터의 `KOR | EN`으로 전환합니다.
디자인은 Qbasis.One Design System 토큰을 따르고, 레이아웃은 jasper.ai를 참고했습니다.

## 실행

```bash
pnpm install
pnpm dev        # http://localhost:4321
pnpm build      # 타입 검사(astro check) 후 dist/ 생성
```

## 내용 교체

코드를 열지 않고 아래 파일만 고치면 됩니다.

| 바꿀 것 | 파일 |
| --- | --- |
| 한국어 문구 | `src/content/ko.json` |
| 영어 문구 | `src/content/en.json` |
| 코드 예제 | `src/content/snippets/ko/*.py`, `src/content/snippets/en/*.py` |
| 회사명, 문의 메일, 이미지 경로 | `src/content/site.json` |
| 측정값(회로 재현도, 게이트 수), VQE 차트 설정 | `src/content/site.json`의 `measured`, `vqe` |
| 로고, 파비콘 | `public/brand/`의 파일을 같은 이름으로 덮어쓰기 |

- `ko.json`과 `en.json`은 키 구조가 같아야 합니다. 한쪽에만 키가 있으면 `pnpm build`의 타입 검사가 실패합니다.
- 측정 타일의 `+820`, `×4.7`과 차트의 배수는 `site.json`의 숫자로 빌드할 때 계산합니다.
  본문 문구(`features.items`의 "약 820 게이트", "약 4.7배")는 직접 맞춰야 합니다.
- 이미지 경로는 `public/` 기준 상대 경로입니다(예: `brand/logo.svg`).

## 디자인 시스템

- `src/styles/design-system/`: Design System 아티팩트의 `tokens/*.css`를 그대로 복사한 파일입니다. 토큰이 바뀌면 다시 복사합니다.
- `src/styles/global.css`: 사이트 전용 규칙입니다. 폰트 스택도 여기서 덮어씁니다.
- 폰트: Space Grotesk(헤드라인), IBM Plex Sans(본문), JetBrains Mono(코드)는 디자인 시스템 폰트입니다.
  세 폰트에 한글 글리프가 없어 나눔고딕을 두 번째 폰트로 둡니다. 모두 OFL-1.1이고 `@fontsource`로 저장소에 포함됩니다.
- 나눔고딕은 400/700/800 굵기만 있어서, 한국어 페이지는 헤드라인 굵기를 600으로 올립니다(`--fw-display`). 한글은 700으로 표시됩니다.

## 배포 (GitHub Pages)

`.github/workflows/deploy.yml`이 `main` 브랜치 push마다 빌드해서 Pages에 올립니다.

1. GitHub 저장소를 만들고 push합니다.
2. 저장소 Settings → Pages → Source를 **GitHub Actions**로 설정합니다.
3. 주소는 `https://<계정>.github.io/<저장소명>/`입니다. 하위 경로는 workflow가 `BASE_PATH`로 넘겨서 링크, 이미지, 폰트에 자동 반영됩니다.
