import string


def split_bag_compartments(bag):
    n = len(bag)
    if n % 2 == 0:
        bag_one = bag[0:n // 2]
        bag_two = bag[n // 2:]
        return bag_one, bag_two
    else:
        bag_one = bag[0:(n // 2 + 1)]
        bag_two = bag[(n // 2 + 1):]
        return bag_one, bag_two


def find_packing_errors(bags):
    compartment_one = [*bags[0]]
    compartment_two = [*bags[1]]
    items_in_both_compartments = set(compartment_one).intersection(compartment_two)
    return [*items_in_both_compartments][0]


def improperly_packed_item_priority(items):
    lowercase_priority_dictionary = dict(zip(string.ascii_lowercase, range(1, 27)))
    uppercase_priority_dictionary = dict(zip(string.ascii_uppercase, range(27, 53)))
    priority = 0

    for item in items:
        if item.isupper():
            priority = priority + uppercase_priority_dictionary[item]
        else:
            priority = priority + lowercase_priority_dictionary[item]
    return priority


with open('input.txt') as file:
    content = file.readlines()
    lines = [x.strip() for x in content]
    improperly_packed_items = []
    for line in lines:
        improperly_packed_items.append(find_packing_errors(split_bag_compartments(line)))
    print('Priority Sum: %s' % improperly_packed_item_priority(improperly_packed_items))
