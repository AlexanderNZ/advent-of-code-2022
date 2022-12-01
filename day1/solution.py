with open('input.txt') as file:
    content = file.readlines()
    lines = [x.strip() for x in content]
    fattest_elf = 0
    potential_fat_elf = 0

    for line in lines:
        if line != '':
            potential_fat_elf = potential_fat_elf + int(line)
        else:
            fattest_elf = max(fattest_elf, potential_fat_elf)
            potential_fat_elf = 0
print('Current Elf: %s' % fattest_elf)
