def createCcaProject(name):
    os.system(f"mkdir {name}")
    with open(f"{name}/index.cca", "w+") as file:
        file.write(f'''stp''')
    os.chdir(f"{name}")
    os.system("git init")
    os.system("fsutil file createnew README.md 0")
