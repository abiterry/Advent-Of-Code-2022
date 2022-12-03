with open("input.txt", "r") as f:
    contents = f.readlines()
    print(contents)

total_score = 0
for i in range(int(len(contents)/3)):
    elf1 = contents[3*i].replace('\n', '')
    elf2 = contents[3*i + 1].replace('\n', '')
    elf3 = contents[3*i + 2].replace('\n', '')
    common = list(set(elf1) & set(elf2) & set(elf3))
    for x in common:
        if x.islower():
            group_score = ord(x) - 96
        else:
            group_score = ord(x) - 38
    total_score = total_score + group_score

print(total_score)
