with open("input.txt", "r") as f:
    contents = f.readlines()

my_score = 0
shape = ['X', 'Y', 'Z']
elf = ['A', 'B', 'C']
for x in contents:
    shape_score = shape.index(x[2]) + 1
    if x[0] == elf[(shape.index(x[2]) + 1) % 3]:
        result_score = 0
    elif x[0] == elf[(shape.index(x[2]) + 2) % 3]:
        result_score = 6
    else:
        result_score = 3
    my_score = my_score + shape_score + result_score
print(my_score)
