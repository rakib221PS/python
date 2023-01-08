# Python Program illustrating
# numpy.flip() method

import numpy as geek

array = geek.arange(8).reshape((2,2,2))
print("Original array : \n", array)

print("Flipped array : \n", geek.flip(array, 1))
