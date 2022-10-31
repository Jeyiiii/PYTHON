# SIMPLE PHYSICS CALCULATOR

# Function that solves SPEED problem
def Speed (x, y):
    return x / y

# Function that solves DENSITY Problem
def Density (x, y):
    return x / y

# Function that solves FORCE problem
def  Force(x, y):
    return x * y

# Function that solves MASS problem
def Mass (x, y):
    return x * y

# Function that solves POWER problem
def Power (x, y):
    return x / y

# Taking name input from the user
name = input("ENTER YOUR NAME: ")

print ("WELCOME TO PHYSICS CALCULATOR " + name +  "!")
print ("Select Formula")
print ("1. Speed")
print ("2. Density")
print ("3. Force")
print ("4. Mass")
print ("5. Power")

while True:
    choice = input("Enter choice 1/2/3/4/5: ")

# Checking if the choice is one of the five options
    if choice == '1' :
            num1= float(input("Enter value for Distance(in Meters): "))
            num2= float(input("Enter value for Time (in Seconds) : "))

            print ("Speed = ", num1, "/", num2, "=", Speed(num1, num2), "m/s")
            
    elif choice == '2':
            num1= float(input("Enter value for Mass(in Kilograms): "))
            num2= float(input("Enter value for Volume (in Cubic Meters) : "))

            print(" Density = ", num1, "/", num2, "=", Density(num1, num2), "kg/m^3")
           
    elif choice == '3':
            num1= float(input("Enter value for Mass(in Kilograms): "))
            num2= float(input("Enter value for Acceleration (in Meters/seconds^2) : "))

            print("Force = ", num1, "*", num2, "=", Force(num1, num2), "N")
           
    elif choice == '4':
            num1= float(input("Enter value for Density(in Kilogram per Cubic Meter): "))
            num2= float(input("Enter value for Volume (in Cubic Meter) : "))

            print("Mass = ", num1, "*", num2, "=", Mass(num1, num2), "kg")
           
    elif choice == '5':
            num1= float(input("Enter value for Work(in Joules): "))
            num2= float(input("Enter value for Time (in Seconds) : "))

            print("Power = ", num1, "/", num2, "=", Power(num1, num2), "W")

    # Checking if the user input is not applicable or invalid
    else:
        print ("Invalid choice. Please Try Again")

    # Checking if the user wants to execute another calculation
    next_calculation = input("Let's do next calculation?(Yes/No): ")
    
    # Breaking the while loop if the answer is "no"
    if next_calculation == "no":
        print ("Thank You for using the calculator " + name + "!")
        break

    # Redirecting back to the while loop
    else:
        choice