def diff(seq):
    if len(seq) <= 1:
        return seq ## Simply return, without value
    for v, w in zip(seq[:-1], seq[1:]): ## Looks good!
        yield w - v


seq = [3, 1, 6, 10, 20]
gen = diff(seq)
assert list(gen) == [-2, 5, 4, 10]

seq = []
gen = diff(seq)
assert list(gen) == []
seq = [1]
gen = diff(seq)
assert list(gen) == []

def diff_it(it):
    iterator_list = list(it) ## it may be infinite!
    # for i in it:
    #     yield next(it) - i
    if len(iterator_list) <= 1:
        return iterator_list
    for v, w in zip(iterator_list[:-1], iterator_list[1:]):
        yield w - v

it = iter([3, 1, 6, 10, 20])
gen = diff_it(it)
assert list(gen) == [-2, 5, 4, 10]

it = iter([])
gen = diff_it(it)
assert list(gen) == []
it = iter([1])
gen = diff_it(it)
assert list(gen) == []