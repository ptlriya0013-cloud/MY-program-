#Print your name, age, and city in one line
name, age, city = "Riya ", 21, "Chikhli" 
print(name, age, city)

#Take user input for two numbers and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

#Convert temperature from Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

#Store your name in a variable and print it in uppercase
name = "Riya Patel"
print(name.upper())

#Ask the user for their birth year and calculate current age
birth_year = int(input("Enter your birth year: "))
current_year = 2026
print("Your age is:", current_year - birth_year)



#Swap the values of two variables
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

#Calculate the area of a rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)



#Check if a number is positive or negative
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")


#Ask for two numbers and print their average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
avg = (a + b) / 2
print("Average =", avg)


