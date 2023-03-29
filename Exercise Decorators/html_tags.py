def tags(parameter):
    def decorator(func):
        def wrapper(*args):
            return f"<{parameter}>{func(*args)}</{parameter}>"

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

