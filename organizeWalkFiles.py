#!/usr/bin/python
import os.path
import shutil

__author__ = 'egoodwin'

# The top argument for walk. The
# Python27/Lib/site-packages folder in my case

fromdirtree = '/Volumes/archive/photos/years/'
todir = '/Volumes/archive/videos/incoming/'

# The arg argument for walk, and subsequently ext for step
exten = '.mov'
#
def copysafe(fromdir, fname):
     suffix = 1
     fromuri = os.path.join(fromdir, fname)
     touri = os.path.join(todir, fname)

     while(os.path.exists(touri)):
         newfname = os.path.splitext(touri)[0] + "_" + str(suffix) + os.path.splitext(touri)[1]
         touri = os.path.join(todir, newfname)
         suffix = suffix + 1
     print("Copying [" + fromuri + "] to [" + touri + "]")
     shutil.copy2(fromuri, touri)

def copystep(ext, fromdirname, names):
    ext = ext.lower()
    for name in names:
        if name.lower().endswith(ext):
            copysafe(fromdirname, name)

# Start the walk
os.path.walk(fromdirtree, copystep, exten)