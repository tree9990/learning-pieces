class Cache:
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self, *args, **kwargs):
        func = self.func
        data = self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            print('cached')
            print(key, result)

        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
            print(key, result)
        return result

@Cache
def rectangle_area(length, width):
    return length * width

rectangle_area(2, 3)
# calculated
# 6

rectangle_area(2, 3)
# cached
# 6
