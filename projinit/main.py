import subprocess
import argparse

from projinit.license import license

toml_template = '''
    cat >> {} << EOF
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "{}"
version = "0.0.1"
requires-python = ">=3.13.0"
readme = "README.md"
dependencies = []

[project.scripts]
{} = "{}.main:main"
EOF
'''

main_template = '''
def main():
    print('Hello World')

if __name__ == '__main__':
    main()
'''
def run_command(cmd):
    # Run the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, shell=True)
    
    stdout, stderr = process.communicate()

    if stdout:
        print(f"output: \n{stdout}")

    # Throw exception if not successful
    if process.returncode != 0:
        raise Exception(f"Error processing {cmd}. Error = {stderr}")

def get_args():
    parser = argparse.ArgumentParser(
                    prog='projinit',
                    description='setups up a python project')
    parser.add_argument('filepath', help="Full project path to create python project directory structure")
    parser.add_argument('name', help="Package Name of the project")
    args = parser.parse_args()
    
    return args

def main():
    args = get_args()
    print(f"Full path = {args.filepath}, package name = {args.name}")

    #Create the python directory structures
    run_command(f"mkdir -p {args.filepath}/{args.name}/{args.name}")
    #Create __init__.py
    run_command(f"touch {args.filepath}/{args.name}/{args.name}/__init__.py")
    #Create README.md
    run_command(f"echo \"#{args.name} package\" > {args.filepath}/{args.name}/README.md")
    #Create toml project
    toml = toml_template.format(args.filepath + '/' + args.name + '/pyproject.toml', args.name, args.name, args.name)
    run_command(toml)
    #Create MIT license
    run_command(f"cat > {args.filepath}/{args.name}/LICENSE << EOF {license['mit']}")
    #Create the main script entry point
    run_command(f"cat > {args.filepath}/{args.name}/{args.name}/main.py << EOF {main_template}")

if __name__ == '__main__':
    main()
    