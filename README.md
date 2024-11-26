# CS5001_Gjerasi_Final_Project

## Table of Contents
-[Sources Used](#sources)
-[Libraries](#Libraries)
-[Dependencies](#Dependencies)
-[Instructions](#Instructions)

## Sources

List of documentation, articles, and other guides that I used to help me put this project together:

- [One](https://phoenixnap.com/kb/ffmpeg-mac)
- [Two](https://docs.pysimplegui.com/en/latest/documentation/module/elements/)
- [Three](https://windowsloop.com/install-ffmpeg-windows-10/)
- [Four](https://trac.ffmpeg.org/wiki/CompilationGuide/macOS)
- [Five](https://docs.python.org/3/library/subprocess.html#subprocess.run)
- [Six](https://trac.ffmpeg.org/wiki/Concatenate)

## Libraries

Libraries that are required to be installed prior to running the code:

- PySimpleGUI | GUI creation
  - This library will require you to create an account and get a key. This is totally free. 
  - Upon running the code you will be prompted to input your key. Once this is done you will never have to input it again.
- PyAudio | Audio Playback...Not 100% required but if playing from IDE this will need to be installed.


## Dependencies

Any dependencies that are required to get this program working as intended:

-Homebrew (OSX only) | Software manager for OSX | https://brew.sh/
  -Install with following command: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
  -Upon install, brew will give you 3 commands that you will need to run. These will add homebrew as a PATH variable and ensure that every terminal instance you open has BREW applied.
  -Run `brew install ffmpeg` in terminal 

-ffmpeg | This is the open source engine that drives the audio manipulation capabilities of PyDub. Can be found here:  https://ffmpeg.org/download.html


## Instructions
