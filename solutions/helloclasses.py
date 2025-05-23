'''

>>> fido = Dog("Fido")
>>> fido.describe()
'Fido the dog says: Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.describe()
'Fifi the kitty cat says: Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.describe()
'Nemo the fish says: '

'''

# Write your code here:

class Pet:
    sound = ''
    type = ''

    def __init__(self, name):
        self.name = name

    def describe(self):
        return "{} the {} says: {}".format(self.name, self.type, self.sound)


class Dog(Pet):
    sound = 'Woof!'
    type = 'dog'


class Cat(Pet):
    sound = 'Meow!'
    type = 'kitty cat'


class Fish(Pet):
    sound = ''
    type = 'fish'
# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# From Powerful Python. Copyright MigrateUp LLC. All rights reserved.
