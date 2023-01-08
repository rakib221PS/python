# lab 4 problem 3

# It corresponds to the function whose zero we are looking for.
# when f() is zero within it,

# I did not understand this two condition



from math import isclose, cos, pi

default_abs_tol = 1e-6
def find_root(f, a, b, abs_tol=1e-6):
    # if(b-a<abs_tol):
        return (a+b)/2
        
f = lambda x: x
# z = find_root(f, -1, 2)
# assert isclose(z, 0, abs_tol=default_abs_tol)

z = find_root(cos, 0, pi)
assert isclose(z, pi / 2, abs_tol=default_abs_tol)