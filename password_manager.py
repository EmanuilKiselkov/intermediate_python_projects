from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''



def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            decrypted_password = fer.decrypt(passw.encode()).decode()
            print("User:", user, ", Password:", decrypted_password)

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        encrypted_password = fer.encrypt(password.encode()).decode()
        f.write(name + " | " + encrypted_password + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":

        view()
    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue