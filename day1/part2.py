with open("input.txt", "r") as f:
    contents = f.readlines()

elf_sums = []
current_sum = 0
for x in contents:
    if x != '\n':
        current_sum = current_sum + int(x)
    else:
        elf_sums.append(current_sum)
        current_sum = 0

elf_sums.sort(reverse=True)
top3_sum = elf_sums[0] + elf_sums[1] + elf_sums[2]
print('The three elves carrying the most calories are carrying', top3_sum, 'total calories!')
