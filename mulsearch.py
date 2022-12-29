import os
import threading
import concurrent.futures
import time

start=time.perf_counter()
def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
drivees=["C:","E:","F:"]
inp_file="documentation.txt"
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(find_files,inp_file,i) for i in drivees]
for r in concurrent.futures.as_completed(results):
    print(r.result())
finish=time.perf_counter()
print(f"time is {finish-start} seconds")