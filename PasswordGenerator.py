import random

name = input("Enter your Name: ")

print("          Welcome "  +  name + "!")
print('This is your Random Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_.'

number = input("How many passwords do you want to generate " + name + "? ")
number = int(number)

length = input('Input your desired password length: ')
length = int(length)

print("\n Here are your random passwords " + name + "! ")

for p in range(number):
    passwords = ''
    for c in range(length):
    #getting random characters from the 'chars' string
        passwords += random.choice(chars)
    print(passwords)