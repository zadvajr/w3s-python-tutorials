
exit_word = "chupacabra"

while True:
    user_input = input("Guess a word to Quit: ")
    if user_input == exit_word:
        print("You've successfully left the loop.")
        break