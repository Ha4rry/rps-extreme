import random
import time

# V3

def newline():
    print("\n")

playerscore = 0
computerscore = 0



print("""


 ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█   ▄  █ █       █       █  █       █  █▄█  █       █   ▄  █ █       █  █▄█  █       █
█  █ █ █ █    ▄  █  ▄▄▄▄▄█  █    ▄▄▄█       █▄     ▄█  █ █ █ █    ▄▄▄█       █    ▄▄▄█
█   █▄▄█▄█   █▄█ █ █▄▄▄▄▄   █   █▄▄▄█       █ █   █ █   █▄▄█▄█   █▄▄▄█       █   █▄▄▄ 
█    ▄▄  █    ▄▄▄█▄▄▄▄▄  █  █    ▄▄▄██     █  █   █ █    ▄▄  █    ▄▄▄█       █    ▄▄▄█
█   █  █ █   █    ▄▄▄▄▄█ █  █   █▄▄▄█   ▄   █ █   █ █   █  █ █   █▄▄▄█ ██▄██ █   █▄▄▄ 
█▄▄▄█  █▄█▄▄▄█   █▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄▄█ █▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█
  

Hello, Welcome To RPS Extreme! (Rock Paper Scissors).
Each Run, You Get Five Goes To See Who Will Win,
You, or a Computer?
Play On To Find Out!


""")
username = input("Enter Your Name: ")

newline()

possible = ["r", "p", "s"]


def game():
    playerscore = 0
    computerscore = 0
    i = 1
    while i <= 5:
        computerChoice = random.choice(["Rock", "Paper", "Scissors"])
        userchoice = input("Ok Then, Type R for Rock, P for Paper or S for Scissors: ")
        userchoice = userchoice.lower()
        if userchoice in possible:
            if userchoice == 'r':
                time.sleep(0.1)
                print(f"You Chose Rock, The Computer Chose {computerChoice}.")
                time.sleep(0.5)
                if computerChoice == 'Scissors':
                    print("Player Wins Round")
                    playerscore += 1
                elif computerChoice == 'Paper':
                    print("Computer Wins Round")
                    computerscore += 1
                elif computerChoice == 'Rock':
                    print("Draw! No Points Given!")
                newline()
                    
            
            elif userchoice == 'p':
                time.sleep(0.1)
                print(f"You Chose Paper, The Computer Chose {computerChoice}.")
                time.sleep(0.5)
                if computerChoice == 'Scissors':
                    print("Computer Wins Round")
                    computerscore += 1
                elif computerChoice == 'Rock':
                    print("Player Wins Round")
                    playerscore += 1
                elif computerChoice == 'Paper':
                    print("Draw! No Points Given!")
                newline()
            
            elif userchoice == 's':
                time.sleep(0.1)
                print(f"You Chose Scissors, The Computer Chose {computerChoice}.")
                time.sleep(0.5)
                if computerChoice == 'Paper':
                    print("Player Wins Round")
                    playerscore += 1
                elif computerChoice == 'Rock':
                    print("Computer Wins Round")
                    computerscore += 1
                elif computerChoice == 'Scissors':
                    print("Draw! No Points Given!")
                newline()
            
            i += 1
        elif userchoice not in possible:
            print("ERROR: Please Enter A Valid Answer.")

    time.sleep(0.7)
    print("As It Turns Out... ")
    time.sleep(1)
    if computerscore > playerscore:
        print("""

     ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
    █  █ █  █       █  █ █  █  █   █   █       █       █       █
    █  █▄█  █   ▄   █  █ █  █  █   █   █   ▄   █  ▄▄▄▄▄█▄     ▄█
    █       █  █ █  █  █▄█  █  █   █   █  █ █  █ █▄▄▄▄▄  █   █  
    █▄     ▄█  █▄█  █       █  █   █▄▄▄█  █▄█  █▄▄▄▄▄  █ █   █  
      █   █ █       █       █  █       █       █▄▄▄▄▄█ █ █   █  
      █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  

    """)
        time.sleep(0.5)
        print(f"The Computer Won! (Sorry {username}!)")
    elif playerscore > computerscore:
        print("""

     ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄     ▄ ▄▄▄ ▄▄    ▄ 
    █  █ █  █       █  █ █  █  █ █ ▄ █ █   █  █  █ █
    █  █▄█  █   ▄   █  █ █  █  █ ██ ██ █   █   █▄█ █
    █       █  █ █  █  █▄█  █  █       █   █       █
    █▄     ▄█  █▄█  █       █  █       █   █  ▄    █
      █   █ █       █       █  █   ▄   █   █ █ █   █
      █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄▄▄█▄█  █▄▄█


    """)
        time.sleep(0.5)
        print(f"The Player Won! (Yes You, {username})")
    elif playerscore == playerscore:
        print("""
     ▄▄▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄▄▄ ▄     ▄ 
    █      ██   ▄  █ █      █ █ ▄ █ █
    █  ▄    █  █ █ █ █  ▄   █ ██ ██ █
    █ █ █   █   █▄▄█▄█ █▄█  █       █
    █ █▄█   █    ▄▄  █      █       █
    █       █   █  █ █  ▄   █   ▄   █
    █▄▄▄▄▄▄██▄▄▄█  █▄█▄█ █▄▄█▄▄█ █▄▄█

    """)
        time.sleep(0.5)
        print("It Was a Draw, No-one Wins, Thats Sad. :(")
    time.sleep(1)
    print(f"Your Score Was {playerscore} and The Computer's Score Was {computerscore}!")
    time.sleep(1.35)
    def isplayagain():
        newline()
        playagain = input("Do You Want To Play Again?: [y/n]: ")
        playagain = playagain.lower()
        if playagain == 'y' or 'yes':
            print("Starting Again...")
            newline()
            time.sleep(1)
            game()
        elif playagain == 'n' or 'no':
            newline()
            print("Quitting...")
            time.sleep(1)
            quit()
        else:
            print("Invalid Answer")
            isplayagain()
    isplayagain()
    

game()


while True:
    input()
    

