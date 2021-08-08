import keyboard
import threading
from pynput.mouse import Controller

"""
This is used to block the user from using the keyboard or mouse while the program is running.
The user can gain access again after the program is over. I had some big headaches by mistakenly 
locking myself.
"""

def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()


def unblockinput():
    blockinput_stop()


def blockinput_start():
        mouse = Controller()
        global block_input_flag
        for i in range(150):
            keyboard.block_key(i)
        while block_input_flag == 1:
            mouse.position = (0, 0)

def blockinput_stop():
    global block_input_flag
    for i in range(150):
        keyboard.unblock_key(i)
    block_input_flag = 0


