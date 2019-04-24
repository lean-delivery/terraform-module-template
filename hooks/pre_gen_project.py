import os
import shutil
from time import gmtime, strftime

def main():
    if "{{ cookiecutter.creating_tests }}" == "No":
        return 0
    creating_backup(".", "backup/")

    if not os.path.exists(".backups/"):
        os.mkdir(".backups/")


    creating_backup(".", ".backups/" + strftime("%Y.%m.%d-%H.%M.%S", gmtime()))

def creating_backup(src, dest):
    try:
        os.mkdir(dest)
    except OSError:
        print ("Creation of the directory %s failed" % dest)

    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)

if __name__== "__main__":
    main()

