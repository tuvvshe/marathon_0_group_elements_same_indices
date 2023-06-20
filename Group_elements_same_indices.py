input_lists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
output_lists = []
index = 0

for i in range(len(input_lists[0])):
    output_lists.append([])
    for j in range(len(input_lists)):
        output_lists[index].append(input_lists[j][ index])
    index = index + 1
a, b, c = output_lists[0], output_lists[1], output_lists[2]
print(a, b, c)    