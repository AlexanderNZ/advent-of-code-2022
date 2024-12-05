def check_update_order(rules_section, updates_list):
    # Parse the rules into a dictionary
    rules = {}
    for rule in rules_section:
        x, y = rule.split('|')
        if x not in rules:
            rules[x] = []
        rules[x].append(y)

    def is_in_right_order(update):
        # Create a position map for quick lookup
        position = {page: idx for idx, page in enumerate(update)}
        for x, ys in rules.items():
            if x in position:
                for y in ys:
                    if y in position and position[x] > position[y]:
                        return False
        return True

    def get_middle_page(update):
        mid_index = len(update) // 2
        return update[mid_index]

    # Check each update and determine if it is in the right order
    result = []
    for update in updates_list:
        order_status = "right_order" if is_in_right_order(update) else "wrong_order"
        middle_page = get_middle_page(update) if order_status == "right_order" else None
        result.append((update, order_status, middle_page))

    return result

def sum_middle_pages(results):
    return sum(int(middle_page) for _, order_status, middle_page in results if order_status == "right_order")

# Read the content of the file
with open('input.txt', 'r') as file:
    content = file.read().splitlines()

# Find the index of the empty line that separates the two sections
separator_index = content.index('')

# Split the content into two sections
rules_section = content[:separator_index]
updates_section = content[separator_index + 1:]

updates_list = []
for line in updates_section:
    updates_list.append(line.split(','))

result = check_update_order(rules_section, updates_list)

# Print each tuple on a new line with the update number, order status, and middle page number if applicable
for idx, (update, order_status, middle_page) in enumerate(result, start=1):
    if order_status == "right_order":
        print(f"{idx}: {order_status}, {middle_page}, {update}")
    else:
        print(f"{idx}: {order_status}, {update}")

# Calculate and print the sum of middle pages from correctly ordered updates
total_middle_pages = sum_middle_pages(result)
print(f"Sum of middle pages: {total_middle_pages}")