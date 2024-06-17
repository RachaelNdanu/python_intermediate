import functools

def start_end_decorator(func):
     @functools.wraps(func)
     def wrapper(*args, **kwargs):
        print('start')
        result = func (*args , **kwargs) 
        print(result)
        print('end')
        
        return result
     return wrapper


@start_end_decorator
def add5(x):
    return x + 5

add5(10)