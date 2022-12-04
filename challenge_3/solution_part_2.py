import string


def find_badge_matches(bags):
    compartment_one = [*bags[0]]
    compartment_two = [*bags[1]]
    compartment_three = [*bags[2]]
    badge_candidate = set(compartment_one).intersection(compartment_two).intersection(compartment_three)
    return [*badge_candidate][0]


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


def grouper(iterable, n, fillvalue=None):
    try:
        from itertools import izip_longest
    except ImportError:
        from itertools import zip_longest as izip_longest

    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


with open('input.txt') as file:
    badges = []
    for lines in grouper(file, 3, ''):
        assert len(lines) == 3
        bag_group = [x.strip() for x in lines]
        badges.append(find_badge_matches(bag_group))
    badge_priority_sum = improperly_packed_item_priority(badges)
    print('Badge Priority Sum: %s' % badge_priority_sum)
