import managesortdirs
import os
import watch_desktop
import threading
from constants import *

def main_loop():
    while True:
        cmd = input(">> ")

        if (cmd == ""):
            continue
        elif (cmd.lower().split()[0] == "addpair"):
            print(sort.add_prefix_dir_pair(cmd.split()[1], cmd.split(' ', 2)[2]))
            sort.save_dict()
        elif (cmd.lower().split()[0] == "removepair"):
            print(sort.remove_prefix_dir_pair(cmd.split()[1]))
            sort.save_dict()
        elif (cmd.lower() == "displaypairs"):
            print(sort)
        elif (cmd.lower() == "quit"):
            watch.cancel()
            break
        elif (cmd.lower() == "sortnow"):
            watch.manual_sort(False)
        else:
            print(NO_CMD)

sort = managesortdirs.ManageSortDirs()
print(WELCOME)

if (sort.check_path_file()):
    sort.load_dict()
    print(PATHS_YES)
else:
    print(PATHS_NO)

print(INFO)

watch = watch_desktop.WatchDesktop(sort.get_dict())
watch.start()
main = threading.Thread(target=main_loop)
main.start()
