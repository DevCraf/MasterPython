number_table = int(input("What is the number of multyply table "))
count = 0
result = 0

while count <= 10:
    result = number_table * count
    print(f"Table is {number_table} X {count} = {result}")
    count += 1
