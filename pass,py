import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password has at least one character from each set
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all sets combined
    all_chars = lowercase + uppercase + digits + special_chars
    password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle the list to avoid predictable sequences
    random.shuffle(password_chars)

    # Join list to form the final password string
    return ''.join(password_chars)

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4, or 0 to quit): "))
            if length == 0:
                print("Exiting password generator.")
                break
            if length < 4:
                print("Password length must be at least 4. Please try again.")
                continue
            password = generate_password(length)
            print(f"Generated password: {password}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()
