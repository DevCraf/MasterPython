
count = 1
aproved = 0
denegade = 0

students_number = int(input('What number of students do you have ?: '))

while count <= students_number:
    note = int(input(f"What is note of students {count} :"))
    if note >= 5:
        aproved += 1
    else:
        denegade += 1
    count += 1

print(f"Students \"aproved\" are: {aproved}")
print(f"Students \"denegae\" are: {denegade}")
