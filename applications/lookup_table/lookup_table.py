# Your code here
import math
import random
import time


faster = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):

    key = (x, y)
    if key in faster:
        print("if key in faster:  \n", faster[key])
        print("<------------------>")
        return faster[key]

    result = slowfun_too_slow(x, y)
    faster[key] = result

    return result


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

# Time: slowfun_too_slow range (500) 9.5367431640625e-07 seconds
# Time Slowfun range(500) 1.1920928955078125e-06 seconds

print(faster, "faster")
start = time.time()
end = time.time()
print(end-start)
