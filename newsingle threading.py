import os
import re
import win32api
import threading
import time
start=time.process_time()

def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                print(os.path.join(root, f))
                break
                # if you want to find only one

def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    s=[]
    for drive in win32api.GetLogicalDriveStrings().split('\000'):
        tr=threading.Thread(target=find_file,args=[drive,rex])
        tr.start()
        s.append(tr)
        #find_file(drive,rex)
        for i in s:
           i.join()

find_file_in_all_drives("documentation.txt")
finish=time.process_time()
print(finish-start)