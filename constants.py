#Well I like this approach since there isn't a real const,
#so unless there is a specific reason not to do it horay.
FILE_NAME = "paths"
WELCOME = "Welcome to Sort Desktop."
PATHS_YES = "Loaded paths file."
PATHS_NO = "Paths file not found, will be added once you add prefix-location pairs."
INFO = "If you are stuck type 'help' and press the enter key."
NO_CMD = "No command found"
PREFIX_NO = "Wrong prefix format!"
PREFIX_NO_EX = "Prefix doesn't exist!"
LOC_NO = "Wrong location format!"
ADDED = "Prefix/location pair added to sorting."
REMOVED = "Prefix/location pair removed from sorting."
HELP = """The following commands are available(not case sensitive, you don't actually write the [] around your arguments):
\naddpair [prefix] [location]
- prefix - the prefix app scans for in folders/files, has to end with '_'.
- location - the location where you want the prefixed files/folders to be sorted to.
- This command will add the prefix/location pair to the sorting of the program.
- You have to add the prefix to the names of files/folders you want sorted.
- The default sort interval is 24h.
\nremovepair [prefix]
- The prefix argument is the same as in addpair.
- This command will remove the prefix/location pair from the sorting of the program.
\ndisplaypairs - display all prefix/location pairs.
\nquit - exits the program.
\nsortnow - uses the prefixes and locations (explained in addpair) to immediately sort files/folders.
\nhelp - this text."""
