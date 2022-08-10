def get_sum(a, b):
    c = 0
    while b!=0:
        c = a&b
        a ^= b
        b = c << 1
    return a


if __name__ == '__main__':
    print(get_sum(-3, 10))