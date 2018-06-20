import ctypes
import time
import win32api
import win32gui


# 定义结构体，存储当前窗口坐标
class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int),
                ('top', ctypes.c_int),
                ('right', ctypes.c_int),
                ('bottom', ctypes.c_int)]


while True:
    rect = RECT()
    HWND = win32gui.GetForegroundWindow()  # 获取当前窗口句柄
    # ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))  # 获取当前窗口坐标
    # for i in range(2, 200):
    #     win32gui.SetWindowPos(HWND, None, rect.left + 5 * random.randint(1, i), rect.top - 5 * random.randint(1, i),
    #                           rect.right - rect.left, rect.bottom - rect.top,
    #                           win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)  # 实现更改当前窗口位置
    # win32gui.SetWindowPos(HWND, None, rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top,
    #                       win32con.SWP_NOSENDCHANGING | win32c
    # on.SWP_SHOWWINDOW)  # 将窗口恢复至初始位置
    t = win32api.GetSystemTime()
    # print(t)
    w = win32gui.GetWindowText(HWND)
    a = win32gui.GetClassName(HWND)
    print(w)
    p = win32gui.FindWindow(None, w)
    # print(p)
    w2 = win32gui.GetWindowText(p)
    print(w2)
    print('----')
    time.sleep(2)
