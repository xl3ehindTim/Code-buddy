import os
def createPythonProject(name):
    os.system(f"mkdir {name}")
#   os.system(f"cd {name}")
    with open(f"{name}/main.py", "w+") as file:
        file.write(f'''def main():
    pass

if __name__ == "__main__":
    main()''')
    os.chdir(f"{name}")
    os.system(f"mkdir helpers")
    os.system("git init")
    os.system("fsutil file createnew README.md 0")