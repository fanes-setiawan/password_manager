import mysql.connector
from getpass import getpass
import hashlib


# Database setup
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="password_manager"
)
cursor = conn.cursor()

def register():
    name = input("Name: ")
    email = input("Email: ")
    username = input("Username: ")
    password = hash_password(getpass("Password: "))

    cursor.execute("INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)", (name, email, username, password))
    conn.commit()
    print("User registered successfully!")

def login():
    username = input("Username: ")
    password = getpass("Password: ")

    cursor.execute("SELECT id, password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user and check_password(password, user[1]):
        print("Logged in successfully!")
        return user[0]
    else:
        print("Invalid username or password.")
        return None

def add_account(user_id):
    name = input("Account Name: ")
    username = input("Account Username: ")
    password = getpass("Account Password: ")

    cursor.execute("INSERT INTO accounts (name, username, password, user_id) VALUES (%s, %s, %s, %s)", (name, username, password, user_id))
    conn.commit()
    print("Account added successfully!")

def update_account(user_id):
    account_id = int(input("Enter the ID of the account you want to update: "))
    cursor.execute("SELECT id FROM accounts WHERE user_id = %s", (user_id,))
    accounts = cursor.fetchall()
    if (account_id,) in accounts:
        name = input("New Account Name: ")
        username = input("New Account Username: ")
        password = getpass("New Account Password: ")

        cursor.execute("UPDATE accounts SET name = %s, username = %s, password = %s WHERE id = %s", (name, username, password, account_id))
        conn.commit()
        print("Account updated successfully!")
    else:
        print("Invalid account ID.")

def delete_account(user_id):
    account_id = int(input("Enter the ID of the account you want to delete: "))
    cursor.execute("SELECT id FROM accounts WHERE user_id = %s", (user_id,))
    accounts = cursor.fetchall()
    if (account_id,) in accounts:
        cursor.execute("DELETE FROM accounts WHERE id = %s", (account_id,))
        conn.commit()
        print("Account deleted successfully!")
    else:
        print("Invalid account ID.")
        
def display_accounts():
    cursor.execute("SELECT name, username, password, id FROM accounts")
    accounts = cursor.fetchall()
    for account in accounts:
        print("===============================================================================")
        print("Name     : ", account[0])
        print("Username : ", account[1])
        print("Password : ", account[2])
        print("ID       : ", account[3])
        print("===============================================================================")
        print("\n")
        
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, hashed_password):
    return hash_password(password) == hashed_password

# Main function
def main():
    while True:
        choice = input("1. Register\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                while True:
                    choice = input("1. Add Account\n2. Update Account\n3. Delete Account\n4. display_accounts \n5. Logout\nEnter your choice: ")
                    if choice == "1":
                        add_account(user_id)
                    elif choice == "2":
                        update_account(user_id)
                    elif choice == "3":
                        delete_account(user_id)
                    elif choice == "4":
                        display_accounts()
                    elif choice == "5":
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

