import os
import argparse
import datetime

from pathlib import Path


def run_flake8(args):
    print('run flake8..')

    if args is not None:
        output_file_name = Path(args).stem + '_flake8_output.log'
        os.system(
            f"flake8 {args} --output-file=tmp/{output_file_name}"
        )


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
