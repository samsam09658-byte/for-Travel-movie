import os
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, ColorClip

title = os.environ.get("ISSUE_TITLE", "여행 정보")
body = os.environ.get("ISSUE_BODY", "즐거운 여행 되세요.")
text = f"{title}\n\n{body}"

# 1. 음성 생성
tts = gTTS(text=f"{title}. {body}", lang='ko')
tts.save("voice.mp3")

# 2. 숏폼 배경(세로형 1080x1920) 및 오디오 설정
audio = AudioFileClip("voice.mp3")
background = ColorClip(size=(1080, 1920), color=[30, 30, 30], duration=audio.duration)

# 3. 화면 자막 생성
txt_clip = TextClip(text, fontsize=60, color='white', size=(900, 1500), method='caption')
txt_clip = txt_clip.set_duration(audio.duration).set_position('center')

# 4. 영상과 자막, 음성 합성
video = background.set_audio(audio)
final_video = video.set_duration(audio.duration)

# 5. MP4 영상 파일로 저장
final_video.write_videofile("travel_short.mp4", fps=24, codec="libx264")
