def main():
    word = str(input("Podaj slowo"))
    hangman(word)

def hangman(word):
    wrong = 0
    stages = ["",
    "________        ",
    "|               ",
    "|       |       ",
    "|       O       ",
    "|      /|\      ",
    "|      / \      ",
    "|               ",
    ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Hangman Game")
    while wrong < len(stages) - 1:
        print("\n")
        msg = input("Guess the letter: ")
        char = msg
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0: e]))
            if "__" not in board:
                print("You Won!")
                print(" ".join(board))
                win = True
                break
            if not win:
                print("\n".join(stages[0: wrong]))
                print("You Loss! The word is: {}.".format(word))


if __name__ == "__main__":
    main()