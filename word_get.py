import random

def get_word(a_file):
    with open(a_file) as a_file:
        text = a_file.read()
    word_list = text.split()
    random_word = random.choice(word_list)
    return random_word
