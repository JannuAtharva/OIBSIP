import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not any([include_letters,include_numbers,include_symbols]):
        print("Please select at least one type of character.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to your PASSWORD GENERATOR!!")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")


    while True:

        include_letters = input("Do you want to add letters? (y/n): ").lower()== "y"
        include_numbers = input("Do you want to add numbers? (y/n): ").lower()== "y"
        include_symbols = input("Do you want to add symbols? (y/n): ").lower()== "y"

        if not any([include_letters, include_numbers, include_symbols]):
            print("Please select at least one type of character.")
            continue
        else:
            break

    pwd = generate_password(length,include_letters,include_numbers,include_symbols)
    if pwd:
        print("Your generated password is:", pwd)

if __name__ == "__main__":
    main()
    
