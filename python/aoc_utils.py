from time import time


def part_header(part: int):
    """
    Prints a header and some new line spacing for the Advent of Code solutions
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"############ Part {part} ############")
            func(*args, **kwargs)
            print()

        return wrapper

    return decorator


def highlight(text: str, color: str = "red", padding: int = 0) -> str:
    """
    Deocorates the text by returning the string with appropriate color code.
    """
    colors = {
        "black": "\x1b[30m",
        "red": "\x1b[0;30;41m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[4;30;46m",
        "magenta": "\x1b[35m",
        "cyan": "\x1b[36m",
        "white": "\x1b[37m",
    }

    if color in colors:
        this_color = colors[color]
    else:
        this_color = color

    return f"{this_color}{text:{padding}}\x1b[0m"


def timer_func(func):
    """
    Prints the execution time of the decorated function
    """

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        # print(f"Function {func.__name__!r} executed in {(t2 - t1):.5f}s")
        print(f"\n\tTime: {(t2 - t1):.5f}s")
        return result

    return wrap_func
