# python virtual environment cheatsheet

## Default Step_01: For Global Installation and One Time Only
`pip install virtualenv`

## Create a new virtual environment Step_02
`python -m venv env_name`

## Install packages Step_03: For Windows_with_git_bash -
`source env_name/Scripts/activate`

## Install packages Step_04
`pip install package_name`

## Save installed packages to a file Step_05
`pip freeze > requirements.txt`
or 
`pip list --format=freeze > requirements.txt`

## Install packages from a file Step_06
`pip install -r requirements.txt`

## Deactivate the current virtual environment Step_07
`deactivate`



## In Linux or Mac, activate the new python environment
`source env_name/bin/activate`
## Or in Windows
`.\env_name\Scripts\activate`