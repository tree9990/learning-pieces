def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print ("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print ("say {}!".format(something))

say("hihihihi")
