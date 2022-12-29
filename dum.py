import os
import re
import win32api
import threading
import time

start = time.perf_counter()

def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                print(os.path.join(root, f))
                break  # if you want to find only one


def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    for _ in range(5):
        thread = threading.Thread(target=find_file, args=[3])

    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file(drive, rex)
finish=time.perf_counter()



find_file_in_all_drives("documentation.txt")
print("time is {0} seconds".format(finish-start))
