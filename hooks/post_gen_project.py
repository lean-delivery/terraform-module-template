#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Steps after creating templates"""

from __future__ import print_function
import re
import os
import shutil


def main():
    """Main function"""
    if "{{ cookiecutter.creating_tests }}" == "Yes":
        restoring_from_backup("backup/", ".")
        making_maintf()
        making_outputstf()
        making_variablestf()
        require_vars = check_require_vars("variables.tf")
        for __var__ in require_vars:
            print("Warning! Require vriable: " + __var__)


def restoring_from_backup(src, dest):
    """Restore all files from backup after using overwrite-if-exists key"""
    src_rest_files = os.listdir(src)
    for file_name in src_rest_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
    shutil.rmtree(src)


def get_namelist(prefix, postfix, file_path):
    """get all names between prefix and postfix"""
    array = []
    tf_file = open(file_path)
    for line in tf_file:
        if find_word("^" + prefix + "[A-z]*" + postfix + "$", line):
            array.append(
                find_word(
                    "^" + prefix + "[A-z]*" + postfix + "$",
                    line,
                    prefix,
                    postfix
                )
            )
    return array


def find_word(regexp, line, cut_prefix="", cut_postfix=""):
    """find word between prefix and postfix"""
    result = re.match(regexp, line)
    if result:
        raw_string = "{}".format(result.group(0))
        return raw_string[len(cut_prefix):len(raw_string)-len(cut_postfix)]
    return 0


def text_addition(file_path, test_postfix):
    """adding text to file"""
    tf_file = open(file_path, "a")
    tf_file.write(test_postfix)
    tf_file.close()


def spaces_gen(count):
    """getting N spaces"""
    spases = ""
    for _ in range(count):
        spases = spases + " "
    return spases


def making_variablestf():
    """creating and writing variables.tf-file in examples"""
    tf_file = open("variables.tf")
    text_addition("examples/variables.tf", "\n")
    for line in tf_file:
        text_addition("examples/variables.tf", line)


def making_outputstf():
    """creating and writing outputs.tf-file in examples"""
    outputs_list = get_namelist("output \"", "\" {", "outputs.tf")
    for __var__ in outputs_list:
        output_string = ("\noutput \"" +
                         __var__ +
                         "\" {\n  value = \"${module." +
                         "{{ cookiecutter.example_module_name}}" +
                         "." +
                         __var__ +
                         "}\"\n}\n")
        text_addition("examples/outputs.tf", output_string)


def making_maintf():
    """creating and writing main.tf-file in examples"""
    variables_list = get_namelist("variable \"", "\" {", "variables.tf")
    text_addition(
        "examples/main.tf",
        "\nmodule \"" +
        "{{ cookiecutter.example_module_name}}" +
        "\" {\n"
    )

    bigest_len = 0
    for __var__ in variables_list:
        if bigest_len < len(__var__):
            bigest_len = len(__var__)

    for __var__ in variables_list:

        spases_str = spaces_gen(bigest_len - len(__var__))
        variable_string = ("  " +
                           __var__ +
                           spases_str +
                           " = \"${var." +
                           __var__ +
                           "}\"\n")

        text_addition("examples/main.tf", variable_string)
    text_addition(
        "examples/main.tf",
        "  source" +
        spaces_gen(bigest_len - len("source")) +
        " = \"../../\"\n}\n"
    )


def check_require_vars(varfile_path):
    """Check and show all requare variables (without defailt-value)"""
    prefix = "variable \""
    postfix = "\" {"
    array = []
    variable = []
    variable_array = []

    tf_file = open(varfile_path)

    for line in tf_file:
        result = re.match(r'variable ".*" {$', line, flags=re.MULTILINE)
        if result:
            result_str = "{}".format(result.group(0))
            if result_str[:10] == "variable \"":
                variable_array.append(variable)
                variable = []
        variable.append(line)

    del variable_array[0]

    for __var__ in variable_array:
        flag = False
        for line in __var__:
            result = re.match(r'^  default .*$', line)
            if result:
                flag = True

        if (flag is False and
                find_word(
                    "^" + prefix + "[A-z]*" + postfix + "$",
                    __var__[0]
                )):
            array.append(
                find_word(
                    "^" + prefix + "[A-z]*" + postfix + "$",
                    __var__[0],
                    prefix,
                    postfix
                )
            )
    return array


if __name__ == "__main__":
    main()
