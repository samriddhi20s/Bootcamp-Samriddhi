#Static Variables and Methods: Explore the use of static variables and methods in a class.
#Example: Track the number of instances created for a class using a static variable.
class MyClass:
    # Static variable to count instances
    instance_count = 0

    def __init__(self):
        MyClass.instance_count += 1

    @staticmethod
    def get_instance_count():
        # Static method to access the static variable
        return MyClass.instance_count

# Creating instances of the class
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

# Accessing the static method to get the count of instances
print(f"Number of instances created: {MyClass.get_instance_count()}")  
