print("Hello, welcome to Python Basics!\n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2

print("\nSum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Division:", division_result)

if num1 > num2:
    print("\nnum1 is greater than num2")
elif num1 == num2:
    print("\nnum1 is equal to num2")
else:
    print("\nnum1 is less than num2")

for i in range(5):
    print("Iteration", i+1)

count = 0
while count < 5:
    print("Count:", count+1)
    count += 1

def greet(name):
    print("\nHello,", name)

greet("Alice")

fruits = ["apple", "banana", "orange"]
print("\nFruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("grape")
print("Updated fruits:", fruits)

fruits.remove("banana")
print("Updated fruits after removing banana:", fruits)

person = {"name": "John", "age": 30, "city": "New York"}
print("\nPerson:", person)
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
