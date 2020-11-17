import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(m_link):
    subprocess.call(r'C:\Users\dishu\AppData\Roaming\Zoom\bin\Zoom.exe')
    time.sleep(10)

    join_btn=pyautogui.locateCenterOnScreen('z.png',grayscale=False)
    pyautogui.moveTo(join_btn)
    print(join_btn)
    pyautogui.click()

    time.sleep(5)

    meeting_link_btn=pyautogui.locateCenterOnScreen("z1.png",grayscale=False)
    pyautogui.moveTo(meeting_link_btn)
    print(meeting_link_btn)
    pyautogui.click()
    pyautogui.write(m_link)
    
    time.sleep(2)

    media_btn=pyautogui.locateAllOnScreen('z2.png',grayscale=True)
    for btn in media_btn :
        pyautogui.moveTo(btn)
        print(media_btn)
        pyautogui.click()
        time.sleep(2)

    join=pyautogui.locateCenterOnScreen('z3.png',grayscale=False)
    pyautogui.moveTo(join)
    print(join)
    pyautogui.click()

    time.sleep(5)

    password=pyautogui.locateCenterOnScreen('z4.png',grayscale=False)
    pyautogui.moveTo(password)
    print(password)
    pyautogui.click()
    pyautogui.write("000")

    time.sleep(2)

    final=pyautogui.locateCenterOnScreen('z5.png',grayscale=False)
    pyautogui.moveTo(final)
    print(final)
    pyautogui.click()

df=pd.read_csv('links.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
      # m_pswd = str(row.iloc[0,2])

       sign_in(m_id)
       time.sleep(40)
       print('signed in')