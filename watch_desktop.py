import threading
import time
import shutil
import os

class WatchDesktop(threading.Thread):
    def __init__(self, dic):
        threading.Thread.__init__(self)
        self.dic = dic

    def run(self):
        while True:
            time.sleep(15)
            first = True #trying to minimize retarded format due to input and output interacting with console

            desktop = os.getenv("SystemDrive") + os.environ["HOMEPATH"] + "\\desktop"
            everything = os.listdir(desktop)

            for prefix, location in self.dic.items():
                for item in everything:
                    if ("_" not in item):
                        continue
                    
                    if (item.split("_")[0] + "_" == prefix):
                        if (first == True):
                            print("")
                        
                        os.rename(desktop + "\\" + item, desktop + "\\" + item.split("_", 1)[1])
                        shutil.move(desktop + "\\" + item.split("_", 1)[1], location)
                        first = False
                        print("Item " + item + " moved to " + location)
            
