import random

def pick_winner(teams):
    """
    picks one of the teams selected, or, picks a tie
    """
    teams.append('TIE')
    return random.choice(teams)