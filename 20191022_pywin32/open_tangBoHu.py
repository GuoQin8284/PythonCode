import win32api

import win32gui

import win32con

TangBoHuPos=(36, 958)
w1hd=win32gui.FindWindow("Qt5QWindowIcon",None)
print(w1hd)
a=win32api.GetCursorPos()
shouQuan=(857, 650)
win32api.SetCursorPos((36, 958))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.SetCursorPos((857, 650))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)

print(a)