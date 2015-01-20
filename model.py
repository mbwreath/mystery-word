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


#
#     if word == choice:
#         print ("Victory!")
#         sys.exit()
#         else:
#         return guess_counter(count,addCount,letters) #repeats until win or lose
#         else:
#     if choice in letters:
#         print ("Wag of the finger...You've already guessed that letter!")
#         return guess(count,addCount,letters)
#         count += addCount
#         letters[count] = choice
#     if count == 0:
#         print ("O")
#         addCount = 1
#     elif count == 1:
#         print ("O<")
#         addCount = 2
#     elif count == 2:
#         print ("0<-")
#         addCount = 3
#     elif count == 3:
#         print ("O<-<\n Game Over")
#         sys.exit()
#         print ("Letters missed: ", ' ').join(letters)
#         guess(count,addCount,letters))
# return
