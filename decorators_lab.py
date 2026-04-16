# def outer():
#     def inner():
#         print("Inner")
#     return inner

# f = outer()
# f()

def my_decorator(func):
    def wrapper():
        print("🔵 לפני הפונקציה")
        func()
        print("🔴 אחרי הפונקציה")
    return wrapper

def say_hello():
    print("Hello")
say_hello = my_decorator(say_hello)
say_hello()