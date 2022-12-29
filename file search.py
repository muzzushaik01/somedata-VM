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


find_file_in_all_drives("documentation.txt")
import time
import os
start=time.perf_counter()
def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


print(find_files("documentation.txt", "C:"))
print(find_files("documentation.txt", "D:"))
print(find_files("documentation.txt", "E:"))
finish=time.perf_counter()

print("time is {0} seconds".format(finish-start))