# 딥하우스 파일 안내

현재 작업은 지정 플레이리스트 첫 곡0~222초 재현이다. 날짜나 문서 번호만 보고 다음 작업을 정하지 않고, [현재 상태](CURRENT_STATUS.md)를 우선한다.

## 지금 보는 문서

| 목적 | 파일 |
|---|---|
| 최근 사용자 평가·미해결 사항·다음 행동 | [CURRENT_STATUS.md](CURRENT_STATUS.md) |
| 원곡에서 확인한 제작 기준 | [12_FIRST_TRACK_SYNTHESIS_20261103.md](12_FIRST_TRACK_SYNTHESIS_20261103.md) |
| 실제 입력 전문·설정·실행 기록과 미실행S007 수정안 | [13_FIRST_TRACK_PROMPT_LOG.md](13_FIRST_TRACK_PROMPT_LOG.md) |
| 최근 가이드 시험과 “G12가 상대적으로 가깝지만 턱없이 부족”한 사용자 평가 | [19_HARMONIC_GUIDE_COMPARISON.md](19_HARMONIC_GUIDE_COMPARISON.md) |
| G12의SW보완비교·A/B음원·S007 v0.7.1 수정근거 | [20_G12_SW_REVIEW_20261103.md](20_G12_SW_REVIEW_20261103.md) |

## 찾으신 기존 보고서

[04_PROMPT_SOUND_REPORT.md 백업 원문](../../claude/archive_backup/claude-documents_2026-11-03/projects/deep-house/04_PROMPT_SOUND_REPORT.md)

기존 `projects/deep-house/04_PROMPT_SOUND_REPORT.md`는 문서 정리 때 백업 후 활성 위치에서 제거했다. 실제 백업은29,561bytes이며, 백업 원장과SHA256 일치를 확인했다. 파일명 변경이나 현재S006 비교 문서로의 대체가 아니다. 원문의 당시 실험·피드백과 현재 실험을 혼합하지 않는다.

## 필요할 때 보는 누적 기록

| 내용 | 문서 |
|---|---|
| 기능/자료 조사 | [04 Suno 분리·마감 조사](04_SUNO_STEM_WORKFLOW_CHECK_20261102.md), [05 PDF 검토](05_PDF_GUIDE_REVIEW_20261102.md), [10 채널 업데이트 검토](10_CHANNEL_UPDATE_REVIEW_20261103.md) |
| 첫 곡 분석의 과정 | [06 방법](06_FIRST_TRACK_ANALYSIS_METHOD.md), [07 초기 결과](07_LOST_IN_THE_ECHOES_ANALYSIS.md), [08 보완 계획](08_FIRST_TRACK_DEEPENING_PLAN.md), [09 점검 항목](09_FIRST_TRACK_ANALYSIS_CRITERIA_V1.md), [11 보완 결과](11_FIRST_TRACK_REFINEMENT_20261103.md) |
| 이전 생성/수정 경과 | [14 첫 생성 비교](14_FIRST_GENERATION_COMPARISON.md), [15 보컬 누락 수정](15_VOCAL_CHOP_REVISION.md), [16 보컬 Cover 경로](16_COVER_VOCAL_ROUTE.md), [17 저음/편곡 수정](17_G05_HARMONY_ARRANGEMENT_REVISION.md), [18 합성 가이드 제안](18_HARMONIC_GUIDE_PROPOSAL.md) |
| 누적 작업 이력 | [CODEX_WORK_HISTORY.md](CODEX_WORK_HISTORY.md) |
| 재현 가능한 분석/가이드 제작 코드 | [analysis/](analysis/) |

이전 문서의 '미실행'·'응답 대기'는 당시 기록일 수 있다. 현재 실행·허용 범위는CURRENT_STATUS와13의 실제 실행 기록을 확인한다.

## 음원·원자료 위치

- 기준 원본: `../../assets/audio/deep-house/hyper-focus.  deep house music for coding.mp3`.
- 현재 비교 음원/실행JSON/분리 결과: `../../local/deep-house/generation_R01S006_20261103/` — 실제C 일반 폴더.
- S007: `../../local/deep-house/generation_R01S007_20261103/` — 입력 초안만 있고 새 생성 음원은 없다.
- 원곡의 첫222초와 분석 환경: `../../local/deep-house/first_track_20261102/`.
- 수집 ZIP: `../../assets/channel-research/deeparchive_raw_data.zip`. 과거 채널 문서는 위 백업 구역에 있다.

사용자 지시에 따라 실제 재배치를 마쳤다. [claude/](../../claude/README.md)에 기존 작업과백업을, [assets/](../../assets/README.md)에 사용자 원본을 모았다. Codex의첫 곡 분석·생성S001~S007·합성 가이드는local/deep-house에 남겼으며 필요한R01 참조13개도 검증 사본으로 유지한다. 상세 이동표는 `../../local/maintenance/workspace_reorganization_20261103.json`.
