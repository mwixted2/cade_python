import random

#guessesTaken = 0
guessesTaken = 

print("Hello! What is your name?")

#raw_input("Enter your name: ")
myName = raw_input()

#number = random.randint(1, 20)
number = random.randint(, )

#print("Well, " + myName + ", I am thinking of a number between 1 and 20.")
print("Well, " +  + ", I am thinking of a number between 1 and 20.")

#while guessesTaken < 5:
while guessesTaken < :
	print("Take a guess.")
	guess = raw_input()
	guess= int(guess)

	
	guessesTaken = guessesTaken + 1

	if guess < number:
		#print("Your guess is too low")
		print("")

	if guess > number:
		#print("Your guess is too low")
		print("")

	if guess == number:
		break


if guess == number:
	guessesTaken = str(guessesTaken)
	#print("Good job, " + myName + "! You guessed my number in " + guessesTaken + "guesses!")
	print("Good job, " +  + "! You guessed my number in " +  + " guesses!")

if guess != number:
	number = str(number)
	#print("Nope. The number I was thinking of was " + number)
	print("Nope. The number I was thinking of was" + )

	