#The death module (end of the game - lost).

class Death():

    def gogo():

        print("Hope you enjoyed the game. Donate on Patreon!")
        play_again = input("Play again? (Y/N) >\t")

        if play_again == "Y" or play_again == "y":

            from ex45a import Start

            Start.gogo()

        else:
            exit(0)
