#Password generator

import random
import string
 
def generate_password(length):
    # Defining the characters that can be used in the password (these)
    all_characters = string.ascii_letters + string.digits + string.punctuation
 
    # Ensuring that the password is at least 1 character long
    if length < 1:
        return "Password length must be at least 1."
 
    #Generate a random password of the specified length
    #randomchoice picks a random character from all_characters  string defined above
    #for loop runs till the input length
    #the --''.join-- joins each element iterated
    password = ''.join(random.choice(all_characters) for _ in range(length))
 
    return password
 
def pwdgeneration():
    # Prompt the user to enter the desired password length
    try:
        length = int(input("Enter the desired length of the password: "))
 
        # Generate the password
        password = generate_password(length)
 
        # Display the generated password
        print("Generated password for you:", password)
 
    except ValueError:
        print("Invalid input. Please enter a valid number")
 

pwdgeneration()
