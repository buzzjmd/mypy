# Notes

## Setup github repository

Create an empty github repository buzzjmd/mypy
* public
* dont create any of the suggested files


## Setup local repository

Create a file called README.md and add the text "# mypy-cli"

```
$ git init -b main
$ git add README.md
$ git commit -m "initial commit"
```

## Connect local repository to github

```
$ git remote add origin https://github.com/buzzjmd/mypy-cli.git
$ git push -u origin main
```

## Create and move to `dev` branch

```
$ git checkout -b dev
```
Work from this dev branch, merging to main branch when appropriate

## Create .gitignore

As this is a python package get the standard Python `.gitignore` file from [github/gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore).