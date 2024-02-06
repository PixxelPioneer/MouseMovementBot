MouseMovementBot - Python Script

Description



The move.py script is designed to automate mouse movements on your screen. 
It randomly moves the mouse cursor to different positions within a specified range, 
providing a basic demonstration of mouse automation.

Features



Randomized mouse movements within a 500x500 pixel range.
Logs each movement with time and coordinates.
Safe to use with a built-in mechanism to stop the script with user interruption.

Requirements

Python 3.10

PyAutoGUI


This script depends on PyAutoGUI, a cross-platform GUI automation Python module. 
PyAutoGUI allows the script to control the mouse and keyboard to automate 
interactions with other applications.


Installing Dependencies
Ensure you have Python 3.10 installed, then install PyAutoGUI using pip:


pip3 install pyautogui

Usage

To run the script, navigate to the directory containing mouse_movement.py and run the
following command in your terminal:


python3 move.py



Safety Feature


The script includes a failsafe feature. Quickly moving the mouse to
any corner of the screen will stop the script immediately.
