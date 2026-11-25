# 작업 규칙 (공통)

2026-11-14 정리본. 지금 유효한 규칙만 적는다. 바뀐 경과는 [common/CHANGELOG.md](common/CHANGELOG.md)에 있다.

## 사용자 메시지마다 적용하는 규칙

사용자 메시지를 받을 때마다 답변하거나 도구를 사용하기 전에, 이번 요청에 조사가 필요한지와 필요한 정보가 빠져 있는지를 다시 판단한다. 후속 질문, 정정, 작업 도중의 추가 지시에도 적용한다.

- **조사가 필요하면 반드시 웹 검색부터 한다.** 검색한 원문을 확인한 뒤 근거를 바탕으로 판단한다. 제품 기능과 분석 기법은 공식 문서·논문을, 사용 경험은 커뮤니티 원문을 확인하고 사용한 출처를 결과에 연결한다. 프로젝트의 주제·곡 버전·청취 평가는 해당 원장, 실제 음원, 사용자 답변과 대조한다.
- 오타 수정, 단순 조회, 지시가 명확한 작업은 질문 없이 바로 수행한다.
- 요청에 상위 목표(Why), 대상(Who), 완료 기준(Success), 제약 조건(Constraint) 중 하나라도 빠져 있어서 방향이 달라질 수 있다면, 계획·코드 작성 전에 반드시 `interview-me` 스킬을 먼저 실행한다. 진행 중 새로 발견한 정보 누락에도 같은 기준을 적용한다.
- 인터뷰로 의도가 확정되면 목표(Why)와 하지 않을 것(Out of scope)을 해당 작업의 파일로 저장하고, 새 세션에서 깔끔하게 구현할 수 있도록 그 자리에서 턴을 멈춘다.

## 프로젝트

| 제작 프로젝트 | 현재 작업 경로 | 시작점 |
|---|---|---|
| Lofi | `projects/Lofi/` | [현황](projects/Lofi/CURRENT_STATUS.md) · [제작 기준](projects/Lofi/02_PRODUCTION_STANDARD.md) · [입력 원장](projects/Lofi/18_PROMPT_REGISTER.md) |
| Off the leon | `projects/Off the leon/` | [현황](<projects/Off the leon/CURRENT_STATUS.md>) · [곡 원장](<projects/Off the leon/music/SONG_PRODUCTION_REGISTER.md>) · [채널 규칙](<projects/Off the leon/channel/CHANNEL_RULES.md>) |
| Deep house and R&B | `projects/Deep house and R&B/Deep house/`, `projects/Deep house and R&B/R&B/` | [딥하우스 현황](<projects/Deep house and R&B/Deep house/CURRENT_STATUS.md>) · [R&B 현황](<projects/Deep house and R&B/R&B/CURRENT_STATUS.md>) |

popment 원자료는 [Off the leon의 레퍼런스](<projects/Off the leon/reference/popment/README.md>)에서 찾는다. 직접 생성한 곡은 곡 ID로 소속을 확인한다. 상세 경계와 참조 전환은 [분리 계획](common/migration/PROJECT_SEPARATION_PLAN_20261119.md)을 따른다.

## 시작할 때 읽는 것

1. 이 문서.
2. 해당 프로젝트의 CURRENT_STATUS.md. 현재 결정, 미해결, 다음 할 일만 담은 짧은 문서다. 지난 경과는 같은 폴더의 STATUS_LOG 파일에서 필요한 부분만 찾아 읽는다.
3. 하려는 일에 해당하는 문서를 실제로 연다.

| 하려는 일 | 읽을 문서 |
|---|---|
| 음악·오디오 분석 | common/AUDIO_ANALYSIS_WORKFLOW.md |
| 음악 제작 | common/WORK_METHOD.md, 프로젝트의 제작 기준과 입력 원장 |
| off the leon 곡 제작 | [프로젝트 작업 규칙](<projects/Off the leon/AGENTS.md>)에 따라 제작 방법과 곡 원장을 읽는다. 가사 작성·수정·검수 시작 전에는 [작사 방법](<projects/Off the leon/music/LYRIC_WRITING_METHOD.md>) 전문을 실제로 읽는다. |
| Suno 기능·설정 판단 | common/SUNO_NOTES.md, 프로젝트의 당시 관찰 기록 |
| Suno 곡 WAV 녹음(링크 하나 또는 원장 번호) | [녹음 방법](common/recording/README.md) |
| AI Studio 보완 분석 | common/AI_ANALYSIS_SETTINGS.md |
| 이미지 평가 | common/IMAGE_REVIEW_METHOD.md |
| 채널 제목·설명·썸네일·이미지 프롬프트 | projects/Off the leon/channel/CHANNEL_RULES.md |

## 일하는 방식

- 사용자의 최신 지시가 우선이다. 기준 채널, 방향, 캐릭터, 음악 장르 같은 결정은 사용자가 한다. 판단과 근거를 제시하고 결정을 받는다.
- 요청받은 범위까지 한다. 분석·조사·프롬프트 작성 요청은 생성, 유료 실행, 업로드, 게시 요청이 아니다. 이미 허용된 작업은 다시 묻지 않고 진행한다.
- 합성, 색 보정, 후처리, 조사처럼 직접 할 수 있는 일은 직접 한다.
- 프롬프트에는 사용자가 요청한 속성만 넣는다. 수정은 최신 채택본에서 요청받은 부분만 바꾸고 나머지는 보존한다.
- 읽고 확인한 것만 말한다. 프롬프트의 의도, 제품 기능, 생성 결과, 신호 측정, 사용자 청취 평가, AI 직접 청취를 구분해서 적는다.
- 음악 조사도 위 메시지별 규칙을 따른다. 실제 음원 측정과 모델 분석은 [로컬 오디오 분석 절차](common/AUDIO_ANALYSIS_WORKFLOW.md)에 따라 진행한다.
- Suno 입력은 Style, Exclude, 필요한 설정을 모두 담은 통합본으로 제공하고 프로젝트 원장에 전문과 버전을 남긴다.
- 수정본을 전달할 때는 변경 사항을 모든 해당 위치에 반영한 전체본을 답변 본문에 먼저 제시한다. 복사할 텍스트는 실제 입력칸마다 완전한 블록 하나로 제공한다. 변경 설명은 전체본 뒤에 둔다.
- 한 프로젝트의 음악 조건을 다른 프로젝트에 옮기지 않는다. 새 장르나 목적 변경은 요구 정리부터 한다.

## 기록

- CURRENT_STATUS.md는 덮어써서 갱신한다. 현재 결정, 미해결, 다음 할 일만 두 장 이내로 유지한다.
- 경과는 STATUS_LOG 파일에 날짜별로 덧붙인다. 실제로 한 일과 제안, 사용자 실행과 AI 실행을 구분한다.
- 규칙 문서에는 현재 규칙만 적는다. 바뀐 경과는 common/CHANGELOG.md에 적는다.
- 같은 규칙을 여러 문서에 복사하지 않는다. 원문 한 곳을 가리킨다.
- 한국어 문장은 띄어쓰기를 지켜 쓴다.

## 저장

- 수정 전에 git status와 원격 변경을 확인한다. 사용자나 다른 에이전트의 변경을 덮어쓰지 않는다. 같은 파일을 두 에이전트가 동시에 고치지 않는다.
- 커밋과 원격 반영은 사용자 지시가 있을 때만 한다. 했을 때만 무엇을 했는지 보고한다.
- 음원, 임시 분석물, 모델, 인증 정보는 커밋하지 않고 local/ 아래에 둔다.

## 과거 자료

claude/archive_backup/과 각 프로젝트의 보관 폴더는 과거 자료다. 현재 시작점으로 읽지 않는다. 근거가 필요할 때만 원문을 확인한다.
