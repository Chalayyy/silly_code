def make_song(lines = 99, drink = "soda"):
    for count in range(lines, -1, -1):
    	if count > 1:
    		lyrics= "{} bottles of {} on the wall.".format(count, drink)
    		yield lyrics
    	elif count == 1:
    		lyrics= "Only 1 bottle of {} left!".format(drink)
    		yield lyrics
    	else:
	    	lyrics= "No more {}!".format(drink)
	    	yield lyrics

# song = make_song(5)
# print(next(song))
# print(next(song))
# print(next(song))
# print(next(song))
# print(next(song))
# print(next(song))