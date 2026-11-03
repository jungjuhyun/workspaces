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

## R01-S004 — v0.4 / 2026-11-03 / G05 보컬 유지·저음 골격과 편곡 수정

사용자 확인: G05/G06 제시 구간 모두 보컬찹이 들리고, 두 곡 중 G05가 더 가깝다. G02와 G05의 직접 우열을 추가로 확인받았다고 확대하지 않는다. 보컬찹 존재는 다시 미확인으로 되돌리지 않는다.

G05의 저음 후보는 C2/Db2/Bb1/F1 등의 움직임을 보이며 원곡의 Gb1/Bb1 장기 교대와 다르다. 60~178초 범위에서 8초 평균 드럼 최저 창은 G05 138.25~146.25초, 원곡 150~158초다. 이 창을 정확한 섹션 시작·끝으로 쓰지 않는다. 이제 이 두 음악적 차이를 수정하고 짧은 Ah/Oh 입력은 유지한다.

### 통합 Styles

```text
105 BPM restrained hypnotic deep house, 4/4, B-flat minor. Bass alternates G-flat1 for four bars and B-flat1 for four bars; only a brief low D-flat1 turnaround, then G-flat1 again. Harmony: G-flat major7 (Gb Bb Db F), then B-flat minor (Bb Db F); sparse upper Bb/Db/F figures. Keep bass notes long, with gentle kick-synced level dips. Retain the reference's muffled rounded kick, subdued backbeats, thin quiet offbeat hats and hazy electronic chords. Keep sparse recognizable HUMAN VOCAL CHOPS: one or two clipped pitched ah/oh attacks, real gaps and lingering stereo echo tails. Sparse texture opening, voice hints near 0:20, full groove near 0:39. Small gaps near 1:13 and 1:48; brighter upper texture at 1:52. Remove bass and drums near 2:29, return near 2:47. Deconstruct after 3:23 into a fading tail. Center the deep low end; keep chord and vocal tails spacious, restrained and soft. About 3:42.
```

### 통합 Exclude

```text
intelligible lyrics, continuous lead singing, long melisma, choir, busy moving bassline, frequent chord changes, extended solos, string-like leads, brass-like synth leads, piercing hats, hard snares, busy fills, EDM risers, festival drops
```

### 통합 Lyrics — S003과 동일

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

### 필요한 설정과 실행 전 실제 관찰

- Advanced / Cover / v6-mini. 참조는 G05: https://suno.com/song/a887f233-3a95-4173-aafb-efec3f100ab5.
- G05 페이지의 Cover 진입은 기존 G02가 연결된 입력을 열었다. 이 상태를 G05 참조라고 기록하거나 실행하지 않았다. Audio→Browse의 Library에서 썸네일 ID a887f233…인 G05를 선택해, 실제 연결 제목 R01-S003 Vocal Chop / 길이 03:05를 확인했다.
- Styles 901자 / Exclude 238자 / Lyrics 197자. Duration Custom **3:42 / 222초**, Weirdness50 / Style50 / Audio50 / Variety0 / MaxOff / PersonalizeOff / 성별 지정 없음.
- S003의 Audio80에서 50으로 바꾼 이유는 기존 진행을 그대로 답습하는 것보다 요청한 저음·편곡 변경 여지를 주기 위해서다. 원곡 측정에서 도출한 최적값이나 고정 성공 조합은 아니다. 반주/음색 보존 보장은 하지 않는다.
- Gbmaj7→Bbm의 명시적 음 구성은 12의 유력 화성 후보를 구현하려는 제작 선택이다. 원곡 모든 보이싱의 전사 완료로 표현하지 않는다. 저음은 대표 8마디의 Gb1 장기→Bb1 장기→짧은 Db1 연결을 목표로 한다.
- 제목 R01-S004 Harmonic Return. 일반 Create 1회로 2곡만 계획한다. 설정·참조·스타일이 함께 바뀌므로 단일 문구의 인과 실험이 아니다. 작성 시점 실제 생성은 0회다.

### 실제 실행 — S004

- 위 실제 설정과 입력으로 Create 1회 → G07/G08 두 곡. 크레딧 12,042→12,032(10 사용), S001~S004 전체 40 사용.
- G07: https://suno.com/song/4b8cd4c2-2137-4686-a512-850fc19fd712 — 221.640초 WAV.
- G08: https://suno.com/song/f9d4a6b7-e720-47b9-9e04-6db12c82ff7e — 221.560초 WAV.
- 각 곡 페이지의 Cover of 링크가 G05(a887f233…)임을 확인했다. 둘 다 48 kHz stereo PCM16 다운로드·분리 분석 완료. Copy lyrics는 위 197자와 같았다.
- 저음은 G05의 C2/Db2/Bb1/F1 계열 순서를 계속 따라 Gb1/Bb1 변경 목표를 달성하지 못했다. G07/G08을 원곡에 더 가깝다고 채택하지 않고 G05를 보존한다. 이 실패를 단일 설정의 인과 규칙으로 확대하지 않는다. 상세 17.
- 생성 전 입력 901자는 위 원문 그대로였지만 실제 Copy styles는 아래와 달랐다. `major7` 위치에 의도하지 않은 장르 표현이 표시된 관찰이며, 내부 처리/실제 장르를 이 표시만으로 확정하지 않는다.

```text
105 bpm restrained hypnotic deep house 4 4 b flat minor bass alternates g flat1 for four bars and b flat1 for four bars only a brief low d flat1 turnaround then g flat1 again harmony g flat Psychedelic Trance, Full-On gb bb db f then b flat minor bb db f sparse upper bb db f figures keep bass notes long with gentle kick synced level dips retain the reference s muffled rounded kick subdued backbeats thin quiet offbeat hats and hazy electronic chords keep sparse recognizable human vocal chops one or two clipped pitched ah oh attacks real gaps and lingering stereo echo tails sparse texture opening voice hints near 0 20 full groove near 0 39 small gaps near 1 13 and 1 48 brighter upper texture at 1 52 remove bass and drums near 2 29 return near 2 47 deconstruct after 3 23 into a fading tail center the deep low end keep chord and vocal tails spacious restrained and soft about 3 42, ‑intelligible lyrics, ‑continuous lead singing, ‑long melisma, ‑choir, ‑busy moving bassline, ‑frequent chord changes, ‑extended solos, ‑string-like leads, ‑brass-like synth leads, ‑piercing hats, ‑hard snares, ‑busy fills, ‑EDM risers, ‑festival drops
```

## R01-S005 — v0.5 / 2026-11-03 / 오디오 참조 없이 새 Advanced 생성

Cover가 기존 저음 진행을 이어간 S004 결과에 따라, 오디오 조건을 제거하고 새 텍스트 생성으로 전환한다. G05는 음색 비교 앵커로 보존한다. G05 자체를 참조 오디오로 입력했다고 기록하지 않는다. Lyrics의 짧은 Ah/Oh 입력은 유지하며 화음 이름 `major7`은 `major seventh chord`로 풀어 쓴다. 표시상의 의도하지 않은 장르 문구를 피하려는 수정이며 성공 보장은 없다.

### 통합 Styles

```text
Restrained hypnotic deep house, 105 BPM in B-flat minor. Two-chord cycle: G-flat major seventh chord for four bars, B-flat minor chord for four bars. Deep bass holds G-flat in its low first octave, then B-flat in the same octave; rare low D-flat turnaround before G-flat. Upper chord tones B-flat, D-flat and F. Long bass notes with gentle kick-synced dips. Muffled rounded four-on-floor kick, quiet short backbeats, thin subdued offbeat hats, hazy soft electronic chords. Sparse HUMAN VOCAL CHOPS: one or two clipped pitched ah/oh attacks, real gaps, lingering stereo echo tails. Texture-led opening; voice hints near 0:20, full bass/drum groove near 0:39. Brief gaps near 1:13 and 1:48, upper texture opens at 1:52. Remove bass and drums at 2:29, restore the groove at 2:47; deconstruct after 3:23 into a fading harmonic tail. Compact centered low end, spacious restrained chord and voice tails. About 3:42.
```

### 통합 Exclude

```text
intelligible lyrics, continuous lead singing, long melisma, choir, busy moving bassline, frequent chord changes, extended solos, string-like leads, brass-like synth leads, piercing hats, hard snares, busy fills, EDM risers, festival drops
```

### 통합 Lyrics

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

### 필요한 설정·실행 범위

- Songs / Advanced / v6-mini / 오디오·Voice 참조 없음. Styles 909자, Exclude 238자, Lyrics 197자.
- Duration Custom 3:42(222초), Weirdness50 / Style50 / Variety0 / MaxOff / PersonalizeOff / 성별 지정 없음. 오디오를 제거하므로 Audio Influence를 적용했다고 기록하지 않음.
- 제목 R01-S005 New Harmonic Base. Create 1회로 2곡만 계획. 저음·보컬·편곡·G05 방향을 대조한다. 오디오 참조를 제거하므로 G05 음색 보존을 보장하지 않는다.
- 작성 시점 생성 0회. 새 진행도 구현되지 않으면 같은 텍스트 생성을 계속 반복하지 않고 현재까지의 한계를 기록한다. 구매·구독 변경·다른 레퍼런스 곡 분석은 하지 않는다.

### 실제 실행 — S005

- 위 통합 입력으로 오디오 조건 없는 Advanced/v6-mini 새 텍스트 Create 1회 → G09/G10 두 곡. 생성 전 Duration222 / Weirdness50 / Style50 / Variety0 / MaxOff / PersonalizeOff와 오디오 조건 0개를 실제 확인했다. 크레딧 12,032→12,022(10 사용), S001~S005 전체 50 사용.
- G09: https://suno.com/song/3bb0a259-95a1-422f-8e66-06651e8b9f50 — 실제 WAV **147.200초**. Custom222 입력을 실제 길이로 소급하지 않는다.
- G10: https://suno.com/song/9253e9b1-c218-4524-bcd1-396448daa8eb — 실제 WAV **221.560초**.
- 둘 다 48 kHz stereo PCM16 다운로드·분리 분석 완료. 보컬 배정 성분 최고 .25초 RMS 약 -20.05/-20.20 dBFS. 새 곡의 사용자 청취 확인이나 AI 직접 청취로 바꾸지 않는다.
- 저음은 Bb1/Ab1/Eb1 등의 후보로 바뀌어 원곡의 Gb1/Bb1 교대 목표 미달이다. G10 원본 64.25~64.75초의 약 38.6/77.5/116.3/154.9 Hz 계열도 Eb1 후보를 지지한다. 모든 피크를 독립 음표로 해석하거나 전체 조성을 확정하지 않는다.
- G05를 현재 비교 후보로 보존한다. S004 Cover 반복과 S005 동일 텍스트 재생성 반복을 종료한다. G09/G10을 원곡에 더 가깝다고 채택하거나 사용자에게 다시 보컬 존재를 확인하도록 요구하지 않았다. 신호 근거·실패 범위는 17.
- 실제 Copy lyrics는 위 197자와 같았다. Copy styles는 두 곡에서 같고, 이전의 의도하지 않은 장르 문구는 표시되지 않았다. 이 표시 변화가 소리 변화의 원인이라는 결론은 아니다.

```text
Restrained hypnotic deep house, 105 BPM in B-flat minor, Two-chord cycle: G-flat major seventh chord for four bars, B-flat minor chord for four bars, Deep bass holds G-flat in its low first octave, then B-flat in the same octave; rare low D-flat turnaround before G-flat, Upper chord tones B-flat, D-flat and F, Long bass notes with gentle kick-synced dips, Muffled rounded four-on-floor kick, quiet short backbeats, thin subdued offbeat hats, hazy soft electronic chords, Sparse HUMAN VOCAL CHOPS: one or two clipped pitched ah/oh attacks, real gaps, lingering stereo echo tails, Texture-led opening; voice hints near 0:20, full bass/drum groove near 0:39, Brief gaps near 1:13 and 1:48, upper texture opens at 1:52, Remove bass and drums at 2:29, restore the groove at 2:47; deconstruct after 3:23 into a fading harmonic tail, Compact centered low end, spacious restrained chord and voice tails, About 3:42, ‑intelligible lyrics, ‑continuous lead singing, ‑long melisma, ‑choir, ‑busy moving bassline, ‑frequent chord changes, ‑extended solos, ‑string-like leads, ‑brass-like synth leads, ‑piercing hats, ‑hard snares, ‑busy fills, ‑EDM risers, ‑festival drops
```

## R01-S006 — v0.6 / 2026-11-03 / 로컬 연주 가이드 참조

**상태 정리(2026-11-03):** 아래는 실행 전에 작성한 제안이다. 이후 사용자가 업로드/시험과 업로드 약관 동의를 허용했고, 가이드 업로드와 Create1회/2곡 생성·다운로드·분리/신호 비교를 완료했다. 12,022→12,012로10크레딧 사용. 디스크 정리 후 최신 지시로 C의 실제 폴더에서 분석을 재개했다. Gb1/Bb1/짧은 Db1 연결은 원본 믹스와 대조했고, 편곡·공간 차이를 기록해 청취 비교를 준비했다([19](19_HARMONIC_GUIDE_COMPARISON.md)). 이후 사용자는G12가 셋 중 가장 가깝지만 턱없이 부족하고 보컬찹이 이어져 노래처럼 들린다고 답했다. 아래 '미실행/미적용/허용 대기'는 제안 작성 당시 상태이며 현재 실행을 취소하거나 되돌리는 지시가 아니다.

### 실행 전 작성한 제안

텍스트만으로 정확한 저음 진행을 구현하지 못한 현재 결과에 따라, 분석한 골격을 새로 연주한 22.857초 가이드를 준비했다. 원곡 녹음·G05 음원을 복사한 파일이 아니다. 실제 업로드 허용을 질문했고, 사용자는 '프롬프트로 생성하는 데 무리가 있어서인가'라고 이유를 물었다. **질문은 업로드 허용 답변이 아니다.** AI가 현재 v6-mini 결과에서 확인한 저음 재현 한계와 보컬 입력 개선의 차이를 설명했으며 업로드·새 생성은 하지 않았다.

### 통합 Styles

```text
Restrained hypnotic deep house at 105 BPM. Follow the guide's bass pitch sequence and slow harmonic pace: low G-flat held for four bars, B-flat for most of four bars, brief low D-flat turnaround, then G-flat again. Keep the upper B-flat, D-flat and F colors. Reimagine the guide with a soft rounded muffled kick, subdued backbeats, thin quiet offbeat hats and hazy electronic chord textures. Add sparse HUMAN VOCAL CHOPS: one or two sharply clipped pitched ah/oh attacks with recognizable vocal formants, real gaps and lingering stereo echo tails. Sparse texture opening, voice hints near 0:20, full groove near 0:39. Brief gaps near 1:13 and 1:48; upper texture opens at 1:52. Remove bass and drums near 2:29, restore the familiar groove near 2:47. Subtract drums and bass after 3:23 into a fading harmonic tail. Center kick and bass; keep chord and voice tails spacious, restrained and soft. About 3:42.
```

### 통합 Exclude

```text
intelligible lyrics, continuous lead singing, long melisma, choir, busy moving bassline, frequent chord changes, extended solos, string-like leads, brass-like synth leads, piercing hats, hard snares, busy fills, EDM risers, festival drops
```

### 통합 Lyrics

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

### 필요한 설정과 전송 범위 — 제안값, 미적용

- 업로드할 제안 파일: `local/deep-house/harmonic_guide_20261103/R01_harmony_guide_10bars_105bpm.wav`만. 합성 저음·화음·드럼 22.857초, 105 BPM, 10마디, 48 kHz stereo PCM16. 원곡 녹음·보컬·개인정보를 포함하지 않는다.
- Advanced / Cover / v6-mini를 제안. Duration222 / Weirdness50 / Style50 / Audio80 / Variety0 / MaxOff / PersonalizeOff / 성별 지정 없음. 실제 UI 확인 전 적용값으로 기록하지 않는다.
- Styles 905자 / Exclude238자 / Lyrics197자. 제목 R01-S006 Harmonic Guide. 허용 후 일반 Create1회/2곡만 계획. 현재 Create0회·업로드0회, 마지막 크레딧12,022.
- 가이드가 음정 전달을 돕는지는 새 결과에서 검증해야 한다. 음색·그루브·편곡 재현을 보장하지 않는다. 가이드의 코드 보이싱·음색·덕킹 곡선은 AI 구현 선택이며 원곡 정밀 전사가 아니다. 상세 18.

### 실제 실행 — S006

- 사용자 “그럼 한번 시험해봐22.86초 연주가이드로”, 약관 “동의하고 시험 계속” 허용 후 실행했다. 위 통합 Styles905자 / Exclude238자 / Lyrics197자를 사용했다. 실제 Advanced Cover / v6-mini / Duration222 / Weirdness50 / Style50 / Audio80 / Variety0 / MaxOff / PersonalizeOff / 성별 지정 없음 확인. Create1회,2곡,12,022→12,012(10 사용). 이번 재개에서는 추가 생성하지 않았다.
- 업로드는 Song Demo, 가이드 https://suno.com/song/1f7ead8c-0549-4cb8-ad59-fb1933432acb. 실제 설명 전문237자:

```text
Locally synthesized 105 BPM harmonic demo: low Gb1 for four bars, Bb1 for three and a half bars, Db1 for half a bar, then Gb1 for two bars. Soft G-flat major seventh and B-flat minor chord tones with restrained drums. Instrumental guide.
```

- G11: https://suno.com/song/94335ca6-a80d-4681-b0bf-8238ae6fb7de — 221.880초 /48kHz stereo PCM16 WAV.
- G12: https://suno.com/song/e83d79e1-b157-4e5d-93c1-2f1b107786bb — 221.600초 /48kHz stereo PCM16 WAV.
- 두 곡 페이지의 Cover of가 업로드 가이드 ID임을 확인했다. 실제 Copy lyrics는197자 원문과 일치했고 Copy styles는 문장부호 변경 및 Exclude 태그를 포함해 별도 로컬 파일로 보존했다. 입력 전문과 제품 표시를 구별한다.
- WAV·UI 캡처·실행JSON·분리/비교 결과는 `local/deep-house/generation_R01S006_20261103/`에 있다. 디스크 부족으로 한때 D에 있었으나 최신 사용자 지시로34개 파일을 해시 검증해 C의 일반 폴더로 되돌렸다. 원본 G11/G12 SHA256은 실행JSON과 일치한다.
- 원곡/G05/G11/G12 청취 파일은18초씩 -20LUFS로 맞췄다. 원곡 첫 곡222초 이내만 사용했다. 신호 결과·남은 차이·사용자 새 청취 응답은19에 기록했다. AI 직접 청취·EQ/리버브·최종 채택은 하지 않았다.

## R01-S007 — v0.7 / 2026-11-03 / 보컬 배치 수정안, 미입력

S006 사용자 평가: G12가G05/G11/G12 중 가장 가깝지만 턱없이 부족하고, 보컬찹이 계속 이어져 노래처럼 들린다. 저음 골격의 신호 개선은 유지하되 전체 재현 달성으로 보지 않는다. 다음 한 시험에서는 보컬의 연속성을 줄이는 입력 묶음을 바꾼다. 큰 음색·공간·편곡 차이는 별도로 남겨 두며 EQ/리버브로 해결됐다고 보지 않는다.

### 통합 Styles — 965자

```text
Restrained hypnotic deep house at 105 BPM. Follow the guide's bass pitch sequence and slow harmonic pace: low G-flat held for four bars, B-flat for most of four bars, brief low D-flat turnaround, then G-flat again. Keep the upper B-flat, D-flat and F colors. Reimagine the guide with a soft rounded muffled kick, subdued backbeats, thin quiet offbeat hats and hazy electronic chord textures. Use occasional single clipped vocal-sample hits with human vowel formants. Cut each dry syllable short, then leave voice-free bars while its stereo echo fades. Keep the groove foregrounded; voices never form a tune. Sparse texture opening, voice hints near 0:20, full groove near 0:39. Brief gaps near 1:13 and 1:48; upper texture opens at 1:52. Remove bass and drums near 2:29, restore the familiar groove near 2:47. Subtract drums and bass after 3:23 into a fading harmonic tail. Center kick and bass; keep chord and voice tails spacious, restrained and soft. About 3:42.
```

### 통합 Exclude — 305자

```text
intelligible lyrics, continuous lead singing, long melisma, choir, busy moving bassline, frequent chord changes, extended solos, string-like leads, brass-like synth leads, piercing hats, hard snares, busy fills, EDM risers, festival drops, sustained vowel singing, wordless lead vocal, nonstop vocal chops
```

### 통합 Lyrics — 231자

```text
[Instrumental intro]

[Single clipped vocal hit]
Ah

[Instrumental groove - voice rests]

[Single clipped vocal hit]
Oh

[Instrumental groove - voice rests]

[Instrumental break]

[Single clipped vocal hit]
Ah

[Instrumental outro]
```

### 필요한 설정과 검증 범위

- Advanced / Cover / v6-mini. 참조는 이미 업로드한 합성 가이드 https://suno.com/song/1f7ead8c-0549-4cb8-ad59-fb1933432acb. G12나 원곡의 새 업로드는 제안하지 않는다.
- Duration222 / Weirdness50 / Style50 / Audio80 / Variety0 / MaxOff / PersonalizeOff / 성별 지정 없음. S006과 같은 제안값이며 이번에는 실제 UI에 입력하지 않았다. 원곡 보존·최적 설정이라는 보장이 아니다.
- 비보컬 Styles는S006과 문자 단위로 같다. 보컬 문단/Exclude 추가/Lyrics의 배치만 수정했다.6음절을3음절로 줄여 발음 사이 연주 공간을 요청한다. 이 수는 원곡 사건 수의 정확한 전사가 아니며, 태그가 실제 쉼표/게이트로 작동한다는 검증도 없다. 보컬 존재가 사라지거나 여전히 긴 가창으로 이어질 수 있다.
- 평가: 원곡과 음량을 맞춰 **짧은 목소리 조각 뒤에 실제 목소리의 빈 공간이 생기는지** 확인한다. 분리 성분의 긴 꼬리와 발음은 구별한다. 기존 저음 골격 유지와 전체 음색/공간이G12보다 더 멀어지는지도 함께 본다. 기준은 첫 곡이며 원곡을 매8마디에 한 번 찹이 있는 고정 규칙으로 새로 단정하지 않는다.
- 계획 상한은 일반Create1회/2곡/10크레딧. 이전S006 허용10크레딧은 사용 완료했으므로 이번 새 유료 실행은 허용을 받고 진행한다. 동일 방법에서 연속 가창이 지속되거나 보컬이 없어지면 같은 입력으로 추가Create를 계속 누르지 않는다.
- 작성 상태: 로컬 통합 입력 준비. Suno 입력0회 / 생성0곡 / 사용0크레딧 / 출력URL 없음. 구매·새 업로드·EQ/리버브·최종 채택 없음. 로컬 `generation_R01S007_20261103/draft_record.json`에 제안값/실제 미실행을 구별했다.
