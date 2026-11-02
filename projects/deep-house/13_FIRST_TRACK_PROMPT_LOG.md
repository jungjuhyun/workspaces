# 첫 곡 재현 입력 원장

## R01-S001 — v0.1 / 2026-11-03 / 미입력 초안

근거 문서: 07 초기 분석, 11 보완 결과, **12 통합 제작 명세와 사용자 보컬찹 확인**. 백지화 이후의 이 프로젝트에는 기존 생성 입력 원장이 없었으며 이번에 새로 작성했다. 백업의 과거 프롬프트·결론을 가져오지 않았다. 아래는 실제 입력·생성 기록이 아닌 제안 전문이다.

### 제안 모드와 설정

| 항목 | 제안 | 근거·한계 |
|---|---|---|
| 경로 | Simple, 새 텍스트 생성 | 한 통합 입력으로 음악·편곡·제외 조건을 전달. Cover/업로드 경로를 실행하지 않음 |
| 모델 | v6-mini를 첫 기준 후보로 제안 | 사용자의 기존 mini 선호를 출발점으로 삼은 임시 선택. 이 첫 곡/딥하우스에서 우수함을 확인한 모델 순위가 아님 |
| Variety | 0 | 직접 작성한 스타일 지시를 유지하기 위한 공식 설명에 따른 제안 |
| Max Mode | 첫 기준 생성에서는 끔 | 초기 결과의 방향을 비교하기 위한 제안. 원곡 재현 최적 설정이라고 검증한 값이 아님 |
| Personalize | 표시되는 경우 끔 | 레퍼런스 외 개인화가 비교에 섞이지 않게 하려는 실험 설계 선택 |
| 가사 | 별도 가사·편곡 태그를 입력하지 않음. 가사 칸이 있다면 비움 | 사용자 방식 유지. 아래 본문에서 비언어 보컬찹과 긴 리드 보컬을 구분 |
| 기타 슬라이더 | 표시되는 화면 기본값을 유지하고 실제 실행 시 기록 | 측정에서 최적값을 도출한 근거가 없음. 과거 다른 장르의 고정 조합을 가져오지 않음 |
| 실행 | 미실행, 생성 횟수 0 | 이번 사용자 지시는 중단된 분석 재개이며 유료 생성 승인으로 바꾸지 않음 |

사용자 제공 Simple 한도는 3,000자다. 현재 계정 화면에서 이 설정들이 모두 노출되는지 이번에는 확인하지 않았다. 실제 입력 전에는 AI가 화면의 모드·모델·설정을 확인하고 실행 기록에 남겨야 한다. 사용자에게 기술 설정이나 새 프롬프트 작성을 맡기지 않는다.

### 통합 입력 전문

```text
Create a deep house track for coding and deep focus, approximately 3 minutes 42 seconds. 105 BPM, steady 4/4, restrained and hypnotic, with spacious repeating midrange textures and a grounded low end.

Use a rounded, muffled four-on-the-floor kick, short subdued backbeats, and thin quiet offbeat hi-hats behind the low groove. The hats remain present without a sharp metallic foreground. Keep the kick and bass centered. The deep bass holds a simple pitch center across several bars while its level repeatedly dips around each kick and swells back before the next beat. Build long G-flat1 and B-flat1 root regions, with an occasional brief low D-flat1 turnaround before returning to G-flat1; avoid a busy moving bassline.

Use soft electronic chord tones and small repeating pitched figures in the midrange, with a B-flat-minor color and B-flat/D-flat/F-centered upper harmony. Keep the palette limited, with overlapping sustained tails and softly repeating echoes. Let the register and brightness shift between phrases rather than keeping one static pad throughout. The middle passage exposes more upper-register texture while the bass groove remains familiar.

Include intermittent processed vocal chops: short pitched, non-lyrical vocal fragments with space between phrases and lingering stereo tails. Introduce a chop around 20 seconds and let this element recur selectively, including around 1:33. These are brief musical fragments, not a lead singer or a continuous vocal hook.

Arrangement: a sparse opening, with background texture first and brief bass/vocal hints after about 18 seconds; the full kick-and-bass body enters around 39 seconds. Keep the groove stable with small gaps around 1:13 and 1:48. Bring the upper texture forward around 1:52. Strip back the low groove around 2:29, leaving spacious pitched remnants and occasional small events, then restore the original groove around 2:47. Gradually remove bass and drums after about 3:23, ending in a fading harmonic tail. Treat these times as approximate musical landmarks.

Keep the low end compact and the midrange background spacious. Some short sounds leave wider tails; do not wash every layer in the same reverb. Avoid intelligible lyrics, sung verses, full vocal toplines, constant vocal chopping, string-like leads, brass-like synth leads, extended solo melodies, piercing hats, aggressive snare cracks, busy fills, big EDM risers, and explosive festival drops.
```

### 분석에서 입력으로 옮긴 범위

- 105 BPM·리듬 골격·저음 교대·짧은 Db1 연결·중앙 저역/넓은 중역·편곡 랜드마크는 07·11·12의 근거에서 가져왔다.
- 보컬찹은 사용자 청취 확인으로 반영했다. ‘no vocals’처럼 이 요소까지 지울 수 있는 넓은 금지 표현을 쓰지 않았다. 정확한 성별·샘플·음절은 새로 정하지 않았다.
- B-flat-minor와 B-flat/D-flat/F는 현재 근거가 있는 **화성 설계 후보**이며 원곡의 모든 보이싱을 확정한 악보가 아니다. 간헐적 Db1 연결을 매 순환의 의무 패턴으로 강제하지 않았다.
- 약 0.43초 반복의 물리적 원인이 미확정이므로 검증되지 않은 정확한 딜레이 노브·음표열은 입력하지 않았다. 부드러운 반복음과 이어지는 꼬리라는 출력 특징으로 전달한다.
- 제외 조건도 이 통합본에 포함했다. 다만 Simple 본문의 Avoid는 Custom의 별도 Exclude 필드와 동일한 기능이라고 주장하지 않는다.
- 문장·초시각·음 이름을 썼다고 구현이 보장되지는 않는다. 원곡을 기준으로 실제 결과의 그루브·음색·공간·전개를 대조해야 한다.

### 실행 전후 기록란

- 실제 실행자/시각: 미실행.
- 실제 계정 모드/모델/슬라이더: 미확인.
- 생성 결과 링크/파일: 없음.
- 원곡 비교·사용자 청취 평가: 없음.
- EQ/리버브 후처리: 없음.

### 기능 관련 확인 출처

2026-11-03 공식 본문 확인: [v6 FAQ](https://help.suno.com/en/articles/13924481)는 Simple에서 복합적인 음악 지시를 전달하는 경로, 모델 구분과 Variety 0의 용도를 설명한다. [Exclude 안내](https://help.suno.com/en/articles/3161921)는 Custom의 Advanced Options에 있는 별도 Exclude를 설명한다. 이 공식 기능 설명을 본 초안의 지시 준수 성능이나 계정 화면의 실제 관찰로 바꾸지 않는다.

## R01-S001 — v0.1 첫 실행 / 2026-11-03

- 사용자 실행 지시: 첫 생성·원곡 비교 단계 제안에 “진행해”. AI가 Suno UI를 조작했다.
- 위 입력 전문은 수정하지 않았다. 실제 Simple 텍스트 영역의 길이 2,437자를 확인했다.
- 실제 화면: Songs / Simple / **v6-mini**. 진입 당시 v6에서 v6-mini로 바꿨다. 입력 전 크레딧 표시: **12,072**.
- 오디오·Voice·이미지·별도 가사·추가 Styles는 첨부하지 않았다. 본문의 보컬찹·제외 조건을 포함한 텍스트만 입력했다.
- **제안 설정과 실제 설정의 차이:** 관찰한 Simple 화면과 추가 메뉴에는 Variety·Max Mode·Personalize 조절이 노출되지 않았다. 따라서 위의 0/끔 제안값을 적용했다고 기록하지 않는다. 이 첫 결과는 실제 UI가 제공한 Simple/v6-mini 설정의 기준 결과다. 다른 숨은 슬라이더 값을 추측하지 않는다.
- Create 1회로 아래 2곡의 생성·다운로드를 확인했다. 크레딧 표시 12,072→12,062, **10 사용**. 추가 Create는 누르지 않았다.
- 로그인은 처음 필요했으나 사용자가 직접 완료했다고 답했고 생성 화면 접근을 확인했다. 비밀번호·인증코드를 수집하거나 AI가 로그인했다고 기록하지 않는다.
- 증거: 로컬 `generation_R01S001_20261103/execution_record.json`, `before_create.png`. 음원·스크린샷·원자료는 커밋하지 않는다.

| 결과 | Suno 링크 | 실제 WAV 길이 |
|---|---|---|
| G01, Focused Groove | https://suno.com/song/2b947d64-cb2e-4c3c-a172-550a4d623cb8 | 221.600초 |
| G02, Focused Groove | https://suno.com/song/658b3d33-09fe-4a28-91e1-6f63a7dc7af4 | 221.960초 |

두 파일 모두 48 kHz stereo PCM16 WAV다. 원본 보관 위치는 `local/deep-house/generation_R01S001_20261103/R01-S001_G01_2b947d64.wav`, `R01-S001_G02_658b3d33.wav`다. 기존 Premier 다운로드 할당에서 2곡을 Unlock & Download했다. 다운로드 창은 첫 곡 전 19, 두 번째 곡 전 18을 표시했다. 새 구독/크레딧 구매는 하지 않았다.

### Suno가 실제로 표시한 Styles 전문 — 두 결과에서 동일

아래는 사용자가 입력한 원문과 다르다. Simple 경로에서 Suno가 정리한 출력 메타데이터를 UI의 Copy styles로 기록했다. 정확한 초시각·일부 세부 제외 문구가 이 표시에서 사라졌지만, 숨은 내부 처리까지 이 표시와 동일하다고 추측하지 않는다.

```text
Deep house for focused coding, 105 BPM steady 4/4, restrained hypnotic pulse and compact centered low end, Sparse opening with spacious softly repeating midrange chords and small pitched figures; subdued rounded muffled four-on-the-floor kick, quiet short backbeats and thin soft offbeat hats tucked behind the groove, Simple sustained G-flat root bass regions alternating with B-flat, with rare brief low D-flat turnaround; bass ducks gently around each kick and swells between beats, no busy runs, B-flat-minor color with upper harmony centered on B-flat, D-flat and F, Limited palette, overlapping sustained tails, softly repeating echoes, brightness and register changing between phrases, Full groove enters late after a long texture-led intro; brief groove gaps; middle section opens the upper register while the low pulse stays familiar; later strip back to airy pitched remnants before restoring the groove; gradually shed drums and bass into a fading harmonic tail, Intermittent short non-lyrical processed vocal fragments, spaced selectively with lingering stereo tails, never a lead vocal, Distinct dry low-end against roomy midrange, varied restrained reverbs, no abrupt drop
```

### Suno가 실제로 표시한 Lyrics — 두 결과에서 동일

```text
[Instrumental]
[Non-lyrical vocal chops: brief, sparse, processed fragments]
```

위 가사 태그는 **AI가 가사 칸에 직접 작성한 입력이 아니다.** Simple 생성 후 서비스가 표시한 내용이다. 태그에 vocal chops가 있다는 사실은 실제 음원에 보컬찹이 있다는 증거가 아니다. 14의 측정과 사용자 청취 확인을 따로 기록한다. 음원에 대한 AI 직접 청취는 하지 않았다.


## R01-S002 — v0.2 / 2026-11-03 / 보컬찹 필수 층 강조

사용자 피드백: S001 G02가 더 가깝고 두 비교 구간 모두 보컬찹이 들리지 않음. 수정 목적과 사전 비교 질문은 15에 기록했다. 기존 드럼/베이스·상층 화음·편곡 문단은 유지하고, 보컬 문단의 위치·우선도·음색/발음 명세 및 관련 제외 표현을 수정했다.

### 통합 입력 전문

```text
Create a wordless vocal-chop deep house track for coding and deep focus, approximately 3 minutes 42 seconds. 105 BPM, steady 4/4, restrained and hypnotic, with spacious repeating midrange textures and a grounded low end.

Clearly audible chopped HUMAN VOICE samples are an essential musical layer. Use recognizable human-vowel formants with short pitched syllabic attacks, processed into a sparse vocal-chop motif. Each phrase is one or two clipped wordless vowel sounds followed by lingering stereo tails, with real gaps between phrases. Introduce this voice motif around 20 seconds and let it recur selectively, including around 1:33. Keep the voice fragments easy to distinguish from the electronic chord texture while the overall track remains restrained and suitable for focus.

Use a rounded, muffled four-on-the-floor kick, short subdued backbeats, and thin quiet offbeat hi-hats behind the low groove. The hats remain present without a sharp metallic foreground. Keep the kick and bass centered. The deep bass holds a simple pitch center across several bars while its level repeatedly dips around each kick and swells back before the next beat. Build long G-flat1 and B-flat1 root regions, with an occasional brief low D-flat1 turnaround before returning to G-flat1; avoid a busy moving bassline.

Use soft electronic chord tones and small repeating pitched figures in the midrange, with a B-flat-minor color and B-flat/D-flat/F-centered upper harmony. Keep the palette limited, with overlapping sustained tails and softly repeating echoes. Let the register and brightness shift between phrases rather than keeping one static pad throughout. The middle passage exposes more upper-register texture while the bass groove remains familiar.

Arrangement: a sparse opening, with background texture first and brief bass/vocal hints after about 18 seconds; the full kick-and-bass body enters around 39 seconds. Keep the groove stable with small gaps around 1:13 and 1:48. Bring the upper texture forward around 1:52. Strip back the low groove around 2:29, leaving spacious pitched remnants and occasional small events, then restore the original groove around 2:47. Gradually remove bass and drums after about 3:23, ending in a fading harmonic tail. Treat these times as approximate musical landmarks.

Keep the low end compact and the midrange background spacious. Some short sounds leave wider tails; do not wash every layer in the same reverb. Avoid intelligible sentences, lyrical verses, continuous lead-vocal melodies, nonstop chopped-voice phrases, string-like leads, brass-like synth leads, extended solo melodies, piercing hats, aggressive snare cracks, busy fills, big EDM risers, and explosive festival drops.
```

### 필요한 설정과 실행 범위

- Songs / Simple / v6-mini. 텍스트 2,720자, 별도 Lyrics·Audio·Voice·Image·Styles 첨부 없음.
- Simple에서 노출되지 않는 Variety/Max/Personalize 값을 적용했다고 기록하지 않음. 다른 장르의 슬라이더 수치를 가져오지 않음.
- 기존 일반 생성·비교 작업을 사용자 청취 피드백에 따라 이어가는 수정이다. 이번 버전은 Create 1회, 기본 2곡을 계획한다. 계정 구매·구독 변경·추가 유료 옵션은 포함하지 않는다.
- 원곡과 S001 G02를 비교 앵커로 보존. 새 생성의 음색이 G02와 동일하다고 가정하지 않음.
- 작성 시점: 미입력/미생성. 실제 실행 시각·결과·크레딧은 아래에 별도로 남긴다.


### 실제 실행 결과 — R01-S002

- Songs / Simple / v6-mini에 위 2,720자 원문을 입력하고 Create 1회, 2곡을 생성했다. 크레딧 12,062→12,052(10 사용). Simple에 보이지 않는 슬라이더 값을 적용했다고 기록하지 않는다.
- G03 Focused Flow: https://suno.com/song/8cf03875-c3ef-47d3-9dd3-92075e73647f — WAV 222.000초.
- G04 Focused Flow: https://suno.com/song/6dbb5c47-473b-41b9-a8f7-4851c69e6b49 — WAV 221.600초.
- 둘 다 48 kHz / stereo / PCM16 다운로드. 실제 표시 Lyrics는 두 곡 모두 아래 한 줄이었다. 신호 비교 결과는 15, 로컬 원본·해시·측정은 `local/deep-house/generation_R01S002_20261103/`에 둔다.

```text
[Instrumental]
```

Suno 표시 Styles 전문은 두 곡에서 같았다. 입력 의도가 실제 음원에서 실현됐다는 증거로 사용하지 않는다.

```text
Restrained hypnotic deep house for deep focus, 105 BPM steady 4/4, Sparse opening with roomy midrange texture, then brief low-groove and human-vowel hints around 18 seconds; full rounded muffled four-on-floor kick and compact centered bass enter near 39 seconds, Quiet short backbeats and thin subdued offbeat hats, never metallic-forward, Bass holds long G-flat1 and B-flat1 root regions with occasional brief low D-flat1 turn, gentle kick-synced dips and smooth returns, B-flat-minor color with upper B-flat, D-flat and F tones; soft electronic chord voicings and small repeating pitched figures, overlapping sustained tails and selective soft echoes, Clearly recognizable human-vowel formants as a sparse, distinct motif: one or two clipped pitched wordless syllabic attacks per phrase, then lingering stereo tails and real gaps; first around 20 seconds and recurring selectively, including near 1:33, Groove stays familiar through small gaps near 1:13 and 1:48; bring upper-register texture forward around 1:52, Strip low groove around 2:29 to spacious pitched remnants and occasional small events, restore the original groove near 2:47, then gradually remove bass and drums after 3:23 into a fading harmonic tail, Compact centered low end, spacious midrange, restrained dynamics, varied register and brightness between phrases, soft-focus clean production
```

## R01-S003 — v0.3 / 2026-11-03 / G02 참조 Cover + 비언어 음절

S002의 문구 강조만으로도 보컬 배정 성분이 거의 나타나지 않아 그 경로를 종료한다. 더 가까웠던 G02를 서비스 안에서 참조하는 Cover로 바꾼다. 현재 Remix/Edit 메뉴에는 공식 문서의 Add Vocals 항목이 없고 Cover가 제공된다. 실제 경로를 Add Vocals 실행으로 기록하지 않는다.

가사 칸을 비우던 기존 방식을 이번에 변경한다. 입력은 문장 가사 없이 짧은 Ah/Oh와 편곡 의도 태그뿐이다. 원곡/다른 사람 음원을 새로 업로드하지 않는다. 참조는 사용자의 계정에서 이번 작업으로 만든 G02다.

### 통합 입력: Styles

```text
105 BPM hypnotic deep house. Retain the reference groove: rounded muffled four-on-floor kick, subdued backbeats, thin quiet offbeat hats, deep pulsing bass and hazy midrange electronic chords. Add intermittent HUMAN VOCAL CHOPS: one or two sharply clipped, pitched ah/oh syllables with recognizable vocal formants and short staccato mouth attacks, real gaps between phrases and lingering stereo echo tails. Keep each sung fragment brief; let only its tail linger. Introduce the voice after the sparse opening, then occasional accents over the groove and after the central break. Keep the restrained low energy, slow harmonic pace, short groove gaps, central break and familiar return. Center kick and bass, keep chord and vocal tails spacious. Finish by subtracting drums and bass into an echo tail. About 3:42.
```

### 통합 입력: Exclude

```text
intelligible sentences, lyrical verses, rap, spoken narration, continuous lead singing, long melisma, choir, string-like leads, brass-like synth leads, piercing hats, hard snare cracks, busy fills, EDM risers, festival drops
```

### 통합 입력: Lyrics

```text
[Intro]

[Short wordless vocal chops]
Ah
Oh

[Groove: sparse clipped vocal accents]
Ah

[Space for the echo]
Oh

[Central break: voice rests]

[Return: short vocal chops]
Ah
Oh

[Outro: echo fades]
```

### 필요한 설정

- Advanced / Cover / v6-mini. 참조: https://suno.com/song/658b3d33-09fe-4a28-91e1-6f63a7dc7af4 (G02, Focused Groove).
- Weirdness 50, Style Influence 50: 현재 기본값 유지.
- Audio Influence 80: 현재 UI 기본 25(Loose)보다 참조를 더 따르게 하려는 실용 후보. 측정으로 도출한 최적값이나 보존 보장값이 아님. PDF의 고정 90/20 조합을 가져온 것이 아님.
- Variety 0, Max Mode Off, Personalize Off. Duration Auto. Vocal Gender는 지정하지 않음.
- Title: R01-S003 Vocal Chop. Create 1회만 계획. 원본 G02를 덮어쓰지 않음.
- 실제 입력·설정 확인·생성 결과는 실행 뒤 별도 기록. 이 문단 작성 시점에는 아직 생성하지 않음.

가사·참조·모드가 함께 바뀌므로 특정 한 요소의 인과 실험으로 해석하지 않는다. 목표는 보컬찹 존재와 G02 방향 유지이며, 성공 여부는 실제 결과와 사용자 청취로 확인한다.

### 실제 실행 결과 — R01-S003

- 위 Styles 811자 / Exclude 224자 / Lyrics 197자를 실제 입력하고 Advanced / Cover / v6-mini로 Create 1회, 2곡을 생성했다. 참조는 서비스 내부의 G02다.
- 생성 직전 실제 확인: Weirdness 50 / Style Influence 50 / Audio Influence 80 / Variety 0 / Max Off / Personalize Off / Duration Auto / Vocal Gender 지정 없음. 슬라이더의 Home/End가 값을 바꾸지 않아 화살표로 조정한 뒤 **실제 표시 80/0을 다시 확인**했다. 잘못된 중간값으로 생성하지 않았다.
- 크레딧 12,052→12,042(10 사용). 이번 피드백 이후 S002+S003 합계 20, 새 제작 전체 S001~S003 합계 30 사용. 구매·구독 변경·공개 Publish는 하지 않았다.
- G05 R01-S003 Vocal Chop: https://suno.com/song/a887f233-3a95-4173-aafb-efec3f100ab5 — WAV **184.800초(3:05 표시)**.
- G06 R01-S003 Vocal Chop: https://suno.com/song/62168222-e422-485c-876f-3007578dc973 — WAV **202.120초(3:22 표시)**.
- 두 파일 모두 48 kHz / stereo / PCM16 다운로드. About 3:42라는 입력을 실제 길이로 기록하지 않는다. 새 결과의 표시 Lyrics는 위 통합 Lyrics와 문자 단위로 같았다. Copy styles는 문장을 쉼표로 정리하고 Exclude를 부호와 함께 합친 1,050자이며, 두 결과에서 같았다. 실제 표시 전문은 아래에 보존한다. 입력 필드의 811자와 표시 1,050자를 혼동하지 않는다.
- 원본 WAV·입력 파일·UI 스크린샷·해시·실제 표시 전문·실행 JSON은 `local/deep-house/generation_R01S003_20261103/`에 둔다. 결과 대조는 16. 보컬 배정 성분은 나타났으나 사용자 청취 확인 전이며, AI 직접 청취나 재현 성공으로 기록하지 않는다.

### 실제 Copy styles 전문 — G05/G06 동일

```text
105 BPM hypnotic deep house, Retain the reference groove: rounded muffled four-on-floor kick, subdued backbeats, thin quiet offbeat hats, deep pulsing bass and hazy midrange electronic chords, Add intermittent HUMAN VOCAL CHOPS: one or two sharply clipped, pitched ah/oh syllables with recognizable vocal formants and short staccato mouth attacks, real gaps between phrases and lingering stereo echo tails, Keep each sung fragment brief; let only its tail linger, Introduce the voice after the sparse opening, then occasional accents over the groove and after the central break, Keep the restrained low energy, slow harmonic pace, short groove gaps, central break and familiar return, Center kick and bass, keep chord and vocal tails spacious, Finish by subtracting drums and bass into an echo tail, About 3:42, ‑intelligible sentences, ‑lyrical verses, ‑rap, ‑spoken narration, ‑continuous lead singing, ‑long melisma, ‑choir, ‑string-like leads, ‑brass-like synth leads, ‑piercing hats, ‑hard snare cracks, ‑busy fills, ‑EDM risers, ‑festival drops
```
