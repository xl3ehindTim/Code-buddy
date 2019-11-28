import os
from getArgs import getArgs
from python import createPythonProject
from javascript import createJavascriptProject
from node import createNodeProject
from html import createHtmlProject
from php import createPhpProject
# from folder import file

# code-buddy.py create (file type) (directory name)
if getArgs(1) == "create":
    projectType = getArgs(2)
    if projectType == "python":
        name = getArgs(3)
        createPythonProject(name)
    elif projectType == "javascript":
        name = getArgs(3)
        createJavascriptProject(name)
    elif projectType == "node":
        name = getArgs(3)
        createNodeProject(name)
    elif projectType == "html":
        name = getArgs(3)
        createHtmlProject(name)
    elif projectType == "php":
        name = getArgs(3)
        createPhpProject(name)
else:
    print(f"argument {getArgs(1)} is unknown")
