print("temparature converter from celsius to fahrenheit")
name = input("What's your name? ")
age = int(input("What's your age? "))
celsius = float(input("whats your temparature in celsius? "))

fahrenheit = (celsius*9/5+32)

print(f"Hello {name}, your age is {age} years old.\n{name} your temparature is {fahrenheit: .2f}F")