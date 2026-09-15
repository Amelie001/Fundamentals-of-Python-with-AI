# Cybersecurity Scan 

class SecurityTool: 

    def __init__(self, system_name): 
        self.system_name = system_name

    def system_info(self): 
        print("\nSystem:", self.system_name)

class PasswordScanner(SecurityTool): 

    def check_password(self, password): 
        score = 0

        if len(password) >= 8: 
            score += 1
        if any(char.isupper() for char in password): 
            score += 1 
        if any(char.isdigit() for char in password): 
            score += 1
        if any(not char.isalnum() for char in password): 
            score += 1 
        if score == 4: 
            print("Password strength: STRONG")
        elif score >= 2: 
            print("Password strength: MEDIUM")
        else: 
            print("Password strength: WEAK")

class FileScanner(SecurityTool): 

    def scan_file(self, filename): 
        suspicious_extensions = [".exe", ".bat", ".cmd", ".scr"]
        suspicious = False

        for extension in suspicious_extensions: 
            if filename.lower().endswith(extension): 
                suspicious = True 

        if suspicious: 
            print("Warning: File requires additional verification.")

        else: 
            print("No suspicious extension detected.")

class SecuritySuite(PasswordScanner, FileScanner): 

    def security_report(self): 
        print("\n===== SECURITY REPORT =====")
        print("System:", self.system_name)
        print("Password scanner: Active")
        print("File scanner: Active")
        print("Security suite ready.")

system = input("Enter computer name: ")

security = SecuritySuite(system)

while True: 

    print("\n===== SECURITY SUITE =====")
    print("1. Check password strength")
    print("2. Scan filename")
    print("3. Security report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1": 

        password = input("Enter password: ")
        security.check_password(password)

    elif choice == "2": 

        filename = input("Enter filename: ")
        security.scan_file(filename)

    elif choice == "3": 

        security.security_report()

    elif choice == "4": 
        print("Security scanner closed.")
        break

    else: 
        print("Invalid choice!")