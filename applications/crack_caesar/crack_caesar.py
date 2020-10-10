
import time


with open("ciphertext.txt") as f:
    words = f.read()

decrypt_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
                'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


def ceasar(letters):
    # Creating tuple list to combine with crypto dict based off frequency. Dycrypt list in order from most frequest to least.
    decrypt_tup = list(enumerate(decrypt_list))

    crypto_dict = {}

# Adding txt file characters to dictionary
    for char in letters:
        if char.isalpha():
            letter = char

            if char not in crypto_dict:
                number = words.count(char)
                crypto_dict[letter] = number

        # sorting dict by occurance of letters decending
    sorted_dict = sorted(
        crypto_dict.items(), key=lambda x: x[1], reverse=True)

    # creating dictionary with 1st index tup(as key) of sorted, and decrypt_tup as value, based on frequesncy of letter.

    decode_dict = {sorted_dict[i][0]: decrypt_tup[i][1]
                   for i, _ in enumerate(decrypt_tup)}

#    Where the Magic happens, decoding text

    encrypted_text = ""

    for char in words:
        if char.isalpha():
            encrypted_text += decode_dict[char]

        else:
            encrypted_text += char

    print(encrypted_text, "encryted txt")
    return encrypted_text


ceasar(words)
