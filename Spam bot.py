import pyperclip
from pynput.keyboard import Key, Listener, Controller
import time
import beemovie
keyb = Controller()

while  True:
    time.sleep(3)

    text = beemovie.text1
    pyperclip.copy(text)
    #print(text)


#Mandando apertar CTRL+V

    with keyb.pressed(Key.ctrl):
        keyb.press('v')
        keyb.release('v')


#Monitorando o teclado

    #def press (key):
    #print(key)

    def release(key):
        if key == Key.shift:
            return False
    with Listener(on_press=press, on_release=release) as listener:
        listener.join()
    

