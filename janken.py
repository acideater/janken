print("#######################################")
print("Rock, Paper, Scissor - aka Jan-Ken-Pon")
print("by Ana P. - March 2018")
print("#######################################\n\n")

from random import randint

startGame = input("Start the game? Type 'Yes' or 'No'\n")

while startGame == "Yes":
    #create a list of options
    playList = ["Rock", "Paper", "Scissors"]
    #assign a random play to the computer
    computer = playList[randint(0,2)]	
    #loop starts while player is equal 1
    player = 1
    #This keeps happening
    while player == 1:
        player = input("\nRock, Paper or Scissors?\n")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose! " + computer + " covers " + player)
            else:
                print("You win! " + player + " smashes " + computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose! " + computer + " cut " + player)
            else:
                print("You win! " + player + " covers " + computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose! " + computer + " smashes " + player)
            else:
                print("You win! " + player + "cut" + computer)
        else:
            print("This is not a valid play. Check your spelling!")

    #To continue the loop forever
    player = 1
    computer = playList[randint(0,2)]
		
if startGame == "No":
    print("Ok. Come again later!")
