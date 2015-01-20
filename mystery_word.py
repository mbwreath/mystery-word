import random
#use import random

print("Welcome to Mystery Game!!...Do you have what it takes, in less than 8 mistakes!!")


a_file = ("/usr/share/dict/words")
guesses=0
letters_guessed = []
guess_counter = 8
word = []
# easy_word_range = [>=4: <=6]
# medium_word_range = [>6: <=10]
# hard_word_range = [>10]

def get_word(a_file):
    with open(a_file) as a_file:
        text = a_file.read()
    word_list = text.split().lower()
    random_word = random.choice(word_list)
#
# def choose_difficulty():
#     level = input("Please choose a level to play: Easy, Medium, or Hard.")
#     if level == "Easy":
#         word = get_word()
#         if len(word_range.easy_word_range):
#             #need an action here
#         #get_word_from_easy_list = characters ">=4, <= 6"
#     if level == "Medium":
#         word = get_word()
#         if len(word_range.medium_word_range):
#             #need an action here
#         #get_word_from_medium_list = characters ">6, <=10"
#
#     if level == "Hard":
#         word = get_word()
#         if len(word_range.hard_word_range):
#             #need action here
#         #get_word_from_hard_list = characters ">10"
        #
        # return random_word
        #
        # if(word[word_choice]):
        #     print("The length of the word is: " , len(word[a_file]))

def guess_letter(count,addCount,letters):
    choice = input("Please enter a letter:")
    choice = choice.upper()
    if len(choice) > 1:
        print("One letter at a time please.")
        return guess(count,addCount,letters)
    elif choice in letters:
        print("Wag of the finger...You've already guessed that letter!")
        return guess(count,addCount,letters)
    elif not choice.isalpha():
        print ("Wag of the finger...You guessed a number!")
        return guess(count,addCount,letters)
    else:
        return choice

def win_or_lose(guess_counter, word_so_far, mystery_word):
    """It will check if the input so far matches the word or not.
    If the player has guessed too many times, they lose."""
    if guess_counter == 0:
        print("You lost!")
        return "lose"
    elif word_so_far == mystery_word:
        print("You win!")
        return "win"

def say_win():
    return "win"

print(introduction)
game_word = get_word(a_file)
while True:
    






#def letter_guess ()
#    for x in range(len(words[a_file])):
#    word.append('_')

#    while guess_counter < 8:
#    guess=input("Please enter the letter you guess: ")

#    if(guess in words[a_file]):
#        print("Correct!.")
#        for index, letter in enumerate(words[a_file]):
#            if letter == guess:
#                word[index] = guess
#        letters_guessed.append(guess)

#    else:
#        print("BOO!!")
#        guesses=guesses+1
#        letters_guessed.append(guess)

#    print("you have guessed these letters: %s"%(''.join(letters_guessed)))
#    print("Letters matched so far %s"%''.join(word))
#    print()

#a line that prints "you have already guessed that word... you must choose again"
#    if ''.join(word) == words[i]:
#        break

#    if guesses==8:
#    print("Failure!! Boo!! The word was:" , words[i])
#    else:
#    print("You are the BEST!!!")
#    print("You only made %i wrong guesses"%guesses)
