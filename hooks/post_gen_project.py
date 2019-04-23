import re
import shutil

def main():
    if "{{ cookiecutter.creating_tests }}" != "Yes":
        shutil.rmtree("examples/")
        shutil.rmtree("test/")
        return 0

    restoring_from_backup("backup/")
    making_maintf()
    making_outputstf()
    making_variablestf()
    require_vars = check_require_vars("variables.tf")
    for __index__ in range(len(require_vars)):
        print("Warning! Require vriable: " + require_vars[__index__])

def restoring_from_backup(path):
    shutil.copyfile(path + "main.tf", "main.tf")
    shutil.copyfile(path + "variables.tf", "variables.tf")
    shutil.copyfile(path + "outputs.tf", "outputs.tf")
    shutil.rmtree(path)

def get_namelist(prefix, postfix, file_path):
    array = []
    file = open(file_path)
    for line in file:
        if find_word("^" + prefix + "[A-z]*" + postfix + "$", line):
            array.append(find_word("^" + prefix + "[A-z]*" + postfix + "$", line, prefix, postfix))
    return array



def find_word(regexp, line, cut_prefix = "", cut_postfix = ""):
    result = re.match(regexp, line)
    if result:
        raw_string = "{}".format(result.group(0))
        return raw_string[len(cut_prefix):len(raw_string)-len(cut_postfix)]



def text_addition(file_path, test_postfix):
    file = open(file_path, "a")
    file.write(test_postfix)
    file.close()



def spaces_generator(count):
    spases = ""
    for _ in range(count):
        spases = spases + " "
    return spases



def making_variablestf():
    file = open("variables.tf")
    text_addition("examples/variables.tf", "\n")
    for line in file:
        text_addition("examples/variables.tf", line)



def making_outputstf():
    outputs_list = get_namelist("output \"", "\" {", "outputs.tf")
    for __index__ in range(len(outputs_list)):

        output_string = (
                            "\noutput \"" +
                            outputs_list[__index__] +
                            "\" {\n  value = \"${module." +
                            "{{ cookiecutter.example_module_name}}" +
                            "." +
                            outputs_list[__index__] +
                            "}\"\n}\n"
                        )

        text_addition("examples/outputs.tf", output_string)



def making_maintf():
    variables_list = get_namelist("variable \"", "\" {", "variables.tf")
    text_addition("examples/main.tf", "\nmodule \"" + "{{ cookiecutter.example_module_name}}" + "\" {\n")

    bigest_len = 0
    for __index__ in range(len(variables_list)):
        if bigest_len < len(variables_list[__index__]):
            bigest_len = len(variables_list[__index__])

    for __index__ in range(len(variables_list)):

        variable_string = (
                            "  " +
                            variables_list[__index__] +
                            spaces_generator(bigest_len - len(variables_list[__index__])) +
                            " = \"${var." +
                            variables_list[__index__] +
                            "}\"\n"
                        )

        text_addition("examples/main.tf", variable_string)
    text_addition("examples/main.tf", "  source" + spaces_generator(bigest_len - len("source")) + " = \"../../\"\n}\n")



def check_require_vars(varfile_path):
    prefix = "variable \""
    postfix = "\" {"
    array = []
    variable = []
    variable_array = []

    file = open(varfile_path)

    for line in file:
        result = re.match(r'variable ".*" {$', line, flags=re.MULTILINE)
        if result:
            result_str = "{}".format(result.group(0))
            if result_str[:10] == "variable \"":
                variable_array.append(variable)
                variable = []
        variable.append(line)

    del variable_array[0]

    for __index__ in range(len(variable_array)):
        flag = False
        for line in variable_array[__index__]:
            result = re.match(r'^  default .*$', line)
            if result:
                flag = True

        if flag != True and find_word("^" + prefix + "[A-z]*" + postfix + "$", variable_array[__index__][0]):
            array.append(find_word("^" + prefix + "[A-z]*" + postfix + "$", variable_array[__index__][0], prefix, postfix))
    return array



if __name__== "__main__":
    main()
