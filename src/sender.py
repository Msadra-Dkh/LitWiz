import ctypes
import time

user32 = ctypes.windll.user32

KEYEVENTF_KEYUP = 0x0002

VK_CONTROL = 0x11
VK_C = 0x43
VK_V = 0x56


def key_down(vk):
    user32.keybd_event(vk, 0, 0, 0)


def key_up(vk):
    user32.keybd_event(vk, 0, KEYEVENTF_KEYUP, 0)


def ctrl_c():
    key_down(VK_CONTROL)
    key_down(VK_C)

    time.sleep(0.01)

    key_up(VK_C)
    key_up(VK_CONTROL)


def ctrl_v():
    key_down(VK_CONTROL)
    key_down(VK_V)

    time.sleep(0.01)

    key_up(VK_V)
    key_up(VK_CONTROL)