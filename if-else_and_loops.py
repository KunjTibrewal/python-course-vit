#if-else
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(name, "is eligible to vote.")
elif (age < 18 and age >= 0):               #also 0<age<18 can be used  
    print(name, "is not eligible to vote.")
else:
    print("Invalid age entered.")

#loops --FOR
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11, 1):
    print(num, "x", i, "=", num * i)

#loops --WHILE
_ = 11
while _ <= 20:
    print(num, "x", _, "=", num * _)
    _ += 1 