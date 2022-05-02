show_instructions = input("Have you played Lucky Unicorn before?").lower()

if show_instructions.lower() == "yes":
    print("Program continues")

elif show_instructions.lower() == "y":
    print("Display instructions")

elif show_instructions == "no":
    print("Display instructions")

elif show_instructions == "n":
    print("Display instructions")

else:
    print("Please enter yes or no")
