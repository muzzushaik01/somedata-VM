import os
import re
import win32api
import threading
import UploadFiles #filename
import concurrent.futures

def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            print(result)
            if result:
                insert_file_search_results(root, f, 0)
                break  # if you want to find only one


def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        [executor.submit(find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]

def insert_file_search_results(fileLocation, fileName, searchCount = 0):
    UploadFiles.upload_file_results_todb(fileName, fileLocation, searchCount)

def search_forfile_indb(fileName):
    fileSearchStatus = UploadFiles.search_in_db_for_file(fileName)


    if(fileSearchStatus):
        find_file_in_all_drives(fileName)

fileToSearch = input()
search_forfile_indb(fileToSearch)

#UploadFiles.show_file_search_results_fromdb()