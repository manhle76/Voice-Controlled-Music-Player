# Music Player Project
Created by Van Le — Honor Project

## Overview
This project is a voice-controlled music player built using Python. 
It can play MP3 files, recognize voice commands in English or Vietnamese, 
translate Vietnamese commands to English, and display a GUI with buttons, volume, song name, and time.

1) Features

- Play / pause music
- Next song/ previous song
- Volume up / Volume down
- Select a song by speaking its name
- Automatic Vietnamese → English translation
- Graphical interface with buttons, time, volume, name song and progress bar

2) Requirements

- Python 3.10 or newer
- Libraries:
  - pygame
  - mutagen
  - pyttsx3
  - speechrecognition
  - googletrans==4.0.0-rc1
  - pyaudio

3) Installing Python

1)Go to https://www.python.org/downloads/ (should download version older than 3.13)
2)Click “Download Python 3.x.x” for your system (Windows, macOS, or Linux)
3)Open the downloaded file to start installation
4)Check “Add Python 3.x to PATH”
5)Click Install Now and wait until it finishes
6)Open Command Prompt (Windows) or Terminal (Mac/Linux) and type:
  python --version
You should see something like:
  Python 3.11.2
Python is now installed and ready to use.

4) Installing Required Libraries

Open terminal or command prompt and run:

pip install pygame mutagen pyttsx3 SpeechRecognition googletrans==4.0.0-rc1 pyaudio

On Windows, PyAudio may fail. Download the correct .whl file from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/
Then install it:
pip install filename.whl

verify installation
   python -m pip show pygame mutagen pyttsx3 speechrecognition googletrans pyaudio
If information about each library appears, it means they are installed correctly.

5) Running the Program

1. Make sure all project files are in the same folder
2. Add your MP3 files into a folder "Songs"
3. Open terminal / command prompt in the project folder
4. Run:

python play_music.py

6) Common Issues

- Microphone not detected → check PyAudio installation
- API unavailable → check internet connection
- No speech detected → speak clearly and closer to microphone
