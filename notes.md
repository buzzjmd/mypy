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
$ git remote add origin https://github.com/buzzjmd/mypy.git
$ git push -u origin main
```


## Create and move to `dev` branch

```
$ git checkout -b dev
```
Work from this dev branch, merging to main branch when appropriate


## Create .gitignore

As this is a python package get the standard Python `.gitignore` file from [github/gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore).


## Best Practice for Python Projects

[Semantic Versioning](https://semver.org/)

[Conventionsal commits](https://www.conventionalcommits.org/)
* examples are:
* [When to use “chore” as type of commit message? | stackoverflow](https://stackoverflow.com/questions/26944762/when-to-use-chore-as-type-of-commit-message)
* [Karma - Git Commit Msg](http://karma-runner.github.io/0.10/dev/git-commit-msg.html)
* [conventional-changelog/commitlint](https://github.com/conventional-changelog/commitlint)

Information about using pipenv to install packages locally so that they are editable is described in the [pipenv docs here](https://docs.pipenv.org/basics/#editable-dependencies-e-g-e). This is know as 'Editable Dependencies'

Git Flow


## Create Hello World Package

Create the package.

Create setup.py for the package
```
from setuptools import setup, find_packages

setup(name='mypy',
      version='0.1.0',
      description='My Python Library',
      author='buzzjmd',
      author_email='buzzjmd@gmail.com',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},  
)
```

Once setup.py has been created, install the package locally and run it
```
$ pipenv install --dev '-e .'
$ pipenv run python -m mypy
$ pipenv python -c"import mypy.greet; mypy.greet.hello_world()"
```

To remove all artifacts created by pipenv run
```
$ pipenv --rm
```
and delete the egg-info in src, and the files Pipfile, Pipfile.lock and pyproject.toml


## Modify the package

When the package is modified it is necessary to rerun
```
$ pipenv install --dev '-e .'
```


## Create a runable script

This is done by adding entry points to setup.py
```
      entry_points={
            'console_scripts': [
                  'mypy = mypy.greet:hello_world'
      ]},
``` 

