import hashlib

users = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("Username already exists.")
        return
    users[username] = hash_password(password)
    print("Created new user")

def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login Successful")
    else:
        print("Invalid credentials")

register("john", "mypassword")     
login("john", "mypassword")        
login("john", "wrongpassword")     
