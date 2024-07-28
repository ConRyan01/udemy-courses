#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
password_length = nr_letters+nr_symbols+nr_numbers
remaining_chars = password_length

#Attempting to do without list methods except for append obviously

while remaining_chars > 0:
    
  index = random.randint(0,2)

  if index == 0:
    if nr_letters > 0:
      password.append(letters[random.randint(0,len(letters)-1)])
      nr_letters -= 1
    elif nr_letters == 0 and nr_numbers > 0:
      password.append(numbers[random.randint(0,len(numbers)-1)])
      nr_numbers -= 1
    else:
      password.append(symbols[random.randint(0,len(symbols)-1)])
      nr_symbols -= 1

  if index == 1:
    if nr_numbers > 0:
      password.append(numbers[random.randint(0,len(numbers)-1)])
      nr_numbers -= 1
    elif nr_numbers == 0 and nr_symbols > 0:
      password.append(symbols[random.randint(0,len(symbols)-1)])
      nr_symbols -= 1
    else:
      password.append(letters[random.randint(0,len(letters)-1)])
      nr_letters -= 1

  if index == 2:
    if nr_symbols > 0:
      password.append(symbols[random.randint(0,len(symbols)-1)])
      nr_symbols -= 1
    elif nr_symbols == 0 and nr_letters > 0:
      password.append(letters[random.randint(0,len(letters)-1)])
      nr_letters -= 1
    else:
      password.append(numbers[random.randint(0,len(numbers)-1)])
      nr_numbers -= 1

  remaining_chars -= 1

full_pass = ''.join(password)
print(f'Your Password is: {full_pass}')

#Would i have used list methods, shuffle would have made this much cleaner and easier

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

