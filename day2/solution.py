from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)

data = puzzle.input_data

rounds = [round.split(' ') for round in data.split('\n')] 

answer_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

# test = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

def round_score_decider(opponent, player):
    opponent_val, player_val = answer_dict.get(opponent), answer_dict.get(player)
    if player_val == opponent_val+1: 
        return(6+player_val)
    elif player_val == 1 and opponent_val == 3:
        return(6+player_val)
    elif player_val == opponent_val:
        return(3+player_val)                
    else:
        return(player_val)

solution_part_1 = 0

for round in rounds:
    solution_part_1 += round_score_decider(*round)

print(solution_part_1)

def round_score_decider2(opponent, outcome):
    opponent_val = answer_dict.get(opponent)
    if outcome == 'X':
        if opponent_val == 1:
            return(3)
        else:
            return(opponent_val-1)
    elif outcome == 'Y':
        return(opponent_val + 3)
    else:
        if opponent_val == 3:
            return(7)
        else:
            return(opponent_val+7)

solution_part_2 = 0

for round in rounds:
    solution_part_2 += round_score_decider2(*round)

print(solution_part_2)