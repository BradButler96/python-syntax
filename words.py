words = ["hello", "hey", "goodbye", "yo", "yes"]
must_start_with = {'h', 'y'}

def print_upper_words(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())


print_upper_words(words, must_start_with)

