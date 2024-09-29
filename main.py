# -*- coding: utf-8 -*-
# If using Python 2 (do at your own risk), you may need to remove all ASCII art
# Python 2 is not officially supported, compatibility mode is not 100% accurate
import sys
import os
compmode = 3
if sys.version_info.major == 2:
    if raw_input("Python 2.x detected! Are you sure you want to continue? Only do this at your own risk and prepare to lose data. Type \"Yes, I agree!\" to continue: ") == "Yes, I agree!":
        print("Okay, continuing in partial Python 2 compatibility mode...")
        compmode = 2
    else:
        sys.exit(1)
elif sys.version_info.major != 3:
    if input("Python 3.x not detected! Are you sure you want to continue? Only do this at your own risk and prepare to lose data. Type \"Yes, I agree!\" to continue: ") == "Yes, I agree!":
        print("Okay, continuing with Python 3 syntax...")
        compmode = 4
    else:
        sys.exit(1)

print("Welcome to MonoFS!")
if compmode == 3:
    print("███╗░░░███╗░█████╗░███╗░░██╗░█████╗░███████╗░██████╗\n████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔════╝\n██╔████╔██║██║░░██║██╔██╗██║██║░░██║█████╗░░╚█████╗░\n██║╚██╔╝██║██║░░██║██║╚████║██║░░██║██╔══╝░░░╚═══██╗\n██║░╚═╝░██║╚█████╔╝██║░╚███║╚█████╔╝██║░░░░░██████╔╝\n╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═════╝░")
    print("\n╔══╗╔═══╦════╦═══╗\n║╔╗║║╔══╣╔╗╔╗║╔═╗║\n║╚╝╚╣╚══╬╝║║╚╣║─║║\n║╔═╗║╔══╝─║║─║╚═╝║\n║╚═╝║╚══╗─║║─║╔═╗║\n╚═══╩═══╝─╚╝─╚╝─╚╝")
else:
    print(" __  __                   _____ ____                          \n|  \\/  | ___  _ __   ___ |  ___/ ___|                         \n| |\\/| |/ _ \\| \'_ \\ / _ \\| |_  \\___ \\                         \n| |  | | (_) | | | | (_) |  _|  ___) |                        \n|_|__|_|\\___/|_| |_|\\___/|_|   |____/ _ _     _ _ _ _         \n / ___|___  _ __ ___  _ __   __ _| |_(_) |__ (_) (_) |_ _   _ \n| |   / _ \\| \'_ ` _ \\| \'_ \\ / _` | __| | \'_ \\| | | | __| | | |\n| |__| (_) | | | | | | |_) | (_| | |_| | |_) | | | | |_| |_| |\n \\____\\___/|_| |_| |_| .__/ \\__,_|\\__|_|_.__/|_|_|_|\\__|\\__, |\n                     |_|                                |___/ \n\n")
print("MonoFS Beta - s0-290924-2-pub")
#print("This version is not to be released publicly! You may encounter loss of data.")
if compmode == 3:
    input("Press Enter (Return) To continue...")
elif compmode == 2:
    raw_input("Press Enter (Return) To continue at your own risk...")
else:
    print("Unknown compatibility mode " + str(compmode) + " detected!")
    sys.exit(1)
if compmode == 3:
    filename = input("Input file path of MonoFS image: ")
elif compmode == 2:
    filename = raw_input("Enter the file path to a copy of a MonoFS image\nMake sure to make a backup of it or use Python 3: ")
else:
    input("Unknown compatibility mode! Use Python 3.")
    sys.exit(1)
try:
    with open(filename, mode='rb') as file:
        filecontents = file.read()
        def readfile():
            print("hi")
    if len(filecontents) == 8200:
        readfile()
    else:
        if sys.version_info.major == 3:
            if input("The file length is not equal to 8200 bytes. Do you want to format it or attempt to read? Type \"I want to format!\" to format the image or type \"Read\" to read the image: ") == "Read":
                readfile()
            else:
                print("hgfhodfgh")
        else:
            print("The file length is not equal to 8200 bytes. Formatting images and reading images not 8200 bytes long on unsupported Python versions has been blocked to prevent data loss.")
            sys.exit(1)
except IOError:
    print("The file is not found. Is the file path correct?")
    sys.exit(1)
except Exception as excep:
    print("There has been an error.\nError message: " + str(excep))
    if compmode == 3:
        print("Quitting...")
        sys.exit(1)
    else:
        print("Have you tried using Python 3?\nQuitting...")
        sys.exit(1)