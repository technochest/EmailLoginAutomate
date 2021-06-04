import os
import time
import pyautogui as auto
import cv2
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys




WebAddress = "https://www.live.com  "
UserName = "username@live.com"
Password = "password"

#Open Browser

browser = webdriver.Chrome()
time.sleep(2)

browser.get(WebAddress)

time.sleep(2)

Loc_Sign_In = None
while Loc_Sign_In is None:
    Loc_Sign_In = auto.locateOnScreen(
        'C:/Users/..../EmailLoginImage.png', grayscale=False,
        confidence=.80)

time.sleep(2)

auto.click(Loc_Sign_In)

time.sleep(2)

#Enter username
auto.typewrite(UserName)
auto.press('enter')

#Waite 1 second and enter password
time.sleep(2)
auto.typewrite(Password)
auto.press('enter')














