def tribonacci(a = 0, b = 0, c = 1):
    count = 1
    while True:
        if(count == 1):
            count += 1
            yield a
        elif count == 2:
            count += 1
            yield b
        elif count == 3:
            count += 1
            yield c
        else:
            yield a + b + c
            a, b, c = b, c, a + b + c

trib = tribonacci()

assert [next(trib) for n in range(38)] == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274,
                                              504, 927, 1705, 3136, 5768, 10609, 19513,
                                              35890, 66012, 121415, 223317, 410744,
                                              755476, 1389537, 2555757, 4700770, 8646064,
                                              15902591, 29249425, 53798080, 98950096,
                                              181997601, 334745777, 615693474, 1132436852]


trib = tribonacci(-1, 0, 1)
assert [next(trib) for n in range(10)] == [-1, 0, 1, 0, 1, 2, 3, 6, 11, 20]