import os


def run_black(args):
    breakpoint()
    print('run black..')
    cmd = None

    if args is not None:
        cmd = f"black {args}"
    else:
        cmd = "black"

    os.system(cmd)