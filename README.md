# Description
Projinit helps initialize a python project with the following structure:
```
<package name>
    - <package name>
        - __init__.py
        - main.py
    - README.md
    - <MIT License>
    - pyproject.toml
```
After installing projinit, you should be able to create a python project with the following command:
```
projinit <full path to project parent directory> <package name>
```
# Prerequisite
This project requires python3. You will also need to install python build package if not present. 

To install build, run:
```
python3 -m pip install build
```

# Build
Following instruction are to build the project
- `git clone https://github.com/aatong/projinit.git`
- `cd projinit`
- `python3 -m build`

# Installing & Running projinit
Once you have build projinit, you should be able to find the wheel package under dist folder.

To install projinit, run:
```
python3 -m pip install <wheel package name>
```

Once package is install, you can run projinit as follows to initalize python project structure:
```
projinit <full path to project parent directory> <package name>
```

*Note*: pyproject.toml is configured to use setuptools as default backend. If you need to use other backend tools, make appropriate changes.

After running the command successfully, you will have a project which can be built into wheel package and run using the same package name. For example, the following creates a helloworld project with a helloworld script.


>$ projinit . helloworld
>
>$ cd helloworld
>
>$ python3 -m build
>
>$ cd dist/
>
>$ python3 -m pip install helloworld-0.0.1-py3-none-any.whl
>
>$ helloworld 
>
>$ Hello World!
>