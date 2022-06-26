import random 

def play():
 
    option_tool = ['r', 'p', 's']
    user = input(" Enter 'r' for rock, 'p' for papaeror 's' for scissors " )

    while user not in option_tool:
        user = input(" Enter 'r' for rock, 'p' for papaeror 's' for scissors " )

    computer = random.choice(option_tool)

    if user == computer:
        return 'Tie, nobody won!'
    
    if win_player_1(user, computer):
        return 'Congratulations, you won!'
    else:
        return 'You lost!'

def win_player_1(player_1, player_2):
    ''' This function returns true if player wins'''
    if(player_1 == 'r' and player_2 == 's') or (player_1 == 's' and player_2 == 'p') \
        or (player_1 == 'p' and player_2 == 'r'):
        return True
    
    return False

if __name__ == '__main__':
    print(play())
    print("End game!")