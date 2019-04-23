# terraform-module-template

[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/terraform-module-template/master/LICENSE)
[![Build Status](https://travis-ci.org/lean-delivery/terraform-module-template.svg?branch=master)](https://travis-ci.org/lean-delivery/terraform-module-template)

## How to use:

pip install cookiecutter

### Create a new module

```
cookiecutter https://github.com/lean-delivery/terraform-module-template
```

Enter for the role name question a value without the tf-module- prefix, e.g. example.

Make changes in the corresponding files: copyright section in LICENSE, badge section in README.md, etc.

### Update an existing module

If you want to update an existing module that was created using terraform-module-template (.cookiecutter.yml file exists in the repository) then:

1. cd tf-module-NAME
2. cookiecutter https://github.com/lean-delivery/terraform-module-template --output-dir .. --overwrite-if-exists --config-file .cookiecutter.yml --no-input
3. git status
4. git add . -p

```
Useful commands:
- y - add this hunk to commit
- n - do not add this hunk to commit
- d - do not add this hunk or any of the later hunks in this file
- s - split the current hunk into smaller hunks
- e - manually edit the hunk
```

5. git commit -m "Updated by cookiecutter and terraform-module-template"
6. get rid of the garbage (rm or git clean)

### Upgrade a module

If you have a terraform module that was created without terraform-module-template (.cookiecutter.yml does not exist) then:

1. cd tf-module-NAME
2. cookiecutter https://github.com/lean-delivery/terraform-module-template --output-dir .. --overwrite-if-exists
3. proceed with the corresponding "Update an existsing module" steps


# Terratest template

## Description
This tool is designed to automatically generate a simple test pattern for [Terraform](https://www.terraform.io/) modules using [Terratest](https://github.com/gruntwork-io/terratest). Tool automatically creates additional folders and adds the files necessary for the tests. The only test added by this script checks the possibility to create and destroy a resource created by your terraform module.

## How to use:

Run cookiecutter with key "--overwrite-if-exists" ...

```hcl
cookiecutter https://github.com/lean-delivery/terraform-module-template --overwrite-if-exists
```
... and enter your data as you entered before. **WARNING! FOR QUESTION “creating_tests” ENTER “Yes”**
```hcl
creating_tests [No]: Yes
module_name [default_module]:
Select license:
1 - Apache
2 - MIT
3 - BSD-3
4 - GPLv3
Choose from 1, 2, 3, 4 [1]:
author_name [Lean Delivery Team <team@lean-delivery.com>]:
company_name [EPAM Systems]:
role_description [Yet Another Terraform Module From Lean Delivery]:
issue_tracker_url [https://github.com/lean-delivery/tf-module-default_module/issues]:
aws_region [us-east-1]:
example_module_name [example_module]:
```

For running test:
go to folder 'test/'
```hcl
go test
```

## Files to be added
 * examples/main.tf
 * examples/variables.tf
 * examples/outputs.tf
 * [test/tf_module_test.go](tf-module-%7B%7B%cookiecutter.module_name%20%7D%7D/test/tf_module_test.go)

## tf_module_test.go
In order to avoid a name conflict during execution, a random line of text is added to the name of the resource. By default, the name is set by the parameter "name" in the description of the structure that is passed to the module as input parameters.
```hcl
Vars: map[string]interface{}{
    "aws_region": region,
    "name"      : "test_name_" + randSeq(10),
},
```
If the variable name or any other identifier of your resource has a different name, change this name in [tf_module_test.go](tf-module-%7B%7B%cookiecutter.module_name%20%7D%7D/test/tf_module_test.go).
If your module has require variables, tool shows to you list with these variables. WARNING! Add these variables to [tf_module_test.go](tf-module-%7B%7B%cookiecutter.module_name%20%7D%7D/test/tf_module_test.go)


## Terraform versions
Terraform v0.11.13


## GO versions
go version go1.12 darwin/amd64


## Python version
Python 3.7.0 (Jun 26 2018)
