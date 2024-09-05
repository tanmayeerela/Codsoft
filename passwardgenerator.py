import random
import string
def password_generator():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated Password: {password}")

password_generator()
