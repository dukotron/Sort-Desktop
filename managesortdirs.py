import re
import os
import pickle
from constants import *

class ManageSortDirs:
    def __init__(self):
        self.FILE_NAME = "paths"
        self.prefix_loc_dict = {}

    def add_prefix_dir_pair(self, prefix, location):
        if (re.match("^[\w\d_-]*$", prefix) is False or prefix[-1] != '_'):
            return PREFIX_NO

        if (os.path.isdir(location) is False):
            return LOC_NO

        self.prefix_loc_dict[prefix] = location
        return ADDED

    def remove_prefix_dir_pair(self, pref):
        for prefix, location in self.prefix_loc_dict.items():
            if (pref == prefix):
                del self.prefix_loc_dict[pref]
                return REMOVED
        return PREFIX_NO_EX

    def save_dict(self):
        pickle.dump(self.prefix_loc_dict, open(FILE_NAME, "wb"))

    def load_dict(self):
        self.prefix_loc_dict = pickle.load(open(FILE_NAME, "rb"))

    def check_path_file(self):
        return os.path.isfile(FILE_NAME)

    def get_dict(self):
        return self.prefix_loc_dict
        
    def __str__(self):
        s = ""
        s += "PREFIX" + "\tLOCATION".expandtabs(16)
        
        for prefix, location in self.prefix_loc_dict.items():
           s += "\n" + prefix + ("\t" + location).expandtabs(16 + 6 - len(prefix))

        s += "\n\n" + ("{:-^" + str(len(s.split("\n")[-1])) + "}").format('END')

        return s
