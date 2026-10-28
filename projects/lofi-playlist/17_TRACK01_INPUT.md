# 1번 곡 통합 입력 문안
문안1.0 / 2026-10-27 / TRK-000001 / PKG-000001
상태:UI_DRAFT_READY_COST_PENDING. 실제계정폼에1번문안입력·한도/옵션관찰완료. 비용/실행COMMIT은별도대기.

## 입력 전문
Title(작업용): 01_하행 질문과 늦은 저음 답

### Style
```text
Instrumental lo-fi hip hop, 64 BPM, 4/4, straight half-time feel, steady low energy. Small ensemble: softly played Rhodes with rounded attacks and restrained bell tone, warm round upright bass as the sole low-end voice, sparse soft low percussion far behind the music. Dark, muffled, warm tone with distinct notes and short controlled tails. F major; an eight-bar cycle of Fmaj7 for four bars, then Dm7 for four bars. Rhodes: a short three-note descending question on the downbeat, one full bar without keyboard, then a lower two-note answer. Leave real gaps between phrases. Upright bass answers briefly late in the empty bars; keep its notes separate from Rhodes attacks. Establish this relationship immediately and retain it throughout the main body. Every second cycle, omit the final Rhodes answer while the quiet pulse continues. Finish the Rhodes phrase first, then a short bass-root tail. About three minutes.
```

### Exclude
```text
vocals, scat, fast solo, drum fills, tempo changes, key changes, breakdown, build up, drop, bright, crisp hi-hats, sparkly, airy, bright cymbals, wide stereo, long intro, fast tempo, loud drums, punchy drums, snare, crisp snare, boom bap, trap, hard hitting kick, distorted drums, white noise, hiss, clipping
```

## 현재 화면 입력과 설정 확인 — SRC-0089 /2026-10-27

- 고급 새 곡 / 실제 선택 모델 v6-mini.
- Title:01_하행 질문과 늦은 저음 답, Style917/1000,Exclude308/1000 원문동일·무잘림.
- Lyrics빈칸, UI가빈가사를연주곡경로로안내함. 별도Instrumental토글조작없음.
- 기이함50(0~100),스타일영향50(0~100),다양성0(0~4).
- Max끔,길이Auto,개인화끔. 마법봉/보강미사용. 값변경없음.
- 현재위값을관찰한것이며최적설정으로검증한것이아님. 약3분은Style목표,실제길이값은Auto.
- 오디오/Persona/CustomModel참조없음.
- 생성버튼활성상태까지확인했으나누르지않음. 비용/생성허용범위·평가/전체반환기록을확정한후실행COMMIT.
- 현재 UI_DRAFT_READY_COST_PENDING. 실제제출/생성0.

## 설계 대조와 변경
64 BPM·F major·Fmaj7 4마디/Dm7 4마디·하행3음/한마디쉼/낮은2음·늦은업라이트답·격주기마지막답생략·Rhodes먼저종료/짧은근음꼬리를 반영했다.
원본 대비65→64BPM,업라이트+sub→업라이트단독,불특정짧은반복→질문/쉼/답,불특정maj7→4+4화성,brushed drums→작은저타악. 이는16의1번설계에따른새문안이며 원본09를수정하거나 TST-02A 단일변수시험을실행한것이아니다.
Exclude는09 회수 원본28항목과 문자/순서 동일. snare/boom bap을 몰래 완화하지 않았다.
Style917자/Exclude308자는 문자열 실측. 사용자 보고의 고급Style1,000자 이내에917자가 들어가며83자 여유다. 실제계정 Exclude한도1,000자와308자전문유지를 확인했다. Simple3,000자는 고급Style한도로 대신 쓰지 않는다.

## 검토·다음 행동
내용 검토: 둥근Rhodes/절제된밝기·실제쉼·단독저음·작은배경타악·지속본문관계·작은변화·종료가 서로 일치한다. Exclude전체와긍정지시의snare/sub/보컬충돌을대조했다.
실제 제출 후에는 작성/제출/표시Style과모든출력·설정을보존하고지시반영/목표청감/19번대비/누적노출/채택을따로기록한다.
다음은 비용/생성허용범위와 PKG-000001의 실행COMMIT 확정. 음악 기준을 다시 만드는 단계가 아니다.

## 근거
2026-10-27 기존SRC-0006(https://help.suno.com/en/articles/3161921 L9~18) 및SRC-0018(https://help.suno.com/en/articles/3726721 L9~18) 원문 재확인. Custom/Instrumental/Exclude의 공개 역할만 참고하며 실제 계정UI·한도·성공률을확인한것으로확대하지않음. 기존02/06/09/10/13/16 적용.

입력 한도 업데이트 근거:SRC-0088(2026-10-27 최신 사용자 정정). 음악문안1.0의Style/Exclude전문은 변경하지 않았다.

직접UI검토:SRC-0089. 가사한도5,000·Style1,000·Exclude1,000. 입력본문1.0은변경없고설정기록만보완했다.
