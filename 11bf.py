accounts = {
    'ahems33': 88390,
    'dd3002': 39923,
    'hehe333': 34322,
    'ms33': 64340,
    'dd3vdc2': 54923,
    'hevd43' : 34535,
    'aadfe3': 54655,
    'ndsfv': 59033,
    'dfdw4': 90343,
    'sid333': 73903

}

username = input("enter the username: ")
password = int(input("enter the password: "))

if username in accounts:
        if accounts[username] == password:
             print("the username and password is matched successfullly!")
else:
    print("Sorry!, username and password not matched")
