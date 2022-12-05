with open("input.txt", "r") as f:
    contents = f.readlines()

stacks = [[] for _ in range(9)]
for x in contents[7::-1]:
    for i in range(9):
        if x[4*i + 1] != ' ':
            stacks[i].append(x[4*i + 1])

for y in contents[10::]:
    y = y.replace('\n', '')
    y = y.split(' ')
    num_moved = int(y[1])
    start = int(y[3]) - 1
    end = int(y[5]) - 1
    if len(stacks[start]) < num_moved:
        num_moved = len(stacks[start])
    pos_moved = -1 * num_moved
    moved_crates = stacks[start][pos_moved::]
    stacks[end] = stacks[end] + moved_crates
    del stacks[start][pos_moved:]

end_pos = []
for i in range(9):
    end_pos.append(stacks[i][-1])

print(''.join(end_pos))
