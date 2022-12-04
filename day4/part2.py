with open("input.txt", "r") as f:
    contents = f.readlines()

overlap_count = 0
for y in contents:
    x = y.replace('\n', '')
    groups = x.split(',', 1)
    group_a = groups[0].split('-')
    group_b = groups[1].split('-')
    set_a = set(range(int(group_a[0]), int(group_a[1]) + 1))
    set_b = set(range(int(group_b[0]), int(group_b[1]) + 1))
    common = list(set_a & set_b)
    if len(common) != 0:
        overlap_count += 1

print(overlap_count)
