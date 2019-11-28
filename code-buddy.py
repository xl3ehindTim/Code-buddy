from helpers import *

if getArgs(1) == "create":
    projectType = getArgs(2)
    if projectType == "python":
        pass
    elif projectType == "javascript":
        pass
    elif projectType == "node":
        pass
    elif projectType == "html":
        pass
    elif projectType == "php":
        pass
else:
    print(f"argument {getArgs(1)} is unknown")