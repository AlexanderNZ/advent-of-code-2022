with open('input.txt') as file:
    content = file.readlines()
    lines = [tuple(map(int, x.strip().split())) for x in content]

array_one = [x[0] for x in lines]
array_two = [x[1] for x in lines]

print('Array One ():', array_one)
print('Array Two ():', array_two)

# Calculate a total similarity score by adding up each number in array_one
# after multiplying it by the number of times that number appears in array_two.

# Calculate the total similarity score - this is not very efficient
similarity_score = 0
for x in array_one:
    count_in_array_two = array_two.count(x)
    similarity_score += x * count_in_array_two

print('Total Similarity Score:', similarity_score)