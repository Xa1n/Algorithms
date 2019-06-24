result = ""
message = ""
choice = ""

while choice != '-1':
    choice = input("\nDo you want to encrypt or decrypt a message?\nEnter 1 to Encrpyt, 2 to Decrypt, -1 to Exit: ")

if choice == '1':
    message = input("\nEnter the message you want to encrypt: ")

    for i in range(0, len(message)):
        result = result + chr(ord(message[i]) - 2)

    print (result + "\n\n")
    result = ""

    