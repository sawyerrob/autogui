import pyautogui
import os,sys,io
import time
import win32api,win32con,win32clipboard
from PIL import Image,ImageGrab
import pytesseract
import operator

case_number_list = []

#用来存放案号列表的列表

cwd = "G:\\终结执行案件2"
# 定义要创建的根目录


file_object = open('list.txt', 'r')

#打开相关列表文件

try:
    for line in file_object:
        line= line.rstrip("\n")
        case_number_list.append(line)

        # 读取列表中的案号,去掉末尾的回车，加入到列表！

finally:

    file_object.close()

    #关闭文件释放资源
def clean(filename,str):

    # 次函数用来写入文件，用来记录

    f = open(filename, "a+")
    #以追加的方式写文件

    f.write('\n'+str)

    f.close()


#开始创建文件夹

def mkdir(path):
    # 引入模块

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print (path + 'success')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + 'error')
        return False



"""
    以上生成文件夹，以下写函数执行下载
"""

def ocr():
    im = ImageGrab.grab(bbox=(940,511,1136,537))
    im.save("C:\\Users\\Lenovo\\Desktop\\1.jpg")
    time.sleep(7)
    text = pytesseract.image_to_string(Image.open('C:\\Users\\Lenovo\\Desktop\\1.jpg'), lang='chi_sim')
    return text

    #此函数截屏返回是否查询无数据

def fill(str):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(str)
    win32clipboard.CloseClipboard()
    time.sleep(1)
    # 路径复制到剪切板

    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 按下ctrl+v黏贴下载路径
def check_original():

    pyautogui.FAILSAFE = True
    # 鼠标快速移动到左上角，触发exception来停止当前操作

    pyautogui.click(235, 450, button="left",interval=2)
    # 鼠标移动查询按钮，并且点击查询

    errortext = ocr()
    #识别文字
    return errortext

def down_original(path1):
    pyautogui.click(365, 533, button="left",interval=2)
    # 鼠标移动到案子行，并且点击选中

    pyautogui.click(710, 450, button="left",interval=2)
    # 鼠标移动点击下载按钮

    pyautogui.click(1000, 602, button="left",interval=2)
    # 鼠标移动选择自定义

    pyautogui.click(914, 643, button="left",interval=2)
    # 鼠标移动选择正卷下载

    pyautogui.click(978, 571, button="left",interval=2)
    # 鼠标移动点击浏览器弹出的框，选择路径

    pyautogui.hotkey('Ctrl', 'a')
    #全部选择

    pyautogui.press('DELETE')

    #清空案号

    fill(path1) #填写下载正卷的路径

    pyautogui.click(1046, 630, button="left", interval=2)
    # 鼠标移动点击浏览器下载按钮

    pyautogui.click(1289, 325, button="left", interval=2)
    # 鼠标移动点击关闭下载窗口
def down_copy(path2):

    pyautogui.FAILSAFE = True
    # 鼠标快速移动到左上角，触发exception来停止当前操作

    pyautogui.click(714, 450, button="left", interval=2)
    # 鼠标移动点击下载按钮

    pyautogui.click(1000, 600, button="left", interval=2)
    # 鼠标移动选择自定义

    pyautogui.click(920, 640, button="left", interval=2)
    # 鼠标移动选择副本下载

    pyautogui.click(920, 575, button="left", interval=2)
    # 鼠标移动点击浏览器弹出的框，选择路径

    pyautogui.hotkey('Ctrl', 'a')
    # 全部选择

    pyautogui.press('DELETE')

    # 清空路径

    fill(path2)  # 填写下载副卷的路径

    pyautogui.click(1046, 630, button="left", interval=2)
    # 鼠标移动点击浏览器下载按钮

    pyautogui.click(1200, 481, button="left", interval=2)

    # 鼠标移动点击关闭下载窗口

#for i in range(1, 111):
for case_number in range(0, len(case_number_list)):
        # 遍历案号数组，取得每一个值
        # mkpath = cwd + "\\" + case_number_list[i-1]
        # mkpath1 = cwd + "\\" + case_number_list[i-1] + "\\"+"正卷"
        # mkpath2 = cwd + "\\" + case_number_list[i-1] + "\\" + "副卷"
        # mkdir(mkpath)
        # mkdir(mkpath1)
        # mkdir(mkpath2)

    #path0 =mkpath1+"\\"+case_number_list[i-1]+".pdf"
    #print(path0)
    #print(os.path.exists(path0))
    #if os.path.exists(path0):
        #continue

    case_number = case_number_list[case_number]
                    # 取得案件编号

    cases = case_number[6:]
                    # 处理cases，得到想要的字符

    pyautogui.click(300, 350, button="left", interval=2)
                    # 鼠标移动到输入案号的界面,并单击左键

    pyautogui.hotkey('Ctrl', 'a')
                    # 全部选择

    pyautogui.press('DELETE')

                    # 清空案号

    print(cases)
                # pyautogui.typewrite(cases)
                # 输入正确的案号
    fill(cases)  # 调用函数黏贴案号

    time.sleep(1)

    err= check_original()

                # 查询是否存在正本
    mmkpath = cwd + "\\" + "(2018)"+cases
    mmkpath1 = cwd + "\\" + "(2018)"+ cases + "\\" + "正卷"
    mmkpath2 = cwd + "\\" +  "(2018)"+cases + "\\" + "副卷"
    if operator.eq(err, "查i旬 的数据不啼宇茌"):
        clean("nodown_list2",mmkpath)
        time.sleep(4)
        continue
    else:
        down_original(mmkpath1)

        down_copy(mmkpath2)

                # 下载副本

os.system("shutdown -s -t  60 ")
        #休息5S，避免死机，并且进入下一个循环！