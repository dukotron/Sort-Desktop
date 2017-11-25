import managesortdirs
import os

def display_help():
    print()

print("Welcome to Sort Desktop")
print("If you are stuck type 'help' and press the enter key")
sort = managesortdirs.ManageSortDirs()

while True:
    cmd = input(">> ")

    if (cmd == ""):
        continue
    elif (cmd.lower().split()[0] == "addpair"):
        sort.add_prefix_dir_pair(cmd.split()[1], cmd.split(' ', 2)[2])
    elif (cmd.lower() == "displaypairs"):
        print(sort)
    elif (cmd.lower() == "exit"):
        break
    else:
        print("No command found")
