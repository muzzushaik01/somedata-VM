import win32api
import re
import time
start=time.perf_counter()
availableDrives = win32api.GetLogicalDriveStrings()
print(availableDrives)
drives = [drivestr for drivestr in availableDrives.split('\000') if drivestr]
#drives  = drives.split('\000')[:-1]
print(drives)