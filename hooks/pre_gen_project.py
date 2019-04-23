import os
from shutil import copyfile

def main():
    if "{{ cookiecutter.creating_tests }}" == "No":
        return 0
    creating_backup("backup/")

def creating_backup(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)

    copyfile("main.tf", path + "main.tf")
    copyfile("variables.tf", path + "variables.tf")
    copyfile("outputs.tf", path + "outputs.tf")

if __name__== "__main__":
    main()

