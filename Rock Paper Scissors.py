from random import randrange

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
ifRock = {"Rock": "its a tie!", "Paper": "You lose!", "Scissors": "You win!!!"}
ifPaper = {"Rock": "You win!!!", "Paper": "its a tie!", "Scissors": "You lose!"}
ifScissors = {"Rock": "You lose!", "Paper": "You win!!!", "Scissors": "its a tie!"}
playerScore = 0
pcScore = 0

print("Game rules:\nRock(1) beat Scissors(3).\nPaper(2) beat Rock(1).\nScissors(3) beat Paper(2).\n")

isPlaying = input("Do you want to play? Y/N\n").capitalize()

while isPlaying == "Y":
    print("Make your choice:")
    for x in choices:
        print("For", choices[x], "press", x)

    playerChoice = input()

    while playerChoice != '1' and playerChoice != '2' and playerChoice != '3':
        playerChoice = input("Invalid input try again ")

    playerChoice = int(playerChoice)
    pcNumber = randrange(1, 4)

    if 0 < playerChoice < 4:
        print(f"Your choice is: {choices[playerChoice]}\nComputers choice is: {choices[pcNumber]}")

        if playerChoice == 1:
            result = ifRock[choices[pcNumber]]
            print(result)

        elif playerChoice == 2:
            result = ifPaper[choices[pcNumber]]
            print(result)

        else:
            result = ifScissors[choices[pcNumber]]
            print(result)

        if "win" in result:
            playerScore += 1

        elif "lose" in result:
            pcScore += 1

        isPlaying = input(f"Your score is {playerScore}\nComputers score is {pcScore}\n Play again? Y/N ").capitalize()

    else:
        isPlaying = input("Invalid Choice, try again? Y/N ").capitalize()

else:
    print("Thanks for playing!")




