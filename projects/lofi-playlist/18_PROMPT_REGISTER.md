# Suno 프롬프트 누적 기록

문서 버전 1.5 / 묶음 0.19.1 / 작성 2026-10-27T22:32:05+09:00
대상: suno_lofi_research / 현재 lo-fi 의뢰 INTAKE-LOFI-0001.
기록 책임: AI. 프롬프트 전문과 버전의 누적 정본은 이 문서다. 현재 1번 입력용 문서는17_TRACK01_INPUT.md이며, 변경 시 같은 버전의 전문이 일치해야 한다.
음악 기준 정본은02_PRODUCTION_STANDARD.md, 판정은06_SELECTION_CRITERIA.md, 입력 직전 절차 정본은15_REPEATABLE_PRODUCTION_WORKFLOW.md §12다. 설계·실제 생성·청취·채택 이력은04_PRODUCTION_HISTORY.md와 연결한다.


## 최신 심플 시험안 — PRM-000027

2026-10-28 / 심플 한 칸 통합 입력, 네거티브 포함1674자. 미제출 초안. 등록된25개와 대조했으며 미회수 과거20개의 전체 중복 여부는 판정하지 않는다. 기존 공통 분위기/제외조건은 유지하고, 도입·본문 성부관계·타악 재질/패턴을 다르게 설계했다. 후단 PRM-000027 전문 참조.

## 최신 초안 — PRM-000023~000026 / FB-000002

기존21개 전문을 보존하고 후단에 수정 초안4개를 추가했다. 전체26개 완결 버전(기존25+심플1), 부분표현1건, 미회수20개는 그대로다. 새4개는 미제출 초안이며 현재20곡/40후보와 합산하지 않는다. 기존 문안도 새 사용 전 도입/드럼 반복을 다시 검토한다. 상세20.

## 현재 사용 규칙 — 2026-10-28 / R23

현재피아노·건반주역을유지한다.기타주역문안은사용중지,다른비건반주역안은재검토한다.피아노종류/건반음색·발음/질감/감쇠로차별화한다.상세정본은02의R23.
아래전문은생성당시버전의보존본이며새사용허가목록이아니다.기타전체/보조기타금지로확대하지않는다.특정A/B음원을사용자가모두탈락시켰다는의미도아니다.

| 현재 분류 | 곡 번호 | 적용 |
|---|---|---|
| 기타 주역 문안 사용 중지 | 02,06,11,14,18,20 | 현재새생성에재사용하지않음 |
| 건반 주역으로 재검토 | 03,05,08,09,12,15,17 | 주역계열/역할을현재조건에맞게검토 |
| 건반 주역 설계 | 01,04,07,10,13,16,19 | 악기군조건만충족;음색/전체음악채택은별도피드백 |

## 1. 현재 기록 범위

| 구분 | 수량/상태 | 처리 |
|---|---|---|
| 전문을 확보한 입력 | 21개 버전: 회수 원본과현재20곡통합문안 | 아래 Style와 Exclude를 그대로 보존 |
| 과거 수정 단서 | 1건: Exclude 두 표현의 변경 | 완성본으로 재구성하거나 새 곡으로 세지 않음 |
| 이전 대화의 20개 시안 | 04에 존재만 언급됨; 전문 미회수 | 이번 기록의 전문21개와 별개. 전체 이력과 비중복이라고 판정하지 않음 |
| 현재 20곡 설계 | 16/first_batch_designs.json의20개 | 현재1~20번통합문안작성. 실제생성/입력결과는19/상태원장으로분리 |
| 실제 생성/오디오 식별 | 1번 제목/표시Style와일치하는결과2개를현재화면에서관찰;생성요청원문/비용/실행자는미확인 | 사용자 청취 의견은 보존하되 특정 입력의 출력이라고 추정하지 않음 |

조회:09 원본,13 시험 계획,14 접수 양식,16 설계,17 입력,04/상태의 버전/실행 기록.13의 비교 계획·14의 접수 양식과 가상 예시는 실제 작성한 완결 프롬프트가 아니다.
이전 20개 전문 회수를 추가 조회했으나 이번 대화에서는 이전 대화 검색을 이용할 수 없었다. 미확보 전문을 추측하여 채우지 않았다.
PRM-000001~000003은 기존 문안을 소급 등록한 것이다. 당시 입력 직전에02를 읽고 이 기록과 대조했다는 증거를 새로 만든 것이 아니다.

## 2. 유지할 목표와 변화시킬 요소

현재 사용자 재확인: 같은 장르·분위기의 서로 다른 곡으로 플레이리스트를 구성한다. 따뜻하고 먹먹하고 어두우며 차분한 배경 음악이라는 공통 방향과 기존 명시 금지는 유지한다.
도입, 선율, 코드 진행/화성 리듬, 악기 구성과 음색, 드럼 재료/패턴, 베이스, 곡별 템포/그루브, 전개/마무리는 그 범위에서 바꿀 수 있다.
멜로디/코드가 좋다는 평가는 이후 곡에 같은 선율/진행을 고정하라는 지시가 아니다. 건반/드럼 음색만 바꾸라는 제한도 아니다. 모든 축을 매번 강제로 바꿀 필요는 없다.
EDM과120~140 BPM은 사용자의 설명용 예시이며 이 lo-fi 프로젝트의 BPM 조건으로 채택하지 않는다. 상세 기준은02/06을 적용한다.

## 3. 전체 인덱스

| 기록 ID | 성격/계보 | 문안 버전 | 전문 | 입력/사용 상태 | 비교상 유의점 |
|---|---|---|---|---|---|
| PRM-000001 | 회수 기준 원본 / BASELINE-RECOVERED | recovered-1 | Style322자 / Exclude308자 | 이전 사용자 발언 회수; 원 화면/출력 연결 미확인 | 당시 조건 보존용; 현재 모든 곡의 고정 템플릿이 아님 |
| PRM-000002 | TRK-000001 / PKG-000001 | 1.0 | Style917자 / Exclude308자 | 실제 폼 초안 입력 관찰; 비용/생성COMMIT 대기 | 다음 입력 전에 새 절차로 재검토 필요 |
| PRM-000003 | 과거 Exclude 수정 단서 / 기준 원본 관련 | 버전 미상 | 부분 표현만 확보 | 채택·입력 여부 미확인 | 완결본/현재 적용본으로 쓰지 않음 |
| PRM-000004 | TRK-000002 / PKG-000002 | 1.0 | Style943자 / Exclude355자 | 문안완료; 실제 입력상태/검토는04·상태의사용기록참조 | 1번·11번/기존표시이력과비교 |
| PRM-000005 | TRK-000003 / PKG-000003 | 1.0 | Style821자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000012와본문구별 |
| PRM-000006 | TRK-000004 / PKG-000004 | 1.0 | Style781자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000010와본문구별 |
| PRM-000007 | TRK-000005 / PKG-000005 | 1.0 | Style769자 / Exclude355자 | 묶음검토/생성원장은19 | TRK-000017와본문구별 |
| PRM-000008 | TRK-000006 / PKG-000006 | 1.0 | Style756자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000018와본문구별 |
| PRM-000009 | TRK-000007 / PKG-000007 | 1.0 | Style733자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000013와본문구별 |
| PRM-000010 | TRK-000008 / PKG-000008 | 1.0 | Style786자 / Exclude355자 | 묶음검토/생성원장은19 | TRK-000003와본문구별 |
| PRM-000011 | TRK-000009 / PKG-000009 | 1.0 | Style795자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000005와본문구별 |
| PRM-000012 | TRK-000010 / PKG-000010 | 1.0 | Style767자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000004와본문구별 |
| PRM-000013 | TRK-000011 / PKG-000011 | 1.0 | Style783자 / Exclude355자 | 묶음검토/생성원장은19 | TRK-000002와본문구별 |
| PRM-000014 | TRK-000012 / PKG-000012 | 1.0 | Style783자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000003와본문구별 |
| PRM-000015 | TRK-000013 / PKG-000013 | 1.0 | Style763자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000007와본문구별 |
| PRM-000016 | TRK-000014 / PKG-000014 | 1.0 | Style774자 / Exclude355자 | 묶음검토/생성원장은19 | TRK-000011와본문구별 |
| PRM-000017 | TRK-000015 / PKG-000015 | 1.0 | Style793자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000006와본문구별 |
| PRM-000018 | TRK-000016 / PKG-000016 | 1.0 | Style792자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000010와본문구별 |
| PRM-000019 | TRK-000017 / PKG-000017 | 1.0 | Style776자 / Exclude355자 | 묶음검토/생성원장은19 | TRK-000005와본문구별 |
| PRM-000020 | TRK-000018 / PKG-000018 | 1.0 | Style778자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000006와본문구별 |
| PRM-000021 | TRK-000019 / PKG-000019 | 1.0 | Style791자 / Exclude308자 | 묶음검토/생성원장은19 | TRK-000001와본문구별 |
| PRM-000022 | TRK-000020 / PKG-000020 | 1.0 | Style861자 / Exclude355자 | 묶음검토/생성원장은19 | TRK-000011와본문구별 |
| GAP-LEGACY-20 | 이전 대화의20개 미검증 시안 | 미상 | 미회수 | 04의 과거 언급만 확인 | 내용 비교 미완료; 복원하지 않음 |

## 4. PRM-000001 — 회수 기준 원본

출처:09_ORIGINAL_ANALYSIS.md §1 / SRC-0008. 관련 사용자 발언 시각은2026-10-26 21:55:06(Asia/Seoul)로 회수되었으나 문안 최초 작성 시각은 미확인.
음악 지문은 지시 내용의 요약이며 실제 음원 분석이 아니다.

| 비교 축 | 입력에 적힌 내용 |
|---|---|
| 분위기 | 느리고 먹먹하고 어둡고 따뜻한 연주곡, underwater 이미지 |
| 도입 | 첫 소리/진입 순서 미지정 |
| 건반/주역 음색 | warm Rhodes; 구체 어택/벨 성분/잔향 미지정 |
| 드럼 음색·역할 | soft brushed drums, far in the background |
| 리듬·저음 | 65 BPM, half-time; 전면 업라이트+부드러운sub |
| 화성·선율 | F major, major7; 짧은 반복 구절, 실제 진행/음표 미지정 |
| 본문·끝 | steady hypnotic loop, minimal melody; 구체 전개/끝 미지정 |
| 충돌/미정 | brushed drums와snare전체제외, 저음중첩 가능성은09에 보존 |

### Style 전문
```text
slow lo-fi hip hop, 65 BPM, half-time groove, warm round upright bass forward in the mix, deep soft sub bass, warm Rhodes piano playing a short repeating phrase, soft brushed drums far in the background, F major, major 7th chords, steady hypnotic loop, minimal melody, muffled dark warm tone, underwater feel, instrumental
```

### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

Lyrics·구조 입력, 모델/모드/옵션/참조:미확보. 없는 필드는 빈칸을 실제로 사용했다고 바꾸지 않는다.
전문 SHA-256: Style 07194888e5ba4ae4818f431e6d462c3550d784e1b0433fc10d75c30c982479f2 / Exclude 872fdacf449b9172d6dc94414b7536213a3175a8d82b6859267c724b070b81cc.

## 5. PRM-000002 — 1번 통합 문안

출처:17_TRACK01_INPUT.md / state.track01_input / TRK-000001 설계1.0 / 문안1.0.
작성일2026-10-27; 소급 등록일은 위 기록 작성 시각. 관련 문안인 PRM-000001과 동일 곡 계보인지 확인되지 않아 supersedes로 단정하지 않는다.

| 비교 축 | 입력에 적힌 내용 |
|---|---|
| 분위기 | dark/muffled/warm, 둥근 발음, 낮고 일정한 에너지 |
| 도입 | Rhodes 하행3음 질문을 첫 박/첫 구절에 제시 |
| 건반/주역 음색 | softly played Rhodes, rounded attacks, restrained bell tone, 짧고 통제된 꼬리 |
| 드럼 음색·역할 | sparse soft low percussion, far behind; 구체 재질 대비는 미지정 |
| 리듬·저음 | 64 BPM, 4/4, 직선 하프타임; 단독 업라이트가 빈마디 뒤쪽에 짧게 답함 |
| 화성·선율 | F major; Fmaj7 4마디→Dm7 4마디; 하행3음→한마디쉼→낮은2음 |
| 본문·끝 | 질문/쉼/저음답 지속, 격주기 마지막답 생략; Rhodes 먼저종료/짧은베이스꼬리 |
| PRM-000001과 공통 | Rhodes, 느린하프타임, F장조/7화음색채, 조용한뒤타악, 공통청감, Exclude전문 |
| PRM-000001과 차이 | 구체 진행/음형/쉼/응답/생략/끝; sub없이 단독저음. 원본 세부 미지정으로 실제 동일성은 판단불가 |
| 남은 유사 위험 | Rhodes 계열과 일반적인soft low percussion의 반복. 음색 차이가 충분하다고 확정하지 않음 |
| 현재20곡 설계 비교 | 가장 유사한19번: 긴첫음+짧은두음/다음화음전베이스 vs1번하행질문/빈마디늦은답.19번 프롬프트 전문은 아직 없음 |

### Style 전문
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4, straight half-time feel, steady low energy. Small ensemble: softly played Rhodes with rounded attacks and restrained bell tone, warm round upright bass as the sole low-end voice, sparse soft low percussion far behind the music. Dark, muffled, warm tone with distinct notes and short controlled tails. F major; an eight-bar cycle of Fmaj7 for four bars, then Dm7 for four bars. Rhodes: a short three-note descending question on the downbeat, one full bar without keyboard, then a lower two-note answer. Leave real gaps between phrases. Upright bass answers briefly late in the empty bars; keep its notes separate from Rhodes attacks. Establish this relationship immediately and retain it throughout the main body. Every second cycle, omit the final Rhodes answer while the quiet pulse continues. Finish the Rhodes phrase first, then a short bass-root tail. About three minutes.
```

### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

Lyrics:빈칸. 별도 구조 입력 없음; 구조 의도는Style에 포함. 연주곡은 빈 가사 안내와instrumental지시로 준비했으며 별도Instrumental토글을 조작하지 않았다.
실제 관찰 설정(SRC-0089):Advanced/v6-mini, 기이함50, 스타일영향50, 다양성0, Max끔, 길이Auto, 개인화끔, 오디오/보이스/영감참조 미첨부. 이번 기록 작업에서는 변경하지 않았다.
Style1000/Exclude1000/Lyrics5000은 이 계정의 관찰 한도. 입력된 전문은917/308자로 확인되었다. 이번 문안의 목표 약3분과 실제Length Auto를 구분한다.
과거 상태:UI_DRAFT_READY_COST_PENDING. 이번 기록으로 실제 생성/비용/채택 상태를 승격하지 않는다.
입력 전 검토 상태:REVIEW_REQUIRED_BEFORE_NEXT_INPUT. 지금 등록했다고 과거 입력 절차를 통과한 것으로 소급하지 않는다.
전문 SHA-256: Style 2e5541e492c80aa435c870587a52e5c4e41ace74a279721ff6c65a24a4458bbf / Exclude 872fdacf449b9172d6dc94414b7536213a3175a8d82b6859267c724b070b81cc.

## 6. PRM-000003 — 과거 수정 단서

09에 보존된 표현은 snare → loud snare, boom bap → aggressive boom bap이다.
Style/Exclude 수정 전문, 버전/작성시각, 모델/설정, 실제 입력/출력/채택 여부는 미확인이다. 두 표현을 PRM-000001의 원문에 치환해 과거 완성본을 만들어 넣지 않는다.
신규 입력에 자동 적용하지 않으며 원본 전체 Exclude는 보존한다.

## 7. 사용자 청취 의견 — 입력/출력 연결 미확정

이번 대화에서 사용자는 음악이 나쁘지 않고 괜찮으며 건반 선율/코드진행은 좋지만, 비슷한 시작과 건반/드럼 음색의 반복을 지적했다.
최종 의도는 분위기 유지와 곡 전체의 다양한 구성이다. 특정 선율/코드 고정이나 음색 두 항목만의 수정으로 좁히지 않는다.
어느 음원/요청 ID에 해당하는지는 아직 연결되지 않았다. 이 의견을 삭제하거나 특정 PRM/생성 시도의 직접 평가라고 지정하지 않는다.

## 8. 이후 누적 기록 양식

새 문안 또는 수정본을 작성할 때 아래 항목을 이 문서에 추가한다. 이전 버전을 덮어쓰지 않는다.

- 기록 ID, 작성 시각, 곡/플레이리스트/패키지 ID, 문안 버전, 같은 곡의 이전 버전과 수정 이유.
- Style/Exclude 전문, Lyrics/구조 전문 또는 빈칸/미사용/미확보의 구분, 모델/모드/옵션/참조와 입력 한도.
- 도입, 건반·주역 음색/발음, 드럼 재질·타격/잔향, 편성·역할, 선율/쉼, 화성 진행/지속, BPM/그루브·베이스, 본문·마무리.
- 비교한 PRM/설계 ID·버전과 범위, 가장 유사한 후보와 공통점/도입 차이/본문에 남는 차이/음색 차이, 명시 충돌·남은 공백.
- 입력 전검토 ID/판정은 state.prompt_input_policy의 receipt와 연결. 입력된 전문/변경·생성/출력/사용자 평가가 생기면04에 연결.

같은 문안의 재입력/버튼 재시도는 새 곡이나 새 프롬프트 버전으로 늘리지 않고 사용 이력으로 추가한다. 같은 곡의 수정은 같은 곡 ID에서 새 문안 버전으로 보존한다.
문자열 동일/비동일은 중복 탐색의 보조 신호다. 동의어·키/템포만의 변경으로 구별 판정을 대신하지 않는다.
실제 소리가 비슷하다는 의견이 생기면 해당 출력 연결과 입력 설계를 재검토하며, 프롬프트 차이만으로 오디오 비중복을 보장하지 않는다.

## 9. PRM-000004 — 2번 통합 문안

작성 2026-10-27T23:21:04+09:00. TRK-000002 설계1.0 / PKG-000002 문안1.0. 새 곡의 입력이며 PRM-000002를 덮어쓰거나 원본09를 바꾸지 않는다.
Style943/1000자, Exclude355/1000자. 가사빈칸. Title:02_띄엄띄엄 벌어진 기타.
모델/모드:v6-mini/Advanced. 기이함50·스타일영향50·다양성0·Max끔·길이Auto·개인화끔은 현재폼 관찰값을 유지한다. 오디오/보이스/영감첨부없음. 별도Instrumental토글조작없음.
아래는 입력용 완결 전문이다. 실제입력/문자열일치/후속사용시각은04 및 state.track02_input의 사용기록에 연결한다.

### Style 전문
```text
Instrumental lo-fi hip hop, 66 BPM, 4/4, light swing, steady low energy. Dark, muffled, warm mix. Nylon-string guitar leads: soft finger-pad plucks, rounded woody tone, gently damped notes. Upright bass is the only bass voice. Dry, muted frame-drum taps sit far behind, with short skin resonance and soft attacks. F major: F6 for 3 bars, Bbmaj7 for 3, C6 for 2. Open with two separated guitar chord tones, low then high, over a quiet bass root. Continue low-high-middle chord tones within a compact middle register with real silence between them, at most three guitar notes per bar; leave the next bar's first beat empty. Bass plays briefly only at chord changes, leaving guitar gaps unfilled. Keep this dispersed chord pattern through the main body, not a continuous arpeggio or question-and-answer riff. Later omit the middle guitar tone on alternate cycles. End on one low guitar chord tone and a damped bass note. No keyboards. About 2:55.
```

### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```

### 2번의 음악 특징과 비교

| 비교 축 | 2번의 지시/비교 결과 |
|---|---|
| 공통 분위기 | 따뜻하고먹먹하고어두운연주곡·낮은에너지·조용한뒤타악·단독둥근저음;밝은공격/소음으로차이를만들지않음 |
| 첫 사건 | 기타의낮은음→떨어진높은음,조용한베이스근음과시작.1번첫박하행3음질문과구분 |
| 주역 음색 | 나일론/손가락살탄현·둥근나무질감·짧은제음·좁은중간음역.1번Rhodes벨성분/건반반복과구분 |
| 타악 음색 | 마른제음프레임드럼·짧은가죽울림·부드러운발음·뒤배치.1번의일반적인soft low percussion보다재료/꼬리를구체화;실제차이는후속확인 |
| 그루브 | 66 BPM/4분의4/가벼운스윙.1번64/직선하프타임과박내움직임을구분 |
| 화성 | F6 3마디→Bbmaj7 3마디→C6 2마디.1번Fmaj7 4→Dm7 4와진행/지속구분 |
| 본문 | 낮음-높음-중간의화음음을쉼으로분산;한마디최대3음/다음첫박비움.1번하행질문/빈마디/낮은답을복제하지않음 |
| 베이스 | 화음변경지점만짧게지지,기타빈곳을채우지않음.1번빈마디뒤쪽의저음응답과구분 |
| 작은 전개/끝 | 후반격회차중간음생략;낮은기타화음음하나/제음베이스로종료 |
| 가장 유사한 설계11번 | 같은기타군이나11은동시긴두음+저음D-C-Bb-C.2번은시간적으로분리한화음음+변경시점근음 |
| 기타 관련 설계 | 6번완성질문후Rhodes화음답,14번제음화음점/저음답,18번미완성선율felt인계,20번동시두음상성부하행과각각구분 |
| 충돌 대조 | 원본Exclude28항목전문/순서유지.이번무건반설계에piano/electric piano/Rhodes/keyboard leads만추가.스네어/밝은하이햇/강한킥지시없음 |
| 범위/공백 | 현재20설계전체와확보전문2개/과거수정단서·현재보이는과거표시이력을비교.과거20전문전체/오디오비교아님 |
| 판정 범위 | 문안/설계구별의현재범위검토.음색만교체한복제로보지않으며실제오디오반영/유사도는미판정 |

근거 재확인:SRC-0054 Yamaha L8~10(나일론현의부드러운음색),SRC-0090 Remo L9/16/37(프레임드럼의따뜻함/낮은기본음).손가락살/제음/낮은타격과기타·드럼조합은AI편곡제안이며Suno성공률/특정제품재현의근거가아니다.
SRC-0067 스윙자료는이번재접근403이므로이번에본문을새로확인한것으로세지않고기존12/16의설계용범위로재사용했다.
Style SHA-256:28d00dd154e7f1886c0ea40a83011fd14f4ec57b6c3a7240c020fc09ea4d3cbc
Exclude SHA-256:baf6bf017017a248f98e0dac3177f317f7e183e63001f3519d3d6ee8e109b5da

## 10. 현재 화면의 기존 결과 관찰 — SRC-0091

- 1번과제목/표시Style가일치하는결과2개: https://suno.com/song/392e7b57-5437-496f-bda2-3f74773f2710 (표시3:04), https://suno.com/song/c6fa5e4a-f9cb-4d65-8ef9-f87672910cb6 (표시2:50). 생성동작을AI가수행한것/요청횟수·사용크레딧/사용자채택으로추정하지않는다.
- 비교에참고한과거표시예: E장조felt의낮은두음후3도위단음, G장조muted grand의같은음두번후한음아래응답, F장조Rhodes의베이스선행/상행3도. 모두화면에표시된설명이며정확한입력원문전문·설정·오디오를회수한것이아니다.
- 위표시정보는소급승인/실제청취결과/기존20개전문완전회수가아니다.나일론분산음/스윙/짧은손북재료/저음비응답이라는이번차이를검토하는보조로사용했다.

## 11. PRM-000005 — 03 길게 머문 뒤 짧게 대답
작성 2026-10-27T23:44:20+09:00. TRK-000003 / PKG-000003 / 설계1.0·문안1.0.
Style821/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:낮은 박/짧은 felt 화음과 클라리넷 긴 음을 첫 구절에 함께 드러냄. 본문:낮은 클라리넷 한 음을 길게 놓고 끝에서만 이웃음으로 짧게 귀환;긴 음-짧은 귀환-침묵을 유지; 중간 구절 하나는 클라리넷 응답 없이 화음만.
화성/박:62 BPM,D minor,Dm7 4마디,Gm7 2마디,Am7 2마디.
가장유사설계:TRK-000012 v1.0,03은 긴 음 하나의 머무름과 끝 귀환이다.12는 같은 선율 조각을 클라리넷과 felt가 나눠 완성. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 62 BPM, 4/4, straight sparse pulse, steady low energy. Dark, muffled, warm. Low clarinet with a smooth woody tone; dry felt-piano chords only occasionally in the middle register. Short round synth-bass roots, softly felt-struck low tom taps far behind. D minor: Dm7 4 bars, Gm7 2, Am7 2. Open with a long low clarinet note over a brief felt chord and quiet pulse. Let the held note make a tiny neighbor-note return only at its end, then leave a real melodic silence. Keep this long-note, short-return, silence relationship throughout. Let each tail clear before the next phrase; no busy clarinet solo. Bass supports roots briefly, separate from clarinet. In one middle phrase omit the clarinet return, leaving only sparse harmony. Clarinet finishes first; leave a short chord tail. About 3:05.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 12. PRM-000006 — 04 한 음의 끊어진 리듬
작성 2026-10-27T23:44:20+09:00. TRK-000004 / PKG-000004 / 설계1.0·문안1.0.
Style781/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:첫 단음과 짧은 빈자리 자체를 도입으로 사용. 본문:Rhodes 같은 음의 길고 짧은 두 타격이 쉼을 사이에 두고 되돌아옴;같은 음의 길이/쉼이 본문 중심; 후반 한 회차는 두 번째 타격을 생략.
화성/박:65 BPM,F major,F6 6마디,Gm7 2마디.
가장유사설계:TRK-000010 v1.0,04는 같은 음의 두 번 타격과 6+2 화음 지속이다.10은 두 음을 번갈아 구절 끝에서만 제시. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 65 BPM, 4/4, sparse straight pulse, steady low energy. Dark, muffled, warm. Dry tine electric piano with rounded attacks, little bell tone, short tails; upright bass alone in the low end. A soft low kick and dull cloth-muted wooden taps sit far back. F major: F6 6 bars, Gm7 2. Start with one middle-register piano note and a deliberate gap. Repeat that same pitch as a long hit then a short weak-beat hit, followed by a full bar of piano silence. Occasional thin chords support this one-note rhythmic cell; no running melody. Keep the long-short-gap identity through the main body. Bass marks the larger pulse without copying the piano rhythm. In a late cycle omit the second piano hit. Finish with a short stable root, without a drum fill. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 13. PRM-000007 — 05 고정 저음 위의 느린 화성
작성 2026-10-27T23:44:20+09:00. TRK-000005 / PKG-000005 / 설계1.0·문안1.0.
Style769/1000,Exclude355/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:박/페달과 얇은 화성을 처음부터 함께 제시. 본문:저음 Bb는 고정하고 pad 위 화음의 중간 성부만 느리게 이동;페달은 유지하고 위 화음만 교대; 작은 변화는 내성 생략/복귀로 제한.
화성/박:61 BPM,Bb major,Bbmaj7/Bb 4마디,Ebmaj7/Bb 4마디.
가장유사설계:TRK-000017 v1.0,05는 저음이 움직이지 않고 위 화음만 변한다.17은 고정 화음 성격 위로 업라이트의 짧은 상행이 중심. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 61 BPM, 4/4, quiet steady low pulse. Dark, muffled, warm, low energy. A soft matte analog pad holds thin middle-register harmony, without a lead melody. Short rounded synth-bass Bb pulses form the only low-end voice; quiet damped hand-tom touches behind. Bb major: Bbmaj7/Bb 4 bars, Ebmaj7/Bb 4. Begin pulse, bass pedal and thin harmony together. Keep bass Bb fixed while inner chord voices move slowly above it. Leave room between pad renewals; keep its low frequencies clear of bass. Preserve this moving-harmony-over-fixed-bass relationship throughout, without a plucked ostinato. Occasionally leave an inner voice out and bring it back quietly. End the pad first, then one short Bb bass tail. No piano or electric-piano lead. About 2:50.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```

## 14. PRM-000008 — 06 기타 질문과 화음 대답
작성 2026-10-27T23:44:20+09:00. TRK-000006 / PKG-000006 / 설계1.0·문안1.0.
Style756/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:기타 질문 바로 뒤 첫 화음 응답으로 관계를 보여줌. 본문:기타 하행 3음 질문을 완성한 뒤 Rhodes가 선율이 아닌 얇은 화음으로 답함;질문과 화음 답의 역할은 본문 내내 고정; 중간에는 질문 끝 음만 생략.
화성/박:67 BPM,Bb major,Bbmaj7 2마디,Gm7 2마디,Cm7 2마디,F6 2마디.
가장유사설계:TRK-000018 v1.0,06은 기타가 질문을 완성하고 Rhodes가 화음으로 답한다.18은 기타가 끝내지 않은 선율의 마지막을 felt가 맡는다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 67 BPM, 4/4, gentle swing, steady low energy. Dark, muffled, warm. Softly thumb-plucked nylon guitar, a woolly Rhodes used only for thin chord answers, and rounded upright bass. Dry soft palm-drum taps remain far behind. Bb major: Bbmaj7, Gm7, Cm7, F6, two bars each. Guitar opens with a complete descending three-note question; after a gap Rhodes answers with a short chord, not another melody. Alternate guitar-question bars and chord-answer bars, with neither covering the other's space. Keep this relationship through the body. Bass roots are shorter than the Rhodes chords and separated from their attacks. In a middle cycle omit the last guitar note. Stop on a brief final Rhodes answer with a controlled tail. About 3:10.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 15. PRM-000009 — 07 위 음 아래에서 움직이는 내성
작성 2026-10-27T23:44:20+09:00. TRK-000007 / PKG-000007 / 설계1.0·문안1.0.
Style733/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:Bb가 포함된 얇은 화음과 낮은 박으로 바로 시작. 본문:felt의 위 공통음 Bb는 가끔만 재타격하고 내부 음 D↔Eb 이동을 드러냄;공통음-내성 교대가 본문 중심; 일부 회차는 위 음 재타격을 생략.
화성/박:63 BPM,G minor,Gm7 4마디,Ebmaj7 4마디.
가장유사설계:TRK-000013 v1.0,07의 중심은 화음 안쪽 성부의 이동이다.13은 별도의 상하 왕복 선율과 선율이 비는 박이 중심. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, sparse straight pulse, quiet even energy. Dark, muffled, warm. Felt upright piano has a soft hammer onset, thick matte middle tone and short room tail. Upright bass provides G and Eb roots; small dull low wooden taps sit behind. G minor: Gm7 4 bars, Ebmaj7 4. Open with a thin piano chord containing Bb over a low pulse. Let the upper common Bb stay understated while the inner voice moves D to Eb and back with the harmony. Space the chord attacks widely, with real rests; Bb must not become a high repeating hook. Keep the inner-voice movement as the main identity. Some cycles omit the upper-note reattack. Stop the inner movement and finish with a short G-minor-colored chord. About 2:55.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 16. PRM-000010 — 08 두 음의 올라가는 답
작성 2026-10-27T23:44:20+09:00. TRK-000008 / PKG-000008 / 설계1.0·문안1.0.
Style786/1000,Exclude355/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:박 위 기타 화음 뒤 짧은 상행 답을 곧 제시. 본문:클라리넷의 작은 상행 2음 뒤 기타가 짧은 내려놓는 화음으로 응답;상행 2음과 내려놓는 화음의 대비 유지; 중간은 클라리넷 없는 회차 포함.
화성/박:64 BPM,G minor,Gm7 3마디,Cm7 3마디,F6 2마디.
가장유사설계:TRK-000003 v1.0,08은 상행 두 음과 기타 화음 답이다.03은 긴 단음 머무름과 끝 귀환이며 felt가 드문 화성을 받친다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4, light swing, quiet low energy. Dark, muffled, warm. Rounded finger-plucked nylon chords and mellow low clarinet, upright bass as the only bass. Soft leather-like low drum taps, dry and far behind. G minor: Gm7 3 bars, Cm7 3, F6 2. Start with a short guitar chord over the pulse, then introduce a small rising two-note clarinet answer. In the body clarinet appears late in phrases, followed by a gently placed guitar chord and an empty next bar. Keep the two-note rise and chord-response contrast; avoid long clarinet solo lines. Bass supports the roots without following the melody. Include a middle cycle with no clarinet, keeping the groove quiet. End with damped guitar and a short bass note, clearing the wind tail. No keyboards. About 3:05.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```

## 17. PRM-000011 — 09 숨을 쉬는 화음과 한 음 답
작성 2026-10-27T23:44:20+09:00. TRK-000009 / PKG-000009 / 설계1.0·문안1.0.
Style795/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:가벼운 박/화음 뒤 첫 빈자리를 일찍 제시. 본문:pad 화음이 잔향을 정리하며 다시 나타나고 felt는 그 사이 한 음만 답함;화음의 등장-정리와 단음 답 관계 지속; 후반 일부 답을 생략.
화성/박:62 BPM,Bb major,Bbmaj7 2마디,Dm7 2마디,Ebmaj7 4마디.
가장유사설계:TRK-000005 v1.0,09는 화성층이 짧게 비고 felt가 답한다.05는 화성층과 페달을 유지한 채 위 화음만 교대. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 62 BPM, 4/4, straight soft pulse, steady low energy. Dark, muffled, warm. A restrained velvety pad carries middle harmony; distant dry felt piano gives rare single-note replies. Short rounded synth bass, quiet low felt-beater drum pulses behind. Bb major: Bbmaj7 2 bars, Dm7 2, Ebmaj7 4. Open with pulse and a thin pad chord, showing an early gap as the pad is damped. At the end of two-bar chord groups let the pad clear completely; a single piano note sometimes answers in that space. Leave other gaps empty. Preserve this chord-appearance, clearing, occasional-note relationship throughout. Bass sounds briefly at chord starts without long sub tails under pad releases. Later omit several piano answers. Finish piano first, then cut the pad tail short. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 18. PRM-000012 — 10 구절 끝의 두 음 교대
작성 2026-10-27T23:44:20+09:00. TRK-000010 / PKG-000010 / 설계1.0·문안1.0.
Style767/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:저음/조용한 박 뒤 첫 구절 후반의 두 음으로 정체성 제시. 본문:Rhodes 두 음을 번갈아 놓되 구절 머리는 비우고 끝에서만 나타남;끝머리 두 음의 교대와 앞머리 쉼을 유지; 후반 교대 순서만 반전.
화성/박:65 BPM,D minor,Dm7 2마디,C6 2마디,Bbmaj7 2마디,Am7 2마디.
가장유사설계:TRK-000004 v1.0,10은 서로 다른 두 음을 구절 끝에서 교대한다.04는 같은 음의 장단 두 타격을 구절 앞쪽에 쓴다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 65 BPM, 4/4, straight half-time pulse, quiet even energy. Dark, muffled, warm. Muted reed-like electric piano, rounded low-mid body and subdued attack; upright bass forward but controlled. Short soft low kick thuds and dry fingertip frame-drum touches far behind. D minor: Dm7, C6, Bbmaj7, Am7, two bars each. Begin with bass and quiet pulse, leaving the piano silent in the first bar. Only late in the second bar, alternate two different piano notes briefly, then leave the next phrase head empty again. Keep the late two-note alternation through the body, not a same-note long-short cell. Bass leads the root path independently of the piano rhythm. Reverse the two-note order in a later phrase. End briefly on the lower note. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 19. PRM-000013 — 11 긴 두 음과 내려가는 저음
작성 2026-10-27T23:44:20+09:00. TRK-000011 / PKG-000011 / 설계1.0·문안1.0.
Style783/1000,Exclude355/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:두 음 화성과 낮은 박을 동시에 조용히 제시. 본문:기타의 두 음을 동시에 길게 울리고 베이스의 D→C→Bb→C 경로를 따라 화음 갱신;긴 두 음-저음 하행의 관계 지속; 중간은 위 음 한 번만 생략.
화성/박:60 BPM,D minor,Dm7 2마디,C6 2마디,Bbmaj7 2마디,C6 2마디.
가장유사설계:TRK-000002 v1.0,11은 동시 두 음의 긴 울림과 하행 저음이다.02는 화음음을 낮음-높음-중간으로 시간 분리. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 60 BPM, 4/4, sparse straight pulse, low steady energy. Dark, muffled, warm. Soft nylon guitar plays two chord tones together with rounded thumb attacks and a warm sustained body; upright bass is shorter and drier. Damped low hand-drum strokes sit far behind. D minor: Dm7, C6, Bbmaj7, C6, two bars each. Open a gentle guitar dyad and low pulse together. Let each dyad ring quietly across the gap without additional picking; update harmony as bass follows D, C, Bb, C. Bass plays one short root at each chord change, not melodic answers. Keep the simultaneous long dyad and descending bass identity through the body. In a middle cycle omit the upper guitar tone once. Finish the final C6 dyad briefly and damp its tail. No keyboard instruments. About 3:05.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```

## 20. PRM-000014 — 12 선율 끝을 건네는 관악
작성 2026-10-27T23:44:20+09:00. TRK-000012 / PKG-000012 / 설계1.0·문안1.0.
Style783/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:클라리넷 조각 뒤 첫 felt 마지막 음으로 바로 전달 관계 제시. 본문:클라리넷이 하행 2음 조각을 내고 felt가 마지막 음 하나를 받아 완성;부분 선율 전달을 본문에 유지; 중간 일부 구절은 마지막 음 생략.
화성/박:63 BPM,F major,Fmaj7 3마디,Am7 1마디,Bbmaj7 3마디,C6 1마디.
가장유사설계:TRK-000003 v1.0,12는 분할한 선율을 두 악기가 완성한다.03은 긴 음 자체가 중심이고 felt는 선율 전달이 아닌 화성. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, quiet straight pulse, steady low energy. Dark, muffled, warm. Low clarinet has a soft rounded reed onset; a small dry felt-piano tone supplies only the final note and occasional thin chords. Short round synth bass and very quiet padded low drum taps behind. F major: Fmaj7 3 bars, Am7 1, Bbmaj7 3, C6 1. Open with a descending two-note clarinet fragment; across the bar boundary felt piano supplies the one last note that completes the phrase. Leave a real gap between the two players. Keep this divided three-note melody through the body, without overlapping or doubling it. Sparse roots stay clear of wind and piano attacks. Some middle phrases omit the final piano note entirely. Clarinet stops first; end on a short felt note. About 2:55.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 21. PRM-000015 — 13 작은 3도의 왕복
작성 2026-10-27T23:44:20+09:00. TRK-000013 / PKG-000013 / 설계1.0·문안1.0.
Style763/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:첫 왕복 음형을 완성한 뒤 의도한 빈 마디를 도입에서 제시. 본문:felt가 작은 3도 안에서 위아래로 돌아오고 마지막 반복 자리를 비움;왕복 후 비우는 구조 유지; 중간은 마지막 복귀 음을 늦추고 큰 에너지는 유지.
화성/박:64 BPM,F major,F6 4마디,Bbmaj7 2마디,C6 2마디.
가장유사설계:TRK-000007 v1.0,13은 독립적인 3도 왕복 선율이다.07은 위 공통음 아래 내성 이동이 중심이며 별도 왕복 훅이 없다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4, light swing, quiet even energy. Dark, muffled, warm. Soft felt grand piano with a muted rounded attack and small warm room, no bright upper ringing. Upright bass and soft dry low skin-drum taps behind. F major: F6 4 bars, Bbmaj7 2, C6 2. Start a small middle-register melody that goes up then back within a third, using a short-long shape, followed by a full empty bar. Keep this round trip and silence as the body's identity, not a continuous ostinato. Piano harmony stays thin; bass supports roots without striking together with low piano notes. In a middle phrase delay the final return note while the background pulse remains steady. End by leaving out one return and resting on a stable root-colored note. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 22. PRM-000016 — 14 기타 점과 베이스의 빈자리
작성 2026-10-27T23:44:20+09:00. TRK-000014 / PKG-000014 / 설계1.0·문안1.0.
Style774/1000,Exclude355/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:기타 한 점-짧은 쉼-저음 답을 첫 구절에 배치. 본문:짧게 제음한 기타 화음 점 사이에 합성 베이스가 길음-짧음으로 대답;화음 점/저음 답의 시간 분할 지속; 후반에는 두 번째 짧은 저음 답만 생략.
화성/박:66 BPM,Bb major,Bb6 2마디,Cm7 2마디,F6 4마디.
가장유사설계:TRK-000011 v1.0,14는 짧은 화음 점 사이 베이스가 리듬으로 답한다.11은 화음이 길게 남고 베이스는 화음 변경 때만 움직인다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 66 BPM, 4/4, sparse straight syncopation, low steady energy. Dark, muffled, warm. Palm-damped nylon guitar makes short woody chord dots; round soft synth bass gives the rhythmic answers. Quiet dull padded drum touches sit behind, without a second dominant bass pulse. Bb major: Bb6 2 bars, Cm7 2, F6 4. Open with one clipped guitar chord, a small silence, then a low bass answer. Place guitar dots near the front and back of a bar, bass in between as a long-short reply, never both foregrounded together. Keep the chord-dot and bass-answer division throughout. Leave actual empty spaces rather than filling them with guitar runs. Later omit the second short bass reply. Damp guitar first, finish the bass answer briefly. No keyboards. About 3:10.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```

## 23. PRM-000017 — 15 같은 기타 음 아래 달라지는 화음
작성 2026-10-27T23:44:20+09:00. TRK-000015 / PKG-000015 / 설계1.0·문안1.0.
Style793/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:Rhodes의 얇은 화성과 기타 E 한 음의 관계로 시작. 본문:기타의 중간 E 한 음은 간헐적으로 같게 두고 Rhodes 아래 화음이 바뀜;기타 공통음/화음 변화 관계 유지; 중간 한 회차는 기타 음 없이 화음만.
화성/박:62 BPM,C major,Cmaj7 2마디,Am7 2마디,Fmaj7 4마디.
가장유사설계:TRK-000006 v1.0,15는 같은 기타 음의 의미를 화음이 바꾼다.06은 기타 3음 질문에 Rhodes가 별도 화음으로 답한다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 62 BPM, 4/4, soft straight pulse, quiet steady energy. Dark, muffled, warm. Nylon guitar gives a rounded thumb-plucked middle E only occasionally; a dark softly sustained Rhodes supports thin changing harmony underneath. Upright bass roots, very quiet dry muted low tom taps behind. C major: Cmaj7 2 bars, Am7 2, Fmaj7 4. Open with a thin Rhodes chord and one guitar E. Keep that guitar pitch the same across the changing chords, sounding once after a chord change with long rests, not every beat. Let harmony give the common note its changing meaning through the body, without adding a guitar tune. Bass follows C, A, F, avoiding doubled low Rhodes roots. Leave the guitar absent for one middle cycle. Stop guitar first, then shorten the chord release. About 2:50.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 24. PRM-000018 — 16 네 음이 돌아오는 짧은 원
작성 2026-10-27T23:44:20+09:00. TRK-000016 / PKG-000016 / 설계1.0·문안1.0.
Style792/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:원형 음형 앞부분과 쉼을 첫 구절에 들여놓음. 본문:Rhodes가 작은 음역의 1→2→3→2 윤곽으로 돌고 귀환 직전 쉼;순환과 귀환 직전 쉼 유지; 중간은 마지막 한 음을 다른 화음음으로 대체하는 설계.
화성/박:65 BPM,C major,C6 3마디,Dm7 1마디,Fmaj7 2마디,G6 2마디.
가장유사설계:TRK-000010 v1.0,16은 두 마디에 펼친 네 음의 작은 순환이다.10은 구절 끝의 두 음 교대와 앞머리 쉼. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 65 BPM, 4/4, light swing, low even energy. Dark, muffled, warm. Gently muted Rhodes with a soft rubbery onset, rounded body, very little metallic bell and a short tail. Upright bass, dry low fingertip hand-drum taps far behind. C major: C6 3 bars, Dm7 1, Fmaj7 2, G6 2. Begin the front of a compact four-note piano contour, scale degrees 1-2-3-2, then leave a gap before its expected return. Scatter four events over two bars, retaining that return-point silence throughout the body. Keep the melody in a small middle register, with no fast runs. Bass briefly supports the first beat when piano is absent, not a sustained floor. In a middle cycle replace the last note with another chord tone. End on one stable chord tone before completing the circle. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 25. PRM-000019 — 17 움직이는 저음과 남아 있는 위 음
작성 2026-10-27T23:44:20+09:00. TRK-000017 / PKG-000017 / 설계1.0·문안1.0.
Style776/1000,Exclude355/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:pad/박 아래 첫 짧은 저음 이동을 초반 구절에 제시. 본문:pad의 위 공통음 E는 유지하고 업라이트가 짧은 상행 연결을 가끔 제시;위 음 유지와 경계 앞 상행 저음 관계 지속; 중간 한 경계는 이동 생략.
화성/박:61 BPM,A minor,Am7 4마디,Fmaj7 4마디.
가장유사설계:TRK-000005 v1.0,17은 저음이 화음 경계 앞에서 상행한다.05는 저음 페달이 고정되고 위 화음만 변한다. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 61 BPM, 4/4, sparse straight pulse, steady low energy. Dark, muffled, warm. Thin matte pad harmony with a subdued common E above; plucked upright bass supplies the main movement. Small damped low kick thumps stay behind, leaving space after bass motion. A minor: Am7 4 bars, Fmaj7 4. Start pad and pulse together, introducing one short bass movement early in the phrase. Near the end of an Am7 span bass moves A-C-E; near the end of Fmaj7 it moves F-A-C, each note short. Keep upper E still while bass occasionally climbs before the chord boundary. Do not turn this into walking bass or fill every bar. Omit the movement at one middle boundary. After the last ascent, damp bass root and pad in sequence. No piano or electric-piano lead. About 3:05.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```

## 26. PRM-000020 — 18 끝내지 않은 기타 선율
작성 2026-10-27T23:44:20+09:00. TRK-000018 / PKG-000018 / 설계1.0·문안1.0.
Style778/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:첫 기타 미완결 음형 뒤 felt 꼬리를 일찍 제시. 본문:기타 상행 3음→한 박 쉼→felt 하행 2음으로 미완결 선율을 이어 완성;선율 꼬리 인계 지속; 중간 회차만 felt 꼬리의 마지막 음 생략.
화성/박:64 BPM,A minor,Am7 2마디,Dm7 2마디,Fmaj7 2마디,Em7 2마디.
가장유사설계:TRK-000006 v1.0,18은 미완결된 기타 선율을 felt가 이어 완성한다.06의 Rhodes 답은 선율 꼬리가 아닌 화음. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4, gentle swing, quiet even energy. Dark, muffled, warm. Soft nylon guitar with short rounded plucks, and close dry felt piano with a muted middle-low tone. Upright bass, distant quiet low cloth-damped skin-drum taps. A minor: Am7, Dm7, Fmaj7, Em7, two bars each. Open with an unfinished rising three-note guitar phrase, one beat of silence, then let felt piano complete it with two descending notes. Keep handing the melody tail between instruments through the body; never double the same line together. Bass marks each chord root briefly, separate from low piano replies. In a middle cycle omit only the final piano-tail note. Keep the pulse steady and leave real rests. Guitar stops first; finish on the short low piano tail. About 2:55.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 27. PRM-000021 — 19 긴 한 음 뒤 두 번의 발걸음
작성 2026-10-27T23:44:20+09:00. TRK-000019 / PKG-000019 / 설계1.0·문안1.0.
Style791/1000,Exclude308/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:긴 첫 음과 낮은 박을 바로 제시하고 짧은 두 음 뒤 충분히 비움. 본문:felt 긴 한 음 뒤 내려가는 짧은 두 음, 다음 화음 직전에 베이스 한 번;긴 음-두 짧은 음-휴지/저음 예고의 관계 지속; 후반 한 회차는 픽업 생략.
화성/박:63 BPM,F major,Fmaj7 2마디,Gm7 2마디,C6 4마디.
가장유사설계:TRK-000001 v1.0,19는 긴 첫 음 뒤 짧은 두 음과 화음 직전 저음 예고다.01은 하행 질문 뒤 빈 마디에서 늦은 저음 답. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, straight half-time pulse, steady low energy. Dark, muffled, warm. Mellow felt piano with a rounded hammer onset and dry warm body, no shiny ring; upright bass gives rare soft pickups. Quiet deep padded drum touches stay far behind. F major: Fmaj7 2 bars, Gm7 2, C6 4. Open with one held middle piano note over the low pulse, followed by two shorter descending notes and a long rest. Keep this long-short-short phrase and silence through the body. Just before the next chord, bass quietly anticipates its root on a weak beat and damps it; do not accent that pickup with drums. This is not a three-short-note question with a late bass answer. Omit a pickup in a later cycle. Finish after the last long note, leaving out the two short notes. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 28. PRM-000022 — 20 낮게 내려놓는 두 음 화성
작성 2026-10-27T23:44:20+09:00. TRK-000020 / PKG-000020 / 설계1.0·문안1.0.
Style861/1000,Exclude355/1000. Lyrics빈칸. v6-mini/Advanced,50/50/0,Max끔/Auto/개인화끔,참조없음.
공통분위기:02/06 유지. 도입:작은 두 음 화성과 낮은 박을 동시에 시작. 본문:기타 두 음 화성의 위 음만 천천히 내려오고 pad는 공통음 F를 드물게 지지;위 음의 느린 하행과 공통음 지지 관계 지속; 후반에는 pad가 없는 회차 포함.
화성/박:60 BPM,F major,Fmaj7 4마디,Dm7 4마디.
가장유사설계:TRK-000011 v1.0,20은 위 음이 천천히 내려오는 기타 두 음과 pad 공통음 지지다.11은 저음 경로가 내려가고 기타 긴 화음은 그에 맞춰 갱신. 타악·주역의구체발음/꼬리는아래전문참조.
상태:문안/현재20곡구별검토,실제음원평가는사용자피드백대기. 전체과거이력/실제소리비중복보장아님.
### Style 전문
```text
Instrumental lo-fi hip hop, 60 BPM, 4/4, quiet straight low pulse, steady low energy. Dark, muffled, warm. Softly thumb-played nylon guitar gives simultaneous two-note chords with rounded attacks and gently damped tails. A thin velvety pad supports middle harmony occasionally; short round synth bass follows F then D. Dry softly muted frame-drum touches remain far behind. F major: Fmaj7 4 bars, Dm7 4. Begin a small guitar dyad and low pulse together. Keep the lower guitar tone settled while the upper chord tone descends slowly between dyads, leaving a damped silence between chords. Let pad quietly support a common F only sometimes, not constantly. Preserve the upper-voice descent through the body; include later cycles without pad. Close by reducing guitar from two tones to one, then clear bass and the short common-note tail. No keyboards. About 3:00.
```
### Exclude 전문
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, piano, electric piano, Rhodes, keyboard leads
```


## 도입·드럼 수정 초안 — 공통7번 화성 / 미제출

Gm7 4마디→Ebmaj7 4마디,63BPM, felt upright와 본문 내성 이동은 공통이다. 네 안은 시작/드럼 조합 선택용이며 한 변수 인과 실험이 아니다. 기존 오디오 편집 결과도 아니다.

### PRM-000023 — R07A_화음을 길게 놓고 비우기

계보 REV-TRK000007-A / 문안1.0 / PKG-REV07-A / DRAFT_NOT_SUBMITTED.

Style 875자
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, low even energy. Dark, muffled, warm. Felt upright piano remains the main voice, soft hammer onset, matte middle register, short room; upright bass alone below. G minor: Gm7 4 bars, Ebmaj7 4. Open with one simultaneous middle-register piano chord, a long hold, then a clear release; drums enter in bar 2. The opening is a chord, not a single-note run. Percussion: felt-beater bass drum with a soft rounded acoustic bloom on beats 1 and 3; a dark damped palm clap only late on beat 4 every other bar. Let the unclapped bar breathe. Quiet behind piano, with a smooth body rather than wooden clicks. In the body, piano keeps an understated common Bb while its inner voice moves D to Eb and back with the harmony; widely spaced chord attacks and real rests. Keep the upper note subdued. End with a short G-minor-colored chord. About 2:55.
```

Exclude 308자 — 기존28개 그대로
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

Lyrics: 빈칸. 고급/v6-mini, Weirdness50·Style Influence50·Variety0, Max Off·Length Auto·Personalization Off, 참조 없음. 기존 관찰값을 비교 조건으로 유지하며 최적값이라고 판정하지 않는다. 실제 입력 직전02/18 검토와 현재UI 대조가 필요하다.
SHA-256: Style 0c56a7659474b99d8e0814f2de61dede9fc12f62cdd8bca76adb3f5b773478ff / Exclude 872fdacf449b9172d6dc94414b7536213a3175a8d82b6859267c724b070b81cc.

### PRM-000024 — R07B_짧은 탐 리듬 뒤 두 음 화음

계보 REV-TRK000007-B / 문안1.0 / PKG-REV07-B / DRAFT_NOT_SUBMITTED.

Style 916자
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, low even energy. Dark, muffled, warm. Felt upright piano remains the main voice, soft hammer onset, matte middle register, short room; upright bass alone below. G minor: Gm7 4 bars, Ebmaj7 4. Open with a half-bar low-tom pickup alone. Piano enters on beat 3 as a simultaneous Bb-D dyad, gently held; its next event is an inner-note change, not a three-note lead-in. Percussion uses only two low mallet-struck toms, softly rounded pitched skin resonance. A two-bar phrase places the lower tone on beat 1, upper tone after beat 2, lower tone on beat 4; omit the next bar's first hit. Quiet, slightly resonant, with distinct low drum tones. In the body, piano keeps an understated common Bb while its inner voice moves D to Eb and back with the harmony; widely spaced chord attacks and real rests. Keep the upper note subdued. End with a short G-minor-colored chord. About 2:55.
```

Exclude 308자 — 기존28개 그대로
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

Lyrics: 빈칸. 고급/v6-mini, Weirdness50·Style Influence50·Variety0, Max Off·Length Auto·Personalization Off, 참조 없음. 기존 관찰값을 비교 조건으로 유지하며 최적값이라고 판정하지 않는다. 실제 입력 직전02/18 검토와 현재UI 대조가 필요하다.
SHA-256: Style a03dd165bc368f584fb0a5e2e8b7fb47cbe41a42590536c7d31b227c49045257 / Exclude 872fdacf449b9172d6dc94414b7536213a3175a8d82b6859267c724b070b81cc.

### PRM-000025 — R07C_베이스 뒤 천천히 쌓이는 화음

계보 REV-TRK000007-C / 문안1.0 / PKG-REV07-C / DRAFT_NOT_SUBMITTED.

Style 956자
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, low even energy. Dark, muffled, warm. Felt upright piano remains the main voice, soft hammer onset, matte middle register, short room; upright bass alone below. G minor: Gm7 4 bars, Ebmaj7 4. Open with one short upright-bass root and space; piano enters late in bar 1 with a held D, adding a quiet Bb above in bar 2. Let the harmony accumulate rather than play a pickup melody. Percussion enters in bar 2: a rounded electronic sine-bodied kick with a gentle onset and a dull synthetic rubber knock with a short tail. Kick on beat 1, knock after beat 3; alternate bars move the kick to after beat 2. Spacious two-bar rhythm, quiet but audibly electronic, not acoustic skin taps. In the body, piano keeps an understated common Bb while its inner voice moves D to Eb and back with the harmony; widely spaced chord attacks and real rests. Keep the upper note subdued. End with a short G-minor-colored chord. About 2:55.
```

Exclude 308자 — 기존28개 그대로
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

Lyrics: 빈칸. 고급/v6-mini, Weirdness50·Style Influence50·Variety0, Max Off·Length Auto·Personalization Off, 참조 없음. 기존 관찰값을 비교 조건으로 유지하며 최적값이라고 판정하지 않는다. 실제 입력 직전02/18 검토와 현재UI 대조가 필요하다.
SHA-256: Style 0462a2e4b08488300de891a9d4047409af9ab9df0686ca38b001b1e254e6cccd / Exclude 872fdacf449b9172d6dc94414b7536213a3175a8d82b6859267c724b070b81cc.

### PRM-000026 — R07D_진행 중인 화음 리듬으로 시작

계보 REV-TRK000007-D / 문안1.0 / PKG-REV07-D / DRAFT_NOT_SUBMITTED.

Style 1000자
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4, low even energy. Dark, muffled, warm. Felt upright piano remains the main voice, soft hammer onset, matte middle register, short room; upright bass alone below. G minor: Gm7 4 bars, Ebmaj7 4. Begin as if the piano accompaniment is already underway: a short middle-register chord just after beat 1, then a longer chord on beat 3. Start with chord rhythm, not an isolated single-note melody. Drums enter after this chord pair. Percussion: dark hand-drum center tones with a rounded resonant body, alternating with short damped palm strokes. Place a center tone on beat 2 and two quiet palm strokes after beat 4 in alternate bars; leave the intervening bar sparse. Gentle uneven spacing, steady tempo, no beat build or fill. In the body, piano keeps an understated common Bb while its inner voice moves D to Eb and back with the harmony; widely spaced chord attacks and real rests. Keep the upper note subdued. End with a short G-minor-colored chord. About 2:55.
```

Exclude 308자 — 기존28개 그대로
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

Lyrics: 빈칸. 고급/v6-mini, Weirdness50·Style Influence50·Variety0, Max Off·Length Auto·Personalization Off, 참조 없음. 기존 관찰값을 비교 조건으로 유지하며 최적값이라고 판정하지 않는다. 실제 입력 직전02/18 검토와 현재UI 대조가 필요하다.
SHA-256: Style b4e8e1b478919ceb99f1b7826773a94eff413c6e9396f5713c977b018a89de02 / Exclude 872fdacf449b9172d6dc94414b7536213a3175a8d82b6859267c724b070b81cc.


## PRM-000027 — 역재생 건반 화음과 도자기 타악 / 심플 통합본

작성 2026-10-28T08:55:49+09:00 / PKG-SIMPLE-0001 / 문안1.0 / DRAFT_NOT_SUBMITTED.
심플/v6-mini. 다음 블록 전체를 한 설명란에 붙여 넣는다. 네거티브 포함1674자(사용자 제시3000자 이내). 별도 가사 입력 없음, 오디오 스케치/참조 없음. 고급 슬라이더 값이나 고급 Exclude가 심플에 그대로 적용된다고 가정하지 않는다.

```text
Create an instrumental lo-fi hip hop track, 64 BPM, 4/4, about three minutes. Keep a dark, muffled, warm atmosphere, low steady energy, rounded bass and quiet percussion behind the music. A mellow electric piano is the main instrument: soft attacks, thick middle-register body, restrained metallic overtones and short room ambience.

Begin with one brief reversed electric-piano chord swell, then a small pocket of silence. Let the first normal piano chord land between the beats rather than introduce a three-note melody. Continue with short offbeat chord pairs alternating with held chords. Let the upper voice rise while a lower chord voice falls; keep the movement spacious and unhurried.

Harmony: Ebmaj9, Gm9, Fm9, Bb13, two bars each. Warm upright bass follows the roots with short notes. Use a small percussion kit of hollow clay-pot bass hits and muted ceramic fingertip taps, with rounded resonant bodies rather than brush swishes or wooden clicks. Make a sparse two-bar groove: one low hit near the first bar's start, a second low hit late in the next bar, and a few soft offbeat ceramic taps between them. Keep this drum identity through the body. Occasionally leave a piano chord pair unanswered; finish by damping the final chord.

Avoid these elements:
-vocals, -scat, -fast solo, -drum fills, -tempo changes, -key changes, -breakdown, -build up, -drop, -bright, -crisp hi-hats, -sparkly, -airy, -bright cymbals, -wide stereo, -long intro, -fast tempo, -loud drums, -punchy drums, -snare, -crisp snare, -boom bap, -trap, -hard hitting kick, -distorted drums, -white noise, -hiss, -clipping, -guitar lead, -three-note piano pickup, -metallic bell keyboard tone
```

비교: 26 uses an ongoing offbeat felt-piano accompaniment with a common Bb and skin handdrum; this uses reversed-EP opening, contrary chord voices, clay-shell percussion and different harmony. 도입의 역재생 부풀림은 짧게 요청해 기존 long intro 제외와 충돌하지 않도록 했다.31개 네거티브 중 기존28개는 유지하고 기타주역·세음도입·금속성벨발음3개를 추가했다. 모든 기타/모든 건반 금지로 확대하지 않는다.

표시 문법: Avoid these elements와 각 항목의 대시는 자연어 제외 지시와 목록 표시다. 심플의 전용 네거티브 파라미터로 인식됨이 검증된 사실은 아니다. 현재 심플 기본 화면/추가 메뉴에서 별도 Exclude는 관찰하지 못했다. Negative:를 쓴 커뮤니티 글의 제목 Simple Prompt를 Simple Mode 확증으로 읽지 않는다. SRC-0006/0009/0096/0097 참조.

타악 재질 근거SRC-0098은 점토 껍질/손바닥·손끝 연주에 관한 제조사 설명이다. 이 모델의 해당 소리 재현 성공을 증명하지 않는다. 개별 소리 적합성/중복 여부/드럼과 도입 변화는 출력 피드백으로 별도 판단한다.
전문SHA-256 86de52a0f4e7187047e65b788e086c733ef46c1688b063bd79ca8e3b49385da3.


## 2026-10-29 추가20곡 — 드럼10 / 퍼커션5 / 무타악5

최신 사용자 지시로 생성 허용. 도입 차별화 재시험을 반복하지 않고, 건반 음색·본문 화성/연주·타악 음색/패턴을 설계한다. v6-mini 고급, 가사 빈칸, Weirdness50 / Style Influence50 / Variety0, Max Off / Length Auto / Personalization Off. 실행·출력은 second_batch.json과22 문서에서 기록한다. 아래는 실행 전 등록본이다.

### PRM-000028 — 22_D01_천으로 덮은 밤

그룹 D / 문안1.0 / Style 670자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4. Dark, muffled, warm, steady low energy. Felt upright piano, dense matte midrange, very short dry decay is the main voice, with rounded bass. Harmony: Ebmaj7 3 bars, Fm9 1, Abmaj7 2, Bb6 2. A compact melody descends a fourth then answers with a held inner third; chord stabs leave the fourth beat empty. An acoustic felt-beater kick with a soft broad body and towel-damped rack tom; kick on 1, low tom late on 3, omit tom every second bar. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000029 — 23_D02_고무빛 전류

그룹 D / 문안1.0 / Style 679자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 67 BPM, 4/4. Dark, muffled, warm, steady low energy. Tine electric piano, rubbery attack, almost no bell partials, close and dry is the main voice, with rounded bass. Harmony: Cm9 2 bars, Abmaj7 2, Fm7 2, Gm7 2. Short upper dyads alternate with a sustained lower chord tone across two bars; melody avoids outlining every chord root. An electronic round sine-body kick with a short low rubber tom; kick on 1 and after 2, tom quietly on 4 only in alternate bars. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000030 — 24_D03_느린 해머의 온기

그룹 D / 문안1.0 / Style 718자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 62 BPM, 4/4. Dark, muffled, warm, steady low energy. Una-corda grand piano, soft woolly hammer, rounded woody body and gentle medium release is the main voice, with rounded bass. Harmony: Bbmaj9 4 bars, Eb6 2, Cm7 1, Fsus2 1. Thin chord voicings move in parallel thirds before a single held resolving note, with a whole bar of melodic rest. A deep loose bass drum and low felt-mallet floor tom, soft resonant skin rather than clicks; one bass hit per bar, two separated tom answers across four bars. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000031 — 25_D04_갈색 리드의 틈

그룹 D / 문안1.0 / Style 715자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 66 BPM, 4/4. Dark, muffled, warm, steady low energy. Reed electric piano at soft velocity, dark hollow midrange, short rounded attack, no overdrive is the main voice, with rounded bass. Harmony: Dm9 2 bars, Gm9 2, Bbmaj7 3, A7sus4 1. A gently syncopated five-note phrase stretches across four bars; sustain the second note, shorten the last two. A dry padded bass drum and tiny low-passed closed hi-hat, no cymbal wash; bass hits on 1 and the last eighth of 3, hats only two weak eighths per bar. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000032 — 26_D05_둥근 펠트의 잔상

그룹 D / 문안1.0 / Style 702자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 65 BPM, 4/4. Dark, muffled, warm, steady low energy. Felt grand piano, velvety midrange with a longer dark decay and restrained pedal is the main voice, with rounded bass. Harmony: Fmaj9 2 bars, Am7 1, Dm9 3, Gm7 1, C6 1. Melody repeats a gentle downward second while inner harmony ascends; use broad spaced chord holds rather than a constant riff. A soft vintage low kick with a very brief papery muted tom; a three-bar sparse phrase shifts the tom answer one beat later each cycle. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000033 — 27_D06_닫힌 뚜껑의 화음

그룹 D / 문안1.0 / Style 692자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 61 BPM, 4/4. Dark, muffled, warm, steady low energy. Closed-lid upright piano, close woody and mellow, rounded attacks, almost no room tail is the main voice, with rounded bass. Harmony: Gm9 3 bars, Cm7 1, Ebmaj9 3, Dm7 1. Two low-middle chord inversions alternate with a short rising third; let bass enter in the piano rests. A small shallow bass drum with a soft woody body and a dark padded palm clap; bass on 1, clap faintly late on 4 every two bars, no backbeat snare. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000034 — 28_D07_전기 속 짧은 숨

그룹 D / 문안1.0 / Style 719자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 68 BPM, 4/4. Dark, muffled, warm, steady low energy. Suitcase tine piano, thick low-mid body, soft compressed attack, subtle slow tremolo and little metallic ring is the main voice, with rounded bass. Harmony: Abmaj7 2 bars, Bbm7 2, Dbmaj9 2, Eb6 2. Repeated two-note chord answers move down by step; a held inner note bridges every second chord change. A rounded electronic kick and two softly pitched analog toms with unequal decays; alternate low-high tom replies in the spaces after piano chords. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000035 — 29_D08_목재의 낮은 울림

그룹 D / 문안1.0 / Style 696자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4. Dark, muffled, warm, steady low energy. Soft studio upright piano, rich woody body, softly muted hammer and a small warm room is the main voice, with rounded bass. Harmony: Am9 2 bars, Em7 2, Fmaj9 2, Dm7 1, G6 1. A descending chord voice crosses beneath a quiet stationary melody tone, followed by two widely separated notes. A large pillow-damped kick and a short dull closed hi-hat; kick starts alternate bars, hat gives a sparse offbeat pair with long silence. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000036 — 30_D09_어두운 아날로그 건반

그룹 D / 문안1.0 / Style 722자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 66 BPM, 4/4. Dark, muffled, warm, steady low energy. Analog electric-piano keyboard with a softly triangular body, rounded plucky onset and dark short release, not a bell is the main voice, with rounded bass. Harmony: Cmaj9 3 bars, Fmaj7 1, Dm9 2, Em7 2. A four-bar melody rises slowly by seconds then drops a fourth; leave chord tones unfilled rather than playing scales. A low soft kick with a slow round attack and a softly mallet-hit medium tom, bass drum once in odd bars and tom once in even bars. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000037 — 31_D10_묵직한 해머의 그림자

그룹 D / 문안1.0 / Style 740자 / Exclude 350자.

Style
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4. Dark, muffled, warm, steady low energy. Mellow low-velocity grand piano, thick middle notes, rounded hammer transients and a close narrow image is the main voice, with rounded bass. Harmony: Fm9 2 bars, Bbm9 2, Dbmaj7 1, Eb6 1, Cm7 2. A pair of sustained chord tones trades which voice moves, with small low-register piano replies every four bars. A short tight felt kick and a dark damped floor tom, low transient but clear body; two quiet kick hits spaced across one bar, one long tom response in the next. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone
```

### PRM-000038 — 32_P01_점토의 둥근 호흡

그룹 P / 문안1.0 / Style 700자 / Exclude 402자.

Style
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4. Dark, muffled, warm, steady low energy. Reed electric piano, velvety low-mid tone, smooth onset and softly damped tails is the main voice, with rounded bass. Harmony: Ebmaj9 2 bars, Cm7 3, Abmaj7 1, Fm9 2. A held melody note is revoiced below, then answers with a falling third after a full beat of silence. Only clay udu, hollow rounded air-body bass tones with quiet damped fingertip shell taps; alternate one deep tone with two separated soft touches over two bars. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drum kit, kick drum, hi-hat, cymbals, drum machine
```

### PRM-000039 — 33_P02_나무 상자의 빈자리

그룹 P / 문안1.0 / Style 732자 / Exclude 402자.

Style
```text
Instrumental lo-fi hip hop, 66 BPM, 4/4. Dark, muffled, warm, steady low energy. Soft felt upright piano, dry compact midrange, gentle percussive hammer and brief release is the main voice, with rounded bass. Harmony: Bbmaj7 3 bars, Gm9 1, Ebmaj7 2, Cm9 1, F6 1. A short rising dyad resolves into a held single melody tone; sustained chord inversions avoid constant root-position blocks. Only a snareless Peruvian cajon, low wooden center thumps and padded side touches; one center hit on 2 and a muted side answer late in the following bar. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drum kit, kick drum, hi-hat, cymbals, drum machine
```

### PRM-000040 — 34_P03_낮은 가죽의 결

그룹 P / 문안1.0 / Style 735자 / Exclude 402자.

Style
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4. Dark, muffled, warm, steady low energy. Warm tine electric piano, soft elastic attack, thick slightly sustained mids with bell component suppressed is the main voice, with rounded bass. Harmony: Dm9 3 bars, Fmaj7 1, Bbmaj9 2, Gm7 2. Two chord tones move in contrary directions, followed by a sparse melody pickup near each fourth bar ending. Only a low conga with damped open tones and very soft muted palm strokes; one low tone at the phrase head and a quiet two-stroke answer, no slaps or busy tumbao. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drum kit, kick drum, hi-hat, cymbals, drum machine
```

### PRM-000041 — 35_P04_두 통의 느린 대화

그룹 P / 문안1.0 / Style 731자 / Exclude 402자.

Style
```text
Instrumental lo-fi hip hop, 62 BPM, 4/4. Dark, muffled, warm, steady low energy. Una-corda grand piano, dark rounded body, soft felt-like onset, short warm room and moderate sustain is the main voice, with rounded bass. Harmony: Abmaj9 4 bars, Fm9 2, Bbm7 1, Eb6 1. One inner note moves while the upper melody rests; every other four-bar phrase uses a slow descending pair. Only muted bongos played gently on the lower drum, two subtly different skin pitches with rounded attacks; isolated low-high pair in one bar followed by an empty bar. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drum kit, kick drum, hi-hat, cymbals, drum machine
```

### PRM-000042 — 36_P05_부드러운 알갱이

그룹 P / 문안1.0 / Style 712자 / Exclude 402자.

Style
```text
Instrumental lo-fi hip hop, 65 BPM, 4/4. Dark, muffled, warm, steady low energy. Mellow reed electric piano, dry smoky middle register, soft onset and very short dark decay is the main voice, with rounded bass. Harmony: Cm9 2 bars, Ebmaj7 1, Abmaj9 3, Gm7 2. The melody holds across a chord change then descends a fifth; detached chord replies occupy the rests. Only a soft low-volume studio shaker with a dark rounded granular texture, brief separated gestures on weak beats and full silent bars; no continuous swishing. Keep the keyboard in a comfortable middle register, all rhythm quiet behind it. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drum kit, kick drum, hi-hat, cymbals, drum machine
```

### PRM-000043 — 37_N01_박자만 남은 방

그룹 N / 문안1.0 / Style 638자 / Exclude 444자.

Style
```text
Instrumental lo-fi hip hop, 62 BPM, 4/4. Dark, muffled, warm, steady low energy. Felt upright piano, close dry woody body and soft rounded hammer is the main voice, with rounded bass. Harmony: Fmaj9 3 bars, Gm9 1, Bbmaj7 3, C6 1. A short chord and held melody note alternate across bars; rhythmic gaps carry the pulse. No drums or percussion at any point; only piano and sparse warm upright bass, with bass roots on selected chord changes. Keep the keyboard in a comfortable middle register, leave real silence between phrases. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drums, percussion, kick drum, toms, hi-hat, cymbals, claps, shaker, hand drums, drum machine
```

### PRM-000044 — 38_N02_잔향 사이의 저음

그룹 N / 문안1.0 / Style 702자 / Exclude 444자.

Style
```text
Instrumental lo-fi hip hop, 60 BPM, 4/4. Dark, muffled, warm, steady low energy. Warm tine electric piano, velvety sustained body, gently rounded onset, muted metallic overtones is the main voice, with rounded bass. Harmony: Gm9 2 bars, Bbmaj7 2, Cm9 3, Dm7 1. Sparse upper thirds resolve into a single middle note; sustain harmony but leave long melodic rests. No drums or percussion at any point; piano is the only melodic instrument, a short round synth bass quietly supports alternate chord changes. Keep the keyboard in a comfortable middle register, leave real silence between phrases. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drums, percussion, kick drum, toms, hi-hat, cymbals, claps, shaker, hand drums, drum machine
```

### PRM-000045 — 39_N03_천천히 접히는 화음

그룹 N / 문안1.0 / Style 694자 / Exclude 444자.

Style
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4. Dark, muffled, warm, steady low energy. Closed-lid grand piano, soft low-velocity hammer, thick mellow body and restrained pedal is the main voice, with rounded bass. Harmony: Ebmaj9 4 bars, Abmaj7 1, Fm9 2, Bb6 1. Slowly rolling three-note chords alternate with simultaneous dyads, with a sparse falling melody across the voicings. No drums or percussion at any point; piano and dry plucked upright bass only, bass phrases never double the piano attack. Keep the keyboard in a comfortable middle register, leave real silence between phrases. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drums, percussion, kick drum, toms, hi-hat, cymbals, claps, shaker, hand drums, drum machine
```

### PRM-000046 — 40_N04_리드 건반의 고요

그룹 N / 문안1.0 / Style 705자 / Exclude 444자.

Style
```text
Instrumental lo-fi hip hop, 61 BPM, 4/4. Dark, muffled, warm, steady low energy. Reed electric piano, hollow rounded middle tone with soft onset, no bark and a dark short release is the main voice, with rounded bass. Harmony: Am9 3 bars, Dm9 1, Em7 2, Fmaj7 2. A quiet low piano reply follows a sustained upper chord; move the inner voice only at phrase endings. No drums or percussion at any point; keyboard alone carries harmony and melody, round bass notes appear sparingly with no regular beat pattern. Keep the keyboard in a comfortable middle register, leave real silence between phrases. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drums, percussion, kick drum, toms, hi-hat, cymbals, claps, shaker, hand drums, drum machine
```

### PRM-000047 — 41_N05_펠트 뒤로 남은 빛

그룹 N / 문안1.0 / Style 708자 / Exclude 444자.

Style
```text
Instrumental lo-fi hip hop, 63 BPM, 4/4. Dark, muffled, warm, steady low energy. Felt grand piano, soft broad midrange attack, dark medium decay and a tiny warm room is the main voice, with rounded bass. Harmony: Bbmaj9 2 bars, Dm7 1, Gm9 3, Cm7 1, Eb6 1. A restrained melody ascends a fourth then settles through two widely spaced notes; chord changes use smooth inversions. No drums or percussion at any point; piano and sparse warm upright bass only, calm measured spacing supplies a gentle internal pulse. Keep the keyboard in a comfortable middle register, leave real silence between phrases. Maintain this identity through the body. Thin one phrase later; finish with a gently damped chord. About 3:00.
```

Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping, guitar lead, metallic bell keyboard tone, drums, percussion, kick drum, toms, hi-hat, cymbals, claps, shaker, hand drums, drum machine
```


### 추가20곡 실행 결과 — 2026-10-29

PRM-000028~000047 모두 v6-mini 고급 입력 후 각2후보 생성 완료. 제목·Style·Exclude의 브라우저 입력 패키지를 원장과20개 모두 대조했다. 실제20건/40후보,200크레딧. 결과 링크와 길이는22_SECOND_BATCH.md, 세부 실행은 second_batch.json. 사용자 청취 피드백과 최종 채택 대기.
