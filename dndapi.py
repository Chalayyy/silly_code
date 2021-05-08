import requests
url_blank = "https://www.dnd5eapi.co/api/classes/"
classes = ["Barbarian", "Bard"]
for x in classes:
	url = url_blank+x.lower()
	res = requests.get(url, headers = {"Accept":"application/json"})
	data = res.json()
	print(f"{x}'s Hit Die: d{data['hit_die']}")
	
	print(f"{x}'s Skill Proficiencies: Select " + 
		str(data['proficiency_choices'][0]['choose']) + " from ")

	for x in range(len(data['proficiency_choices'][0]['from'])):
		print(data['proficiency_choices'][0]['from'][x]['name'])
		
	