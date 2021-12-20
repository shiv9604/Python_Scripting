# class method = where we can call directly the function without defining the object to the class
# static method = where we have to define the object to the class and then we can call it...

class employee:

    @classmethod
    def greet(self):
        print("Good Morning Sir..")

    @staticmethod
    def greetspecific(name):
        print(f"Good Morning {name}")

employee.greet()
employee.greetspecific("Shiv")