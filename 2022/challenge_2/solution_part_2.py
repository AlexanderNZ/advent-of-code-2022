def tally_score(desired_round_result, opponenent_pick):
    # X - Lose: 0 Point
    # Y - Draw: 3 Points
    # Z - Win: 6 Points

    # Rock: 1 Point
    # Paper: 2 Points
    # Scissors: 3 Points

    if opponenent_pick == 'A' and desired_round_result == 'X':
        return 0 + 3  # To lose against rock, I need to play scissors
    if opponenent_pick == 'B' and desired_round_result == 'X':
        return 0 + 1  # To lose against paper, I need to play rock
    if opponenent_pick == 'C' and desired_round_result == 'X':
        return 0 + 2  # To lose against scissors, I need to play paper

    if opponenent_pick == 'A' and desired_round_result == 'Y':
        return 3 + 1  # To draw against rock, I need to play rock
    if opponenent_pick == 'B' and desired_round_result == 'Y':
        return 3 + 2  # To draw against paper, I need to play paper
    if opponenent_pick == 'C' and desired_round_result == 'Y':
        return 3 + 3  # To draw against scissors, I need to play scissors

    if opponenent_pick == 'A' and desired_round_result == 'Z':
        return 6 + 2  # To win against rock, I need to play paper
    if opponenent_pick == 'B' and desired_round_result == 'Z':
        return 6 + 3  # To win against paper, I need to play scissors
    if opponenent_pick == 'C' and desired_round_result == 'Z':
        return 6 + 1  # To win against scissors, I need to play rock


with open('input.txt') as file:
    content = file.readlines()
    lines = [x.strip() for x in content]
    score_accumulator = 0
    for line in lines:
        split = line.split()
        score_accumulator = score_accumulator + tally_score(desired_round_result=split[1], opponenent_pick=split[0])
    print(score_accumulator)
