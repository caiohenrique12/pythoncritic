import os
import argparse

from pathlib import Path

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('src/pythoncritic/templates'))


def run_flake8(args):
    print('run flake8..')
    output_file_name = None

    if args is not None:
        output_file_name = Path(args).stem + '_flake8_output.json'
        os.system(
            f"flake8 --format=json {args} > tmp/{output_file_name}"
        )

    template = env.get_template('flake8.html')

    with open('tmp/flake8_output.html', 'w') as f:
        breakpoint()
        f.write(template.render(data=output_file_name))


def run_black(args):
    print('run black..')
    cmd = None
    output_file_name = Path(args).stem + '_black_output.log'

    if args is not None:
        cmd = f"black --check {args} 2> >(tee -a tmp/{output_file_name} >&2)"
    else:
        cmd = "black"

    os.system(cmd)

def run_coverage():
    print('initializing coverage..')


def pythoncritic():
    print("run all tools")


parser = argparse.ArgumentParser(prog='pythoncritic')
subparsers = parser.add_subparsers(title="subcommands", help="improve your code")

arg_template = {
    "dest": "operands",
    "type": str,
    "nargs": '*',
    "metavar": "OPERAND",
    "help": "print hello world",
}


add_parser = subparsers.add_parser('flake8', help='run flake8 in your project')
add_parser.add_argument(**arg_template)
add_parser.set_defaults(func=run_flake8)


add_parser = subparsers.add_parser('black', help='run black in your project')
add_parser.add_argument(**arg_template)
add_parser.set_defaults(func=run_black)


add_parser = subparsers.add_parser('coverage', help='run coverage in your project')
add_parser.add_argument(**arg_template)
add_parser.set_defaults(func=run_coverage)


add_parser = subparsers.add_parser('pythoncritic', help='run flake8, black, and coverage')
add_parser.add_argument(**arg_template)
add_parser.set_defaults(func=pythoncritic)


args = parser.parse_args()

print(args.func(*args.operands))
