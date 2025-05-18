class Person:

    # create a class variable called amount
    amount = 0

    # all methods in class must contain self
    def __init__(self, name, age, height):

        # following are called attributes of the person
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1 # a class variable have to be accessed through class name

    # this function is called when use function del
    # it is also called at the end
    def __del__(self):
        Person.amount -= 1
        print("Object '{}' deleted!".format(self.name))

    # what do I get if I print some instance
    def __str__(self):
        return "Name: {}, Age: {}, Height:{}".format(self.name, self.age, self.height)

    def get_older(self, years):
        self.age += years

# when creating instance do not need to call init 
# just use the class name
person1 = Person("Mike", 23, 183)
person2 = Person("Henry", 20, 175)

print(Person.amount)

person1.name = "Tommy"
print(person1.name)
del person1

print(Person.amount)
print(person2)