"""
This program is a word guessing game. The function chooses a random word from a list of words, and the user has 6 tries to guess the word.
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Nov 3, 2022
"""
import random

def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the secret word
    """

    #DO NOT MODIFY THIS FUNCTION
    
    validWords = ["could", "smile", "ultra", "extra", \
                  "beacon", "hearts", "cap", "wordle", \
                  "computing", "program", "python"]

    #random.randint(0, 5) will generate an integer between 0 and 5 (inclusive)
    #this is then used to select a value from the list validWords.

    wordPosition = random.randint(0,5)

    return validWords[wordPosition]

    

def checkLetters(secretWord, userWord):
    """
    This function checks the letters guessed by the user against the secret
    word and informs the user as to which letters are in the correct location,
    which letters are in the word but not in the correct location and which
    letters are not in the word.
    Paramters:   secretWord, userWord - strings
    Returns:  None
    """

    for userWordLetterPosition in range(len(userWord)):
        # if letter in userWord is in the secretWord and same position
        if userWord[userWordLetterPosition] == secretWord[userWordLetterPosition]:
                print(userWord[userWordLetterPosition] + " - in correct place")
        else:
            inWord = "no"
            # looping secretWord to search for the letter guessed in every position of secretWord
            for secretWordLetterPosition in range(len(secretWord)):
                # if letter in userWord is in the secretWord (not same position)
                if userWord[userWordLetterPosition] == secretWord[secretWordLetterPosition]:
                    print(userWord[userWordLetterPosition] + " - in word but wrong place")
                    inWord = "yes"
            # if letter in userWord is not found in the secretWord
            if inWord == "no": 
                print(userWord[userWordLetterPosition] + " - not in word")
    
def checkForDuplicates(userWord):
    """
    This function checks the user's word for duplicate letters.
    If there are duplicate letters, the function returns True, otherwise, False.
    Parameters:  userWord - string
    Return:  Boolean
    """
    # empty list
    repeat = []
    for i in userWord:
        # if letter in userWord has already been added to repeat (list)
        if i in repeat:
            return True
        else:
            # adding letter to repeat (list) if its the first time seen
            repeat += [i]   
    # returns false if no letters repeat 
    return False

def play(secretWord):
    """
    This function allows the user to play the game, entering up to 6 words to
    try to guess the secret word. When the correct word is guessed, the play
    stops and the user is congratulated.
    Parameters: string representing the secretWord
    Return Value:  None
    """
    # for loop (6 guesses)
    for x in range(6):
        userWord = input("Guess the word:")
        # if statement runs checkForDuplicates function and checks if it returns True
        if checkForDuplicates(userWord) == True:
            print("Sorry, your word has duplicate letters.  Enter a word with no duplicates:")
        
        # if userWord is not a duplicated
        else: 
            if userWord == secretWord:
                print("YOU WIN!")
                break
            # running checkLetters function to check letters in userWord
            checkLetters(secretWord, userWord)
    
def main():
    """
    This implements the user interface for the program.
    """
    # running chooseWord function to get the secret word
    secretWord = chooseWord()
    
    # printing secretWord (for testing purposes)
    print("The secret word is " + secretWord + " (Leaving this in for testing)")

    # telling user how many letters are in the secret word
    print("This word has " + str(len(secretWord)) + " letters.")

    # starting the game
    play(secretWord)

main()