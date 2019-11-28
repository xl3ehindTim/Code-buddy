import os

def createPhpProject(name):
    os.system(f"mkdir {name}")
    with open(f"{name}/index.php", "w+") as file:
        file.write(f'''<!DOCTYPE HTML>
<html lang="nl">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="css/style.css">
    </head>
    <body>
        <?php

        ?>
    </body>
</html>''')
    os.chdir(f"{name}")
    os.system(f"mkdir css")
    os.system(f"mkdir php")
    with open(f"php/form.php", "w+") as file:
        pass
    with open(f"php/navbar.php", "w+") as file:
        pass
    with open(f"php/footer.php", "w+") as file:
        pass
    with open(f"css/style.css", "w+") as file:
        pass
    os.system("git init")
    os.system("fsutil file createnew README.md 0")
