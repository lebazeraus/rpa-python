# !#/usr/bin/python3
import pyautogui as robot
import time
#
criterio = 'youtube'
xyIconoFirefox = 1306, 516
xyLinkGoogleYouTube = 285, 286
xyPlay = 477, 600
xyCerrarNevegador = 1343, 20
#
def step(xy, click=1):
  robot.moveTo(xy)
  robot.click(clicks=click)

# Ubicar y abrir FireFox
step(xyIconoFirefox, click=2)
time.sleep(5)

# Maximizar el navegador
robot.hotkey('alt', 'space')
time.sleep(.3)
robot.typewrite('x')
time.sleep(.3)

# Tipear "youtube" y presionar <enter>
robot.typewrite('youtube')
robot.hotkey('enter')
time.sleep(3)

# Ubicar y abrir el enlace "Google Youtube"
step(xyLinkGoogleYouTube)
time.sleep(3)

# Ubicar el video principal y abirlo
step(xyPlay)
time.sleep(10)

# Ubicar el botón de cerrar del navegador y cerrar
step(xyCerrarNevegador)
#
print('Success')
