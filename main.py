# Colorful VALORANT by b0kch01

import os, ctypes

# Disable quick-edit mode (pauses bot)
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

from pyfiglet import Figlet
from termcolor import cprint, colored
import colorama
import keyboard
import time


# Fix legacy console color
colorama.init()

cprint("Setting up...")
cprint(" - [¤] Windows", "green")
cprint(" - [¤] Imported Modules", "green")

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    cprint(" - [x] Please run as administrator", "red")
    input("[ ENTER ] to quit")
    exit(0)

def clear():
    os.system("cls")

# User Interface
f = Figlet(font="ogre")

bgs = ["on_red", "on_yellow", "on_green", "on_blue", "on_magenta"]

CACHED_TITLESCREEN = f"""
{ "".join([colored("  " + "COLORFUL"[i] + "  ", "grey", bgs[i % 4]) for i in range(8)]) }
{ colored(f.renderText("Valorant"), "red")  }
{ colored(" Created with ♥ by b0kch01!             ", "grey", "on_white") }
{ colored(" USE AT YOUR OWN RISK                   ", "grey", "on_yellow") }
"""

i = 0
colors = [
    "<enemy>",
    "<team>",
    "<system>",
    "<notification>",
    "<warning>"
]

colorMap = [
    "red",
    "blue",
    "yellow",
    "green",
    "magenta"
]

def goUp():
    global i
    i += 1
    render()

def goDown():
    global i
    i -= 1
    render()

def makeColor():
    time.sleep(0.05)
    keyboard.send("home")
    keyboard.write(colors[i % 5])
    keyboard.send("end")
    keyboard.send("backspace")
    keyboard.write("</>")
    keyboard.send("\n")


def render():
    global i
    clear()
    print(CACHED_TITLESCREEN)
    print("Color: " + colored(colors[i % 5], "white", "on_" + colorMap[i % 5]))

keyboard.add_hotkey("\\", makeColor)
keyboard.add_hotkey("up", goUp)
keyboard.add_hotkey("down", goDown)

try:
    render()
    print("Instructions are on https://github.com/b0kch01/ColorfulValorant")
    print("\nEnjoy! :)")
    keyboard.wait("up + down")
except KeyboardInterrupt:
    exit(0) 