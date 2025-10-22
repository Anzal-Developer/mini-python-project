import random

# WINNING PATTERNS
# Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard,
# Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
# Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock,
# Rock crushes Scissors

win = [("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"),
       ("lizard", "spock"), ("spock", "scissors"), ("scissors", "lizard"),
       ("lizard", "paper"), ("paper", "spock"), ("spock","rock"),
       ("rock", "scissors")
       ]
# INSTUCTIONS
print("There are 6 rounds.\nYou playing against computer.\nYou will win if you a higher point.\nEnter scissors, paper, rock, lizard or spock.\nLIVE LONG AND PROSPER!!!")

# CHOICES FOR THE COMPUTER TO CHOOSE FROM
choices = ["scissors", "paper", "rock", "lizard", "spock"]

# TO COUNT THE NUMBER OF ROUNDS 2
count = 0

# TO COUNT THE PLAYER'S POINTS
player_points = 0

# TO COUNT THE COMPUTER'S POINTS
computer_points = 0

# WHILE LOOP TO SET THE NUMBER OF ROUNDS 
while count != 6:
    # input player's choice
    player = input("Enter your choice:")
    # computer's select random choice
    computer = random.choice(choices)
     # UNCOMMENT THE LINE BELOW IF YOU WISH TO SEE COMPUTRONS' CHOICE
    # print("Computer's choice:", computer)

    if player == computer:
        # check for patterns
        playerWins = (player, computer)
        computerWins = (computer, player)
        if playerWins in win:
            if playerWins == win[0]:
                 #print("✂ cuts 📃 \nYou Won!")
                print("scissors cuts paper \nYou Won!") 
            elif playerWins == win[1]:
                print("paper covers rock \nYou Won!")
            elif playerWins == win[2]:
                print("rock crushes lizard \nYou Won!")
            elif playerWins == win[3]:
                print("lizard poisons spock \nYou Won!")
            elif playerWins == win[4]:
                print("spock smashes scissors \nYou Won!")
            elif playerWins == win[5]:
                print("scissors decapitates lizard \nYou Won!")
            elif playerWins == win[6]:
                print("lizard eats paper \nYou Won!")
            elif playerWins == win[7]:
                print("paper disproves spock \nYou Won!")
            elif playerWins == win[8]:
                print("spock vaporizes rock \nYou Won!")
            elif playerWins == win[9]:
                print("rock crushes scissors \nYou Won!")
            player_points += 1
        elif computerWins in win:
            if computerWins == win[0]:
                print("scissors cuts paper \nComputer Won!")
            elif computerWins == win[1]:
                print("paper covers rock \nComputer Won!")
            elif computerWins == win[2]:
                print("rock crushes lizard \nComputer Won!")
            elif computerWins == win[3]:
                print("lizard poisons spock \nComputer Won!")
            elif computerWins == win[4]:
                print("spock smashes scissors \nComputer Won!")
            elif computerWins == win[5]:
                print("scissors decapitates lizard \nComputer Won!")
            elif computerWins == win[6]:
                print("lizard eats paper \nComputer Won!")
            elif computerWins == win[7]:
                print("paper disproves spock \nComputer Won!")
            elif computerWins == win[8]:
                print("spock vaporizes rock \nComputer Won!")
            elif computerWins == win[9]:
                print("rock crushes scissors \nComputer Won!")
            computer_points += 1
            # PLAYER DID NOT INPUT scissors, paper, rock, lizard or Spock
        else:
            print("invlid response.\ncomputer wins!")
            computer_points += 1
    # Draw same choice
    elif player == computer:
        print("Draw, player and computer get 1 point ")
        player_points += 1
        computer_points += 1
# empty line for a neater/clearer output
    print("")

    # increment count after each round
    count += 1

# comparison to determine overall winner after 6 rounds
if player_points > computer_points:
    print("You are the overall winner!!!")
elif player_points == computer_points:
    print("You and computer are tied!!!")
else:
    print("Computer is the overall winner!!!, try again ")



