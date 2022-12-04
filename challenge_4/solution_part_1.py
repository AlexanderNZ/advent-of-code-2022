def expand_assigned_sections(section):
    expanded_range = []
    for subsection in section.split(','):
        if '-' not in subsection:
            expanded_range.append(int(subsection))
        else:
            l, h = map(int, subsection.split('-'))
            expanded_range += range(l, h + 1)
    return expanded_range


with open('input.txt') as file:
    content = file.readlines()
    lines = [x.strip() for x in content]
    duplicate_assignments = 0
    for line in lines:
        section_one, section_two = line.split(',')
        left_section = ''.join([str(x) for x in expand_assigned_sections(section_one)])
        right_section = ''.join([str(x) for x in expand_assigned_sections(section_two)])

        if left_section in right_section or right_section in left_section:
            duplicate_assignments += 1
    print(duplicate_assignments)


