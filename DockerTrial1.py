#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
difficulty = input("Would you like an easy or a hard password? Please enter 'E' for easy or 'H' for hard.\n")
difficulty = difficulty.lower()
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Select random characters from list based on input
ran_letters = random.choices(letters, k = nr_letters)
ran_symbols = random.choices(symbols, k = nr_symbols)
ran_numbers = random.choices(numbers, k = nr_numbers)
if difficulty == "e":
    #Combine characters into a list
    easy_password = ran_letters + ran_symbols + ran_numbers
    #Convert list into str and print
    easy_password_str = map(str, easy_password)
    result = "".join(easy_password_str)
    print(f"Your easy password is: {result}")
elif difficulty == "h":
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    hard_password_list = ran_letters + ran_symbols + ran_numbers
    hard_password = random.sample(hard_password_list, len(hard_password_list))
    hard_password_str = map(str, hard_password)
    hard_result = "".join(hard_password_str)
    print(f"Your hard password is: {hard_result}")