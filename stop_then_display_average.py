numbers = []

while True:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input) 
    except ValueError:
        print("Invalid number!")
        break 
    numbers.append(number)
    
if numbers:
    average = sum(numbers) / len(numbers)
    print(average)
else:
    print("No numbers to calculate the average.")
