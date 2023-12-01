def part_header(part: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"############ Part {part} ############")
            func(*args, **kwargs)
            print()

        return wrapper

    return decorator
