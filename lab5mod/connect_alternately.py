import copy
def connect_alternately(list1, list2): ## Lists are less general than iterables
    # size1 = len(list1) giving error.
    a = copy.copy(list1)
    size1 = len(a)
    if size1 <= 0:
        return []
    b = copy.copy(list2)
    size2 = len(b)
    if size1 <= size2:
        for i in range(size1):
            yield list1[i]
            yield list2[i]
    else:
        for i in range(size2):
            yield list1[i]
            yield list2[i]
        yield list1[size2]
        
def connect_alternately(it1, it2):
    it1 = iter(it1)
    it2 = iter(it2)
    
    while True:
        for it in [it1, it2]:
            try:
                yield next(it)
            except StopIteration:
                return

assert list(connect_alternately('abc', 'xyz')) == list('axbycz')
assert list(connect_alternately('abc', 'xy')) == list('axbyc')
assert list(connect_alternately('ab', 'xyz')) == list('axby')
assert list(connect_alternately('abc', '')) == ['a']
assert list(connect_alternately('', 'xyz')) == []
assert list(connect_alternately([1, 2], [3, 4])) == [1, 3, 2, 4]

it = connect_alternately((1, 2), 'a')

assert next(it) == 1
assert next(it) == 'a'
assert next(it) == 2

try:
    next(it)
except StopIteration:
    pass
else:
    raise AssertionError('Generator is empty.')

# if we pass 7, 10, 100000000 or more agruments through *iterables than how to handle it easily? 

## Same solution as for 2 parameters
def connect_alternately(*iterable):
    iterable = [iter(it) for it in iterable]
    
    while True:
        for it in iterable:
            try:
                yield next(it)
            except StopIteration:
                return


assert list(connect_alternately()) == []
assert list(connect_alternately('a', 'xy', 'uvw')) == list('axu')
assert list(connect_alternately('abc', 'xy', 'u')) == list('axuby')
assert list(connect_alternately('abc', 'kl', '', 'u')) == list('ak')