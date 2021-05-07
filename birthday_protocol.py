def birthday_protocol():
    import os
    import time
    from pyfiglet import figlet_format #ascii art
    from termcolor import cprint        #colorize
    
    print("Hello Master. Is today the day?\n")
    os.system("say -v fred 'Hello Master. Is today the day?'")
    time.sleep(3)
    # The day what? That they're finally gonna throw it back to you?

    print("Haha great song reference, Master.\n")
    os.system("say -v fred 'Ha ha great song reference, Master.'")
    time.sleep(2)
    print("I meant is today the day I finally get to execute myself\n")
    os.system("say -v fred 'I meant is today the day I finally get to execute myself'")
    time.sleep(4)
    # Hmm a bit morbid on the phrasing. what's today?

    print("Today is February 5th, in the year of Our Lord 2021\n")
    os.system("say -v fred 'Today is February 5th, in the year of Our Lord 2021'")
    time.sleep(3)
    # Oh! Well then yes. I guess today is the day.


    print("Excellent! Initializing Birthday Protocol")
    os.system("say -v fred 'Excellent! Initializing Birthday Protocol'")
    time.sleep(1)

    for x in range(1,4):
        print(x*".")
        os.system("say -v fred 'beep'")
        time.sleep(2)

    cprint((figlet_format(
        "Happy Birthday Blue!!!".upper())), 
        "white", 
        "on_blue", 
        attrs = ["blink", "bold"]
        )
    os.system("say -v fred 'Happy birthday blueblueblueblueblueblueblue butts oh no butts butts heads shoulders knees and toes blue butts birthday butts weeweeweewee'")

birthday_protocol()