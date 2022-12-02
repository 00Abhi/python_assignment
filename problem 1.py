print('\n')
list_one = [1, 2, 3, 4]
list_two = [5, 6, 7, 8]
print("List 1 and List 2: ", list_one, 'and', list_two, '\n')
print("Adding this two list index wise: ")

total = []
for item in range(len(list_one)):
    list_three = list_one[item] + list_two[item]
    total.append(list_three)

print(total)
