def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element


list(chain([2,3,4,5],[7,8,9,0]))