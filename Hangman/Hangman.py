import random
HANGMAN_PICS = ["""
    +---+
        |
        |
        |
       ===""","""
    +---+
    O   |
        |
        |
       ===""","""
    +---+
    O   |
    |   |
        |
       ===""",""""
    +---+
    O   |
   /|   |
        |
       ===""",""""
    +---+
    O   |
   /|\  |
        |
       ===""","""
    +---+
    O   |
   /|\  |
   /    |
       ===""","""
    +---+
    O   |
   /|\  |
   / \  |
       ===""","""
    +---+
    O   |
   /|\, |
   / \  |
       ===""","""
    +---+
    O   |
  ,/|\, |
   / \  |
       ===""","""
    +---+
    O   |
  ,/|\, |
   / \. |
       ===""","""
    +---+
    O   |
  ,/|\, |
  ./ \. |
       ==="""]
lesserKnownAnimals = "axolotl blobfish sawfish guiterfish komododragon serval kinkajou binturong capybara paca iguana mink".split()
programNames = "sql java javascript bash docker python html raspian c cplus csharp cplusplus php rust assembly react swift".split()

words = """ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle elephant ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra red orange yellow green blue indigo violet white black 
brown grey square triangle rectangle circle ellipse rhombus trapezoid pentagon hexagon septagon octogon cube pyramid cylinder apple orangle lemon 
lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato carrot cucumber blueberry peach raspberry lettuce celery""".split()
print("My version of Hangman comes with colors, animals, and fruits/vegetables in the default list of words. " +
    "But I have two more catagories I can add if you would like: ")
print("Would you like to add less known animals to the list (y or n)")
choice = input().lower()
if choice == "y":
    words = words + lesserKnownAnimals
while choice != "y" and choice != "n":
    print("ERROR. Please enter y or n")
    choice = input().lower()
    if choice == "y":
        words = words + lesserKnownAnimals
print("Would you like to add programming language names to the list (y or n)")
choice = input().lower()
if choice == "y":
    words = words + programNames
while choice != "y" and choice != "n":
    print("ERROR. Please enter y or n")
    choice = input().lower()
    if choice == "y":
        words = words + programNames
def getRandomWord(wordList):
    # This function returns a random string from the passed list of of strings.
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters:" , end = " ")
    for letter in missedLetters:
        print(letter, end= " ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        # Replaces blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:
        # Show the secret word with spaces in between each letter.
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. this function makes sure the player entered a single letter and not something else
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is \"" + secretWord + "\"! You have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check to see if player has guessed to many times and has lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You have run out of guesses!\nAfter " + 
                str(len(missedLetters)) + " missed guesses and " +
                str(len(correctLetters)) + " correct guesses, the word was \"" +
                secretWord +"\"")
            gameIsDone = True

    # Ask the player if they want to play again (but only if game has ended)
    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

