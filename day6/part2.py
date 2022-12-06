with open("input.txt", "r") as f:
    contents = f.read()

marker = []
found = 0
counter = 0
for x in contents:
    counter += 1
    if len(marker) <= 13:
        marker.append(x)
        found = 0
    else:
        marker.pop(0)
        marker.append(x)
        sum_instances = 0
        for i in range(14):
            sum_instances += marker.count(marker[i])
        if sum_instances == 14:
            found = 1
            print(counter)
            break
        else:
            found = 0

print(contents[counter - 14:counter])
