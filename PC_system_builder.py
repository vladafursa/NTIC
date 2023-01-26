def niceOutput(components, i): #for more readable output
    print("name: ", components[i][0])
    print("manufacturer: ", components[i][1])
    print("description: ", components[i][2])
    print("price: ", components[i][3])

def getNumber():   #input correct number and positive
    loop = True
    while (loop == True):
        number = input("Your choice is: ")
        if (number.isdigit() == False) or (int(number) < 0):
            print("You didn't type in right(it should be numbers or positive)")
        else:
            number = int(number)
            loop = False
    return number

def change(list, oldBasket, cost):#changing components
    loop = True
    while loop == True:
        choiceChange = input(("Do you want to change something?")).lower()
        if choiceChange == "yes":
            for i in range(len(oldBasket)):
                print(list[i][0], ":")#printing available
                niceOutput(oldBasket, i)
            loop1 = True
            while loop1 == True:
                urChange = input("what do you want to change? ").upper()
                count = len(basket)
                for i in range(len(basket)):
                    if (urChange == list[i][0]):
                        count = count - len(basket)
                        cost = cost - oldBasket[i][3]
                        oldBasket.pop(i)
                        for k in range(len(list[i][1])):
                            print(k, ":")#printing types
                            niceOutput(list[i][1], k)
                        choice = getNumber()
                        for k in range(len(list[i][1])):
                            if choice == k:
                                oldBasket.insert(i, list[i][1][k])
                                cost = cost + list[i][1][k][3]
                if count == 0:
                    loop1 = False
                else:
                    print("you didn't choose")
            loop = False
        elif choiceChange == "no":
            loop = False
        else:
            print("you didn't choose")
    return cost

def components(list, cost):#adding required components
    for i in range(len(list)):
        print("what type of ", list[i][0], " do you want? ")
        for k in range(len(list[i][1])):
            print(k, ":")
            niceOutput(list[i][1], k)
        loop = True
        while loop == True:
            choice = getNumber()
            count = 0
            for k in range(len(list[i][1])):
                if choice == k:
                    basket.append(list[i][1][k])
                    cost = cost + list[i][1][k][3]
                    cost = change(mainComponents, basket, cost)
                else:
                    count = count + 1
            if count == len(list[i][1]):
                print("You didn't choose the type")
            else:
                loop = False
    basket.insert(0, cost)
    return basket

def additional(oldBasket, cost):#adding additional stuff
    count = len(additionalComponents)
    loop = True
    while loop == True:
        choice = input("Do you want to add additional staff? ").lower()
        if choice == "yes":
            for i in range(len(additionalComponents)): #print the list of additional components
                print(i, " - ", additionalComponents[i][0])
            choice = getNumber()
            for i in range(len(additionalComponents)):
                if choice == i:
                    for k in range(len(additionalComponents[i][1])):#print the types of additional components
                        print(k, ":")
                        niceOutput(additionalComponents[i][1], k)
                    newChoice = getNumber()
                    for k in range(len(additionalComponents[i][1])):
                        if newChoice == k:
                            oldBasket.append(additionalComponents[i][1][k]) #add this to the basket
                            cost = cost + additionalComponents[i][1][k][3]
                            oldBasket.pop(0)
                            mainComponents.append(additionalComponents[i])#adding this component to main
                            additionalComponents.pop(i)#to have only one piece
                            cost = change(mainComponents, basket, cost)
                            oldBasket.insert(0, cost)
                            count = count - 1
                            if count == 0:
                                print("there are no components to add")
                                loop = False
        elif choice == "no":
            print("that's all")
            loop = False
        else:
            print("you didn't choose")
    return oldBasket

def readFromFile(): #reading data from file
    try:
        # code modified from https://learning.oreilly.com/library/view/python-cookbook/0596001673/ch04s07.html#pythoncook-CHP-4-SECT-7.3
        # Data accessed  27/11/2022
        with open("pc.txt") as file:
            count = 0
            for line in file:
                print(count, " - ", line)
                count = count + 1
    except FileNotFoundError:
        print("sorry, file doesn't exist, new file was added")
        file = open("pc.txt", "x")
        file.close()
    return count

def writeToFile(basket):#writing to file
    try:
        file = open("pc.txt", "a")
        file.writelines(basket)
        file.close()
    except:
        print("you cannot write to file")

def compaire(first, second): #compaires chosen PCs by price
    with open("pc.txt") as file:
        lines = file.readlines()
        pc1 = lines[first]
        pc1 = pc1[1:].split(',')[0]
        pc2 = lines[second]
        pc2 = pc2[1:].split(',')[0]
        if float(pc1)<float(pc2):
            print("first is better", "it's cost is", pc1)
        elif float(pc1)>float(pc2):
            print("second is better", "it's cost is", pc2)
        else:
            print("price is equal")

#main
CPU =("CPU", (("AMD Ryzen 7 5800X Processor", "AMD", "8C/16T, 36MB Cache, Up to 4.7 GHz Max Boost", 244.49),("Intel Core i7 9700K 3.6GHz Octa Core ", "Intel", "8 Cores, 12 MB Cache", 317.99)))
GPU = ("GPU", (("NVIDIA GeForce RTX 3060", "NVIDIA", "Core Clock 1320 MHz / Boost Clock 1777 MHz / 12 GB GDDR6 / 15 Gbps / 192 Bit", 375.95), ("EVGA GeForce RTX 2060 KO ULTRA GAMING", "EVGA", "6GB GDDR6, Dual Fan, Metal Backplate", 389.51)))
motherboard = ("MOTHERBOARD", (("AMD B450 - Micro ATX", "AMD", "Supports 4 x DDR4 Dual Channel Non-ECC Unbuffered DIMMs", 79.99), ("Motherboard for Intel B75", "Intel", "M.2 High-Speed Hard Disk 1155-Pin USB3.0 SATA3 DDR3", 81.99)))
RAM = ("RAM", (("Qumox 16 GB (2x 8 GB) 204 pin DDR3L-1600 SO-DIMM", "Qumox", "1600Mhz, PC3L-12800S, CL11, 1.35V, Low Voltage", 51), ("pc3-12800u", "motoeagle", "DDR3/DDR3L 1600 MHz UDIMM RAM 16GB Kit (8GBx2) PC3/PC3L 12800U 8GB 1.35V/1.5V 240-Pin Non-ECC Unbuffered 2RX8 Dual Rank", 36.99)))
PowerSupplyUnit = ("PowerSupplyUnit", (("GOLDEN FIELD 550W Semi Modular Power Supply Unit", "GOLDEN FIELD", "80 PLUS Bronze certified pc power supply, DC to DC Circuit Design, Runs cooler and uses less power than less efficient power supplies", 92.99), ("Corsair CP-9020102-UK CX550M 550 W 80+ Bronze Certified ATX Po Wer Supply Unit", "Corsair", "81 PLUS Bronze certified: High efficiency operation for less excess heat and lower operating costs.Continuous output rated temperature (°C)40°C", 67.99)))
case = ("CASE", (("iONZ KZ07 PC", "iONZ", "Space for 5 x 120mm Cooling Fans. None Supplied. Case Size : 460 x 185 x 420mm", 31.95), ("MSI MAG VAMPIRIC 100R", "MSI", "1x 120mm ARGB PWM Fan, 1x 120mm PWM Fan, RGB Front Panel, Tempered Glass, MSI Center, ATX, mATX, mini-ITX", 49.99)))
SSD = ("SSD", (("Kingston SSDNow A400", "Kingston", "240GB SATA 3 Solid State Drive ", 41.99), ("Crucial BX500", "Crucial", "480GB 3D NAND SATA 2.5 Inch Internal SSD ", 40.44)))
M2 = ("M2", (("Crucial P3 500GB M.2", "Crucial", "Up to 3500MB/s", 34.99), ("fanxiang S500 Pro", "fanxiang", "512GB NVMe SSD M.2 PCIe Gen3x4 2280", 32,98)))
MECHANICAL = ("MECHANICAL", (("Seagate BarraCuda", "Seagate", ".5 Inch SATA 6Gb/s 7200 RPM 256MB Cache 3.5-Inch", 53.49), ("Sonnics 2TB 3.5", "Sonnics", "7200RPM Desktop PC/Surveillance Storage Hard Drive CCTV Camera CCTV System DVR ", 32.99)))
mainComponents = [CPU, GPU, motherboard, RAM, PowerSupplyUnit, case, SSD, M2, MECHANICAL]
Keyboard = ("KEYBOARD", (("Arteck 2.4G Wireless Keyboard", "Arteck", "Keyboard with Media Hotkeys for Computer Desktop PC Laptop Surface Smart TV and Windows ", 14.99), ("Bactlit Gaming Keyboard", "RII", "7 Color Rainbow LED Backlit Mechanical Feeling USB Wired Gaming Keyboard",15.99)))
Mouse = ("MOUSE", (("Logitech B100 Wired USB Mouse", "Logitech", "3-Buttons, Optical Tracking", 5.99),("Eono Wireless Mouse", "Amazon", "Adjustable DPI, 1600DPI Silent USB Mice", 9.99)))
soundCard = ("SOUND CARD",(("TechRise USB Sound Card","TechRise","USB External Stereo Sound Adapter Splitter Converter with Volume Control for Windows and Mac", 7.64),("Solustre PCIe Sound Card","Solustre","5.1 Internal Sound Card 3D Stereo PCI-e Audio Card with Low Profile Bracket for PC Windows 10 CMI8738 Chip 32/64 Bit Sound Card PCI Express Adapter", 16.70)))
secondHardDrive = ("SECOND HARD DRIVE",(("UnionSine External Hard Drive","UnionSine","320GB Ultra Slim Portable Hard Drive USB 3.0 HDD", 26.19),("SUMJON 2TB External Hard Drive","SUMJON","Portable SSD Drive,Solid State Data Storage Hard Drives,Small Computer Backup Small Disk Drive USB3.0 ", 39.99)))
computerMonitor = ("COMPUTER MONITOR", (("Samsung S22A336NHU - S33A", "Samsung", "1920 x 1080 Full HD (1080p)", 74),("HUAWEI Display 24 Inch Monitor Full HD 1080P","HUAWEI"," Ultra-Slim Bezels with 90% Screen to Body Ratio - Low Blue Light to Decrease Eye Fatigue, 5ms Flicker Free", 99)))
OpticalDrive = ("OPTICAL DRIVE", (("DANGZW External CD DVD Drive","DANGZW","USB 3.0 Slim Portable External CD DVD Rewriter Burner Writer, High Speed Data Transfer", 22.99),("HATOKU External CD DVD Drive","HATOKU"," USB C Slim Portable External CD DVD Writer Burner with SD/TF Card Reader & 2 USB 3.0 Port, High Speed Data Transfer Optical Drive for PC ", 29.99)))
additionalComponents = [Mouse, Keyboard, OpticalDrive, secondHardDrive, computerMonitor, soundCard]
cost = 0
basket = []
basket = components(mainComponents, cost)
cost = basket[0]
additional(basket, cost)
cost = basket[0]
#checking compatibility
while (basket[1][1] == "Intel" and basket[3][1] == "AMD") or (basket[1][1] == "AMD" and basket[3][1] == "Intel") or (basket[3][1] == "AMD" and basket[2][1] == "NVIDIA"):
    print("CPU - ", basket[1][1])
    print("GPU - ", basket[2][1])
    print("motherboard - ", basket[3][1])
    basket.pop(0)
    print("it is not compatible, CPU or motherboard or GPU should be changed")
    newcost = change(mainComponents, basket, cost)
    basket.insert(0, newcost)
writeToFile(str(basket) + "\n")
cost = basket[0]
print("final cost: ", cost)
basket.pop(0)
for i in range(len(basket)):
    print(mainComponents[i][0])
    niceOutput(basket, i)
#compairing 2 builds
print("which 2 PCs do you want to compare?")
loop = True
count = int(readFromFile())
while loop == True:
    first = getNumber()
    second = getNumber()
    if first<=count and second<=count:
        loop = False
    else:
        print("you didn't choose 2 PCs from the list")
compaire(first, second)
