# Notification System 

from abc import ABC, abstractmethod

class Notification(ABC): 

    def __init__(self, message): 
        self.message = message 

    @abstractmethod 
    def send(self): 
        pass 

    def show_message(self): 
        print("Message:", self.message)

class EmailNotification(Notification): 

    def send(self): 
        print("Sending Email...")
        print("Email sent successfully!")

class SMSNotification(Notification): 

    def send(self): 
        print("Sending SMS...")
        print("SMS sent successfully!")

class PushNotification(Notification): 

    def send(self): 
        print("Sending Push Notification...")
        print("Push Notification sent successfully!")

message = input("Enter notification message: ")

print("\n1. Email")
print("2. SMS")
print("3. Push Notification")

choice = input("Choose notification type: ")

if choice == "1": 
    notification = EmailNotification(message)

elif choice == "2": 
    notification = SMSNotification(message)

elif choice == "3": 
    notification = PushNotification(message)

else: 
    print("Invalid choice!")
    exit()

notification.show_message()
notification.send()