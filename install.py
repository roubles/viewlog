#!/usr/bin/env python

import os
import argparse
from shutil import copy

def getAbsolutePath (path):
    if path is None:
        return path
    return os.path.abspath(os.path.expandvars(os.path.expanduser(path)))

def setupParser ():
    parser = argparse.ArgumentParser(description='Install viewlog')
    parser.add_argument('--prefix', help="Alternate path to install viewlog", default="/usr/local/bin/")
    return parser

parser = setupParser()
args = parser.parse_args()
installpath = getAbsolutePath(args.prefix)

if not os.path.exists(installpath):
    print "Attempting to make path " + installpath
    os.makedirs(installpath)
print "Copying py/viewlog to " + installpath
copy("py/viewlog", installpath)
path = os.path.join(installpath, "viewlog")
os.chmod(path, 0755)
