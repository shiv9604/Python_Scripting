
def func1(called_func):
    print("This is the first main function")
    def func2(called_func):
        print("This is second function inside the function")
        called_func()
    return func2(called_func)

@func1
def func3():
    print("This is the third function and the outer function which is not related to the above functions...")

# func1(func3) # --> we are passing the func3 as a object in the func1
func3()