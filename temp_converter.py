print("Temparature converter from celsius to fahrenheit\n")

name = input("What's your name? ")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5 + 32)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = ((fahrenheit-32)*5/9)
    return celsius




running = True

while running:
    print(f"\nHello {name} choose between 1 or 2; \n(1) to convert your temparature from celsius to fahrenheit or \n(2) to convert your temparature from fahrenheit to celsius")
    choice  = int(input("\nEnter your choice, 1 or 2 : "))
    if choice ==  1:
        celsius = float(input("\nWhat's the temparature in celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{name} the temparature is changed from {celsius} to {result:.2f} Fahrenheit.")
    elif choice == 2:
        fahrenheit = float(input("\nWhat's the temparature in fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{name} the temparature is changed from {fahrenheit} to {result:.2f} Celsius.")

    answer = input("To Continue type \"y\". \nTo quit type \"q\". : ")
    if answer == "q":
        running = False

print(f"Thank you {name} for using me to Convert your temparatures")
