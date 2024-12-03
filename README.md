## Sources

List of documentation, articles, and other guides that I used to help me put this project together:

- [One](https://phoenixnap.com/kb/ffmpeg-mac)
- [Two](https://docs.pysimplegui.com/en/latest/documentation/module/elements/)
- [Three](https://windowsloop.com/install-ffmpeg-windows-10/)
- [Four](https://trac.ffmpeg.org/wiki/CompilationGuide/macOS)
- [Five](https://docs.python.org/3/library/subprocess.html#subprocess.run)
- [Six](https://trac.ffmpeg.org/wiki/Concatenate)


## Instructions


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
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

The largest challenge by far was the realization that the audio manipulation library "PyDub" did not support audiobook files (m4a/m4b). This project was going to be significantly more straightforward as the PyDub library wrapped ffmpeg commands in very neat methods. When I figured out this would not work I had to learn how to trigger my prompts to hit the terminal directly. 

This is where the subprocess library came into play. I had to learn this library and re-start my project from the ground up basically. I think my main challenge with this library was the snytax of my code as it had to be formatted perfectly or the commands would not execute. 

A smaller challenge, yet still quite annoying, was learning PySimpleGUI. This library is not particularly difficult but the challenge was learning the syntax and setting up my GUI the way that the creators of the library intended. Documentation was quite solid but sometimes lacked detail on certain aspects; I found the lack of documentation on getting values input from layout keys to be quite difficult at first to understand.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
