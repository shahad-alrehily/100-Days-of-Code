# Predefined users with passwords and greetings
users = {
    "shahad": {"password": "1234", "greeting": "Welcome back, Shahad! Hope you’re having a productive coding day!"},
    "ahmad": {"password": "abcd", "greeting": "Hey Ahmad! Ready for another Python challenge?"},
    "noura": {"password": "xyz9", "greeting": "Good to see you, Noura! Let's keep learning!"},
}

# Ask for login credentials
username = input("Enter your username: ").lower()
password = input("Enter your password: ")

# Check if user exists and password is correct
if username in users and users[username]["password"] == password:
    print(users[username]["greeting"])
else:
    print("Access denied. Please check your username and password.")
