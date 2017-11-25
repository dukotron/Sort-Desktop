import re
import os

class ManageSortDirs:
    def __init__(self):
        self.prefix_loc_dict = {}

    def add_prefix_dir_pair(self, prefix, location):
        if (re.match("^[\w\d_-]*$", prefix) is False or prefix[-1] != '_'):
            print("Wrong prefix format!")
            return

        if (os.path.isdir(location) is False):
            print("Wrong location format!")
            return

        self.prefix_loc_dict[prefix] = location
        
    def __str__(self):
        s = ""
        s += "PREFIX" + "\tLOCATION".expandtabs(16)
        
        for prefix, location in self.prefix_loc_dict.items():
           s += "\n" + prefix + ("\t" + location).expandtabs(16 + 6 - len(prefix))

        s += "\n\n" + ("{:-^" + str(len(s.split("\n")[-1])) + "}").format('END')

        return s
