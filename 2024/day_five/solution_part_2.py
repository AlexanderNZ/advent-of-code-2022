def parse_rules(rules_section):
    rules = {}
    for rule in rules_section:
        x, y = rule.split('|')
        if x not in rules:
            rules[x] = []
        rules[x].append(y)
    return rules

def get_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def check_update_order(rules_section, updates_list):
    rules = parse_rules(rules_section)

    def is_in_right_order(update):
        position = {page: idx for idx, page in enumerate(update)}
        for x, ys in rules.items():
            if x in position:
                for y in ys:
                    if y in position and position[x] > position[y]:
                        return False
        return True

    right_order_updates = []
    wrong_order_updates = []
    for update in updates_list:
        order_status = "right_order" if is_in_right_order(update) else "wrong_order"
        middle_page = get_middle_page(update) if order_status == "right_order" else None
        if order_status == "right_order":
            right_order_updates.append((update, order_status, middle_page))
        else:
            wrong_order_updates.append((update, order_status, middle_page))

    return right_order_updates, wrong_order_updates

def sum_middle_pages(results):
    return sum(int(middle_page) for _, order_status, middle_page in results if order_status == "right_order")

def topological_sort(graph):
    from collections import deque, defaultdict

    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    sorted_list = []

    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list

def correct_order(update, rules):
    graph = {page: [] for page in update}
    for x, ys in rules.items():
        if x in graph:
            for y in ys:
                if y in graph:
                    graph[x].append(y)

    sorted_update = topological_sort(graph)
    return sorted_update

# Read the content of the file
with open('input.txt', 'r') as file:
    content = file.read().splitlines()

separator_index = content.index('')

rules_section = content[:separator_index]
updates_section = content[separator_index + 1:]

updates_list = [line.split(',') for line in updates_section]

rules = parse_rules(rules_section)
right_order_updates, wrong_order_updates = check_update_order(rules_section, updates_list)

corrected_wrong_order_updates = [(correct_order(update, rules), "right_order", get_middle_page(correct_order(update, rules))) for update, _, _ in wrong_order_updates]

print("Correctly ordered updates:")
for idx, (update, order_status, middle_page) in enumerate(right_order_updates, start=1):
    print(f"{idx}: {order_status}, {middle_page}, {update}")

print("\nIncorrectly ordered updates (corrected):")
for idx, (update, order_status, middle_page) in enumerate(corrected_wrong_order_updates, start=1):
    print(f"{idx}: {order_status}, {middle_page}, {update}")

total_middle_pages = sum_middle_pages(right_order_updates)
print(f"Sum of middle pages: {total_middle_pages}")

total_corrected_middle_pages = sum_middle_pages(corrected_wrong_order_updates)
print(f"Sum of middle pages (corrected): {total_corrected_middle_pages}")