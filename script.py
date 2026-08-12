import os
from gtts import gTTS

# 이슈 제목과 내용을 가져와 음성 파일(mp3)로 만드는 기본 코드입니다.
title = os.environ.get("ISSUE_TITLE", "여행 정보")
body = os.environ.get("ISSUE_BODY", "즐거운 여행 되세요.")

text = f"{title}. {body}"
tts = gTTS(text=text, lang='ko')
tts.save("travel_short.mp3")
print("음성 파일 생성 완료!")
