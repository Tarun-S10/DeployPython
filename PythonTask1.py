users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def add_user(new_id, name, email):
    if get_user(new_id):
        print("User ID already exists.")
        return
    users.append({"id": new_id, "name": name, "email": email})
    print("User added.")


def update_user(user_id, name=None, email=None):
    user = get_user(user_id)
    if user:
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        print("User updated.")
    else:
        print("User not found.")

def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    print("User deleted if existed.")

add_user(3, "Charlie", "charlie@example.com")
print(get_user(3))
update_user(3, name="Charles")
delete_user(1)
print(users)
