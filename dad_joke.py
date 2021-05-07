def dad_joke():
    import requests, random, termcolor, pyfiglet

    termcolor.cprint(pyfiglet.figlet_format("DAD JOKE BOT"),
                     "red" )

    url = "https://icanhazdadjoke.com/search"
    term = input("Select a topic (or type q to quit): ")
    while term != "q":
        data = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": term}
        ).json()

        s = data["total_jokes"]
        if s > 1:
            print(f"I have {s} jokes about that! Here's one:\n" +
                  random.choice(data["results"])["joke"])

        elif not s:
            print("I have don't have any jokes about that! Try again:")

        else:
            print("I have one joke about that! Here it is:\n" +
                  data["results"][0]["joke"])
        term = input("Select a topic (or type q to quit): ")

dad_joke()

