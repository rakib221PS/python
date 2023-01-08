number = 100

# z = lambda num: num
# def adder_factory(num):
#     return z(num)

def adder_factory(x):
    return x

f = adder_factory(lambda x: x)

# f = adder_factory
sum = 0
for x in range(0,number+1):
    sum = sum + f(x)

print(sum)