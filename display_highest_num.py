highest = None

while True:
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input!")
        break
    if highest is None or number > highest:
            highest = number
print(highest)
