import sqlite3
import os
import time
from BankAppFunctions import *

# Connect to sqlite3
conn = sqlite3.connect("BankAppDB.db")
cursor = conn.cursor()

# Create bank_users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS bank_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL
)
''')
conn.commit()

# Main loop for user interaction
while True:
    time.sleep(0.5)
    os.system("clear")
    print("Hello User, Welcome to the bank!")
    print("1. Create an Account")
    print("2. Log in")
    print("3. Print DB")
    print("4. Check if account exists")
    print("5. Exit")
    print("6. Delete account")

    choice = input("Select option: ")

    if choice == "1":
        create_account(cursor, conn)
    elif choice == "2":
        check_account(cursor)
    elif choice == "3":
        os.system("clear")
        DBList(cursor)
    elif choice == "4":
        check_account(cursor)
    elif choice == "5":
        print("Exiting the application.")
        break
    elif choice == "6":
        DeleteUser(cursor, conn)
    else:
        print("Invalid option. Please try again.")

# Clean up and close the database connection
conn.close()