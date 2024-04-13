import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

let = int(input("Enter the number of letters:"))
cha = int(input("Enter the number of chars:"))
digi = int(input("Enter the number of digi:"))

# password = ''

# for char in range(1, let + 1):
#     password += random.choice(letters)

# for char in range(1, cha + 1):
#     password += random.choice(chars)
    
# for char in range(1, digi + 1):
#     password += random.choice(digits)
    
# print(password)

password_list = []

for char in range(1, let + 1):
    password_list += random.choice(letters)
    
for char in range(1, cha + 1):
    password_list += random.choice(chars)

for char in range(1, digi + 1):
    password_list += random.choice(digits)
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char
    
print(f" This is your final password: {password}")
