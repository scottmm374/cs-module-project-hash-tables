

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

    print(histo_dict)
    # return word_dict
# hist()
