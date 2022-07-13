

num01 = int(input("first number is "))
num02 = int(input("second number is "))

"""
for human in range(num01, num02):
    print(f"the number is {human}")
"""
if num01 < num02:
    while num01 <= num02:
        print(f"the number is {num01}")
        num01 += 1
else:
    print(f"the number is {num01} es mayor que {num02}")
