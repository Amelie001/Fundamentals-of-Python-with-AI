# Password Manager

class PasswordManager:

    def __init__(self, master_password):
        self.__master_password = master_password
        self.__passwords = {}

    # Check master password
    def authenticate(self, master_password):
        return master_password == self.__master_password

    # Add a website password
    def add_password(self, website, password):
        self.__passwords[website] = password
        print("Password saved for", website)

    # Retrieve a saved password
    def get_password(self, website, master_password):
        if self.authenticate(master_password):
            if website in self.__passwords:
                return self.__passwords[website]
            else:
                return "Website not found."
        else:
            return "Incorrect master password."

    # Delete a saved password
    def delete_password(self, website, master_password):
        if self.authenticate(master_password):
            if website in self.__passwords:
                del self.__passwords[website]
                print("Password deleted for", website)
            else:
                print("Website not found.")
        else:
            print("Incorrect master password.")

    # Change master password
    def change_master_password(self, old_password, new_password):
        if old_password == self.__master_password:
            self.__master_password = new_password
            print("Master password changed successfully.")
        else:
            print("Incorrect master password.")


# Create password manager
manager = PasswordManager("hello123")

manager.add_password("Netflix", "netflix123")
manager.add_password("Google", "google456")

print(manager.get_password("Netflix", "hello123"))

manager.delete_password("Google", "hello123")

manager.change_master_password("hello123", "newpass123")

print(manager.get_password("Netflix", "newpass123"))