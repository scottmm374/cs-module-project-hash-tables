import time  # Your code here

seq_dict = {}


def expensive_seq(x, y, z):
    if x <= 0:
        return y + z

    # else:
    #     return expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    key = (x, y, z)
    if key in seq_dict:
        # print("if key in faster:  \n", seq_dict[key])
        # print("<------------------>")
        return seq_dict[key]

    result_1 = expensive_seq(x-1, y+1, z)
    result_2 = expensive_seq(x-2, y+2, z*2)
    result_3 = expensive_seq(x-3, y+3, z*3)
    results = result_1 + result_2 + result_3
    seq_dict[key] = results

    return results


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")


# print(expensive_seq(2, 3, 4))
# print(expensive_seq(4, 6, 8))
# print(expensive_seq(6, 9, 12))
# print(expensive_seq(30, 45, 50))

    print(expensive_seq(150, 400, 800))
# Calculating  0.000000953674316 seconds(30, 45, 50) with Cache
# Calculating  0.000002145767212 seconds(30, 45, 50)
# Calculating  0.000000953674316 seconds(150, 400, 800) with Cache

# start = time.time()
# end = time.time()
# print(f"Calculating  {(end - start):.15f} seconds")
