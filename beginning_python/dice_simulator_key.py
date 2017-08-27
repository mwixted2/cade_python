#start your code with importing the random function
import random

#give a maximum number and a minimum number
#you can do min = 1 and max = 6, for example
min = 1
max = 6

#set a variable that you can use in a loop
#maybe put "yes" as the valuee
roll_again = "yes"

#create a while loop to roll the dice
#this is so that you can keep rolling your dice
while roll_again == "yes" or roll_again == "y":
	#a couple print statements so you know where you are in your program
	print "Rolling the dice..."
	print "The values are..."
	#random function using a feature called randomint (random integer)
	#here you can call your above variables, min and max, to use with randint
	print random.randint(min, max)
	print random.randint(min, max)

	#ask the user if they want to roll again
	#give a yes answer or no answer
	#put your code between the quotation marks
	roll_again = raw_input("Roll the dices again? ")