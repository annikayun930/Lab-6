#Annika Yun


# Encode 1
def encoder(password):
    encoded = password
    encoded_list = [int(i) for i in str(encoded)]
    encode_dict = {"0": "3", "1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "0", "8": "1", "9": "2"}
    encode = ""
    for i in (encoded_list):
        encode = encode + encode_dict[str(i)]

    encode = int(encode)
    print("Your password has been encoded and stored!")

    return encode




# Decode 2
"""def decoder(secret):
    password = secret
    password_list = [int(i) for i in str(password)]
    password_dict = {"3": "0", "4": "1", "5": "2", "6": "3", "7": "4", "8": "5", "9": "6", "0": "7", "1": "8", "2": "9"}
    passed = ""
    for i in (password_list):
        passed = passed + password_dict[str(i)]

    passed = int(passed)

    return passed"""

#wendy vallejos
def  decode(secret):
    epass = ""
    password_list = [int(x) for x in str(secret)]
    dict = {"3": "0", "4": "1", "5": "2", "6": "3", "7": "4", "8": "5", "9": "6", "0": "7", "1": "8", "2": "9"}
    for x in password_list:
        epass = epass + dict[str(x)]
    epass = int(epass)

    return epass

# Main Menu
def main():
    while True:
        menu = ["Menu", "-------------", "1. Encode", "2. Decode","3. Quit", " "] #menu

        for i in menu:
            print(i)

        num = int(input("Please enter an option: "))


        if num == 1:
            password = int(input("Please enter your password to encode: "))
            secret = encoder(password)  # working 1


        elif num == 2:
            revealed = decode(secret)
            print(f'The encoded password is {secret} and the original password is {revealed}.')


        elif num == 3:
            break

if __name__ == "__main__":
    main()
