#programme that counts calories per minute
def getNumber():   #input currect number and positive
    loop = True
    while (loop == True):
        number = input()
        if (number.isdigit()==False) or (int(number)<0):
            print("You didn't type in right(it should be numbers and positive)")
        else:
            number = int(number)
            loop = False
    return number

def getMeasurement():  #input only kg or pounds
    loop = True
    while(loop == True):
        measurement = (input("Which measurement are you using?( Kg or Pounds) ")).lower()
        if (measurement != "kg") and (measurement != "pounds"):
            print("You didn't type in measurement")
        else:
            loop = False
    return measurement

def weightKg(measurement,weight):  #converts pounds into kg
    if measurement == "pounds":
        weight = weight * 0.453592
        print("weight in kilos: ", weight)
    return weight

def exercise(): #choose exercise
    list = [["callithenics", [["light effort", 4.5], ["vigorous effort", 8.0]], "Upper body stretch"], ["bicycling", [["<10mph", 4], ["10-11.9mph", 6], ["12-13.9mph", 8], ["14-15.9mph", 10], ["16-19mph", 12], [">20mph", 16]], "Just a simple 10 minutes warm down either on the rollers, turbo or simply up and down the road just spinning your legs with very little resistance is all you need to do"], ["cycling", [["50 watts", 3], ["100 watts", 5.5], ["150 watts", 7], ["200 watts", 10.5], ["250 watts", 12.5]], "4 or 5 minutes of easy pedalling after your ride"], ["dancing", [["low impact aerobic", 6], ["high impact aerobic", 7]], "Soaking in a warm bath will relax you after practice"]]
    loop = True
    while loop == True:
        choice = (input("There are callithenics, bicycling, cycling and dancing. Your choice is: ")).lower()
        count = 0 #for correct input
        for i in range(len(list)):
            if choice == list[i][0]:
                for k in range(len(list[i][1])):#prints types of this exercise
                    print(k, "-", list[i][1][k][0])
                loop1 = True #for correct input
                while loop1 == True:
                    print("type of exercise: ")
                    choice = getNumber()
                    count1 = 0
                    for k in range(len(list[i][1])):
                        if choice == k:
                            newList = [list[i][0], list[i][1][k], list[i][2]] #creates a list with exercise, it's type, MET and calming down
                            print("to calm down: ", list[i][2])
                        else:
                            count1 = count1 + 1
                    if count1 == len(list[i][1]):
                        print("you didn't choose the type of exercise")
                    else:
                        loop1 = False
                        loop = False
            else:
                count = count+1
        if count == len(list):
            print("you didn't choose the exercise")
    return newList

def NumberOfCaloriesPerMinute(MET, weight): #calculates the number of calories per minute
    NumberOfCaloriesPerMinute = 0.0175*int(MET)*weight
    return NumberOfCaloriesPerMinute

def NumberOfCalories(weight): #calculates the number of calories or workout
    NumberOfCalories = 0
    forStoring = [] #will be used for storing data if it is better workout
    print("It is workout time")
    loop = True
    while loop == True:
        choice = (input("Do you want to add exercise?yes/no - ")).lower()
        if choice == "yes":
            description = exercise()
            MET = int(description[1][1])
            print("Type in duration: ")
            duration = getNumber()
            forStoring.append("exercise: "+ description[0] + ", " + "type: " + description[1][0]+ ", " + "duration: " + str(duration) + ", " + "calming down: " + description[2] + "; ")
            NumberOfCalories += 0.0175 * int(MET) * weight * duration
        elif choice == "no":
            print("thanks")
            loop = False
        else:
            print("you didn't type in accurate choice!")
    forStoring.insert(0, str(NumberOfCalories)) #for convinience
    return forStoring

def readFromFile():#gets a calorie amount from file
    try:      #checking if file exists, if not - creating a new one
        file = open("workout.txt", "r")
        data = file.readline()
        return(data)
        file.close()
    except FileNotFoundError:
        print("sorry, file doesn't exist, new file was added")
        file = open("workout.txt", "x")
        data = file.readline()
        return (data)
        file.close()

def delete():#clears the file
    file = open("workout.txt", "w")
    file.flush()
    file.close()

def writeToFile(workout1):#writing to file
    try:
        file = open("workout.txt", "a")
        file.writelines(workout1)
        file.close()
    except:
        print("you cannot write to file")

def compaire(): #compairs previous workout with a new one and decides whether to store new or not
    try:     #if file is empty the comparible item will be 0
        workout2 = float(readFromFile())
    except ValueError:
        print("you didn't have any workouts before")
        workout2 = 0
    if NumberOfCalories > workout2:
        delete()
        writeToFile(listForStoring[0]+"\n")
        listForStoring.pop(0)
        writeToFile(listForStoring)
        print("Well done!")
    elif NumberOfCalories == workout2:
        print("try a little bit harder")
    else:
        print("There were better workouts")

#main
measurement = getMeasurement()
print("Type in weight: ")
weight = getNumber()
weight = weightKg(measurement, weight)
description = exercise()
MET = description[1][1]
NumberOfCaloriesPerMinute(MET, weight)
print(NumberOfCaloriesPerMinute(MET, weight), "calories/minute")
listForStoring = NumberOfCalories(weight)
NumberOfCalories = float(listForStoring[0])
print(NumberOfCalories, "calories")
compaire()
