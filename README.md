# 음악 작업 폴더

현재 작업에는 Codex가 작성한 문서·코드·생성/분석 결과를 남긴다. Claude의 기존 문서·실험·음원 분리 자료·백업은 **[claude/](claude/README.md)** 한곳에 모았다. 사용자 제공 음원·PDF·수집ZIP은 **[assets/](assets/README.md)** 에 있다.

## 현재 작업 시작점

먼저 [AGENTS.md](AGENTS.md), [공통 작업 방법](common/WORK_METHOD.md), 해당 프로젝트의 현재 상태를 읽는다.

| 프로젝트 | 시작점 |
|---|---|
| 딥하우스 첫 곡 재현 | [파일 안내](projects/deep-house/README.md) · [현재 상태](projects/deep-house/CURRENT_STATUS.md) · [입력 원장](projects/deep-house/13_FIRST_TRACK_PROMPT_LOG.md) |
| 로파이 jazzhop·hiphop | [Codex 후속 기록의 현재 상태](projects/lofi-playlist/CURRENT_STATUS.md) |
| R&B 보컬·가사 | [현재 상태](projects/rnb-vocals/CURRENT_STATUS.md) |

## 폴더 구분

| 폴더 | 내용 |
|---|---|
| projects/ | Codex의 프로젝트 문서·입력 원장·분석 코드 |
| local/deep-house/ | Codex의 첫 곡 분석·S001~S007·합성 가이드와 현재 분석에 필요한 참조 파일 |
| assets/ | 사용자 제공 원본 음원9개·PDF2개·채널 조사ZIP |
| claude/ | Claude의 기존 자료, 과거 실험/분리 파일과 기존 백업. 로파이 jazzhop·hiphop 백업도 이 안에 별도 보존 |
| common/, templates/ | Codex 공통 작업 규칙·제품 관찰·요청 틀·이관 감사 기록 |
| local/tmp/, local/maintenance/ | 임시 PDF 추출물, 정리 도구·이동 원장·검증 기록 |

루트에는 음원·PDF·이전 실험 폴더를 두지 않는다. 생성/분석 작업은 계속C드라이브에서 한다.

## 찾으신 보고서

[04_PROMPT_SOUND_REPORT.md 원문](claude/archive_backup/claude-documents_2026-11-03/projects/deep-house/04_PROMPT_SOUND_REPORT.md)

2026-11-03 문서 정리 때 백업한 파일이며 이번에는 claude 아래로 이동했다. 기존 백업 내용은 변경하지 않았다. 현재 제작 기준은 프로젝트CURRENT_STATUS와입력 원장이 우선한다.

## 보존과 검증

2026-11-03 실제39개 경로를 재배치했다. 이동한808개 파일(22,434,019,238bytes)의SHA256을 전후 대조했다. 현재 분석에서 재사용하는 첫 곡 참조13개는 별도 사본을 만들고 해시 일치를 확인했다. 재사용 참조를 Codex 신규 제작 음원으로 세지 않는다.

상세 이동표·이전/현재 경로·해시는 local/maintenance/workspace_reorganization_20261103.json에 있다. 이전 백업 문서의 절대 경로는 당시 기록으로 보존했으므로 찾을 때 [claude 안내](claude/README.md)와 이동표를 사용한다.

음원·원자료·모델/실행 환경·백업은Git에 넣지 않는다. 문서·코드·안내만 로컬 커밋하며 원격 반영 여부는 별도로 보고한다.
