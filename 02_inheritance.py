class Person:

    def __init__(self, name, age, height):

        # following are called attributes of the person
        self.name = name
        self.age = age
        self.height = height

    def __del__(self):
        print("Object '{}' deleted!".format(self.name))

    def __str__(self):
        return "Name: {}, Age: {}, Height:{}".format(self.name, self.age, self.height)

    def get_older(self, years):
        self.age += years

# put person in parentheses to indicate their parent class
class Worker (Person):

    def __init__(self, name, age, height, salary):
        # call the constructor function from the parent class
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        return super(Worker, self).__str__() + ", Salary: {}".format(self.salary)

    def calc_yearly_salary(self):
        return self.salary * 12
    
worker1 = Worker("Henry", 40, 176, 2000)
print(worker1)
print(worker1.calc_yearly_salary())

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return "X: {}, Y:{}".format(self.x, self.y)
    
v1 = Vector(2, 8)
v2 = Vector(-3, 5)

v3 = v1 + v2
print(v3)
