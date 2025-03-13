numbers = []

for i in range(10):
    number = int(input(f"Enter a number {i+1}: "))
    numbers.append(number)

duplicate = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicate:
            duplicate.append(number)

print(duplicate)