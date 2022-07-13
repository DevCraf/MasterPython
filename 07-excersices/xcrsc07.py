num01 = int(input("first number is "))
num02 = int(input("second number is "))

for impar in range(num01, (num02 + 1)):
    if impar % 2 == 1:
        print(f"{impar}")
