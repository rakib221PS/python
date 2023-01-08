
f = lambda x: x


def max_fragment(fullList, bool_):
    if (f(bool_) == False):
        return []
    else:
        return fullList


assert max_fragment([], True) == []
assert max_fragment([], False) == []
assert max_fragment([3, 6, 9, 0], True) == [3, 6, 9, 0]
assert max_fragment([3, 6, 9, 0], False) == []

# ----------------------------------------------------------------


def is_constant(seq):
    '''Returns True if seq is empty or has only one value'''
    return len(set(seq)) < 2


def max_fragment(seq, is_constant):
    if (is_constant(seq) != True):
        last_index = 0
        temp_last_index = 0
        total = 0
        tmp_total = 0

        for i in range(1, len(seq)):
            if (seq[i] == seq[i - 1]):
                temp_last_index = i
                tmp_total += 1
            else:
                last_index = max(last_index, temp_last_index)
                total = max(total, tmp_total)
                tmp_total = 0

        if (tmp_total > total):
            total = max(total, tmp_total)
            last_index = max(last_index, temp_last_index)
        return seq[last_index - total:last_index + 1]


s = 'abaaabb'
assert max_fragment(s, is_constant) == 'aaa'
s = 'abaaabbb'
assert max_fragment(s, is_constant) == 'aaa'
s = 'abaaabbbb'
assert max_fragment(s, is_constant) == 'bbbb'

# ---------------------------------------------------------


def max_arithmetic(seq):
    if (len(seq) <= 1):
        return seq
    else:
        last_index = 0
        temp_last_index = 0
        total = 0
        tmp_total = 0

        for i in range(1, len(seq)):
            if(seq[i] == seq[i - 1] + 1):
                temp_last_index = i
                tmp_total += 1
            else:
                last_index = max(last_index, temp_last_index)
                total = max(total, tmp_total)
                tmp_total = 0

        if( tmp_total > total):
            total = max(total, tmp_total)
            last_index = max(last_index, temp_last_index)
        return seq[last_index - total:last_index + 1]


assert max_arithmetic(()) == ()
assert max_arithmetic((100,)) == (100,)
assert max_arithmetic([1, 2, 3, 4]) == [1, 2, 3, 4]
assert max_arithmetic([5, 1, 2, 3, 4]) == [1, 2, 3, 4]
assert max_arithmetic([1, -1, 2, 3, 4]) == [2, 3, 4]
assert max_arithmetic([1, 2, -1, 3, 4]) == [1, 2]