import os

def createHtmlProject(name):
    os.system(f"mkdir {name}")
    with open(f"{name}/index.html", "w+") as file:
        file.write(f'''<!DOCTYPE HTML>
<html lang="nl">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="css/style.css">
    </head>
    <body>

    </body>
</html>''')
    os.chdir(f"{name}")
    os.system(f"mkdir css")
    with open(f"css/style.css", "w+") as file:
        pass
    os.system("git init")
    os.system("fsutil file createnew README.md 0")
