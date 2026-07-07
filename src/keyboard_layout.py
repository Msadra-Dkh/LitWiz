# Start

# LibrarZzz!
#-----------------------------------------------------------------------------------------------#
import ctypes
from ctypes import wintypes

#-----------------------------------------------------------------------------------------------#

# CONSTANTZzz!
#-----------------------------------------------------------------------------------------------#
WM_INPUTLANGCHANGEREQUEST = 0x0050
KLF_ACTIVATE = 0x0001

#-----------------------------------------------------------------------------------------------#

# DifineZzz!
#-----------------------------------------------------------------------------------------------#
user32 = ctypes.WinDLL("user32", use_last_error=True)
load_keyboardlayout = user32.LoadKeyboardLayoutW
load_keyboardlayout.argtypes = [wintypes.LPCWSTR, wintypes.UINT]
load_keyboardlayout.restype = wintypes.HKL

post_message = user32.PostMessageW
post_message.argtypes  = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]

get_foreground_window = user32.GetForegroundWindow
get_foreground_window.restype = wintypes.HWND

#-----------------------------------------------------------------------------------------------#

# FunctionZzz!
#-----------------------------------------------------------------------------------------------#
def switch_layout(new_lang_id) :

    hkl = load_keyboardlayout(new_lang_id, KLF_ACTIVATE)

    if not hkl :
        raise RuntimeError("keyboard layout is not installed")
    
    hwnd = get_foreground_window()

    post_message(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, hkl)

#-----------------------------------------------------------------------------------------------#

# the END