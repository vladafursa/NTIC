def readFromFile(): #reading data from file
    users = {}
    try:
        with open("file.txt") as file:
            count = 0
            for line in file:
                if count == 0:
                    user = line.rstrip()
                if count == 1:
                    password = line.rstrip()
                    users[user] = {'password': password, 'personalInfo': {}}
                if 1<count<=7:
                    line = line.rstrip()
                    key, value = line.split(': ')
                    users[user]['personalInfo'].update({key: value})
                count = count+1
                if count == 8:
                    count = 0
    except FileNotFoundError:
        print("sorry, file doesn't exist, new file was added")
        file = open("file.txt", "x")
        file.close()
    return users

def deleteFile():#clears the file
    file = open("file.txt", "w")
    file.flush()
    file.close()

def writeToFile(data):#writing to file
    try:
        file = open("file.txt", "a")
        file.writelines(data)
        file.close()
    except:
        print("you cannot write to file")

def loadDictionary(): #transfer dictionary into file
    for i in range(len(listOfNames)):
        writeToFile(listOfNames[i] + "\n")
        writeToFile(users[listOfNames[i]]['password'] + "\n")
        for k in range(len(listOfDetails)):
            writeToFile(listOfDetails[k] + ": " + users[listOfNames[i]]['personalInfo'][listOfDetails[k]]+ "\n")

def listOfNames():  #list of usernames
    listOfNames = []
    with open("file.txt") as file:
        count = 0
        for line in file:
            if count == 0:
                listOfNames.append(line.rstrip())
            count = count+1
            if count == 8:
                count = 0
    return listOfNames

def printInfo(listOfNames):  #readable way of showing usernames
    for i in range(len(listOfNames)):
        print(listOfNames[i])

def findUser(): #acces to user details
    loop = True
    while loop == True:
        urname = input("Enter the name: ")
        if urname in users:
            loop1 = True
            while loop1 == True:
                urpassword = input("enter password: ")
                if urpassword == users[urname]['password']:
                    print("Personal information of this user: ", users[urname]['personalInfo'])
                    loop1 = False
                else:
                    print("wrong password")
            loop = False
        else:
            print("there is no such user")
    return urname

def appropiatePassword():   #checking if password is with rules
    loop = True
    while loop == True:
        password = input("enter new password: ")
        if len(password)>=11:
            count = 0
            for i in range(len(password)):
                if password[i].isdigit():
                    count = count + 1
            if count>=3:
                count = 0
                for i in range(len(password)):
                    if password[i].isalpha():
                        count = count + 1
                if count >= 2:
                    count = 0
                    for i in range(len(password)):
                        if password[i].isupper():
                            count = count + 1
                    if count >= 1:
                        loop = False
                    else:
                        print("Should be at least 1 upper-case!")
                else:
                    print("Should be at least 2 symbols!")
            else:
                print("Should be at least 3 numbers!")
        else:
            print("should be at least 11 characters!")
    return password

def addNewUser(): #adding new user
    newUser = input("enter new user: ")
    if newUser in users:
        print("there is this name")
    else:
        listOfNames.append(newUser)
        newPassword = appropiatePassword()
        users[newUser] = {'password': newPassword, 'personalInfo': {}}
        newDetails = []
        for i in range(len(listOfDetails)):
            newDetails.append(input("enter the " + listOfDetails[i] + " of new user: "))
            users[newUser]['personalInfo'].update({listOfDetails[i]: newDetails[i]})
        printInfo(listOfNames)

def changeInfo(): #changing info
    urname = findUser()
    loop = True
    while loop == True:
        count = 0
        choice = input("what do you want to change? ").lower()
        for i in range(len(listOfDetails)):
            if choice == listOfDetails[i]:
                users[urname]['personalInfo'][listOfDetails[i]] = input("enter the " + listOfDetails[i] + " of new user: ")
            else:
                count = count + 1
        if count == len(listOfDetails):
            print("you didn't type the appropriate choice")
        else:
            loop = False
    print(users[urname]['personalInfo'])

def changePassword(): #changing password
    urname = findUser()
    newestpassword = appropiatePassword()
    if newestpassword == users[urname]['password']:
        print("new password is the same as old")
    else:
        users[urname]['password'] = newestpassword
        print("new password is ", users[urname]['password'])

def delete(): #deletes a user
    print("Print the name that you want to delete: ")
    urname = findUser()
    users.pop(urname)
    listOfNames.remove(urname)
    print("Now there are", listOfNames)

def updates(): #cleares file and writes new stuff
    deleteFile()
    loadDictionary()

def menu(): #menu to choose what to do
    loop = True
    while loop == True:
        print("1 - access personal information, 2 - create new account, 3 - change info, 4 - change password ,5 - delete account, 6 - show all users , 7 - stop")
        choice = input("what is your choice? ")
        if choice == "1":
            findUser()
        elif choice == "2":
            addNewUser()
            updates()
        elif choice == "3":
            changeInfo()
            updates()
        elif choice == "4":
            changePassword()
            updates()
        elif choice == "5":
            delete()
            updates()
        elif choice == "6":
            printInfo(listOfNames)
        elif choice == "7":
            loop = False
        else:
            print("Your choice was wrong")

#main
users = readFromFile()
listOfNames = listOfNames()
listOfDetails = ['name', 'age', 'address', 'phone_number', 'nationality', 'email_address']
if users == {}:#checking is there is the file is empty
    print("the file was empty, so new account will be added")
    listOfNames = []
    deleteFile()
    addNewUser()
    updates()
print(listOfNames)
menu()

