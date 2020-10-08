import time

with open("robin.txt") as f:
    words = f.read()


# def hist(words):
    histo_dict = {}

  # removes special characters from string
    remove_Special_Chars = words.translate(
        {ord(c): " " for c in "\"!@  # $%^&*()[]{};:,./\\<>?|`~-=_+"}).lower().split()

    max_len = len(max(remove_Special_Chars, key=len))

    for word in remove_Special_Chars:
        words = word

    # if the string does not exist yet
        if word not in histo_dict:
            number = remove_Special_Chars.count(word)
            histo_dict[words] = number


# TODO Also need to alphabetize if value is the same
sorted_dict = sorted(histo_dict.items(), key=lambda x: x[1], reverse=True)

for i in sorted_dict:
    spaces = max_len + 2

    print(i[0])
    print(end=" " * spaces)
    print("#" * i[1])


start = time.time()
end = time.time()
print(f"Calculating too Histo {(end - start):.15f} seconds")
