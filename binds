import pyautogui
import keyboard
import time
mode = True
def twoclick(x):
    pyautogui.keyDown('2')
    pyautogui.click(x)
    pyautogui.keyUp('2')
def bind(x):
    keyboard.add_hotkey(x,pyautogui.click, args=[pyautogui.position()])
    keyboard.add_hotkey('shift+'+x,twoclick, args=[pyautogui.position()])
def bindmode(x):
    time.sleep(1)
    print('Press a key to bind to the current mouse position')
    event = keyboard.read_event()
    bind(event.name)
    position = pyautogui.position()
    print(event.name+' key bound to:')
    print(position)
while mode == True:
    keyboard.wait('ctrl+b')
    bindmode(mode)