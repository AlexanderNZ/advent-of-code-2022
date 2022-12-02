with open('input.txt') as file:
    content = file.readlines()
    lines = [x.strip() for x in content]
    top_three_fattest_elves = {
        'elf_one': 1,
        'elf_two': 2,
        'elf_three': 3,
    }
    potential_fat_elf = 0
    for line in lines:
        if line != '':
            potential_fat_elf = potential_fat_elf + int(line)
        else:
            for elf in top_three_fattest_elves:
                smallest_of_the_fat_key = min(top_three_fattest_elves, key=top_three_fattest_elves.get)
                smallest_of_the_fat_value = min(top_three_fattest_elves.values())
                if smallest_of_the_fat_value < potential_fat_elf:
                    top_three_fattest_elves[smallest_of_the_fat_key] = potential_fat_elf
                break
            potential_fat_elf = 0
print(sum(top_three_fattest_elves.values()))
