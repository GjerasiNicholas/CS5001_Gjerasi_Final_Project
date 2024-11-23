import subprocess
import os
import sys


def ffmpeg_conversion(audio_files: list, container: str,output_name: str):
    '''
    Goal of this function is to get a list of audio files that were selected from the GUI and convert them to a
    specific container type that was also selected from a drop-down on the GUI. Input audio files can be almost
    any format but the containers are only a select few. We dont need to account for someone trying to make an audiobook
    using only lossless audio because thats wasteful of memory.

    Container Options:
        -MP3
        -M4A
        -M4B
    
    
    '''

    with open("mylist.txt","w") as file:
        for i in audio_files:
            file.write(f"file \'{i}\' \n")

    if container == "mp3" or container =="m4a" or container =="m4b":
        subprocess.run([

            "ffmpeg","-y", "-f","concat","-safe","0","-i","mylist.txt","-c","copy",f"Output/{output_name}.{container}"

        ])
    else:
        raise ValueError("You have entered an invalid container...")
        


ffmpeg_conversion(["Audio/artofwar.m4a","Audio/artofwar1.m4a"],"m4a","bigfunctionoutput")