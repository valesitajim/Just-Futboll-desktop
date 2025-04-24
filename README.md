# Just-Futboll-desktop

## Overview
JustFootball desktop is a graphical desktop application built with Python and Tkinter, tailored for football enthusiasts. This GUI provides quick access to essential tools like a terminal, the Nano text editor, a graphical notepad, and a custom shell for JustFutball.
This app offers quick access to essential Unix/Linux tools through a graphical interface, it is designed to simplify and personalize your workflow with a football-inspired interface. It includes real-time clock functionality, clickable icons for tools, 

## Features
**Real-time digital clock**
**One-click access to system terminal**
**Integrated Nano editor launcher**
**Built-in notepad with save functionality**
**Our custom shell launcher (`justfutboll.sh`)**

##  Installation
1. Clone the repository:
bash
git clone https://github.com/yourusername/justfutball-desktop.git
cd justfutball-desktop

2. Run the main script:
python3 justfutball_gui.py

##⚠️ Make sure the required images that you choose (.png) are present in the same folder and that the shell script path is correctly set for your environment.
You can [download the stadium image here](./estadio.png) and use it as the background for the GUI.

## Dependencies
* Python 3.x
* Tkinter (GUI library)
* x-terminal-emulator (or equivalent terminal)
* Nano (CLI text editor)
* WSL with Ubuntu (for running the shell script in Windows)
## Installing Dependencies
## On Ubuntu/Debian-based systems:

sudo apt update
sudo apt install python3 python3-tk nano

## On Windows

- Install Python  
- Enable and configure WSL  
- Ensure your terminal emulator is accessible from Python using `subprocess`  
- Place your custom shell script (`justfutboll.sh`) in your WSL Ubuntu home directory  

## Lincense
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it. sed under the MIT License.

