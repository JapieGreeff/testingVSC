"""
A simple class with functions for use in the classroom to demo
"""
class Dog:
    #class attribute
    species = 'Mammal'
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def speak(self):
        print('Woof')

# at this point dog is defined, and we can use it in our code
lassie = Dog('lassie', 5)
lassieTwo = Dog('lassie', 5)
benji = Dog('benji', 5)

# the references to the objects can go in a list
doglist = []
doglist.append(lassie)
doglist.append(lassieTwo)
doglist.append(benji)

#when comparing objects it is looking at the pointer in memory 
print(lassie == lassieTwo)

#lists of objects can be iterated over
for dog in doglist:
    print(f'{dog.name} is a {dog.age} year old {dog.species}')
    dog.speak()


