"""
count = 0

for count in range(0, 5):
    print(f"Numero {count}")

"""

print("\n########## EJEMPLO ############")

number_table = int(input("What is the number of multyply table "))
count = 0
result = 0
for count in range(1, 11):
    result = count * number_table
    print(f"table is {number_table} X {count} = {result}")
