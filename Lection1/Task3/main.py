print("Hello There, I am simple temperature convertator.\nPick temperature scale and I will convert them!\n1. From Fahrenheit to Celsius\n2.From Celsius to Fahrenheit")
user_choice = int(input ("Write numer 1 or 2 to choose"))
if user_choice == 1:
    farenhait = float(input("Pls enter temperature in Fahrenheit and I will do my magic: "))
    calculus = (farenhait - 32) * 5/9
    print("so your Fahrenheit is ", calculus, "Celsius")
elif user_choice == 2:
    calculus = float(input("Pls enter temperature in Celsius and I will do my magic: "))
    farenhait = (calculus * 9/5) + 32)
    print("so your Celsius is ", calculus, "Fahrenheit")
else:
    print("XD I am from Valve idk numbers higher then 2")