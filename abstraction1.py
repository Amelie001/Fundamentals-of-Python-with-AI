# Cloud Storage System 

from abc import ABC, abstractmethod 

class CloudStorage(ABC): 

    def __init__(self, username): 
        self.username = username 

    @abstractmethod
    def upload_file(self, filename): 
        pass

    @abstractmethod 
    def download_file(self, filename): 
        pass 

    def show_user(self): 
        print("User:", self.username)

class GoogleDrive(CloudStorage): 

    def upload_file(self, filename): 
        print(filename, "uploaded to Google Drive.")

    def download_file(self, filename): 
        print(filename, "downloaded from Google Drive.")

class Dropbox(CloudStorage): 

    def upload_file(self, filename): 
        print(filename, "uploaded to Dropbox.")

    def download_file(self, filename): 
        print(filename, "downloaded from Dropbox.")

class OneDrive(CloudStorage):

    def upload_file(self, filename): 
        print(filename, "uploaded to OneDrive.")

    def download_file(self, filename): 
        print(filename, "downloaded from OneDrive.")

# Main Program 

username = input("Enter username: ")

print("\n1. Google Drive")
print("2. Dropbox")
print("3. OneDrive")

choice = input("Choose storage: ")

if choice == "1": 
    storage = GoogleDrive(username)

elif choice == "2": 
    storage = Dropbox(username)

elif choice == "3": 
    storage = OneDrive(username)

else: 
    print("Invalid choice!")
    exit()

storage.show_user()

filename = input("Enter filename: ")

storage.upload_file(filename)
storage.download_file(filename)