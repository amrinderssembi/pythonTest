from turtle import speed
import pyautogui

speed = input('how fast should it scroll')
sleepTime = input('how long until next scroll')

pyautogui.time.sleep(3)

while 0 < 10:

    pyautogui.scroll(int(speed))

    pyautogui.time.sleep(int(sleepTime))