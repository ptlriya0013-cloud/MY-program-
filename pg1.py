name, age, city = "Riya ", 21, "Chikhli" 
print(name, age, city)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)


name = "Riya Patel"
print(name.upper())


birth_year = int(input("Enter your birth year: "))
current_year = 2026
print("Your age is:", current_year - birth_year)




a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)




num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")



a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
avg = (a + b) / 2
print("Average =", avg)

