import time


def no_dups(s):
    new_str = s.split()
    return (" ".join(sorted(set(new_str), key=s.index)))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

    start = time.time()
    no_dups("spam spam spam eggs spam sausage spam spam and spam")
    end = time.time()
    print(f"Calculating noDupes {(end - start):.10f} seconds")
