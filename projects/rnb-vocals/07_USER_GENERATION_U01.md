# 사용자 생성 U01 — 영어 번안 가사와 V4 스타일

기록일: 2026-11-02 (Asia/Seoul). 사용자가 직접 실행했다고 보고한 생성이다. AI의 생성·청취 기록이 아니다. 생성 횟수, 곡 링크·파일 위치, 실제 곡 제목은 제공되지 않았다.

## 사용자가 보고한 입력

- 가사: 직전 제공한 「나였을 텐데」 영어 번안 V1을 사용했다고 보고. 전문은 06_ID_STILL_BE_ME_EN_ADAPTATION_V1.md에 보존했다. 실제 입력 화면이나 수정 여부를 AI가 확인한 것은 아니다.
- Style 전문:

```text
Moody midtempo contemporary R&B with a humid late-night atmosphere, relaxed syncopated groove, rounded bass, crisp understated drums, muted electric keys, soft hazy synth layers. Smooth youthful male tenor, conversational phrasing, light warm tone with a subtle breathy edge, relaxed speech-like delivery, natural full-voice lead with brief soft falsetto lifts at phrase endings. Keep verses intimate and lightly rhythmic, gently widen the pre-chorus, then open into a warm, easy, memorable singalong chorus with layered harmonies and subtle ad-libs tucked behind the lead. Polished spacious but controlled mix, clear intimate lead vocal.
```

- Exclude 전문:

```text
deep baritone, heavy rasp, forceful belting, excessive vocal runs
```

| 설정 | 사용자 보고 |
| --- | --- |
| Duration | `autio` (원문 그대로 기록; Auto의 오기로 추정되나 직접 확인하지 않음) |
| Max Mode | On |
| Weirdness | 0% |
| Style Influence | 85% |
| Variety | 0% |
| Personalize | Off |
| 이번 생성 모델 | 별도로 명확히 제공되지 않음 |
| Pack Light의 Persona 사용 | 선택하지 않았다고 후속 답변 |
| Pack Light 원곡 모델 | v6라고 후속 답변 |

## 사용자 평가

- 이번 결과에서 저스틴 비버와 비슷한 목소리가 나오지 않았다고 보고했다. 음색 유사성 목표 미달로 기록한다. 곡 전체 품질·가사 전달력·반주 품질의 실패로 확대하지 않는다.
- Pack Light가 가장 가까운 음색이라는 기존 사용자 평가를 유지한다. 이 두 곡을 AI가 직접 청취·비교한 것은 아니다.

## 공식 기능 확인 — 2026-11-02

- https://help.suno.com/en/articles/6141377 : Weirdness는 Safe~Chaos, Style Influence는 스타일 입력을 따르는 강도다. 특정인의 음색 유사도 수치라고 안내하지 않는다.
- https://help.suno.com/en/articles/13924481 : Variety는 스타일 프롬프트를 조정·갱신하여 다양성을 부여하며 0으로 낮추면 스타일 태그 통제를 유지하는 설명. Max Mode는 더 많은 처리를 사용하며 보컬·스타일 일관성 등에 도움을 주는 것으로 설명하지만 특정 가수의 음색 선택을 보장하지 않는다.
- https://suno.com/products/personas : 곡의 보컬·스타일·분위기를 함께 재사용하는 Persona 설명. 보컬만 분리해 완전히 고정한다는 뜻으로 읽지 않는다.
- https://help.suno.com/en/articles/11362433 : 2026-03-26 문서는 Voices 안에 Style Personas가 있다고 안내한다. 같은 문서의 v5.5 전용 설명은 더 최신 2026-09-09 v6 FAQ의 구모델 은퇴 설명과 시점 차이가 있으므로 v5.5 선택을 해결책으로 권하지 않는다. 계정의 실제 UI와 Persona 가용 여부는 미확인이다.

## 정정과 다음 조치

- AI가 추가했던 light/warm/breathy, 본성 중심·짧은 가성 문구가 저스틴 비버 유사도를 높인다는 실증 근거는 없었다. 광범위한 보컬 묘사이며 해당 결과의 유일한 실패 원인이라고도 단정하지 않는다.
- Weirdness 0%, Style Influence 85%, Variety 0%, Max On 중 특정 값을 실패 원인이나 음색 재현 설정으로 단정하지 않는다. 임의의 새 권장 수치는 제시하지 않는다.
- 다음 권고는 Pack Light의 실제 보컬을 출발점으로 삼는 Style Persona를 만드는 것과, 영어 번안 가사에 해당 Persona를 선택하는 것이다. 모델은 확인된 Pack Light의 v6를 출발점으로 삼는다. 프롬프트·슬라이더를 동시에 새 값으로 바꾸는 제안은 하지 않는다.
- Persona를 통한 Pack Light 음색 유지와 저스틴 비버 유사도 추가 개선은 서로 다른 목표다. 전자가 성공하거나 후자가 개선됐다는 검증은 아직 없다. 실제 계정에서 선택·적용·생성은 하지 않았다.
