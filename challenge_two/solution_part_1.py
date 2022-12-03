def get_win_loss_draw_points(opponent_pick, my_pick):
    if opponent_pick == 'A' and my_pick == 'X':
        return 3  # Rock + Rock = We Draw
    if opponent_pick == 'B' and my_pick == 'X':
        return 0  # Paper + Rock = I Lose
    if opponent_pick == 'C' and my_pick == 'X':
        return 6  # Scissors + Rock = I Win
    if opponent_pick == 'A' and my_pick == 'Y':
        return 6  # Rock + Paper = I Win
    if opponent_pick == 'B' and my_pick == 'Y':
        return 3  # Paper + Paper = We Draw
    if opponent_pick == 'C' and my_pick == 'Y':
        return 0  # Scissors + Paper = I Lose
    if opponent_pick == 'A' and my_pick == 'Z':
        return 0  # Rock + Scissors = I Lose
    if opponent_pick == 'B' and my_pick == 'Z':
        return 6  # Paper + Scissors = I Win
    if opponent_pick == 'C' and my_pick == 'Z':
        return 3  # Scissors + Scissors = We Draw


def tally_score(round_result, my_input):
    if my_input == 'X':
        return round_result + 1  # X - Rock: 1 Point
    if my_input == 'Y':
        return round_result + 2  # Y - Paper: 2 Points
    if my_input == 'Z':
        return round_result + 3  # Z - Scissors: 3 Points


with open('input.txt') as file:
    content = file.readlines()
    lines = [x.strip() for x in content]
    score_accumulator = 0
    for line in lines:
        split = line.split()
        victory_points = get_win_loss_draw_points(opponent_pick=split[0], my_pick=split[1])
        score_accumulator = score_accumulator + tally_score(round_result=victory_points, my_input=split[1])
print(score_accumulator)
