import time


with open("ciphertext.txt") as f:
    words = f.read()


def ceasar(letters):

    crypto_dict = {}

    for char in letters:
        # skip non alpha characters
        if char.isalpha():

            letter = char

        if char not in crypto_dict:
            number = words.count(char)
            crypto_dict[letter] = number
    print(len(crypto_dict))
    return crypto_dict


print(ceasar(words))

start = time.time()
end = time.time()
print(f"Calculating Ceasar {(end - start):.10f} seconds")
