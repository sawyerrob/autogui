import pyautogui,os

os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\SogouExplorer\\SogouExplorer")#打开首页

screenwidth,screenheight = pyautogui.size()#取得屏幕尺寸

mouseX,mouseY=pyautogui.position()#取鼠标当前位置

pyautogui.PAUSE = 1.5 # 每个函数执行后停顿1.5秒，便于终止

pyautogui.FAILSAFE = True # 鼠标移到左上角会触发FailSafeException，因此快速移动鼠标到左上角也可以停止

def login():
    pyautogui.click(908, 10, button='left')  #点击切换到浏览器
    pyautogui.click(561, 151, button='left')
    pyautogui.click(clicks=2, interval=0.25)  # 双击，间隔0.25s
    pyautogui.typewrite("admin")
    pyautogui.press('shift')

    pyautogui.moveTo(700,151,duration=0.1)  #在此处点击，以便输入密码
    pyautogui.click(clicks=2, interval=0.25)  # 双击，间隔0.25s
    pyautogui.typewrite("091202")

    pyautogui.moveTo(840,152,duration=0.1)
    pyautogui.click(840, 152, button='left')

    pyautogui.moveTo(716, 340, duration=0.1)  #进入到审判系统
    pyautogui.click(716, 340, button='left')
    pyautogui.PAUSE = 2

    pyautogui.moveTo(436, 119, duration=0.1)  # 切换标签到审判系统
    pyautogui.click(436, 119, button='left')

    pyautogui.moveTo(1097, 165, duration=0.1)  # 点击收立案
    pyautogui.click(1097, 165, button='left')

    pyautogui.moveTo(1285, 398, duration=0.1)  # 关闭提醒框
    pyautogui.click(1285, 398, button='left')

    pyautogui.moveTo(645, 261, duration=0.1)  # 点击新收案件
    pyautogui.click(645, 261, button='left')

    pyautogui.moveTo(1285, 398, duration=0.1)  # 关闭提醒框
    pyautogui.click(1285, 398, button='left')

    pyautogui.moveTo(577, 477, duration=0.1)  # 点击简易程序非小额诉讼
    pyautogui.click(577, 477, button='left')


    return
if __name__ == '__main__':
    login()