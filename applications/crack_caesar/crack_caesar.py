import time


with open("ciphertext.txt") as f:
    words = f.read()

decrypt_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
                'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

decode_table = {}


def decode(decodeList, dict):
    pass


def ceasar(letters):

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

    sorted_dict = sorted(
        crypto_dict.items(), key=lambda x: x[1], reverse=True)
    print(len(crypto_dict))
    return sorted_dict


print(ceasar(words))

start = time.time()
end = time.time()
print(f"Calculating Ceasar {(end - start):.10f} seconds")
