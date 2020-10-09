import time


with open("ciphertext.txt") as f:
    words = f.read()

decrypt_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
                'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


def ceasar(letters):
    decrypt_tup = list(enumerate(decrypt_list))

    crypto_dict = {}

    for char in letters:
        # skip non alpha characters
        if char != char.translate(
                {ord(c): " " for c in "\"!@  # $%^&*()[]{};:,./\\'\n'<>?|`~-=_+"}) or char == (' '):
            continue
        letter = char

        if char not in crypto_dict:
            number = words.count(char)
            crypto_dict[letter] = number
    # sorting dict by occurance of letters decending
    sorted_dict = sorted(
        crypto_dict.items(), key=lambda x: x[1], reverse=True)
    # print(len(crypto_dict))

    # creating dictionary with 1st index tup(as key) of sorted, and decrypt_tup as value, based on frequesncy of letter.

    decode_dict = {sorted_dict[i][0]: decrypt_tup[i][1]
                   for i, _ in enumerate(decrypt_tup)}

    encrypted_text = ""

    for char in words:
        if char.isalpha():
            # if char != char.translate(
            #         {ord(c): " " for c in "\"!@  # $%^&*()[]{};:,./\\'\n'<>?|`~-=_+"}) or char == (' '):
            #     continue
            encrypted_text += decode_dict[char]

    return encrypted_text

    # print("Sorted_dict: \n", sorted_dict)
    # # print("crypto_dict: \n", crypto_dict)
    # # print("Decrypt_tuple: \n", decrypt_tup)
    # print("decode_dict: \n", decode_dict)
    # return decode_dict


# def decode_txt(text):
#     encrypted_text = ""

#     for char in text:
#         encrypted_text += ceasar(words[char])

#     return encrypted_text


print(ceasar(words))

# start = time.time()
# end = time.time()
# print(f"Calculating Ceasar {(end - start):.10f} seconds")
