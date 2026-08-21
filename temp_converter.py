import json

print("Temparature converter from celsius to fahrenheit\n")

class TemparatureConverter:
    def __init__(self, name):
        self.name = name
        try:
            with open("history.json", "r") as file:
                self.history = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.history = []



    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius*9/5 + 32)
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = ((fahrenheit-32)*5/9)
        return celsius


    def save_history(self):
        with open("history.json", "w")as file:
           json.dump(self.history, file)


    def run(self):
        running = True

        menu_text = (f"\nHello {self.name} choose between 1 or 2 or 3; \n\n"
                "(1) To convert your temparature from celsius to fahrenheit or \n"
                "(2) To convert your temparature from fahrenheit to celsius \n"
                "(3) To show history of the last temparature conversions")


        while running:
            print(menu_text)

            while True:
                try:
                    choice  = int(input("\nEnter your choice, 1 or 2 or 3 : "))
                    if choice in (1, 2, 3):
                        break
                    else:
                        print("Please enter either 1, 2, or 3.")
                except ValueError:
                    print("please enter a valid number.")



            if choice ==  1:
                while True:
                    try:
                        celsius = round(float(input("\nWhat's the temparature in celsius: ")), 2)
                        if celsius >= -273.15:
                            break
                        else:
                            print("Enter a valid degree Celsius reading.")
                    except ValueError:
                        print("Please enter a valid temparature reading.")
                result = self.celsius_to_fahrenheit(celsius)
                print(f"\n{self.name} the temparature is changed from {celsius:.2f} to {result:.2f} Fahrenheit.\n")
                self.history.append({"from" : "Celsius", "input" : celsius, "to" : "Fahrenheit", "result": result})
                self.save_file()

            elif choice == 2:
                while True:
                    try:
                        fahrenheit = round(float(input("\nWhat's the temparature in fahrenheit: ")), 2)
                        if fahrenheit >= -459.67:
                            break
                        else:
                            print("Enter a valid Fahrenheit temparature reading.")
                    except ValueError:
                        print("Please enter a valid temparature reading.")
                result = self.fahrenheit_to_celsius(fahrenheit)
                print(f"\n{self.name} the temparature is changed from {fahrenheit:.2f} to {result:.2f} Celsius.\n")
                self.history.append({"from" : "Fahrenheit", "input": fahrenheit, "to" : "celsius", "result" : result})
                self.save_history()

            elif choice == 3:
                if not self.history:
                    print(f"\nNothing in history yet {self.name}.\n")
                else:
                    for index, entry in enumerate(self.history, start = 1):
                        print(f"({index}). Changed your temparature from {entry['from']} :  {entry['input']:.2f} to {entry['to']} : {entry['result']:.2f}\n")

            while True:
                answer = input("To Continue type \"y\". \nTo quit type \"q\". : ")
                if answer in ("y", "q"):
                    break
                else:
                    print("Please enter either 'y' or 'q'.")

                
            if answer == "q":
                running = False

        print(f"Thank you {self.name} for using me to Convert your temparatures")

name = input("What's your name? ")
converter = TemparatureConverter(name)
converter.run()