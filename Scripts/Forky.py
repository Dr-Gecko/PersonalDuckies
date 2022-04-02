import time
import board
import usb_hid
import sys
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
payload = 0
payload_delivered = 0
time.sleep(2)
print("Ready.")
pause = 0.25
def terminal():
    kbd.press(Keycode.GUI)
    kbd.release_all()
    time.sleep(pause)
    layout.write("notepad")
    time.sleep(pause)
    kbd.press(Keycode.ENTER)
    time.sleep(pause)
    kbd.release_all()
    layout.write("   ____          ...    ..      ..       .             _____ \n")    
    layout.write("  / ___|       ..,..   ....     ..                    |  ___|\n")
    layout.write(" | |  _       .,,...  .....    .. ..                  | |_   \n")
    layout.write(" | |_| |     .,,,.............,,....                  |  _|  \n")
    layout.write("  \____|    .,,,...,*/((###########(((/*.             |_|    \n")
    layout.write("   ___     .,,*/##########(((((//((####(((/,.          ___   \n")
    layout.write("  / _ \    .,,*/##########(((((//((####(((/,.         / _ \  \n")
    layout.write(" |  __/  .,,,*//*,,,,...................,*(##(/*,    | (_) | \n")
    layout.write("  \___| .,,,,,,,.........,...........    ..,/###(/.   \___/  \n")
    layout.write(" | |_  .,,,,,..............,........... .. ..,*,.            \n")
    layout.write(" | __| .,,,,...../&@@@@%,........... .   ..            _ __  \n")
    layout.write(" | |_ .,,*,....(@@@@@@@(@(.....,.  ../((,  ..         | '__| \n")
    layout.write("  \__|,,,*,...,@@@@@@@@@@#..,.,,   /@@@&%%. .         | |    \n")
    layout.write("      ,,,,*....%@@@@@@@@%..,,..*.  .#&@@&*...       . |_|    \n")
    layout.write("      ,*****,...,(&&&%/..,,.....,,.      ...... ....   _     \n") 
    layout.write("      ,*******/*,,.,,**,,............,,,...,,,....... | | __ \n")
    layout.write("     .,*********,,,,...................,///*///*..... | |/ / \n")
    layout.write("      ,****/****,,,,,,,,.......,***//////(((#(/*,.... |   <  \n")
    layout.write("      .***///***,,*(//////////////((((/*,,,/((/**.... |_|\_\ \n")
    layout.write("       ,*****//***(((###(((((//**,,,,....,,/((//,...    ___  \n")
    layout.write("        ,*********/#(/((/**,,,,..........,*((//*....   / _ \ \n")
    layout.write("         .***,******((//***,,,..........,*((//*...    |  __/ \n")
    layout.write("Remember   ,,*,,,,****/((/*****,,,,,,,*/////(,...      \___| \n")
    layout.write("To Watch     ,*,,,,******//((////////////(/*...           _  \n")
    layout.write("What People    ,***,************//////*,,,,..          __| | \n")
    layout.write("Do To Your       .,,,,,,***********,,,,,,.            / _` | \n")
    layout.write("Devices            .,,*,,,,,,,,,,,,,,,,..            | (_| | \n")
    layout.write("Love, Gecko          .,,,,,,,,,,,,,,...               \__,_| \n")
    layout.write("You left your device unlocked and unattended. I went and locked it for you \n")
    kbd.release_all()
    
def lock():
    time.sleep(pause)
    kbd.press(Keycode.GUI)
    kbd.release_all()
    time.sleep(pause)
    layout.write("cmd")
    time.sleep(pause)
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(0.5)
    layout.write("Rundll32.exe user32.dll,LockWorkStation & exit")
    kbd.press(Keycode.ENTER), kbd.release_all()
    
while True:
    if button.value is True and payload_delivered is 0:  # run it
        print("Release the water fowl!")  # for debugging in screen or putty
        if payload is 0:
            terminal()
            lock()
            payload_delivered = 1
    if payload_delivered is 1:
     sys.exit()
