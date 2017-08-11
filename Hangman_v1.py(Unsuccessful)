import random

spacing = '_____  '
list_of_words = ['knife', 'highfalutin', 'neck', 'roof', 'earthy', 'gorgeous', 'same', 'screw', 'spotless',
                 'adjustment', 'rescue', 'married', 'scarecrow', 'woozy', 'vacation', 'bang', 'applaud', 'grate',
                 'mellow', 'perpetual', 'prepare', 'secret', 'earthquake', 'shelter', 'anxious', 'card', 'wave', 'song',
                 'spiritual', 'expand', 'activity', 'car', 'need', 'talk', 'disturbed', 'tacit', 'neat', 'fierce',
                 'introduce', 'monkey', 'old', 'current', 'caring', 'limping', 'popcorn', 'structure', 'porter',
                 'naughty', 'unwieldy', 'deer', 'flight', 'cluttered', 'man', 'cross', 'pretty', 'trade', 'feeling',
                 'possessive', 'afraid', 'sturdy', 'person', 'gentle', 'level', 'talented', 'awful', 'prefer',
                 'oceanic', 'plastic', 'purple', 'hateful', 'tan', 'annoyed', 'thumb', 'aberrant', 'tow', 'ear',
                 'bottle', 'tense', 'cherry', 'bomb', 'tense', 'embarrass', 'aquatic', 'quaint', 'abstracted', 'maid',
                 'small', 'plausible', 'apologise', 'attach', 'glistening', 'cook', 'bomb', 'robust', 'sort', 'hook',
                 'alert', 'obey', 'halting']

man_v1='   O'
man_v2='   O\n /'
man_v3='   O\n / |'
man_v4='   O\n / | \ '
man_v5='   O\n / | \ \n   | '
man_v6='   O\n / | \ \n   | \n  / '
man_v7='   O\n / | \ \n   | \n  /  \ '
man_v8='   O\n / | \ \n   | \n  /  \  \n /  '
dead_man = '   O\n / | \ \n   | \n  /  \  \n /    \ \n'
running_word=[]
#num_guess=0

def Hangman_words():
    num_guess = 0
    special_word=random.choice(list_of_words)
    print ("The special word is: ",special_word)
    print ("The length of the word is:", len(special_word),"\n\n")
    visual_word=len(special_word)*spacing
    print (visual_word)
    #
    # while num_guesses<9:
    #     if ' ___ ' in running_word:
    #         Guess_A_Letter()


    while num_guess<9:
        num_guess = num_guess + 1
        guess=input("please guess a letter").lower()
        for letter in special_word:
            if guess==letter:
                running_word.append(letter)
            else:
                running_word.append(' ___ ')
        if ' ___ ' not in running_word:
            num_guess=9
            print ("YOU WON!!!")
        else:
            print (running_word)
            print ("Try Again")


###Current output is appending each guess to the end of the list.
###Need new logic


    #print (running_word)



##currently, the variable visual_word  has a ___  where a letter should be.  Want to determine the position needed and then substitute that position

























########################################################################


print (dead_man)
start = input("Do you want to play hangman?(yes/no): ").lower()
if start == "yes":
    Hangman_words()
else:
    print ("You did not choose 'Yes', exiting now!")
    quit ()
#
# while num_guess<9:
#     if ' ___ ' in running_word:
#         num_guess = num_guess + 1
#         Guess_A_Letter()
