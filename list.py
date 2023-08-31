# Lists
number_list = [1, 3, -5, 105, 182]
print(number_list)
print(number_list[1])

number_list[1] = 2
number_list.append(201)

print()

for i in range(0, len(number_list)):
    print(number_list[i], end =" ")

print("\n")
new_list = []
for number in number_list:
    new_list.append(number * 2)
    print(number)
    
print(new_list)
    