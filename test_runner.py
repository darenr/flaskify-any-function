from importlib import import_module

import sys

def run_fn(fn_name, *args):
    p, m = fn_name.rsplit('.', 1)

    mod = import_module(p)

    fn = getattr(mod, m)

    return fn(*args)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} <function.fn> <arg>")
    else:
        result = run_fn(sys.argv[1], *sys.argv[2:])
        print("OUT:", result)
