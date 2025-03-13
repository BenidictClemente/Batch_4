numbers = []
while True:
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input! Exiting program.")
        break
    numbers.append(number)

# Sort the list from lowest to highest
numbers.sort(reverse=True)

print( numbers)