# Challenge lesson 27

number_list = [3, 5, 78, -7, 45, 99]
print(max(number_list))
print("\n")


def maxNumber(numbers):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value
            
print("Max number in the list is:", maxNumber(number_list))





