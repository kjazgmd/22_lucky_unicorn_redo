# balance for testing with
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play..").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print(rounds_played)
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    play_again = input("Press enter to play again "
                       " or 'xxx' to quit")


if balance < 1:
    play_again = "xxx"


