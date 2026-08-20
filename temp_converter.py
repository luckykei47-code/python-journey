print("Temparature converter from celsius to fahrenheit\n")

name = input("What's your name? ")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5 + 32)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = ((fahrenheit-32)*5/9)
    return celsius


history = []

running = True

menu_text = (f"\nHello {name} choose between 1 or 2 or 3; \n\n"
          "(1) To convert your temparature from celsius to fahrenheit or \n"
          "(2) To convert your temparature from fahrenheit to celsius \n"
          "(3) To show history of the last temparature conversions")


while running:
    print(menu_text)
    choice  = int(input("\nEnter your choice, 1 or 2 or 3 : "))
    if choice ==  1:
        celsius = round(float(input("\nWhat's the temparature in celsius: ")), 2)
        result = celsius_to_fahrenheit(celsius)
        print(f"\n{name} the temparature is changed from {celsius:.2f} to {result:.2f} Fahrenheit.\n")
        history.append({"from" : "Celsius", "input" : celsius, "to" : "Fahrenheit", "result": result})
    elif choice == 2:
        fahrenheit = round(float(input("\nWhat's the temparature in fahrenheit: ")), 2)
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"\n{name} the temparature is changed from {fahrenheit:.2f} to {result:.2f} Celsius.\n")
        history.append({"from" : "Fahrenheit", "input": fahrenheit, "to" : "celsius", "result" : result})
    elif choice == 3:
        if not history:
            print(f"\nNothing in history yet {name}.\n")
        else:
            for index,entry in enumerate(history, start = 1):
                print(f"({index}). Changed your temp from {entry['from']} :  {entry['input']:.2f} to {entry['to']} : {entry['result']:.2f}\n")


    answer = input("To Continue type \"y\". \nTo quit type \"q\". : ")
    if answer == "q":
        running = False

print(f"Thank you {name} for using me to Convert your temparatures")
