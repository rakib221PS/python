## I sent You a solution in previous email.
gen = lattice()

assert next(gen) == (0, 0)
assert next(gen) == (1, 0)
assert next(gen) == (1, 1)
assert next(gen) == (0, 1)
assert [next(gen) for _ in range(5)] == [(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]

gen = lattice()
for _ in range(63):
    next(gen)

assert next(gen) == (0, 7)