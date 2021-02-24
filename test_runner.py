from importlib import import_module


def run_fn(fn_name, *args):
    p, m = fn_name.rsplit('.', 1)

    mod = import_module(p)

    fn = getattr(mod, m)

    return fn(*args)


if __name__ == '__main__':
    result = run_fn('function.fn', "hello")
    print("OUT:", result)
