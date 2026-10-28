# workspaces

음악 제작의 작업 방법, 판단 기준과 프로젝트 기록을 이어서 사용하는 저장소입니다.

## 새 채팅에서 시작하기

이 저장소에 접근 가능한 Work 채팅에서 다음과 같이 요청합니다.

> 이 저장소의 AGENTS.md, common/WORK_METHOD.md를 읽어라. 기존 로파이 작업을 이어간다면 projects/lofi-playlist/CURRENT_STATUS.md부터 확인하라. 새 장르라면 기존 장르의 음악 조건을 가져오지 말고, 내가 원하는 음악부터 접수하라. 필요한 문서를 실제로 읽은 뒤 작업하라.

저장소 연결만으로 모든 문서를 자동으로 읽었다고 가정하지 않습니다. 채팅 기억보다 저장된 요구, 출처, 결정과 실행 기록을 근거로 삼습니다.

## 문서 위치

| 위치 | 용도 |
|---|---|
| [AGENTS.md](AGENTS.md) | AI가 작업할 때 따를 공통 규칙 |
| [common/WORK_METHOD.md](common/WORK_METHOD.md) | 장르를 바꿔도 이어받는 작업 방법 |
| [common/SUNO_NOTES.md](common/SUNO_NOTES.md) | 제품 정보와 계정 관찰을 다루는 방법 |
| [projects/lofi-playlist/CURRENT_STATUS.md](projects/lofi-playlist/CURRENT_STATUS.md) | 현재 로파이 작업의 시작점과 최근 상태 |
| [templates/PROJECT_BRIEF.md](templates/PROJECT_BRIEF.md) | 새 음악 프로젝트를 시작할 때 쓸 접수 틀 |
| [migration/IMPORT_MANIFEST.json](migration/IMPORT_MANIFEST.json) | 가져온 43개 파일의 크기·SHA-256 기록 |

## 저장과 재개

문서의 현재 기준본은 이 저장소에서 관리합니다. 예전에 전달한 개별 파일과 ZIP은 당시 배포본이며, 같은 내용을 양쪽에서 독립적으로 수정하지 않습니다. GitHub 저장까지 완료한 경우에만 원격 저장 완료라고 보고합니다.

작업 시작 시 원격 변경과 작업 폴더의 미저장 변경을 확인합니다. 작업이 끝나면 필요한 문서와 현재 상태를 갱신해 함께 커밋합니다. 다른 채팅에서 동시에 같은 파일을 수정할 때는 작업 범위를 나누고 충돌을 확인합니다. 기존 변경을 임의로 버리지 않습니다.

새 장르는 projects/<project-name>/에서 시작합니다. 공통 절차는 재사용하고, 분위기·주악기·템포·금지 요소·비교 대상은 새 요청으로 정합니다. 장르가 달라졌다는 이유만으로 모든 문서를 다시 작성하지 않습니다.

음원은 기존 보관 위치와 곡 링크를 사용합니다. 원본 음원, 미리듣기 파일, 브라우저 자료, 임시 전송 파일, 인증 정보는 이 저장소에 포함하지 않습니다.

## 최초 이관 기록 — 2026-10-28

기존 main에는 이 README만 있었습니다. suno_lofi_research의 0.19.1 배포본 42개 파일과 이후 음원 비교 보고서 1개를 원문 그대로 가져왔습니다. 최신 상태는 CURRENT_STATUS.md에서 보완하며, 이전 문서의 과거 시점 설명을 현재 결과로 읽지 않습니다.
