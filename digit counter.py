n = int(input("Enter a number: "))
count = 0
while n != 0:
    n //= 10
    count += 1
print(f"The number has {count if count > 0 else 1} digits.")
