#!/usr/bin/python3

#------------------------------------------------------------
# write a python code that handle the following login system.
#------------------------------------------------------------
users = {
    "ahmed": "1394",
    "ali": "6078",
    "amr": "9345",
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Welcome, " + username)
    else:
        print("Incorrect entry")

if __name__ == "__main__":
    login()