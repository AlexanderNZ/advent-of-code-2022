import re
import json


def remove_corrupted_input(input_string):
    # Use regex to find all valid mul(X,Y) patterns where X and Y are 1-3 digit numbers
    valid_sets_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    valid_sets = valid_sets_pattern.findall(input_string)
    cleaned_string = ''.join(valid_sets)

    return cleaned_string

def remove_bad_mul_calls(potential_unsafe_mul):
    valid_mul_pattern = re.compile(r'^mul\(\d+,\d+\)$')
    filtered_list = [item for item in potential_unsafe_mul if valid_mul_pattern.match(item)]

    return filtered_list

def split_mul_declarations(input_string):
    mul_declarations = []
    i = 0
    while i < len(input_string):
        if input_string[i:i+4] == 'mul(' or input_string[i:i+4] == 'mul[' or input_string[i:i+4] == 'mul{':
            start = i
            i += 4
            counter = 1
            while i < len(input_string) and counter > 0:
                if input_string[i] in '([{':
                    counter += 1
                elif input_string[i] in ')]}':
                    counter -= 1
                i += 1
            mul_declarations.append(input_string[start:i])
        else:
            i += 1
    return mul_declarations

def evaluate_mul_expression(expression):
    match = re.match(r'^mul\((\d+),(\d+)\)$', expression)
    if match:
        return int(match.group(1)) * int(match.group(2))
    else:
        raise ValueError("Invalid mul expression")

with open('input.txt') as file:
    content = file.read()
    cleaned_content = remove_corrupted_input(content)
    mul_list = split_mul_declarations(cleaned_content)
    filtered_mul_list = remove_bad_mul_calls(mul_list)

print(json.dumps({"Actual": filtered_mul_list}, indent=4))

total_result = 0

for mul_expression in filtered_mul_list:
    result = evaluate_mul_expression(mul_expression)
    total_result += result

# Print the accumulated result
print(f"Result: {total_result}")