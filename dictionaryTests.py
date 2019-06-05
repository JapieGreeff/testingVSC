from collections import *

#dictionaries - looping over the keys
d = {'first':'gold', 'second':'silver', 'third':'bronze'}
for k in d:
    print(f'{k}: {d[k]}')

#if you want to mutate the dictionary then you can get the keys as a new list and iterate over them
for k in list(d.keys()):
    if k == 'first':
        del d[k]
print(d)

#looping over a dictionary and getting the key value pair without indexing
for k,v in d.items():
    print(f'{k} : {v}')

# constructing a dictionary from two separate lists
keys = ['first','second','third']
values = ['gold','silver','bronze']
dic = dict(zip(keys, values))
print(dic)

# counting with a dictionary.

d = {}
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    if colour not in d:
        d[colour] = 0
    d[colour] += 1
print(d)

# dictionary get can take a default parameter though, so the same can be achieved with
d = {}
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    d[colour] = d.get(colour, 0) + 1
print(d)

# another option is to use a default dictionary where you specify the type of item will be in the dict and it uses that kind of default
d = defaultdict(int)
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    d[colour] += 1
print(d)

# default dict can also make use of more complex types
d = defaultdict(list)
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    d[colour].append(True) 
print(d)

# grouping with dictionary
d = {}
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    key = len(colour)
    if key not in d:
        d[key] = []
    d[key].append(colour)
print(d)

# you can also use set default - this will return the dictionary item if it is there or the default if it is not
d = {}
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    key = len(colour)
    d.setdefault(key, []).append(colour)
print(d)

# or you can use the defaultdict again
d = defaultdict(list)
colours = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for colour in colours:
    key = len(colour)
    d[key].append(colour)
print(d)

#popitem is an atomic operation
d = {'first':'gold', 'second':'silver', 'third':'bronze'}
while d:
    key, value = d.popitem()
    print(f'{key} : {value}')
print(d)
