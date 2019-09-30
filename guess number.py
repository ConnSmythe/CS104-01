import random
theComputerNumber = random.randint(1, 1000000)
print(theComputerNumber)
lowGuessRange=1
highGuessRange=1000000
numberOfGuesses = 0
while numberOfGuesses<20:
    print ("Enter a guess in range from", lowGuessRange, "to",
           highGuessRange)
    playerGuess = int(input("Enter your guess: "))
    print(playerGuess)
    if (playerGuess < lowGuessRange or playerGuess > highGuessRange):
        print ("Guess out of range, try again")
        continue
    if (playerGuess == theComputerNumber):
        print ("Your guess was correct congrats your RNG is good!!!!")
        numberOfGuesses=20
        continue
    if (playerGuess < theComputerNumber):
        print ("Your guess was too low.")
        lowGuessRange=playerGuess
        continue
    if (playerGuess > theComputerNumber):
        print ("Your guess was too high.")
        highGuessRange=playerGuess
        continue

