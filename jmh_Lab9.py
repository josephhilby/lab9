def encode(password):
    encoded_password = ""
    for digit in password:
        n = int(digit) + 3
        n = n%10
        encoded_password += str(n)
    return encoded_password


def main():
    print(encode("00009962"))


if __name__ == "__main__":
    main()
