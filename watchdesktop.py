from threading import Thread
import time
import shutil
import os

class WatchDesktop(Thread):
    def __init__(self, dic):
        Thread.__init__(self)
        self.dic = dic
        self.daemon = True
        self.cancelled = False

    def run(self):
        while (not self.cancelled):
            time.sleep(86400)
            self.manual_sort(True)

    def manual_sort(self, auto):
        first = auto #trying to minimize retarded format due to input and output interacting with console, only applicable in loop

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
    
    def cancel(self):
        self.cancelled = True
