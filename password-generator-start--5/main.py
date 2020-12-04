#password_1 Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword_1 Generator!")
nr_letters= int(input("How many letters would you like in your password_1?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_1 =""

for char in range(1,nr_letters + 1):
  password_1 += random.choice(letters)

for char in range(1,nr_symbols + 1):
  password_1 += random.choice(symbols)

for char in range(1,nr_numbers + 1):
  password_1 += random.choice(numbers)
print(password_1) 

#print(''.join(random.sample(password_1,len(password_1))))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_1 =[]

for char in range(1,nr_letters + 1):
  password_1 += random.choice(letters)

for char in range(1,nr_symbols + 1):
  password_1 += random.choice(symbols)

for char in range(1,nr_numbers + 1):
  password_1 += random.choice(numbers)
# print(password_1) 


random.shuffle(password_1)
PASSWORD = ""
for char in password_1:
  PASSWORD += char

print(f"Your Password is {PASSWORD}")



# Another method

import random, string
password_1_length = int(input("Length???"))

characters = string.ascii_letters + string.digits + string.punctuation

password_1 = []

for x in range(password_1_length):
  password_1.append(random.choice(characters))
print(''.join(password_1))
