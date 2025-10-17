def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.get('count')
        result = None
        for _ in range(count):
            result = func(*args)
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)

example('print me', count = 3)
