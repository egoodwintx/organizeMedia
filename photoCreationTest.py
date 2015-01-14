#!/usr/bin/python

__author__ = 'egoodwin'

import sys
import os, shutil
import os.path
import time
import subprocess
from datetime import datetime


def photoDate(f):
  "Return the date/time on which the given photo was taken."

  cDate = subprocess.check_output(['sips', '-g', 'creation', f])
  cDate = cDate.split('\n')[1].lstrip().split(': ')[1]
  return datetime.strptime(cDate, "%Y:%m:%d %H:%M:%S")

if __name__ == "__main__":
    fname = "/Volumes/archive/photos/archive/unsorted/2397184056_c5843e7483_b.jpg"
    try:
        print(photoDate(fname))
    except:
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fname)
        print "last modified: %s" % mtime
        #cTime = time.ctime(ctime)
        pDate = datetime.fromtimestamp(mtime)
        cDate = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(mtime))

        print "filename str: %s" % cDate

        yr = pDate.year
        mo = pDate.month
        print yr
        print mo
