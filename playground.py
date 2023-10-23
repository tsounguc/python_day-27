def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 5, 6))
