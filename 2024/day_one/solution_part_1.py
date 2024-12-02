with open('input.txt') as file:
    content = file.readlines()
    lines = [tuple(map(int, x.strip().split())) for x in content]

array_one = [x[0] for x in lines]
array_two = [x[1] for x in lines]

# Sort both arrays from highest to lowest
array_one_sorted = sorted(array_one, reverse=True)
array_two_sorted = sorted(array_two, reverse=True)

# Calculate the distance
distance = [abs(a - b) for a, b in zip(array_one_sorted, array_two_sorted)]
total_distance = sum(distance)
print('Total Distance:', total_distance)