# Your code here
import math
import random
import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# TODO finish this


def slowfun(x, y):
    pass
    # faster = {}

    # x = faster[0]
    # y = faster[1]

    # if not in faster:
    #     faster[[x][y]] = (x, y)


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')


start = time.time()
end = time.time()
print(f"Calculating too slow took {(end - start):.5f} seconds")

start = time.time()
# slowfun(x, y, {})
end = time.time()
print(f"Calculating slowfun took {(end - start):.5f} seconds")
