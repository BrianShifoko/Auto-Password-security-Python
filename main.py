# Kibo FPWP Final Project
#welcoming note and name input
print("\n" "Welcome to BlogVot Password Security Center Creater")

print("\n------------------------------------------")

name = input("\n" "What is your name kindly or your Company name ?")

print("\n"
      "welcome! ", name, " to Free BlogVot Password Security center Creater")
# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = int(
    input("\n"
          "Input length of password characters to generate for you?"))

# generate a password string
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

# generate password meeting constraints
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd)
            and sum(char in digits for char in pwd) >= 2):
        print("\n" "Your Password generated is: ", pwd)
        print("\n" "Do you want to use this password ?")
        ans = input(str("yes or no? "))
        yes = "string"
        no = "string"
        if ans == "yes":
            print("\n" "Welcome again! Your Security is our pride \U0001F609")
            break  #break the password generation if user is satisfied
        elif ans == "no":
            print("\n" "*********** Your New password is*********")
        continue  #continue to generate passwords for the user
print("\n" "***************************************")
