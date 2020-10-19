from pynput.keyboard import Key, Controller
import time
import pyautogui

keyboard = Controller()

'''time.sleep(2)
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
time.sleep(5)'''K
pyautogui.write('Kelh')
time.sleep(5)
pyautogui.click(850, 560)
time.sleep(3)
pyautogui.moveTo(840, 860, duration=0.55)
pyautogui.click(840, 860)
time.sleep(3)
pyautogui.write('Hola soy Alienware un programa, hecha solamente para enviarte este mensaje programado por Lucas mi creador :P')
pyautogui.write(['enter'])

#keyboard.press('a')

'''pyautogui.click(1440, 730)#Clicar em compartilhar
time.sleep(2)
pyautogui.click(1280, 485)#clicar em áudio
time.sleep(2)
pyautogui.click(1080, 355)#clicar em output.mp3
time.sleep(2)
pyautogui.click(1530, 730)#clicar em enviar
time.sleep(1)
pyautogui.click(1350, 550)#confirmar envio'''