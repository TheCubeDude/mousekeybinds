import pyautogui
import keyboard
import time

modifiers = set()

def click(x, ev: keyboard.KeyboardEvent):
    print(modifiers, ev.name)

    for key in modifiers:
        pyautogui.keyDown(key)

    pyautogui.click(x)

    for key in modifiers:
        pyautogui.keyUp(key)
    modifiers.clear()

def holdModifier(key):
    print(f"Holding {key}")
    modifiers.add(key)

def bindClick():
    time.sleep(0.5)

    print('Press a key to bind to the current mouse position')
    key = keyboard.read_key()
    pos = pyautogui.position()
    keyboard.on_press_key(key, lambda ev: click(pos, ev))
    
    print(f'{key} key bound to:')
    print(pos)

def bindModifier():
    time.sleep(0.5)

    print('Press the modifier key, then the hotkey you want to bind to it')
    modifier = keyboard.read_key()
    time.sleep(0.5)

    print(f'Press the hotkey you want to bind to {modifier}')
    hotkey = keyboard.read_key()
    keyboard.on_press_key(hotkey, lambda ev: holdModifier(modifier))

    print(f'{hotkey} key bound to holding {modifier} for one click')

def main():
    print("ctrl+b to bind a hotkey")
    print("ctrl+shift+b to bind a modifier key")
    print("")

    while True:
        hotkey = keyboard.read_hotkey(suppress=False)
        if hotkey == "ctrl+b":
            bindClick()
        if hotkey == "ctrl+shift+B":
            bindModifier()

main()