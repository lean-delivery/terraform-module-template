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
