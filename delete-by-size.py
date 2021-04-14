import sys
import os, os.path

oDir = sys.argv[1] 

filesNotDeleted = 0

for root, _, files in os.walk(oDir):
   for f in files:
      fullpath = os.path.join(root, f)
      if(os.path.getsize(fullpath) < (1 * 1024)):
         filesNotDeleted += 1
         os.remove(fullpath)
         print("Removed: " + fullpath)
