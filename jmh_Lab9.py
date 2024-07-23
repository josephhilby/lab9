def encode(password):
    encoded_password = ""
    for digit in password:
        n = int(digit) + 3
        n = n % 10
        encoded_password += str(n)
    return encoded_password


def decode(password):
    # trying again
    decoded_password = ""
    for digit in password:
        n = int(digit) - 3
        n = n % 10
        decoded_password += str(n)
    return decoded_password


def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")


def main():
    logged_in = True
    current_password = None

    while logged_in:
        display_menu()
        user_input = input("Please enter an option: ")

        match user_input:
            case "1":
                user_input = input("Please enter the password to encode: ")
                current_password = encode(user_input)
                if current_password:
                    print("Your password has been encoded and stored!")
                else:
                    print("Your password was not stored!")
            case "2":
                if current_password:
                    decoded_password = decode(current_password)
                    print(f"The encoded password is {current_password}, and the original password is {decoded_password}")
                else:
                    print("No password to decode!")
            case "3":
                logged_in = False
        print("")


if __name__ == "__main__":
    main()
