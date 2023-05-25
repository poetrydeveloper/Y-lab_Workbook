def get_fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


def zeros(n):
    res = 0
    count = list(str(get_fact(n)))

    for el in reversed(count):
        if el != '0':
            break
        else:
            res += 1
    return res


if __name__ == "__main__":
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
