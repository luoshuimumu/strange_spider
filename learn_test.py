import functools


def outer(text='lsmm'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('outer call %s,%s' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@outer()
def inner(text='None'):
    print('inner call ',text)

inner()
print(inner.__name__)
