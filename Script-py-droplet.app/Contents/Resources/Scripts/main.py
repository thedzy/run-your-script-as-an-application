#!/usr/bin/env python3

""" 
main.py

Created by _yourname_
Copyright (c) 2010 _comapnyname_, All Rights Reserved.
"""

import os
import sys

"""
TODO
	- Edit info.plist for copyright and organisation
	- Replace cmd.icns
	- Insert/chnage code
"""

def main():
	# Insert code or replace
    basepath = os.path.abspath(__file__ + "/../../../../..")

    # Create a file at the same location as the app
    filename = basepath + "/files.log"

    # Write all the files passed to the file above
    with open(filename, 'w+') as logfile:
        for file in sys.argv[1:]:
            logfile.write("Path: " + file + "\n")
            print("Path: " + file + "\n")


if __name__ == "__main__":
    main()
