import password_generator as pg

def main():
    print()
    
    while True:
        try:
            min_length = int(input("Enter the minimum length of the password: ").strip())
            break
        except ValueError as e:
            print("Invalid input. You must enter a number.", end="\n\n")
            continue

    digits = input("Do you want digits in the password (y/n)?: ").strip().lower() == "y"
    special = input("Do you want special characters in the password (y/n)?: ").strip().lower() == "y"
    unique = input("Do you duplicate characters in the password (y/n)?: ").strip().lower() != "y"
    save = input("Do you want to save the password in a password.txt file (y/n)?: ").strip().lower() == "y"

    print("Your generated password is:",pg.generate_password(min_length,digits,special,unique,save))


if __name__ == "__main__":
    main()
