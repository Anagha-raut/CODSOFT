import random
def get_computer_choice():
    """Generate a random choice for the computer """
    choices =['R','S','p']
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    """Determine the winner on the game logic"""
    if user_choice == computer_choice :
        return"It,s a tie"
    if (user_choice=='R' and computer_choice=='S') or\
        (user_choice=='S' and computer_choice=='P')or\
        (user_choice=='P'and computer_choice=='R'):
            return"YOU WIN"
    return"YOU LOSE"

def play_game():
    """Play a round of Rock-Paper-Scissors"""
    print ("**WELCOME TO ROCK-PAPER-SCISSORS!**")
    print("**Please choose one of the following options:**")
    print("*Rock(R)")
    print("*Paper(P)")
    print("*Scissors(S)")
    user_choice=input("**Type 'R','P','S',to make your choice:**").upper()
    while user_choice not in ['R','S','P']:
        user_choice=input("Invaild input.Please enter 'R','P','S':").upper()
        
        computer_choice=get_computer_choice()
        print(f"\n**You chose:**{user_choice}")
        print(f"**Computer chose:**{computer_choice}\n")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
def main():
    """Main game loop"""
    play_again='Y'
    user_score=0
    computer_score=0
    while play_again.upper()=='Y':
        play_game()
        print(f"\n**Score -You: {user_score},Computer:{computer_score}**")
        play_again=input("\n**Do you want to play again? (Y/N)")
        while play_again.upper()not in ['Y','N']:
            play_again=input("Invalid input.Please enter'Y' or 'N':")
if __name__=="__main__":
    main()         
   
           
    
    
    