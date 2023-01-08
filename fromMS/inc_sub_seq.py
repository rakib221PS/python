## Version for sequences
def increasing_sub_seq(seq):
    if not seq: ## If empty
        return 
    
    mx = seq[0] ## Current maximum
    yield mx
    
    for a in seq[1:]:
        if a > mx:
            mx = a
            yield mx

## Version for any iterable object
def increasing_sub_seq(it):
    it = iter(it)
    
    try:
        mx = next(it)
    except StopIteration:
        return
    
    yield mx
    
    for a in it:
        if a > mx:
            mx = a
            yield mx

assert list(increasing_sub_seq([])) == []
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

it = iter([1, 3, 3, 8])
assert list(increasing_sub_seq(it)) == [1, 3, 8]