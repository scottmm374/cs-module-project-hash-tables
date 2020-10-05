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


def slowfun(x, y):
    pass

    # Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

start = time.time()
slowfun_too_slow(x, y)
end = time.time()
print(f"Calculating too slow took {(end - start):.5f} seconds")

start = time.time()
# slowfun(x, y, {})
end = time.time()
print(f"Calculating slowfun took {(end - start):.5f} seconds")
