import itertools
value = None
def predicate(x): return x > value

def increasing_sub_seq(seq):
    l = len(seq)
    if l <= 0:
        return seq
    yield seq[0]
    for i in range(1, l):
        if(seq[i]>seq[i - 1]):
            yield seq[i]
    

assert list(increasing_sub_seq([])) == []
assert list(increasing_sub_seq([3])) == [3]
assert list(increasing_sub_seq([1, 3, 3, 8])) == [1, 3, 8]
assert list(increasing_sub_seq([7, 3, 2, 8])) == [7, 8]
assert list(increasing_sub_seq([7, 3, 2, 1])) == [7]


gen = increasing_sub_seq([7, 3, 10, 2, 1])
assert next(gen) == 7
assert next(gen) == 10

try:
    next(gen)
except StopIteration:
    pass
else:
    raise AssertionError('Empty iterator.')
