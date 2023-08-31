# User input

# name = input("Give me your name: ")
# print("Hello", name, "!")

number = int(input("Enter a number between 1 and 100: "))
   

if number < 1 or number > 100:
    print("Wrong number:", number)
else:
    print("Number is in range 1 - 100:", str(number))
