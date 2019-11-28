import os
from getArgs import getArgs
from modules import python, javascript, html, php, bootstrap
# from folder import file

# code-buddy.py create (file type) (directory name)

# Checks for "create"
if getArgs(1) == "create":
  # Checks for which file type
    projectType = getArgs(2)
    # Checks for file name
    if projectType == "python":
        name = getArgs(3)
        python.createPythonProject(name)
    elif projectType == "javascript":
        name = getArgs(3)
        javascript.createJavascriptProject(name)
    elif projectType == "html":
        name = getArgs(3)
        html.createHtmlProject(name)
    elif projectType == "php":
        name = getArgs(3)
        php.createPhpProject(name)
    elif projectType == "bootstrap":
        name = getArgs(3)
        bootstrap.createPhpProject(name) 
        # If not valid file type       
    else:
        print(f"argument {getArgs(2)} is unknown, try: 'python, javascript, html, php'")
else:
    # If invalid "create"
    print(f"argument {getArgs(1)} is unknown, use 'create' to create a folder")
