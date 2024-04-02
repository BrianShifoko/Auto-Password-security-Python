# Kibo FPWP Final Project
#welcoming note and name input

import secrets
import string

def generate_password(length, min_digits=2, require_special=True):
    """Generate a password meeting specified constraints."""
    # Define character sets for password generation
    alphabet = string.ascii_letters + string.digits + string.punctuation if require_special else string.ascii_letters + string.digits
    
    # Initialize list to store password characters
    password_characters = []
    
    # Add required minimum digits to the password
    for _ in range(min_digits):
        password_characters.append(secrets.choice(string.digits))
    
    # Fill the remaining characters with a mix of letters and special characters
    for _ in range(length - min_digits):
        password_characters.append(secrets.choice(alphabet))
    
    # Shuffle the characters to provide a more randomized but structured arrangement
    secrets.SystemRandom().shuffle(password_characters)
    
    # Concatenate the characters to form the password
    return ''.join(password_characters)

def get_integer_input(prompt, error_message="Please enter a valid integer."):
    """Prompt the user for an integer input."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(error_message)

def get_yes_no_input(prompt):
    """Prompt the user for a yes or no input."""
    while True:
        response = input(prompt).lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    print("\nWelcome to BlogVot Password Security Center Creator")
    print("------------------------------------------")
    name = input("\nWhat is your name or your Company name? ")
    print("\nWelcome, {}! to Free BlogVot Password Security Center Creator".format(name))
    
    while True:
        pwd_length = get_integer_input("\nEnter the length of the password you want to generate: ")

        print("\nGenerating password...")
        password = generate_password(pwd_length)

        print("\nYour generated password is:", password)
        if get_yes_no_input("\nDo you want to use this password? (yes/no): "):
            print("\nWelcome again! Your Security is our pride \U0001F609")
            break
        else:
            print("\n*********** Let's generate a new password *********")

if __name__ == "__main__":
    main()
