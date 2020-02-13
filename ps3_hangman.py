# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # Check if the chars in "secretWord" are contained in the "lettersGuessed" array, if not return False
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    # Otherwise return True
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # Copy secretWord into new variable
    word = secretWord[:]
    # Iterate through the copy and replace chars that are not yet guessed with '_ '
    for char in secretWord:
        if char not in lettersGuessed:
            word = word.replace(char, '_ ')
    # Return the modified copy
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Set all lowercase US alphabet letters
    abc = string.ascii_lowercase
    # Create copy
    aux = abc[:]
    # Iterate through lettersGuessed and replace each (delete) from copy of abc
    for char in lettersGuessed:
        if char in aux:
            aux = aux.replace(char, '')
    # Return the modified copy
    return aux
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Set length for welcome messages
    len_word = len(secretWord)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len_word))
    print('-------------')
    # Initiate lettersGuessed and guesses
    lettersGuessed = []
    guesses = 8
    # Iterate until word is correctly guess or running out of guesses
    while guesses > 0:
        # Check is word has been correctly guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            return
        # Otherwise start asking for input, give feedback from input and adjust lettersGuessed and guesses accordingly
        # This cycle will repeat until running out of guesses
        else:
            print('You have {} guesses left'.format(guesses))
            print('Available letters: ', getAvailableLetters(lettersGuessed))
            guess = input('Please guess a letter: ')
            letter = guess.lower()
            # Feedback if letter is already in lettersGuessed array
            if letter in lettersGuessed:
                print('Oops! You\'ve already guessed that letter: ', 
                      getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
            else:
                # Adjust lettersGuessed by appending letter guessed
                lettersGuessed.append(letter)
                # Feedback if it is a good guessed letter
                if letter in secretWord:
                    print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
                    print('-------------')
                else:
                    # Decrement guesses and send feedback about wrong guessed letter
                    guesses -= 1
                    print('Oops! That letter is not in my word: ',
                          getGuessedWord(secretWord, lettersGuessed))
                    print('-------------')
    # Ran out of guesses, send GAME OVER message
    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
    return

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
