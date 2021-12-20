
# *args is used to pass the n number of arguements

# def func1(*args):
#     for i in args:
#         print(i)


def func1(*args,**kwargs):
    for i in kwargs.items():
        print(i)

func1(a=10,b=20,c=30,d=40,e=50)

