try:
    age = int(input("Enter your age: "))
    assert age > 0
    print("Your age is:", age)

except AssertionError:
    print("Assertion Error: Age must be greater than 0!")