"""
Simple Python things that are very different to C like languages
"""
from collections import *

# range returns an iterable range object. Looks 
for i in range(6):
    print(i)

# range is different to what it was in python 2 where a list was returned.
a = [0,1,2]
b = range(3)
print(type(a) == type(b))
# range is not a list like it was in python 2.x, it now is an object of type range. 

# iteration is the standard way of looping - it is like foreach in other languages
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
for colour in colours:
    print(colour)
# to iterate in reverse use reversed which works on lists
for colour in reversed(colours):
    print(colour)
# to get the idex as well if you need it
for i, colour in enumerate(colours):
    print(f'{i} = {colour}')

#looping over two lists simultaniously (will only loop till the smallest list is completed) using a zip object
names = ['rendani','alice', 'bob', 'carol', 'dan']
surnames = ['smith','abrahams','burt', 'cleeves', 'du roodt']
for name, surname in zip(names, surnames):
    print(f'{name} {surname}')

# you can also iterate over a sorted list that is sorted by a key function 
# sorting by the surnames by selecting the second variable using a lambda function
for name , surname in sorted(zip(names, surnames), key=lambda x:x[1]):
    print(f'{name} {surname}')

# sorting by the length of the names from longest to shortest (just remember the key is a function)
for name in sorted(names, key=len, reverse=True):
    print(f'{name}')

# instead of flag variables we can use the else statement on for loops which runs if it was not stopped by break
def findValue(target, coll):
    for i in coll:
        if i == target:
            break
    else:
        return -1
    return i

values = range(9)
print(findValue(5, values))
print(findValue(11, values))

# it is worth remembering that named tuples are compatible with tuples
TestTuple = namedtuple('tupleA', ['valueOne', 'valueTwo'])
a = TestTuple(1,2)
print(f'{a} {a[0]} {a[1]}')

#sequences are like tuples, but can be unpacked as follows
seq = 'hello ', 'world ', 'and also japie', 100
hello, world, text, number = seq
print(hello)


#when you are writing and importing modules, the following structure lets you run things if it is the main file, or not if it is imported
def run():
    print('hello world!')

if __name__ == "__main__":
    run()