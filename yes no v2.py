
show_instructions = ""

while show_instructions.lower() != "xxx":
    show_instructions = input("Have you played Lucy Unicorn before?").lower()

    if show_instructions.lower() == "yes" or show_instructions == "y":
        print("program continues")

    elif show_instructions .lower() == "no" or show_instructions == "n":
        print("Display Instructions")

    else:
        print("Please enter yes or no")
