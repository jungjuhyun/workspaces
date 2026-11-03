# 음악 작업 폴더

현재 작업 문서·코드와 사용자 제공 음원·자료를 관리한다. 2026-11-03 사용자 지시로 외부 이관본과 Claude 작성 문서를 활성 위치에서 제거하고, Codex 후속 기록을 분리해 남겼다.

## 시작점

1. [작업 규칙](AGENTS.md), [공통 작업 방법](common/WORK_METHOD.md)을 읽는다.
2. 해당 프로젝트의 현재 상태를 읽고 필요한 원장·근거만 확인한다.

| 프로젝트 | 현재 상태 |
|---|---|
| 딥하우스 첫 곡 재현 | [CURRENT_STATUS.md](projects/deep-house/CURRENT_STATUS.md) |
| 로파이 jazzhop·hiphop 후속 제작 | [CURRENT_STATUS.md](projects/lofi-playlist/CURRENT_STATUS.md) |
| R&B 보컬·가사 | [CURRENT_STATUS.md](projects/rnb-vocals/CURRENT_STATUS.md) |

공통 제품 관찰 범위는 [SUNO_NOTES.md](common/SUNO_NOTES.md), 새 의뢰 틀은 [PROJECT_BRIEF.md](templates/PROJECT_BRIEF.md)에 있다. 장르별 음악 조건을 다른 프로젝트에 자동 적용하지 않는다.

## 백업 — 필요할 때만 확인

- [기존 딥하우스 백업](archive_backup/deep-house_2026-11-02/): 기존59개 파일을 변경하지 않았다.
- [로파이 jazzhop·hiphop 별도 백업](archive_backup/lofi-jazzhop-hiphop_2026-11-03/README.md): 정리 전 전체 문서와 0.19.1 이관 원본을 보존했다.
- [Claude 문서 추가 백업과 해시](archive_backup/claude-documents_2026-11-03/BACKUP_MANIFEST.json): 활성 위치에서 제거한 딥하우스/공통 문서와 혼합 문서의 정리 전 사본이다.

백업은 현재 지시나 생성 승인으로 쓰지 않는다. 필요한 원문을 확인할 때만 열고 현재 적용 범위를 구분한다. migration/의 이관 기록과 검증 JSON은 당시의 Codex 관리 기록이며 현재 파일 구조나 음악 품질을 보증하지 않는다.

## 음원과 저장

루트 음원·PDF, Deep house playlist/, local/의 원본·분리·분석 데이터와 수집 ZIP은 사용자 입력/작업 자산으로 보존했다. 문서 작성자 정리만으로 이를 삭제하지 않는다. local/와 음원·임시물·인증 정보·archive_backup/은 Git에 커밋하지 않는다.

수정 전 Git 상태와 원격 변경을 확인한다. 로컬 편집·커밋·원격 반영을 구별하고, 사용자가 요청하지 않은 원격 반영은 하지 않는다.
