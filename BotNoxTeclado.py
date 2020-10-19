from pynput.keyboard import Key, Controller
import time
import pyautogui

keyboard = Controller()

time.sleep(2)
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(2)
keyboard.type('Nox')
time.sleep(2)
keyboard.press(Key.enter) # entrar no nox usando teclado
time.sleep(20)
pyautogui.click(780, 625)    # Click to make the window active.
time.sleep(3)
pyautogui.click(1465, 445)
time.sleep(5) 
pyautogui.write('Samuel')
time.sleep(5)
pyautogui.click(850, 560)
time.sleep(3)
pyautogui.moveTo(840, 860, duration=0.55)
pyautogui.click(840, 860)
time.sleep(3)
pyautogui.write('Hola soy Alienware un programa, hecha solamente para enviarte este mensaje programado por Lucas mi creador :P')
pyautogui.write(['enter'])

#keyboard.press('a')
