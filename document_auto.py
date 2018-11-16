import pyautogui,os,time

# os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\SogouExplorer\\SogouExplorer")#打开首页

screenwidth,screenheight = pyautogui.size()#取得屏幕尺寸

mouseX,mouseY=pyautogui.position()#取鼠标当前位置

pyautogui.PAUSE = 2.5 # 每个函数执行后停顿1.5秒，便于终止

pyautogui.FAILSAFE = True # 鼠标移到左上角会触发FailSafeException，因此快速移动鼠标到左上角也可以停止

def upload():

    # pyautogui.moveTo(700,151,duration=0.1)  #在此处点击，以便输入密码
    # pyautogui.click(clicks=2, interval=0.25)  # 双击，间隔0.25s
    # pyautogui.typewrite("091202")

    pyautogui.moveTo(574, 316, duration=0.1)  #从1425开始
    pyautogui.click(574, 316, button='left')

    pyautogui.moveTo(73, 568, duration=0.1)
    pyautogui.click(73, 568, button='left')
    time.sleep(3)

    pyautogui.moveTo(66, 423, duration=0.1)
    pyautogui.click(66, 423, button='left')
    time.sleep(3)

    pyautogui.moveTo(300, 319, duration=0.1)
    pyautogui.click(300, 319, button='left')

    pyautogui.moveTo(1187, 500, duration=0.1)
    pyautogui.click(1187, 500, button='left')


    pyautogui.moveTo(357, 191, duration=0.1)
    pyautogui.click(357, 191, button='left')
    pyautogui.hotkey('Ctrl', 'a')

    pyautogui.moveTo(601, 446, duration=0.1)
    pyautogui.click(601, 446, button='left')


    pyautogui.moveTo(525, 92, duration=0.1)
    pyautogui.click(clicks=2, interval=0.25)  # 双击，间隔0.25s
    #
    # pyautogui.moveTo(1128, 315, duration=0.1)  #开始移送
    # pyautogui.click(1128, 315, button='left')
    #
    # pyautogui.moveTo(1023, 703, duration=0.1)  # 点击确定
    # pyautogui.click(1023, 703, button='left')
    #
    # pyautogui.moveTo(1009, 730, duration=0.1)  # 开始点击关闭
    # pyautogui.click(1009, 730, button='left')
    time.sleep(3)
    return
if __name__ == '__main__':
    while(True):
        upload()