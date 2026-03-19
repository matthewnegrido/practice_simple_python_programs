#Prog01
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

if num_1 > num_2:
    print(num_1)
elif num_1 < num_2:
    print(num_2)
else:
    print("Both numbers are equal!")

#Prog02
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

if num_1 > num_2:
    print(num_1)
elif num_1 < num_2:
    print(num_2)
else:
    print("Both numbers are equal!")

#Prog03
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))

print(num_1 + num_2)

#Prog04
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))

print(num_1 * num_2)

#Prog05
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))

print(num_1 / num_2)

#Prog06
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))

print(num_1 ** num_2)

#Prog07
total = 0

for i in range(10):
    num = float(input("Enter a number: "))
    total += num

print("The sum is:", total)

#Prog08
odd_count = 0

for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        odd_count += 1

print("Total odd numbers:", odd_count)
