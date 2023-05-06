#1


def my_decorator_func(func):
    def wrapper():
        print(10 + 10)
        func()
    return wrapper


@my_decorator_func
def func1():
    print(10)
func1()


#2

import time

def time_function(func):

    def wrapper(*args , **kwargs):
        start_time = time.time()
        result = func(*args , **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result
    return wrapper


@time_function
def tm():
    time.sleep(2)
tm()


#3



