import random
import string
import hashlib
import json

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def store_password(self, account, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[account] = hashed_password
        self._save_passwords()

    def get_password(self, account):
        if account in self.passwords:
            return self.passwords[account]
        else:
            return None

    def _save_passwords(self):
        with open('passwords.json', 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def load_passwords(self):
        try:
            with open('passwords.json', 'r') as file:
                self.passwords = json.load(file)
        except FileNotFoundError:
            self.passwords = {}

if __name__ == "__main__":
    manager = PasswordManager()
    manager.load_passwords()

    while True:
        print("\n1. Generate Password")
        print("2. Store Password")
        print("3. Retrieve Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter password length: "))
            password = manager.generate_password(length)
            print(f"Generated Password: {password}")

        elif choice == '2':
            account = input("Enter account name: ")
            password = input("Enter password: ")
            manager.store_password(account, password)
            print(f"Password for '{account}' stored.")

        elif choice == '3':
            account = input("Enter account name: ")
            stored_password = manager.get_password(account)
            if stored_password:
                print(f"Password for '{account}': {stored_password}")
            else:
                print(f"No password stored for '{account}'.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
