import sys
if argv[1]=="-h":
  print("pkgr.py -a: Add package\npkgr -h: Get help")
if argv[1]=="-a":
  pkgname = str(argv[2])
  print("Installing %s"pkgname)
