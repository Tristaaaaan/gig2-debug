import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example: Generate a password of length 10
with open('password_storage.txt','w') as pwd_storage:
    password = generate_password(10)
    pwd_storage.write(f'{password},0')
