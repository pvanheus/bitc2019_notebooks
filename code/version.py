import sys

#print(sys.version)
#print(sys.platform)

#print("our commandline parameters:", sys.argv)
if len(sys.argv) == 2:
    # one command line parameter
    print("Hello", sys.argv[1])
else:
    print("Usage: python code/version.py <name>")
