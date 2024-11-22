from pydub import *
from pydub.playback import play

AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe"


book = AudioSegment.from_file("Audio/artofwar.m4a", format="m4a")

book.export("testingme.m4b", format="m4b")