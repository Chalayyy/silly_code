import pyfiglet 
import termcolor 
import os

def sneezy(human, blessing):

	if human.sneeze:
		termcolor.cprint(pyfiglet.figlet_format(f"{blessing} {human}!"), "blue", "on_green", ["blink"])
		os.system(f"say -v Fred {blessing} {human}!")
	return


class Human():

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

	def sneeze():
		return True


name = "Jennifer"
blessing = "Bless you"
sneezer = Human(name)

sneezy(sneezer, blessing)