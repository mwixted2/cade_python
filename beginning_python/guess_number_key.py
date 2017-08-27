#start off with importing the random function
import random

#declare the number of guesses that the user will begin with
#it will be best to set this value to 0
guessesTaken = 0

#use a print statement to ask the user their name
print("Hello! What is your name?")
#set the myName variable to accept input from the user
#you can add other strings to this, such as
#raw_input("Enter your name: ")
myName = raw_input()

#set the variable number to a random integer
#pick the range of numbers, like 1 and 20
number = random.randint(1, 20)

#between "Well, " and ", I am thinking of a number...", add the variable myName
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

#use a while loop to start looking for conditions 
#use while guessesTaken < to come up with your own number
#this will be how many guesses the user gets before the program terminates
while guessesTaken < 6:
	print("Take a guess.")
	#takes in the user input
	guess = raw_input()
	guess= int(guess)

	#add one to the number of guesses, so instead of 0 guesses it will be 1 guess, and so forth
	guessesTaken = guessesTaken + 1

	#go through conditions for guessing
	#should tell the user if the guess is too low or the guess is too high
	if guess < number:
		print("Your guess is too low.")

	if guess > number:
		print("Your guess is too high.")

	#break is used to break the while loop after the user guesses the number
	if guess == number:
		break

#if the user guesses correctly, the program will print the result 
if guess == number:
	guessesTaken = str(guessesTaken)
	#fill in the variables that should go inbetween the plus signs
	print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

#if the user takes too many tries to guess
if guess != number:
	number = str(number)
	#fill in the variable that should go after the plus sign
	print("Nope. The number I was thinking of was" + number)

	