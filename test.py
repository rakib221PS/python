	
import itertools
predicate = lambda x : x < 5
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x

print ("The values after condition returns false : ", end ="")
print (list(dropwhile(predicate, [1,4,6,4,1])))
