# Social Media Account 

class SocialMediaAccount: 
    def __init__(self, username, password): 
        # Public 
        self.username = username 
        # Protected 
        self._followers = 0 
        # Private 
        self.__password = password 

    # Login 
    def login(self, password): 
        if password == self.__password: 
            print("Login successful.")
        else: 
            print("Incorrect password.")

    # Change password 
    def change_password(self, old_password, new_password): 
        if old_password != self.__password: 
            print("Incorrect old password.")
            return
        if len(new_password) < 8: 
            print("Password must contain at least 8 characters.")
            return 

        self.__password = new_password 
        print("Password changed successfully.")

    # Follow someone 
    def follow(self): 
        self._followers += 1 
        print("New follower added.")

    # Unfollow 
    def unfollow(self): 
        if self._followers > 0: 
            self._followers -= 1
            print("Follower removed.")
        else: 
            print("No followers to remove.")

    # Get followers 
    def get_followers(self): 
        return self._followers

account = SocialMediaAccount("rahul123", "password123")

account.login("password123")

account.follow()
account.follow()
account.follow()

print("Followers:", account.get_followers())

account.unfollow()

print("Followers:", account.get_followers())

account.change_password("password123", "newpassword123")

account.login("newpassword123")