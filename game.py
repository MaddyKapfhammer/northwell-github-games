def play_game(input):
    print("Playing game")
    if input > 10:
        return "You win!"
    else:
        return "You lose!"

if __name__ == "__main__":
    print(play_game(5))
    