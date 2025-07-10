                             #Random Password Generator

import random
import string


# ask user for length and preference
length = int (input("enter password length:"))
use_upper= input("Include uppercase letters(y/n):").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

#
char_pool = ''
if use_upper:
    char_pool += string.ascii_uppercase
if use_lower:
    char_pool += string.ascii_lowercase
if use_digits:
    char_pool += string.digits
if use_symbols:
    char_pool += string.punctuation

if not char_pool:
    print("⚠️ You must select at least one character type. Exiting...")
else:
    while True:
        # ✅ Generate password using the already created char_pool
        password = ''.join(random.choice(char_pool) for _ in range(length))
        print(f"\n🔐 Generated Password: {password}")

        # Ask user if they want another password
        again = input("\nDo you want another password? (y/n): ").lower()
        if again != 'y':
            print("👋 Thank you for using the Password Generator!")
            break

