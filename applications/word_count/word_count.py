s = 'Hello, my cat.  And my cat doesn\'t say "hello" back.'
# s = '":;,.-+=/\\|[]{}()*^&'


def word_count(s):

    word_dict = {}
    # removes special characters from string
    remove_Special_Chars = s.translate(
        {ord(c): " " for c in "'\!@  # $%^&*()[]{};:,./\\<>?|`~-=_+"}).lower().split()

    for word in remove_Special_Chars:
        words = word
    # if the string does not exist yet
        if word not in word_dict:
            number = remove_Special_Chars.count(word)
            word_dict[words] = number

    return word_dict

    # if __name__ == "__main__":
    #     print(word_count(""))
    #     print(word_count("Hello"))
    #     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    #     print(word_count(
    #         'This is a test of the emergency broadcast network. This is only a test.'))
    # word_count('":;,.-+=/\\|[]{}()*^&')


x = word_count(s)
print(x)


# s = 'Hello, my cat.  And my cat doesn\'t say "hello" back.'
