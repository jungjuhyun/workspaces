# 음악적 선택지 — 같은 분위기 안에서 다른 곡 만들기

문서 묶음0.8.0 / 2026-10-27 / Q08~Q11 음악 자료 조사 / 기존 E04·D02 적용

## 이번 결과와 사용할 범위

**악기 이름을 바꾸는 것보다 역할·연주 내용·리듬/화성의 움직임을 함께 정하는 방식으로 선택지를 정리했다.** 건반의 편안함은 기존 R22의 음역·음색/발음·단곡 반복·곡 간 누적을 그대로 적용한다. 새 음악 목표나 수치 경계를 추가하지 않았다.

현재 사용할 수 있는 결과는 악기/연주10개, 리듬/베이스5개, 화성8개, 모티브3개, 도입/전개5개인 **D02 음악적 설계 선택지31개**와 아래 조합·충돌 목록이다. 개수는 합격 기준이 아니라 이번 등록 결과다.

기존 SRC-0001을 재사용하고 새 일차 출처27개를 확인했다. 악기/음원 제작사 설명·공식 교육/제품 문서·저자 교재·연구를 사용했다. 같은 회사·같은 교재의 여러 페이지는 서로 독립된 성능 실험이 아니다. 이번 검색9묶음의 정확한 쿼리·접근 한계·출처별 확인 위치는03_EVIDENCE_REGISTER.md에 기록했다.

이 문서의 모든 OPT는 **AI가 E04를 프로젝트 목표에 연결한 설계 제안**이다. 악기/연주/음악 원리의 설명과 제안한 조합을 구분한다. v6-mini 구현·프롬프트 성공률·실제 편안함·1시간 적합성은 미검증이며 음원 직접 청취/생성은0이다. 완성 Style/Exclude를 수정하거나 D03 시험 입력 패키지를 만든 단계가 아니다.

이 문서에서 발음은 소리가 시작되는 모양, 지속은 남는 길이, 보이싱은 화음을 이루는 음들의 배치를 뜻한다.

## 먼저 구별할 것

| 구별 | 자료에서 확인한 내용 | 이 프로젝트의 적용 |
|---|---|---|
| 음높이와 음색 | SRC-0001의 실험은 음높이·지각 음량·지속을 맞춘 합성음에서도 발음 시간·스펙트럼 특성의 음색 차이를 조사했다 | 음을 낮춘 조정과 밝은 울림/시작을 줄인 조정을 따로 기록. 이 논문은 피로 실험이 아님 |
| 악기명과 실제 소리 | NOIRE와 Rhodes 문서는 음색 변화와 기계/환경 소음을 별도로 다룬다 | felt/Rhodes라는 이름만으로 T01/T02/T07/T08 합격 처리 안 함 |
| 발음과 지속 | Attack·Release·필터·공명은 서로 다른 조절 개념이다 | 시작을 둥글게 했어도 긴 잔향이 누적될 수 있음. 해당 노브가 Suno에 있다는 뜻 아님 |
| 전위와 보이싱 | 전위는 전체 최저음, 보이싱은 화음음의 배치에 관한 구분이다 | 건반을 재배치해도 업라이트가 원음을 받치면 전체 화음의 전위는 별도 확인 |
| 템포와 움직임 | BPM은 박의 속도이며 베이스/분할/강조/화음 변경은 따로 설계할 수 있다 | BPM만 바꾼 곡을 다른 곡으로 보지 않음. swing/half-time은 실제 반영 여부를 시험 |
| 어두운 음색과 소음 | felt·기계음·브러시 쓸기에는 별도의 소음 성격이 있을 수 있다 | 소음을 더해야 따뜻해진다는 조리법을 쓰지 않음. 모든 자연 기계음을 새로 금지하지 않고 원본 Exclude/T07에 맞춰 판단 |

## Q08 — 악기·음색·역할

중간/중저역은 기존 기준에 따른 우선 검토 방향이며 고정 옥타브가 아니다. 악기별 실제 음역·연주 가능성·다른 성부와의 배치를 확인한다. '뒤쪽'은 역할/주목도의 의도이며 리버브를 많이 넣으라는 뜻이 아니다.

| 선택지 | 역할·음악 내용 | 표현 후보(미검증 어휘) | 호환·충돌과 적용 한계 | 근거 |
|---|---|---|---|---|
| OPT-I01 felt 계열 피아노 | 화성/짧은 응답. 중간·중저역을 우선 검토하고 둥근 시작, 음 뒤의 쉼, 필요한 만큼의 잔향을 설계. | soft felt piano, rounded attacks, separated phrases | felt도 타격/페달/마찰 소음과 밝은 샘플이 있을 수 있음. 저역 화음 과밀·I09/I10과의 겹침 및 X01/X03/X04 확인. | SRC-0052, SRC-0001 |
| OPT-I02 둥근 Rhodes | 화성 또는 짧은 선율. 벨 같은 시작이 전면에 남지 않도록 발음·배음·음역을 별도로 지정. | softly played rounded Rhodes, restrained bell-like attack | Rhodes라는 이름만으로 어둡지 않음. 소리 크기와 배음 변화가 함께 생길 수 있음. X02/X03/X08. | SRC-0053, SRC-0001 |
| OPT-I03 나일론 기타 | 화성/리듬 응답. 짧은 손가락 탄현과 잔향을 끊는 쉼을 설계해 건반 독주와 다른 역할 배치. | soft nylon-string fingerstyle, short chord replies | 나일론의 부드러운 성격은 자료 근거, 짧은 제음/응답은 AI 설계 제안. 손톱 공격음·주루룩 아르페지오·스크래치 확인. X02/X05. | SRC-0054, SRC-0065 |
| OPT-I04 지판 쪽 운궁 바이올린 | 뒤쪽 화성/짧은 연결 성부. sul tasto의 부드러운 성격을 후보로 두고 전면의 긴 솔로를 피함. | restrained sul tasto violin, gentle connected notes behind the melody | 모든 현악기로 같은 성격을 일반화하지 않음. 높은 지속음·강한 비브라토·활 마찰/긴 잔향 확인. X02/X04. | SRC-0055 |
| OPT-I05 낮은 음역 클라리넷 | 주선율을 계속 맡기기보다 쉼 사이 짧은 응답. 낮은 음역 약주의 성격을 우선 검토. | quiet lower-register clarinet, brief legato answers | 낮다는 이유만으로 합격 아님. 약하면 묻히고 높거나 세면 성격이 달라짐. 들리게 하려고 지나치게 앞세우지 않음. X01/X02. | SRC-0056 |
| OPT-I06 낮거나 중간 음역 플루트 | 가끔 연결하는 짧은 선율. 다른 성부가 비는 위치에 배치하는 후보. | gentle lower-to-middle flute phrases, sparse answers | 낮은 음은 묻히기 쉽고 높은 음은 밝게 돌출할 수 있음. 숨소리/휘파람 같은 울림·강한 지속 확인. X01/X02/X03. | SRC-0057 |
| OPT-I07 제음한 비브라폰 | 간헐적인 화성/응답. 짧은 공명과 음 사이 여백을 설계. | muted vibraphone, damped resonances, occasional low-to-middle replies | 금속성 시작·상부 음역·페달 잔향·박동이 두드러질 수 있음. 긴 pad와 동시 지속하면 X04 확인. | SRC-0058 |
| OPT-I08 완만한 합성 pad | 뒤쪽 화성. 급한 시작과 과한 고역 공명을 줄이고 음 끝이 다음 화음에 누적되지 않게 설계. | subdued synth pad, gentle onset, controlled release | 긴 Attack이 자동으로 편안하지 않음. 긴 Release·필터 공명·자동 밝기 상승은 X02/X04/X06 확인. | SRC-0059, SRC-0001 |
| OPT-I09 피치카토 업라이트 | 저음의 움직임/주요 박. 다음 음을 가릴 만큼 남는 잔향을 점검하고 문장 끝에서 선택적으로 제음. | round plucked upright bass, deliberate note lengths | 활 연주/합성 sub와 구분. slap·현 버즈·무거운 잔향·저역 건반의 겹침 확인. X01/X03. | SRC-0060, SRC-0063 |
| OPT-I10 단순한 합성 베이스 | 저음 지지. 길게 버티거나 드문 응답을 선택하되 업라이트와 겹칠 때 담당 역할을 정함. | soft sustained synth bass, restrained upper harmonics | sub를 더하면 따뜻해진다는 공식 아님. kick·업라이트·낮은 화음과 동시 지속을 점검. X01/X04. | SRC-0059, SRC-0063, SRC-0065 |

## Q09 — 리듬·베이스

같은 BPM 안에서도 패턴의 빈자리, 분할, 강조 간격, 베이스의 길이와 위치를 고를 수 있다. 아래 표현은 음악 설계용 어휘이며 Suno의 비율·슬라이더 값이 아니다. 관현악 큰북/브러시 자료는 발음의 차이를 이해하는 데만 쓰고 특정 lo-fi 드럼의 실제 소리로 간주하지 않는다.

| 선택지 | 역할·음악 내용 | 표현 후보(미검증 어휘) | 호환·충돌과 적용 한계 | 근거 |
|---|---|---|---|---|
| OPT-R01 직선 분할의 성긴 박 | BPM과 별도로 반복 박/빈자리/베이스 응답 위치를 선택. 일정한 박과 적은 사건을 함께 설계. | steady sparse pulse, straight subdivisions | 조용함을 무리한 무박/완전 정지로 바꾸지 않음. BPM만 다른 같은 패턴은 X05. | SRC-0064, SRC-0065 |
| OPT-R02 가벼운 swing | 정박 기반은 유지하며 분할의 불균등함을 음악적 선택으로 검토. | light swing, sparse unequal subdivisions | 고정 2:1·특정 swing 퍼센트는 지정 근거 없음. 모든 악기의 타이밍이 같은 방식으로 움직인다고 가정 안 함. X06/X09. | SRC-0067, SRC-0064 |
| OPT-R03 쉼 뒤의 당김 응답 | 한 악기가 비는 약박/박 사이에 다른 악기가 응답. 단순 음량 강조 없이 리듬 관계를 바꿈. | off-beat replies in the gaps, restrained syncopation | 너무 촘촘하거나 강하면 낮은 에너지를 잃음. 시작 위치만 옮긴 복제와 실제 구별은 별개. X05/X06. | SRC-0066, SRC-0065 |
| OPT-R04 하프타임 느낌·둥근 저타악 | 박의 속도는 유지한 채 강조 간격을 넓히는 설계 후보. 짧고 뒤쪽인 저타악을 검토. | half-time feel, soft low-drum accents, quiet sparse percussion | 하프타임은 AI의 적용 제안이며 정확한 Suno 구현 미확인. 큰북 말렛 자료를 드럼셋 kick의 직접 실증으로 확대 안 함. snare/강한 kick 추가 금지. X01/X03/X09. | SRC-0064, SRC-0061 |
| OPT-R05 베이스의 결합/교대 | 박에 함께 붙는 베이스와 타악기 사이 빈곳에 답하는 베이스를 구분. 음 길이도 함께 기록. | bass supports the pulse / bass answers between percussion hits | 업라이트+sub+kick을 모두 같은 저역 주역으로 쓰지 않음. 복잡한 워킹/빠른 솔로가 필요한 것은 아님. X01/X06. | SRC-0065, SRC-0063 |

## Q10 — 화성·선율

전곡을 F장조·같은 maj7 순환·같은 짧은 Rhodes 음형에 고정하지 않는다. 회수 원본 자체는09에서 보존하며 변형을 아직 채택하지 않았다. 아래는 곡마다 고를 수 있는 음악 설계 방향이다.

| 선택지 | 역할·음악 내용 | 표현 후보(미검증 어휘) | 호환·충돌과 적용 한계 | 근거 |
|---|---|---|---|---|
| OPT-H01 화음 변경 간격 | 전체 템포를 유지하며 코드가 버티는 시간·바뀌는 위치를 곡의 특징으로 선택. | unhurried harmonic rhythm, uneven chord durations where intended | 느린 변경이 무조건 편안하거나 단조롭다는 뜻 아님. 큰 가속·갑작스러운 전개는 X06. | SRC-0071 |
| OPT-H02 전위와 베이스 경로 | 화음 종류와 최저음을 따로 기록하고 베이스가 짧게 연결/유지하는 경로를 설계. | inversions with a deliberate bass path | 건반의 최저음이 전체 최저음은 아닐 수 있음. 동일 진행의 키만 바꾸는 차이와 구분. X01/X05. | SRC-0068, SRC-0065 |
| OPT-H03 보이싱과 상성부 | 화음 구성음을 어떻게 벌리고 생략/중복할지, 가장 위 음이 얼마나 오래 반복되는지 따로 선택. | spaced mid-register voicings, restrained repeating top note | 벌리면 높은 상성부가 더 돌출할 수 있음. '중저역에 모두 몰기'도 금지 공식이 아닌 충돌 검토 대상. X01/X02/X08. | SRC-0069, SRC-0063 |
| OPT-H04 페달음과 위의 화성 | 한 음을 유지하면서 위 화성이 바뀌는 구조를 후보로 두되 실제 동시음 관계를 확인. | stable pedal tone beneath gently changing harmony | 유지음은 비화성음/긴장을 만들 수 있음. 임의 화음을 얹어 안정적이라 단정하지 않음. X04/X07. | SRC-0072 |
| OPT-H05 중심음·장단조·모드 | 장단조/모드 이름과 실제 중심음·특징 음정·멈추는 곳을 연결해 선택. | a stable modal center, restrained harmonic movement | 장조=밝음/단조=어두움·시작 음만 교체=모드 확립·같은 패턴 전조=다른 곡 같은 단정 금지. X05/X07. | SRC-0070, SRC-0073 |
| OPT-H06 진행의 이동 방식 | 같은 키 안에서도 두 화음 왕복·기능적 복귀·페달 위 움직임을 구별하고 저음/도착점을 함께 적는 후보. | a restrained two-chord exchange / a gentle harmonic return | 교과서 진행 자체가 목표에 맞는 공식은 아님. 실제 화음 관계를 확인하고 원본의 key changes 금지를 유지. X05/X07. | SRC-0077, SRC-0072, SRC-0071 |
| OPT-H07 공통음과 내성 연결 | 한 성부는 유지하고 다른 화음음만 움직이게 하는 연결을 보이싱/음형의 설계 제안으로 검토. | retain a common tone, small inner-voice movement | 음 수를 늘리는 대신 움직일 성부를 구별. 고정된 높은 상성부가 계속 전면에 남으면 X02/X08. 제안한 연결의 실제 동시음 검수 필요. | SRC-0069, SRC-0073 |
| OPT-H08 화음 종류와 색채음 | 단순 3화음·선택한 7화음의 구성을 구분하고 색채음을 넣을 위치/밀도를 설계. | simple chord tones with restrained seventh-color notes | maj7·min7·dominant7의 성격을 같게 취급하지 않음. 확장음을 늘리면 따뜻해진다는 공식 금지. X01/X07. | SRC-0078, SRC-0069 |
| OPT-M01 음형의 윤곽 | 짧은 하행 질문과 쉼 뒤의 응답처럼 음정 방향/멈춤 위치를 주된 개성으로 설계. | short descending question, a separated answer | 짧다는 이유로 같은 몇 음을 전곡·여러 곡에 복제하지 않음. 높은 마지막 음의 반복 노출 확인. X02/X05. | SRC-0073, SRC-0075 |
| OPT-M02 리듬 중심 모티브 | 음높이보다 길고 짧음·시작 위치·쉼의 관계를 먼저 구별하고 재등장 방식을 정함. | a recurring rhythmic cell with deliberate rests | 한 음/리듬 셀의 강박적 반복으로 주의를 독점할 수 있음. 짧은 반복 자체를 피로 개선으로 취급 안 함. X05/X08. | SRC-0073, SRC-0066 |
| OPT-M03 악기 간 모티브 교대 | 선율 일부를 다른 악기가 받되 주역/반주의 역할과 비는 위치를 지속해서 구별. | fragmented motif passed between instruments, clear gaps | 모두 동시에 응답하면 사실상 합주 과밀. 악기 이름만 바꾸고 같은 연주를 유지하면 차별화 불충족. X02/X05. | SRC-0073, SRC-0074 |

## Q11 — 도입·곡 안 변화·곡 사이 연결

첫 사건과 본문에서 지속되는 개성을 따로 적는다. 'A악기→베이스→드럼'을 이름만 바꿔 반복하는 방식은 피한다. 여러 설계에서 공통 요소를 남길 수 있으며 모든 축을 억지로 바꿀 필요는 없다.

| 선택지 | 역할·음악 내용 | 표현 후보(미검증 어휘) | 호환·충돌과 적용 한계 | 근거 |
|---|---|---|---|---|
| OPT-F01 처음부터 조용한 편성 | 긴 순차 입장 대신 핵심 박·저음·화성의 관계를 시작부터 드러내는 도입 후보. | immediate quiet ensemble, established low-energy groove | 처음부터 많은 악기를 꽉 채우는 것과 다름. 큰 첫 타격·긴 도입·빌드업은 X02/X06. | SRC-0076, SRC-0074 |
| OPT-F02 픽업/당김 첫 사건 | 첫 짧은 사건이 박의 어디와 연결되는지 구별. 고정된 '건반→베이스→드럼' 이름 바꾸기를 피함. | a brief pickup leading into the established pulse | 첫 사건만 다르고 본문이 같으면 충분하지 않음. 정확한 타이밍은 Suno 시험 필요. X05/X09. | SRC-0066, SRC-0075 |
| OPT-F03 지속과 타격의 대비 | 지속 화성/저음과 짧은 응답의 관계를 시작부터 드러내고 곡 안에서도 유지. | held harmony with sparse punctuating replies | 단순 악기 순차 추가 공식을 되풀이하지 않음. 지속음끼리 겹치면 X04, 높은 응답 반복은 X02. | SRC-0059, SRC-0074, SRC-0076 |
| OPT-F04 작은 빈자리와 역할 교대 | 전체 박/에너지는 유지하며 한 성부의 끝·쉼을 다른 성부가 받도록 편곡. | small textural gaps, alternating foreground roles, steady energy | 전체를 끊는 breakdown/drop이나 강한 build로 확대하지 않음. 건반을 불필요하게 계속 교체할 필요도 없음. X05/X06. | SRC-0074, SRC-0076 |
| OPT-F05 마무리·인접 곡 연결 | 마지막 음형/남길 성부/잔향을 다음 곡의 첫 사건과 함께 검토하는 편곡 선택. | restrained ending, intentional final phrase and tail | 실제 경계의 클릭·조성 관계·음량·잔향은 음원 확보 후 확인. 자동 무봉제 루프/매끄러운 연결이 보장된 표현 아님. X04/X06. | SRC-0076, SRC-0074 |

## 조합해 볼 수 있는 방향

다음 네 조합은 자료에서 그대로 발견한 레시피가 아니라 **역할이 겹치지 않도록 만든 가상 조합**이다. 곡/출력/성공 사례 번호나 제작 이력으로 등록하지 않는다. 어느 조합도 실제 소리 합격은 아니다.

| 가상 조합 | 공통 청감 안의 역할 분담 | 지속되는 구별점·도입 | 충돌 점검 |
|---|---|---|---|
| A: I02+I09, R01/R05, H03, M01 | Rhodes는 짧은 질문, 업라이트는 박과 끝의 응답. 타악기는 뒤에 둠 | 짧은 하행 질문과 저음 응답 관계를 본문에서도 유지. 처음부터 조용한 관계가 드러나는 F01 | 저역 화음/업라이트 겹침, 벨 같은 반복 시작, 모든 박의 동시 발음 |
| B: I03+I10, R03, H01/H06, M02 | 기타의 짧은 화음 응답과 성긴 베이스 지지 | 긴-짧은 리듬/약박의 빈자리, 두 화음의 머무는 시간 차이. F02의 짧은 픽업 | 기타 탄현의 선명함, sub 과다, 밀집 아르페지오. A와 악기명만 다른 패턴이면 수정 |
| C: I01+I05, R01, H02/H07, M03 | 피아노 화성과 클라리넷의 짧은 답을 교대 | 고정 공통음/작은 내성 이동과 악기 간 문장 교대가 본문에 남는 F04 | 같은 음역 동시 연주·긴 클라리넷 솔로·키/페달/숨 소음, 높은 공통음의 반복 |
| D: I08+I07, I09 또는 I10 선택, H04 검토, F03 | pad는 화성, 제음한 비브라폰은 간헐 응답, 저음 담당은 구분 | 지속과 짧은 타격의 관계를 처음과 본문에서 유지 | pad/페달/비브라폰의 누적 잔향, 금속성 어택, 페달과 바뀐 화음의 긴장 |

표의 '+'는 모두 동시에 계속 연주하라는 뜻이 아니다. 이 조합들을 최종20곡 구성으로 확정하지 않았다.

## 호환·충돌 목록

아래 X항목은 새 탈락 기준이 아니라 기존 T01~T08·D02/D06·회수 원본에 따른 조합 점검 위치다.

| ID | 충돌/오해 | 확인과 처리 | 근거/연결 |
|---|---|---|---|
| X01 | 업라이트·sub·kick·저역 화음의 겹침 | 저음 주역/보조의 담당, 동시 발음 위치, 음 길이를 정하고 한꺼번에 남는 소리를 점검한다. 따뜻함을 이유로 저역을 계속 추가하지 않는다. | SRC-0060, SRC-0063 |
| X02 | 또렷한 시작·높은 상성부·응답의 과밀 | 음역·발음·밝음·전면 크기·반복 노출을 따로 기록한다. 'Rhodes/felt/플루트라서 부드럽다'고 통과시키지 않는다. | SRC-0001, SRC-0052, SRC-0053, SRC-0057 |
| X03 | 소음에 기대는 질감 또는 원본 제외와 충돌 | felt/키/페달의 기계음, 지속 마찰음, 브러시 쓸기를 확인한다. 브러시 snare를 '조용한 드럼'이라는 이유로 회수 원본의 snare 금지에서 예외 처리하지 않는다. | SRC-0052, SRC-0053, SRC-0062, SRC-0008 |
| X04 | 지속/잔향의 누적 | pad·비브라폰·업라이트·페달음이 다음 화음/다른 성부를 가리는지 본다. 짧게 할 대상과 남길 대상을 역할별로 정한다. | SRC-0058, SRC-0059, SRC-0060, SRC-0063 |
| X05 | 이름만 바뀐 복제 | 악기·키·BPM·첫 사건의 변경 외에 본문에서도 남는 음형/리듬/화성/역할 차이가 있는지 가장 유사한 후보와 비교한다. | SRC-0073, SRC-0074, SRC-0075 |
| X06 | 차이를 만들다 낮은 에너지를 잃음 | 빠른 솔로·촘촘한 드럼·큰 필/빌드·드롭·긴 도입 등 회수 원본/02와 충돌하는 방향을 확인한다. 작은 역할 변화와 전체 에너지 상승을 구별한다. | SRC-0008, SRC-0064, SRC-0076 |
| X07 | 화성 이름이 안정감을 보장한다는 단정 | 모드의 중심음, 페달과 위 화음의 동시음, 색채음/전위를 실제 설계에서 대조한다. 'maj7=항상 따뜻함'·'단조=항상 먹먹함'을 쓰지 않는다. | SRC-0068, SRC-0070, SRC-0072, SRC-0078 |
| X08 | 악기/음역/음량 조정만으로 R22 해결 선언 | 높은 음 자체의 일괄 금지·중저역 과밀·단순 음량 감소를 해결 공식으로 만들지 않는다. 단곡의 노출과 곡 간 누적/1시간 확인을 별도로 남긴다. | SRC-0001; 02의 R22 / 06의 T08 |
| X09 | 음악 표현과 모델 동작을 같은 것으로 취급 | swing·half-time·음역·시간 표현의 음악적 의도와 실제 저장 입력/출력 반영을 구별한다. 계정에 없는 조절 노브·정확한 비율·초 단위 구현을 만들지 않는다. | SRC-0064, SRC-0067, SRC-0045 |

## 다음 작업자가 적용할 순서

1. 02의 공통 목표·R22와09의 회수 원본/제외를 읽고,11의 실제 사례에서 무엇이 미확인인지 함께 확인한다.
2. 이번에 만들 차이를 '본문에서도 유지되는 연주 관계'로 적는다. 악기/키/BPM 이름 차이만 적지 않는다.
3. 필요한 역할별 OPT를 고르고 음역·발음·지속·밀도/쉼을 적는다. 선택한 악기/패턴을 전곡 공통 의무로 만들지 않는다.
4. 조합의 X충돌, 원본 Exclude, 가장 비슷한 다른 후보와의 구별점을 대조한다. 도입 차이와 지속되는 차이를 각각 남긴다.
5. P4에서 어떤 조건을 고정하고 무엇을 바꿔 볼지, 실패/미판정은 무엇인지 정한다. 실제 입력은 이후 D03/P6에서 Style·필요 구조·Exclude·설정을 통합해 작성한다.
6. 승인 기준/실제 출력이 없으면 D05/D07을 보류한다. 실제 청취와 누적 확인은 음악적 설계 판정과 별도 기록한다.

## 질문별 제출 판정과 남은 범위

| 질문 | 이번 D02 음악 자료 범위 | Suno/청감 범위 |
|---|---|---|
| Q08 | 악기군·역할·발음/지속·음역·위험·표현·근거·조합 연결 READY | v6-mini 악기/발음 반영, 개별/누적 편안함 UNVERIFIED |
| Q09 | 템포/분할/강조·베이스 관계·드럼 재료의 유추/저역 충돌 READY | swing/half-time/음 길이의 정확한 구현·목표 에너지 UNVERIFIED |
| Q10 | 진행·전위/보이싱·화음 변경·페달/모드·음형/쉼·충돌 READY | 특정 코드/전위/중심음의 정확한 출력 반영 UNVERIFIED |
| Q11 | 첫 사건·지속되는 개성·작은 역할 변화·마무리/인접 곡 점검 READY | 실제 시간 배치·곡 간 차이·연결 경계 UNVERIFIED |

**P3의 음악 자료 조사와 D02 선택지 정리는 제출 가능한 상태다.** 이 범위를 마치고 다음은 P4의 근거 통합·비교 계획으로 진행한다. P1의 계정/한도와 P2의 효과 공백은 유지하며 그 단계 전체의 통과 이벤트를 기록하지 않는다. 실제 생성·업로드·크레딧 사용은 수행하지 않았다.

1시간 동안 어떤 건반이 거슬리는지를 보편적으로 증명한 자료는 확보하지 못했다. SRC-0001의 음색 차이 연구, 악기 제작사의 특성 설명, 사용자 본인의 피로 우려를 서로 다른 근거로 유지한다. 현재 승인 음원·실제 청취가 없어도 이번 음악 선택지/비교 계획 작성은 가능하며, 장시간 합격은 보류한다.

## 출처와 기록 위치

SRC-0001은 기존에 등록된 Caclin et al.(2005) 음색 지각 연구로 재사용했다. 아래는 이번 새 출처다. 확인한 위치·좁은 사실·AI 적용 해석·접근 한계는03의 각 SRC가 정본이다.

- [SRC-0052: NOIRE Manual](https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/NOIRE_Manual.pdf) — Native Instruments
- [SRC-0053: Rhodes V8 Owner’s Manual v3](https://download.rhodesmusic.com/assets/RHODES-V8PRO/Rhodes%20V8%20Manual%20v3.pdf) — Rhodes Music
- [SRC-0054: Classical guitars are great for this](https://www.yamaha.com/en/musical_instrument_guide/classical_guitar/mechanism/mechanism002.html) — Yamaha Corporation
- [SRC-0055: Violin: sul tasto / sul ponticello](https://www.vsl.co.at/academy/strings/violin) — Vienna Symphonic Library
- [SRC-0056: Clarinet in Bb](https://www.vsl.co.at/academy/woodwinds/clarinet) — Vienna Symphonic Library
- [SRC-0057: Concert flute](https://www.vsl.co.at/academy/woodwinds/concert-flute) — Vienna Symphonic Library
- [SRC-0058: Vibraphone](https://www.vsl.co.at/academy/percussion/vibraphone) — Vienna Symphonic Library
- [SRC-0059: Live Instrument Reference, Live 12](https://www.ableton.com/en/manual/live-instrument-reference/) — Ableton
- [SRC-0060: Double bass](https://www.vsl.co.at/academy/strings/double-bass) — Vienna Symphonic Library
- [SRC-0061: Bass drum](https://www.vsl.co.at/academy/percussion/bass-drum) — Vienna Symphonic Library
- [SRC-0062: Snare drum: wire brushes](https://www.vsl.co.at/academy/percussion/snare-drum) — Vienna Symphonic Library
- [SRC-0063: What Is Frequency Masking?](https://www.izotope.com/community/blog/what-is-frequency-masking) — iZotope
- [SRC-0064: Beat and tempo](https://learningmusic.ableton.com/make-beats/beat-and-tempo.html) — Ableton
- [SRC-0065: Make basslines](https://learningmusic.ableton.com/make-basslines/make-basslines.html) — Ableton
- [SRC-0066: Syncopation in pop/rock music](https://openmusictheory.github.io/syncopation.html) — Open Music Theory, 2022 사이트
- [SRC-0067: Swing Rhythms](https://viva.pressbooks.pub/openmusictheory/chapter/swing-rhythms/) — Megan Lavengood / Open Music Theory
- [SRC-0068: Inversions](https://learningmusic.ableton.com/advanced-topics/inversions.html) — Ableton
- [SRC-0069: Voicings](https://learningmusic.ableton.com/advanced-topics/voicings.html) — Ableton
- [SRC-0070: Modes](https://learningmusic.ableton.com/advanced-topics/modes.html) — Ableton
- [SRC-0071: Harmonic Rhythm](https://musictheory.pugetsound.edu/mt21c/HarmonicRhythm.html) — Robert Hutchinson / Music Theory for the 21st-Century Classroom
- [SRC-0072: Pedal Point](https://musictheory.pugetsound.edu/mt21c/PedalPoint.html) — Robert Hutchinson / Music Theory for the 21st-Century Classroom
- [SRC-0073: Foundational Concepts for Phrase-Level Forms](https://viva.pressbooks.pub/openmusictheory/chapter/foundational-concepts/) — John Peterson / Open Music Theory
- [SRC-0074: The Cultural Significance of Timbre Analysis](https://www.mtosmt.org/issues/mto.20.26.3/mto.20.26.3.lavengood.html) — Megan Lavengood / Music Theory Online 26(3), 2020
- [SRC-0075: Ride variations](https://learningmusic.ableton.com/make-melodies/ride-variations.html) — Ableton
- [SRC-0076: Play with song structures](https://learningmusic.ableton.com/song-structure/song-structure.html) — Ableton
- [SRC-0077: Harmony in pop/rock music](https://openmusictheory.github.io/popRockHarmony.html) — Open Music Theory, 2022 사이트
- [SRC-0078: Seventh chords](https://learningmusic.ableton.com/advanced-topics/seventh-chords.html) — Ableton
