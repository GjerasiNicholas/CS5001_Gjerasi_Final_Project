from pydub import *
from pydub.playback import play

AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe"

audio = AudioSegment.from_file("Audio/ONE.mp3", format="mp3")

audio2 = AudioSegment.from_file("Audio/TWO.mp3", format="mp3")

audio3 = AudioSegment.from_file("Audio/THREE.mp3", format="mp3")

book = AudioSegment.from_file("Audio/artofwar.mp4", format="mp4")

concat_audio = audio + audio2 + audio3

#book.export("crazyfrog.m4a",format = "m4a")