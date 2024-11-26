import subprocess
import os
import sys

pathway = "Audio/artofwar.m4a"
file_list = ["Audio/artofwar.m4a","Audio/artofwar1.m4a"] # Start thinking about how we can make this part ALWAYS give full path, not relative path.

with open(pathway,'r') as file:
    print(os.path.splitext("Audio/artofwar.m4a")[1] == ".m4a") #This splits the file name into the file name and then the extension WITH period

    print(f"The File Path is {file.name}") #Prints way to get to the file

    print(f"The Directory the file is in specifically is {os.path.dirname(file.name)}") #Specific name of the directory
    

with open("Output/mylist.txt","w") as file:
    for i in file_list:
        full_path = os.path.abspath(i) #Gets the absolute path. Relative paths are tricky and annoying.
        file.write(f'file \'{full_path}\' \n')



print(f"Current Working Directory {os.getcwd()}") #What directory are we executing things in rn?

extension = ".m4b"
subprocess.run([

    "ffmpeg","-y", "-f","concat","-safe","0","-i","Output/mylist.txt","-c","copy",f"Output/concatOutput{extension}"

])


subprocess.run([

    "ffmpeg", "-y",
    "-i", "Audio/artofwar.m4a",
    "-c:a", "libmp3lame",
    "-ab", '190k',
    "Output/outputfrompython.mp3"
]) 
# The "-y" means that ffmpeg will always overwrite instead of prompting me to do so in the console.
# We use just "ffmpeg" not "C:/ffmpeg/bin/ffmpeg.exe" because we set the PATH variable for ffmpeg so we dont need the path.
