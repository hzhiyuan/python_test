'''
Author: Zhiyuan Huang
Contact: 1833472172@qq.com
Description: Python 装饰器，说明装饰器的意义
'''

# 为func函数添加打印函数名的功能
def print_func_name(func):
    def wrapper():
        print(f"[DEBUG]: enter {func.__name__}()")
        func()
    return wrapper


# 1. 不采用装饰器时，为原函数添加一个功能

def hello1():  # 原函数
    print("hello1")

hello1()  # 执行

hello1_warpped = print_func_name(hello1)  # 为原函数手动添加打印函数名功能，并执行
hello1_warpped()


# 2. 采用装饰器后，写法更加优雅

@print_func_name  # 添加装饰器，执行
def hello2():
    print("hello2")

hello2()
