## Sources

List of documentation, articles, and other guides that I used to help me put this project together:

- [One](https://phoenixnap.com/kb/ffmpeg-mac)
- [Two](https://docs.pysimplegui.com/en/latest/documentation/module/elements/)
- [Three](https://windowsloop.com/install-ffmpeg-windows-10/)
- [Four](https://trac.ffmpeg.org/wiki/CompilationGuide/macOS)
- [Five](https://docs.python.org/3/library/subprocess.html#subprocess.run)
- [Six](https://trac.ffmpeg.org/wiki/Concatenate)


# Final Project Report

* Student Name: Nicholas Gjerasi
* Github Username: GjerasiNicholas
* Semester: Fall2024 
* Course: 5001



## Description 

The inspiration for this project came from the very large collection of books-on-tape that my parents have which I am going through currently. When I rip these CDs, typically I end up with multiple files which I then need to manipulate via the terminal using ffmpeg which can get kind of annoying and I always forget the commands between books.

This program allows me to never have to go online and re-learn the ffmpeg commands as they are all baked into a simple script and GUI. When you run the program, a window pops up asking you to select any number of audio files from a directory on your computer. It will then trigger my ffmpeg_conversion function automatically.

## Key Features

I think one of the key features of this project that I would like to focus on is how it is automating what is normally a pretty annoying process into a super streamlined flow. What would normally take 5-10 minutes now only takes about 1. The program checks for errors in your file selection, auto-writes a list of the files and their directories, and triggers ffmpeg using the subprocess library's functionality. This actually executes things directly in the terminal!

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

Running the program is straightforward. The steps are as follows:
  1. Open the Audiobook_GUI.py program
  2. Run the python file
  3. Enter a book name
  4. Click "Browse"
  5. Select your audio files and make sure the chapters are in the correct sequence
  6. Click "Run"
  7. In the "Outpu" directory, there should now be a complete audiobook!

## Installation Instructions

**Libraries Required**

  - PySimpleGUI | GUI creation
  - Run ```pip install PySimpleGUI``` to install library.
  - This library will require you to create an account and get a key. This is totally free. 
  - Upon running the code you will be prompted to input your key. Once this is done you will never have to input it again.
- PyAudio | Audio Playback...Not 100% required but if playing from IDE this will need to be installed.
  - Run ```pip install PyAudio``` to install library.


**FFMPEG: A free and open sources software that is intended to handle and manipulate video, audio, and other multimedia file types**

  -Homebrew (OSX only) | Software manager for OSX | https://brew.sh/
    -Install with following command: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    -Upon install, brew will give you 3 commands in terminal that you will need to copy, paste, and then run. These will add homebrew as a PATH variable and ensure that every terminal instance you open has BREW applied.
    -Run `brew install ffmpeg` in terminal to install FFMPEG on your mac. This will set ffmpeg as a PATH variable which will allow for it to be accessed in any terminal by entering just "ffmpeg".

  -Windows FFMPEG Install:
    -ffmpeg |  https://www.gyan.dev/ffmpeg/builds/
    -Download the most recent breanch of ffmpeg (ffmpeg-git-essentials.7z)
    -Unzip the folder and extract it to your c: drive (or whatever your native base drive is)
    -ffmpeg is now installed, to make life easier we will set it as a PATH variable. This is best shown with screenshots. This source (https://techtactician.com/how-to-install-ffmpeg-and-add-it-to-path-on-windows/) has a detailed explaination with screenshots. Begin at step 4 as steps 1-3 were completed above.

## Code Review

```python 

subprocess.run([

        "ffmpeg","-y", "-f","concat","-safe","0","-i","mylist.txt","-c","copy",f"Output/{output_name}.{container}"

    ])

```

-This snippet of code is what allowed me to overcome the issue of PyDub libary not supporting common audiobook formats. The ```run```function in the subprocess library allows me to execute commands that would normally have to be typed out in the terminal. All I needed to do was format it in such a way that allowed me to dynamically set some of the arguments based on what was passed by the user. This is why I use an f-string for the final argument passed because we want to make sure the name and container are dynamic. The ```Output/``` is just so I can ensure it always goes into the right directory after processing is complete.


```python

layout = [  [sg.Text("Select Files to Concatenate (Acceptable types: mp3, m4a, m4b, aac)")],
            [sg.Text("Enter Book Name:"),sg.Input(key ="-TITLE-",size=(20,10))],
            [sg.LBox([], size=(100,20), key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Run'), sg.Button('Exit')]  
        ]

```
This snippet of code was more annoying than complicated to create. This is the layout of our GUI and within that layout, I had to figure out from PySimpleGUI's documetation how we could store information passed by the user and reference it later (this is why we use the "key" variable). The most difficult part of this entire setup was getting the files selected by the user to actually populate within the UI. The code would work just as intended but seeing the selected files in the UI was a key part of the user validating that they had selected the correct files. The solution to this was found deep in their documentation. This required the use of "enable_events=True" to work properly; with this command in the layout, it allowed the storage of the files selected and would show them properly when initiating the UI.


```python

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

```

This is my error handling code. This will prevent, in most situatiions, errors from being spit out by ffmpeg. These are likely to be the most common errors from a new user:
  1. Forgetting to put in a name for the audiobook
  2. Using an audio format that is not acceptable by ffmpeg
  3. Trying to merge different audio types


### Major Challenges

The largest challenge by far was the realization that the audio manipulation library "PyDub" did not support audiobook files (m4a/m4b). This project was going to be significantly more straightforward as the PyDub library wrapped ffmpeg commands into very neat functions. When I figured out this would not work I had to learn how to trigger my prompts to hit the terminal directly. 

This is where the subprocess library came into play. I had to learn this library and re-start my project from the ground up basically. I think my main challenge with this library was the snytax of my code as it had to be formatted perfectly or the commands would not execute. 

A smaller challenge, yet still quite annoying, was learning PySimpleGUI. This library is not particularly difficult but the challenge was learning the syntax and setting up my GUI the way that the creators of the library intended. Documentation was quite solid but sometimes lacked detail on certain aspects; I found the lack of documentation on getting values input from layout keys to be quite difficult at first to understand.


## Example Runs

I documented running this project in a youtube video! This is the simplest way to make sure the reviewer of this project is actually able to see that it does, in fact, work. Following the README should get you to a state where it works and I have tested this on 3 different computers downloading from GIT and it worked fine. The link to this video has been posted on a throwaway youtube account and the link is below!

[VIDEO OF DEMO](https://youtu.be/tUEc0Z_jq98)

## Testing

Due to the nature of my runs it is a bit difficult to record my tests as audio from many of my audiobooks is copywrited and I do not want to publish them on GitHub and get a strike on my account. I did however include a directory called "tests" where I had my dummy files that I used to get a base understanding of how I would implement this code.

The most important of the two testing files is the commandprompt Tests file. I took notes for every particularly important line of code. This was very much an iterative process and you will notice I dropped a few of the libraries (os / sys) from my final code as I found them unnecessary at the end. These libraries were very helpful for me to figure out what was going on and why my code was not running as expected. This was similar to homework 8 I believe where directories are quite particular about being referenced properly and I used the os library a lot to help me figure out where I was at all times. This test file follows my logic flow and tests in a linear manner.

I do not have all my tests recorded for my output file "mylist.txt" as the entire purpose of the file was to write over itself each time you create an audiobook as that is the driver of the ffmpeg processes runs.

My GUI testing was mostly done in the final Audiobook_GUI.py file and I grew that file slowly adding more and more functionality. You can, however, see the seed of my research and testing in the "GUI Testing.py" file in the same directory as my commandprompt testing file.


## Missing Features / What's Next

Something that I would like to do is figure out a way to get a loading bar in place within the GUI. ffmpeg does show its processes within the console but I thought it would be far too big of a lift to figure out how to parse everything it is doing and translate that into a loading bar. I think this would be a nice touch though.

Another thing I would like to implement is figuring out a way for the converter to send the audiobook to my phone directly somehow. I think this could be done via my FTP server and have the application auto-send whatever file was loaded into the output directory to my FTP, then purge it upon it being successfully uploaded.

One final addition that I would like is to make this entire program an executable so people dont have to download it from GitHub, read my README.md, get ffmpeg, and after all that, run the program. Wrapping it up simply for laypeople to use would be a very nice cherry-on-top. I am not familiar with how this is done so I will leave my program as it stands.

## Final Reflection

I came into this course with a fair amount of experience in Java from a course I took over a few months. I think that did assist me with some of the earlier projects where I felt I knew the content but then homework 4, jailbreak, came along and really made me realize how little I knew. I think throughout the course, I was pretty solid with syntax and picking things up regarding the actual mechanics of coding but what I think my personal biggest takeaway from this class, for which I am very thankful for, is how to approach problems. I found frequently find myself getting very frustrated with assignments that I could not get a solution for on the spot. I learned very quickly that getting frustrated and upset is not the way to resolve coding problems and overcome these challenges. I slowly altered my approach and made it a focus in this course to go into every homework with an open mind and understand that no one was expecting me to get an answer immediately and that instead, it is meant to be a challenge that I need to piece a solution for together.

This course has also drilled into my mind the importance of breaking down a problem into tiny, doable steps. Another issue I had going into this course was I wanted to tackle the assignment in the most "efficient" manner possible which would lead me, in later assignments, to hit brick walls where my approach that I thought would be fastest, ended up taking me way more time than if I had broken it up. I have tried to always see if I can find a subset of problems within a larger problem to tackle as small wins motivate me a lot and keep me going; hitting a brick wall is never fun and can get me to spin my gears and just get frustrated which, as I mentioned above, does NOT help the coding process.

Overall, I would say that this course not only taught me python, but most importantly, it taught me how to think like a computer scientist which was something that I was very much missing. I am now able to calmly approach problems and hiccups in my code, analyze the situation, take a step back, and begin my debugging processes without feeling like I failed entierly. I still have a long way to go and often catch myself still trying to bite off more than I can chew but I think this course, at the end of the day, gave me the ability to actually start recognizing my bad CS habits and begin the journey of fixing my approach to coding and problem solving in general.