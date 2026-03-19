#Prog01
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

if num_1 > num_2:
    print(num_2)
elif num_1 < num_2:
    print(num_1)
else:
    print("Both numbers are equal!")

#Prog02
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

if num_1 > num_2 or num_1 < num_2:
    print("The two numbers are not equal")
else:
    print("The two numbers are equal!")

#Prog03
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

print(num_1 - num_2)

#Prog04
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

print(num_1 // num_2)

#Prog05
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

print(num_1 % num_2)

#Prog06
result = float(input("Enter number 1: "))

for i in range(2, 11):
    num = float(input(f"Enter number {i}: "))
    result -= num

print("The final result is:", result)