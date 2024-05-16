def lcm(a, b):
    for l in range(min(a,b), a * b + 1):
        # print(l)
        if l % a == 0 and l % b == 0:
            return l

    assert False


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

