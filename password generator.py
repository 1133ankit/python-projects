import string
# string module have lots of functionalities
#print(string.ascii_letters) to print all character in upper and lower case#
#print(string.digits) to print ALL digits
#print(string.punctuation) to print all special character
import random
# creat password function
first = input("Enter your first name:")
last =  input ("Enter your last name:")
mail =  first + last + "@"+ "gmail.com"
print("your mail is",mail)
def get_password(length):
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = ' '
    for char in range(num):
        rand_char = random.choice(all_char)
        password = password + rand_char
        return password
num = int(input("how long you password"))
print(get_password(num))
        
