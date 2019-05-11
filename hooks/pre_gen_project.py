#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Steps before creating templates"""

from __future__ import print_function
import os
import shutil
from time import gmtime, strftime


def main():
    """Main function"""
    if "{{ cookiecutter.creating_tests }}" != "No":
        creating_backup(".", "backup/")

        if not os.path.exists(".backups/"):
            os.mkdir(".backups/")

        creating_backup(".",
                        ".backups/" +
                        strftime("%Y.%m.%d-%H.%M.%S", gmtime()))


def creating_backup(src, dest):
    """Creating backups with all files before using overwrite-if-exists key"""
    try:
        os.mkdir(dest)
    except OSError:
        print("Creation of the directory %s failed" % dest)

    src_back_files = os.listdir(src)
    for file_name in src_back_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


if __name__ == "__main__":
    main()
