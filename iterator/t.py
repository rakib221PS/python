import copy
def connect_alternately(list1, list2):
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