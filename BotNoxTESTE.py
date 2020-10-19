import pyautogui
import time
wh = pyautogui.size() #obter a resolução da tela   
#print(wh)
#pyautogui.moveTo  serve para mover o mouse

"""pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)   
pyautogui.moveTo(200, 200, duration=0.25)"""
#pyautogui.moveTo(50, 300, duration=0.25)

print(pyautogui.position()) # Get current mouse position.


"""pyautogui.moveTo(50, 300, duration=0.55)
time.sleep(2)
pyautogui.click(50, 300) # nox
pyautogui.click(50, 300) # nox
time.sleep(20)
pyautogui.click(780, 625)    # Click to make the window active.
time.sleep(3)
pyautogui.click(1465, 445)
time.sleep(5) 
pyautogui.write('Mutter')
time.sleep(5)
pyautogui.click(850, 560)"""
time.sleep(3)
pyautogui.moveTo(840, 860, duration=0.55)
pyautogui.click(840, 860)
time.sleep(3)
pyautogui.write('Olá Edicleia, Eu sou um robo HAHAHAHA')
pyautogui.write(['enter'])

