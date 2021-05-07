def ascii_art():
    from pyfiglet import figlet_format #ascii art
    from termcolor import cprint        #colorize

    # output text
    text = figlet_format(input("What would you like to say? "))

    # text/highlight color options
    valid_colors = (
        "red",
        "yellow",
        "green",
        "blue",
        "magenta",
        "cyan",
        "white")

    # validate color option
    color = input(
        f"What color do you want it to be? \nOptions are {valid_colors} ").lower()
    if color not in valid_colors:
        color = "red"
    
    # validate highlight option
    highlight = input(
        f"What background color do you want? \nOptions are {valid_colors} ").lower()
    if highlight not in valid_colors:
        highlight = None
    else:
        highlight = "on_" + highlight

    # validate effect option
    valid_effects = (
        "bold",
        "dark",
        "underline",
        "blink",
        "reverse",
        "concealed")
   
    effects = input(
        f"Any special effects? \nOptions are {valid_effects} ").split(" ")

    effects = set(effects).intersection(valid_effects)
    
    cprint(text, color, highlight, effects)

ascii_art()
