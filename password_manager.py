from cryptography.fernet import Fernet

'''def write_key():                                 # This will generate an encryption key, use only once and then
    key = Fernet.generate_key()                     # comment out.
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''                                      #comment out up until here after key generation

def load_key():                                     #function to load our encryption key
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()                                    #call the load key function
fer = Fernet(key)

def view():                                         #function to read the txt file and split the inputs as user and password
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("User:", user, ", Password:", fer.dectypt(passw.encode()).decode())
        
def add():                                          # function to add to the txt file
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode + "\n")



while True:                                         #loop to input the username and passwords
    mode = input("Would you like to add a new password or view existing ones? (view, add), press 'q' to quit? " ).lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

