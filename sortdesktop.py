import managesortdirs
import os

def display_help():
    print()

sort = managesortdirs.ManageSortDirs()

print("Welcome to Sort Desktop.")

if (sort.check_path_file()):
    sort.load_dict()
    print("Loaded paths file.")
else:
    print("Paths file not found, will be added once you add prefix-location pairs.")

print("If you are stuck type 'help' and press the enter key.")

while True:
    cmd = input(">> ")

    if (cmd == ""):
        continue
    elif (cmd.lower().split()[0] == "addpair"):
        sort.add_prefix_dir_pair(cmd.split()[1], cmd.split(' ', 2)[2])
        sort.save_dict()
    elif (cmd.lower() == "displaypairs"):
        print(sort)
    elif (cmd.lower() == "exit"):
        break
    else:
        print("No command found")
