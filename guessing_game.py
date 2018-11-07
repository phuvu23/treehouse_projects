from random import seed, randint
# This is my first Project, my coding skills is not good, thanks for checking this out.


def pick_a_number():
	number = 0
	try:
		number = int(input("Pick a number between 1 and 10: "))
		while number < 1 or number > 11:
			if number < 1 or number > 11:
				print("Number must be greater than 0 and smaller than 11")
			number = int(input("Pick a number between 1 and 10: "))
	except ValueError:
		raise ValueError("Your input is wrong format!")
	else:
		return number

def start_game():
	counting = 1
	value = randint(1, 10)
	print("Welcome to the Number Guessing Game!")
	print("------------------------------------")
	while True:
		try:
			guessing_number = pick_a_number()
		except ValueError as err:
			print("{}".format(err))
		else:
			if guessing_number == value:
				print("Got it!")
				if counting == 1:
					print("You took 1 time to correct number")
				else:
					print("You took {0} times to correct number".format(counting))
				break
			elif guessing_number < value:
				print("It's lower")
			else:
				print("It's higher")
			counting += 1

start_game()




