# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 20:07:10 2022
@author: Gazer
"""

import pyautogui
import time
import  pyperclip
from selenium import webdriver
import sys
try:
    EDGEE = {
                "browserName": "MicrosoftEdge",
                "version": "97.0.1072.55",
                "platform": "WINDOWS",
     
                "ms:edgeOptions": {
                    'extensions': [],
                    'args': [
                        '--headless',
                        '--disable-gpu',
                        '--remote-debugging-port=9222',
                    ]}
            }
    
                                #无窗口模式
    driver = webdriver.Edge('./edgedriver_win64/msedgedriver.exe',capabilities=EDGEE)#创建浏览器对象
    #time.sleep(20)
    driver.get("https://chp.shadiao.app/")
    #登录
    time.sleep(1)
    dr = driver.find_element_by_id('txt_chp').text
    pyperclip.copy(dr)
    pyautogui.hotkey('ctrl','alt','w')
    time.sleep(1)
    pyautogui.hotkey('ctrl','f')
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.typewrite('baobao')
    time.sleep(1)
    pyautogui.hotkey('space')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('alt','c')
except:
    pass
time.sleep(3)
driver.close()
sys.exit(0)
    









