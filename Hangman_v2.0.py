##First attempt at writing a game program.
##Issues encountered: global variables vs local; copying a list instead of re-pointing new list;



import random

spacing = '_____ '
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

hangmanpics=['''

   +----+
   |    |
        |
        |
        |
        |
===============''','''

   +----+
   |    |
   O    |
        |
        |
        |
================''','''
             
   +----+
   |    |
   O    |
   |    |
        |
        |
=================''','''

   +----+
   |    |
   O    |
  /|    |
        |
        |
=================''','''

   +----+
   |    |
   O    |
  /|\   |
        |
        |
==================''','''

   +----+
   |    |
   O    |
  /|\   |
  /     |
        |    
==================''','''
        
   +----+
   |    |
   O    |
  /|\   |
  / \   |
        |
===================''']

already_guessed=[]
print (hangmanpics[-1])
word_list=[]
visual_word=[]
running_word=[]
temp_word2=[]
replay="no"

def Hangman_word():
    global word
    word=random.choice(list_of_words)
    #print ("the word chosen is",word)
    word_length=len(word)
    print ('\nThe word is ',word_length,' letters long')
    visual_word=spacing * word_length
    print (visual_word,"\n")
    global word_list  ##Needed to return word to global to be used in another function.
    word_list=list(word)
    global start_word
    start_word=word_list[:]


Hangman_word()
#print ("the returned word is:",word_list)

def Hangman_Guesses():
    running_word = word_list
    guessed_word=len(running_word)*"_"
    guessed_word.split
    guessed_word=list(guessed_word)
    num_misses=0
    num_guesses = 0


    #print ("Guessed_Word:",guessed_word,"Running_word:",running_word)
    while '_' in guessed_word:
        guess=input("\nPlease enter a letter:").lower()
        if guess in already_guessed:
            print ("You have already guessed that letter, please try again!")
        else:
            already_guessed.append(guess)
            for letter in running_word:
                #print("The letter being checked is:", letter, "The letter you have guessed is:",guess,"\n")
                if letter == guess:
                    letter_index=running_word.index(letter)
                    #print("You have guessed a letter! ***", guess, "***The index of the letter is: ", letter_index,"\n\n")

                    running_word[letter_index]=spacing
                    guessed_word[letter_index]=letter
                #print ("Running word(old) is: ",running_word)
            #print ("Word List=",start_word,"::::  Guess=",guess)
            if guess not in start_word:
                num_misses=num_misses+1
                print(hangmanpics[num_misses])

            num_guesses=num_guesses+1
            if num_misses==6:
                print ("\nYOU HAVE LOST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print ("The word that you were trying to solve:",word)
                replay=input ("Would you like to play again?").lower()
                if replay=="yes":
                    Hangman_word()
                else:
                    break

            print ("Guessed word (new) is: ",guessed_word,"\n")
            if '_' not in guessed_word:
                print ("\nYOU HAVE WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                replay=input ("Would you like to play again?").lower()
                if replay=="yes":
                    Hangman_word()
                else:
                    break
        print ("Number of guesses so far=",num_guesses,"Letters used so far=",already_guessed)

Hangman_Guesses()





