import time

with open("robin.txt") as f:
    words = f.read()


# def hist(words):
    histo_dict = {}

  # removes special characters from string
    remove_Special_Chars = words.translate(
        {ord(c): " " for c in "\"!@  # $%^&*()[]{};:,./\\<>?|`~-=_+"}).lower().split()

    for word in remove_Special_Chars:
        words = word

    # if the string does not exist yet
        if word not in histo_dict:
            number = remove_Special_Chars.count(word)
            histo_dict[words] = number

    sorted_dict = sorted(histo_dict.items(), key=lambda x: x[1], reverse=True)
    # longest = [ele for key in sorted_dict for ele in key]
    # print(max(longest)

    for i in sorted_dict:

        print(i[0])
        print(end=" " * 15)
        print("#" * i[1])


start = time.time()
end = time.time()
print(f"Calculating too Histo {(end - start):.15f} seconds")
