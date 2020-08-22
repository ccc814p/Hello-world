import sys
pkglist = ['pkgr']
if argv[1]=="-h":
  print("pkgr.py -a: Add package\npkgr -h: Get help")
if argv[1]=="-a":
  pkgname = str(argv[2])
  print("Installing "+pkgname+"...")
  pkglist.append(pkgname)
if argv[1]=="-r":
  pkgname = str(argv[2])
  print("Removing "+pkgname+"...")
  pkglist.del(pkgname)
if argv[1]=="-l":
  for x in pkglist:
    print(x+"\n")
