d = {
    (True, True): True,
    (True, False): False,
    (False, True): True,
    (False, False): True
}

def implication(p, q):
    if p and not q:
        return False
    else:
        return True

for (p, q), out in d.items():
    assert implication(p, q) == out
    f'{p} => {q}'
    print("assert passed")