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
	- Insert code
"""

def main():
	# Insert code and replce pass
    basepath = os.path.abspath(__file__ + "/../../../..")
    filename = basepath + "/files.log"
    with open(filename, 'a+') as logfile:
        for file in sys.argv[1:]:
            logfile.write("Path:" + file + "\n")


if __name__ == "__main__":
    main()
