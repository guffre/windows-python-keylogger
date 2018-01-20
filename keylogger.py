from ctypes import windll,byref,c_int,c_void_p, POINTER, CFUNCTYPE
from ctypes.wintypes import WPARAM, LPARAM, MSG
import sys
user32 = windll.user32

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
VK_CONTROL = [0x11,0xa2,0xa3]
msg = MSG()
_msg = byref(msg)

LLKP_decl = CFUNCTYPE(c_int, c_int, WPARAM, POINTER(LPARAM))
def LowLevelKeyboardProc(nCode, wParam, lParam):
    if wParam == WM_KEYDOWN:
        vkCode = lParam[0] 
        if vkCode in VK_CONTROL:
            print("Unhooking")
            user32.UnhookWindowsHookEx(hook)
            sys.exit(0)
        sys.stdout.write(chr(vkCode))
    return user32.CallNextHookEx(hook, nCode, wParam, lParam)

callback = LLKP_decl(LowLevelKeyboardProc)

hook = user32.SetWindowsHookExA(WH_KEYBOARD_LL, callback, 0,0)
user32.GetMessageA(_msg,0,0,0)