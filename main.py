#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))

length = int(input("How long should the password be? [8 - 24 characters]\n"))

if length >= 8 and length <= 24:
  #Eazy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  nr_letters = round(length * 0.60) #60% of the password length should be letters for better security
  nr_symbols = random.randint(2, (length - nr_letters)) - 1 #so that there is at least 1 symbol and 1 number
  nr_numbers = length - (nr_letters + nr_symbols)
  easy_password = ''
  for letter in range(0, nr_letters):
    easy_password += random.choice(letters)
  for symbol in range(0, nr_symbols):
    easy_password += random.choice(symbols)
  for num in range(0, nr_numbers):
    easy_password += random.choice(numbers)  
  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  passlist = list(easy_password)
  random.shuffle(passlist)
  hard_password = ''.join(passlist)
  
  print(f"Your password is: {hard_password}")
else:
  print("Invalid input, please enter a number between 8 and 24.")
