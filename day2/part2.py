with open("input.txt", "r") as f:
    contents = f.readlines()

my_score = 0
elf = ['A', 'B', 'C']
results = ['X', 'Y', 'Z']

for x in contents:
    result_score = 3*results.index(x[2])
    diff = results.index(x[2]) + 2
    shape_score = (elf.index(x[0]) + diff) % 3 + 1
    my_score = my_score + result_score + shape_score
print(my_score)
