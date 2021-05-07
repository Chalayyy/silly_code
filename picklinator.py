import time
def picklinate(human, gender, pickle_type):

	input("Please confirm: would you like to turn subject into a pickle? (Yes/No) ")
	if gender.lower() == "male":
		print(" "*30+f"\U0001F934 -HELLO I AM {human}")
	else:
		print(f" "*30+f"\U0001F478 -HELLO I AM {human}")
	time.sleep(2)
	for x in range(61, 0, -2):
		print(" "*(30-x//2)+"'" * x)
		time.sleep(0.1)
	print(" "*30+"\U0001F952")
	time.sleep(1)
	print(f"Congratulations! {human} is now a {pickle_type} pickle!")
	input()

human = input("Please enter the human's name: ")
gender = input(f"Please enter {human}'s gender: ")
pickle_type = input("Please enter a pickle type: ")
picklinate(human, gender, pickle_type)