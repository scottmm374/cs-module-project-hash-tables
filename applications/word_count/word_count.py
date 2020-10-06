s = 'Hello, my cat.  And my cat doesn\'t say "hello" back.'


def word_count(s):

    count = {}
    # removes special characters from string
    remove_Special_Chars = s.translate(
        {ord(c): " " for c in "\"!@  # $%^&*()[]{};:,./<>?|`~-=_+"}).split()

    for word in remove_Special_Chars:
        words = word

        if word not in count:
            count[words] = [words]
        else:
            count[words].append(word)

    return count

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
