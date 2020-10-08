import time  # Your code here


def expensive_seq(x, y, z):

    if x <= 0:
        return y + z
    else:
        return expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    # if __name__ == "__main__":
    #     for i in range(10):
    #         x = expensive_seq(i*2, i*3, i*4)
    #         print(f"{i*2} {i*3} {i*4} = {x}")


# print(expensive_seq(2, 3, 4))
# print(expensive_seq(4, 6, 8))
# print(expensive_seq(6, 9, 12))
print(expensive_seq(30, 45, 50))

# print(expensive_seq(150, 400, 800))


start = time.time()
end = time.time()
print(f"Calculating too slow took {(end - start):.5f} seconds")
