import random
#Limit film watching to 2 films, ~4 hours
ghibli = ["Spirited Away", "My Neighbor Totoro", "Howl's Moving Castle", "Princess Mononoke", "Kiki's Delivery Service", "Castle in the Sky", "Ponyo", "The Wind Rises", "Whisper of the Heart", "Grave of the Fireflies", "Arrietty", "The Cat Returns", "When Marnie was there", "From up on Poppy hill", "Porco Rosso", "Ocean Waves", "Only Yesterday" ]

def randomFilm(self):
	ToWatch = random.choice(ghibli)
	print(ToWatch)
	view = input("Are you going to watch " + ToWatch + " ?")
	if view == "yes":
		for film in ghibli:
			if film == ToWatch:
				ghibli.remove(ToWatch)
		print("Current Movie selection is: ")
		print(ghibli)		
	if view == "no":
		print("Remaining films: ")
		print(ghibli)
		another = input("Should we choose another? ")
		if another == "yes":
			randomFilm(ghibli)
		elif another == "no":
			print("Maybe next movie night!")
	return ghibli


randomFilm(ghibli)
reRun = input("Do you want to watch another film? ")
if reRun != "no":
	randomFilm(ghibli)	
print(ghibli)
exit("Enjoy your day, goodbye!")

		
	




		
	


