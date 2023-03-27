def type_check(parameter):
    def decorator(func):
        def wrapper(*args):

            for el in args:
                if not isinstance(el, parameter):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
