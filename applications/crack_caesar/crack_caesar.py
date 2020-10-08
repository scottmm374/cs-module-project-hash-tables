import time


# crypt_list = []

with open("ciphertext.txt") as f:
    words = f.read()
    # crypt_list.append(words)


def ceasar(letters):

    crypto_dict = {}

    for char in letters:
        letter = char
        # print(char, "characters")

        if char not in crypto_dict:
            number = words.count(char)
            crypto_dict[letter] = number

    return crypto_dict


print(ceasar(words))
