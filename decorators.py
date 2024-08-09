from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except Exception as e:
            print(f"{type(e)}: {e}")

    return inner
