import subprocess

def ffmpeg_conversion(audio_files: list, output_name: str):
    '''
    Goal of this function is to get a list of audio files that were selected from the GUI and convert them to a
    specific container type that was also selected from a drop-down on the GUI. Input audio files can be almost
    any format but the containers are only a select few. We dont need to account for someone trying to make an audiobook
    using only lossless audio because thats wasteful of memory.

    Container Options:
        -MP3
        -M4A
        -M4B
        -aac
    
    Args:
        audio_files (list): list of directory strings: ['/Users/nickgjerasi/Downloads/Book Directory - Test Audio/Test Audio - 001.mp3','/Users/nickgjerasi/Downloads/Book Directory - Test Audio/Test Audio - 002.mp4']
        output_name (str): name of the book : "Dune"

    Returns:
        mylist.txt - file with a list of directories for each file in the audiobook formatted in exactly the way ffmpeg requires for successful conversion
        {output_name}.mp3/m4a/m4b/aac - final audiobook file concatenated properly
    '''
    acceptable_files = ["mp3","m4a","m4b","aac"]

    #Gets the container of the first file. All files must share formate so this will serve as a check.
    container = audio_files[0][-3:] 

    if output_name == "" or output_name == None:
        raise ValueError("Please enter a valid Title!")

    for i in audio_files:
        if not i[-3:] in acceptable_files:
            raise ValueError(f'The only acceptable file types in this program are: {acceptable_files}')


    with open("mylist.txt","w") as file:
        for i in audio_files:
            if i[-3:] == container:
                file.write(f"file \'{i}\' \n")
            else:
                raise ValueError("You selected files of multiple types. Please keep your selection to files of the same type.")

    subprocess.run([

        "ffmpeg","-y", "-f","concat","-safe","0","-i","mylist.txt","-c","copy",f"Output/{output_name}.{container}"

    ])

    