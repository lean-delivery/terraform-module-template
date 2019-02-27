# terraform-development-kit

## How to use:

pip install cookiecutter

### Create a new module

```
- cookiecutter https://github.com/lean-delivery/terraform-development-kit
```

Enter for the role name question a value without the tf-module- prefix, e.g. example.

Make changes in the corresponding files: copyright section in LICENSE, badge section in README.md, etc.

### Update an existing role

1. cookiecutter https://github.com/lean-delivery/terraform-development-kit --output-dir .. --overwrite-if-exists --config-file .cookiecutter.yml --no-input
2. git status
3. git add . -p

```
Useful commands:
- y - add this hunk to commit
- n - do not add this hunk to commit
- d - do not add this hunk or any of the later hunks in this file
- s - split the current hunk into smaller hunks
- e - manually edit the hunk
```

4. git commit -m "Updated by cookiecutter and terraform-development-kit"
5. get rid of the garbage (rm or git clean)
