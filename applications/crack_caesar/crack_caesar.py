import time
crypt_list = []
with open("ciphertext.txt") as f:
    words = f.read(delimiter=" ")
    crypt_list.append(words)


# def hist(words):

crypto_dict = {}

# removes special characters from string

# for word in words:
#     words = word
#     crypt_list.append(word)

# if the string does not exist yet
# if word not in crypto_dict:
#     number = list_of_crypt.count(word)
#     crypto_dict[words] = number

print(crypt_list)
# returns ['ID', 'EWKKF', 'WDQSMDU', 'ID', 'JCW', 'JIEW', 'XB', 'XSU,', 'OCWD', 'QXXU',.....]
