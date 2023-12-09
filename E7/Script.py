from pathlib import Path

#Put your ban units here 
Ban_list = ["mlbellona", "mlchoux"]

#Check general for units name and counters

#DO NOT TOUCH AFTER THIS LINE
#-------------------------------------------------------------------------------------------------------------------------------------------------
def common_counter(a, b):
    result = [i for i in a if i in b]
    return result

def listToString(s):
    str1 = ""
    str1 += ', '.join(s)
    return str1

def inputchecker(prompt):
    while True:
        try:
            answer = str(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that")
            continue

        for line in Counterpicks:
            unit = line.split()
            if answer == unit[0]:
                return answer
        print("Sorry, your response must be in the database")

def inputchecker_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
        except ValueError:
            print("Sorry, your response must be 1 or 2")
            continue

        if answer == 1 or answer == 2:
            return answer
        print("Sorry, your response must be 1 or 2")
 
        
ft = Path(__file__).with_name('First.txt')
FirstTurn = ft.open('r')
st = Path(__file__).with_name('Second.txt')
SecondTurn= st.open('r')
g = Path(__file__).with_name('General.txt')
General = g.open('r')

First = FirstTurn.readlines()
Second = SecondTurn.readlines()
Counterpicks = General.readlines()

First_Update =[]
Second_Update =[]
Third_Update =[]

Enemy_1_Counters = None
Enemy_2_Counters = None
Enemy_3_Counters = None
Enemy_4_Counters = None
Enemy_5_Counters = None

Player_List = []
Enemy_List = {}

Sum_Counters_1 = []
Sum_Counters_2 = []
Final_Sum = []

Ban_list.append(inputchecker('What did they ban first?: '))
Ban_list.append(inputchecker('What did they ban second?: '))

Turn = inputchecker_int('Are you going first or second? (1 or 2): ')
print("\n") 
if Turn == 1:
    repeats = []
    Player_1 = inputchecker("Input your first unit: ")
    Enemy_1 = inputchecker("Input their first unit: ")
    Enemy_2 = inputchecker("Input their second unit: ")
    print("\n") 
    Ban_list.append(Player_1)
    Ban_list.append(Enemy_1)
    Ban_list.append(Enemy_2)

    for line in Counterpicks:
        unit = line.split()
        if unit[0] == Enemy_1:
            Enemy_1_Counters = unit[1:]
            Filter = [i for i in Enemy_1_Counters if i not in Ban_list]
            print(Enemy_1 +" counters: "+ listToString(Filter))
        if unit[0] == Enemy_2:
            Enemy_2_Counters = unit[1:]
            Filter = [i for i in Enemy_2_Counters if i not in Ban_list]
            print(Enemy_2 +" counters: "+ listToString(Filter))
    if Enemy_1_Counters != None and Enemy_2_Counters != None:
        Sum_Counters_1 = common_counter(Enemy_2_Counters, Enemy_1_Counters)
        Filter = [i for i in Sum_Counters_1 if i not in Ban_list]
        print("\n")
        if Filter:
            print("Recommendations: "+ listToString(Filter))
    for line in First:
        unit = line.split()
        if (unit[0] == Player_1 and ((unit[1] == Enemy_1 and unit[2] == Enemy_2) or (unit[1] == Enemy_2 and unit[2] == Enemy_1))):
            if unit[3] not in Ban_list and unit[4] not in Ban_list:
                First_Update = First_Update + [unit]
                if not(([unit[3],unit[4]] in repeats) or ([unit[4],unit[3]] in repeats)):
                    repeats.append([unit[3],unit[4]])
                    print("Popular Choice: " + unit[3] + ", " + unit[4])
    
    print("\n")
    Player_2 = inputchecker("Input your second unit: ")
    Player_3 = inputchecker("Input your third unit: ")
    Enemy_3 = inputchecker("Input their third unit: ")
    Enemy_4 = inputchecker("Input their fourth unit: ")
    print("\n") 
    Ban_list.append(Player_2)
    Ban_list.append(Player_3)
    Ban_list.append(Enemy_3)
    Ban_list.append(Enemy_4)

    for line in Counterpicks:
        unit = line.split()
        if unit[0] == Enemy_3:
            Enemy_3_Counters = unit[1:]
            Filter = [i for i in Enemy_3_Counters if i not in Ban_list]
            print(Enemy_3 +" counters: "+ listToString(Filter))

        if unit[0] == Enemy_4:
            Enemy_4_Counters = unit[1:]
            Filter = [i for i in Enemy_4_Counters if i not in Ban_list]
            print(Enemy_4 +" counters: "+ listToString(Filter))
    if Enemy_3_Counters != None and Enemy_4_Counters != None:
        Sum_Counters_2 = common_counter(Enemy_3_Counters, Enemy_4_Counters)
        Final_Sum = common_counter(Sum_Counters_1, Sum_Counters_2)
        Filter = [i for i in Final_Sum if i not in Ban_list]
        print("\n")
        if Filter:
            print("Recommendations: "+ listToString(Filter))
    for units in First_Update:
        if (((units[3] == Player_2 and units[4] == Player_3) or (units[3] == Player_3 and units[4] == Player_2))
            and ((units[5] == Enemy_3 and units[6] == Enemy_4) or (units[5] == Enemy_4 and units[6] == Enemy_3))):
            if units[7] not in Ban_list and units[8] not in Ban_list:
                Second_Update = Second_Update + [units]
                if not(([units[7],units[8]] in repeats) or ([units[8],units[7]] in repeats)):
                    repeats.append([units[7],units[8]])
                    print("Popular Choice: " + units[7] + ", " + units[8])
    print("\n")
    Player_4 = inputchecker("Input your fourth unit: ")
    Player_5 = inputchecker("Input your last unit: ")
    Enemy_5 = inputchecker("Input their last unit: ")
    print("\n") 


    Enemy_List = dict({Enemy_1: [], Enemy_2: [], Enemy_3: [], Enemy_4: [], Enemy_5: []})
    Player_List.append(Player_1)
    Player_List.append(Player_2)
    Player_List.append(Player_3)
    Player_List.append(Player_4)
    Player_List.append(Player_5)
    
    max = 0
    Ban_unit = ""
    for p in Player_List:
        for line in Counterpicks:
            unit = line.split()
            if unit[0] == p:
                for i in unit[1:]:
                    if i in Enemy_List.keys():
                        Enemy_List[i].append(p)
    for key, value in Enemy_List.items():
        count = len(value)
        print(str(count) + " "+ key + " counters: " + listToString(value))
        if count > max:
            max = count 
            Ban_unit = key
    print("\n")
    for units in Second_Update:
        if (units[9] == Enemy_5):
            print("Popular Ban: "+ units[10])
    print("Recommended Ban: " + Ban_unit)

else:
    repeats = []
    Enemy_1 = inputchecker("Input their first unit: ")
    print("\n") 
    Ban_list.append(Enemy_1)
    for line in Second:
        unit = line.split()
        if ((unit[0] == Enemy_1) and (unit[1] not in Ban_list and unit[2] not in Ban_list)):
            First_Update = First_Update + [unit]
            if not(([unit[1],unit[2]] in repeats) or ([unit[2],unit[1]] in repeats)):
                repeats.append([unit[1],unit[2]])
                print("Popular Choice: " + unit[1] + ", " + unit[2])

    for line in Counterpicks:
        unit = line.split()
        if unit[0] == Enemy_1:
            Enemy_1_Counters = unit[1:]
            Filter = [i for i in Enemy_1_Counters if i not in Ban_list]
            print(Enemy_1 +" counters: "+ listToString(Filter))
    
    print("\n")
    Player_1 = inputchecker("Input your first unit: ")
    Player_2 = inputchecker("Input your second unit: ")
    Enemy_2 = inputchecker("Input their second unit: ")
    Enemy_3 = inputchecker("Input their third unit: ")
    print("\n") 
    Ban_list.append(Player_1)
    Ban_list.append(Player_2)
    Ban_list.append(Enemy_2)
    Ban_list.append(Enemy_3)

    for line in Counterpicks:
        unit = line.split()
        if unit[0] == Enemy_2:
            Enemy_2_Counters = unit[1:]
            Filter = [i for i in Enemy_2_Counters if i not in Ban_list]
            print(Enemy_2 +" counters: "+ listToString(Filter))

        if unit[0] == Enemy_3:
            Enemy_3_Counters = unit[1:]
            Filter = [i for i in Enemy_3_Counters if i not in Ban_list]
            print(Enemy_3 +" counters: "+ listToString(Filter))
    if Enemy_2_Counters != None and Enemy_3_Counters != None:
        Sum_Counters_1 = common_counter(Enemy_2_Counters, Enemy_3_Counters)
        Sum_Counters_2 = common_counter(Sum_Counters_1, Enemy_1_Counters)
        Filter = [i for i in Sum_Counters_2 if i not in Ban_list]
        print("\n")
        if Filter:
            print("Recommendations: "+ listToString(Filter))
    for units in First_Update:
        if (((units[1] == Player_1 and units[2] == Player_2) or (units[1] == Player_2 and units[2] == Player_1))
            and ((units[3] == Enemy_2 and units[4] == Enemy_3) or (units[3] == Enemy_3 and units[4] == Enemy_2))):
            if units[5] not in Ban_list and units[6] not in Ban_list:
                Second_Update = Second_Update + [units]
                if not(([units[5],units[6]] in repeats) or ([units[6],units[5]] in repeats)):
                    repeats.append([units[5],units[6]])
                    print("Popular Choice: " + units[5] + ", " + units[6])
    print("\n")
    Player_3 = inputchecker("Input your third unit: ")
    Player_4 = inputchecker("Input your fourth unit: ") 
    Enemy_4 = inputchecker("Input their fourth unit: ")
    Enemy_5 = inputchecker("Input their last unit: ")
    print("\n") 

    repeats = []
    for line in Counterpicks:
        unit = line.split()
        if unit[0] == Enemy_4:
            Enemy_4_Counters = unit[1:]
            Filter = [i for i in Enemy_4_Counters if i not in Ban_list]
            print(Enemy_4 +" counters: "+ listToString(Filter))

        if unit[0] == Enemy_5:
            Enemy_5_Counters = unit[1:]
            Filter = [i for i in Enemy_5_Counters if i not in Ban_list]
            print(Enemy_5 +" counters: "+ listToString(Filter))

    if Enemy_4_Counters != None and Enemy_5_Counters != None:
        Sum_Counters_3 = common_counter(Enemy_4_Counters, Enemy_5_Counters)
        Final_Sum = common_counter(Sum_Counters_3, Sum_Counters_2)
        Filter = [i for i in Final_Sum if i not in Ban_list]
        print("\n")
        if Filter:
            print("Recommendations: "+ listToString(Filter))
    for units in Second_Update:
        if (((units[5] == Player_3 and units[6] == Player_4) or (units[5] == Player_4 and units[6] == Player_3))
            and ((units[7] == Enemy_4 and units[8] == Enemy_5) or (units[7] == Enemy_5 and units[8] == Enemy_5))):
            if units[9] not in Ban_list:
                Third_Update = Third_Update + [units]
                if not(units[9] in repeats):
                    repeats.append(units[9])
                    print("Popular Choice: " + units[9])
    print("\n")

    Player_5 = inputchecker("Input your last unit: ")
    print("\n") 
    Enemy_List = dict({Enemy_1: [], Enemy_2: [], Enemy_3: [], Enemy_4: [], Enemy_5: []})
    Player_List.append(Player_1)
    Player_List.append(Player_2)
    Player_List.append(Player_3)
    Player_List.append(Player_4)
    Player_List.append(Player_5)
    
    max = 0
    Ban_unit = ""
    for p in Player_List:
        for line in Counterpicks:
            unit = line.split()
            if unit[0] == p:
                for i in unit[1:]:
                    if i in Enemy_List.keys():
                        Enemy_List[i].append(p)
    for key, value in Enemy_List.items():
        count = len(value)
        print(str(count) + " "+ key + " counters: " + listToString(value))
        if count > max:
            max = count 
            Ban_unit = key
    print("\n")
    for units in Third_Update:
        if (units[9] == Player_5):
            print("Popular Ban: "+ units[10])
    print("Recommended Ban: " + Ban_unit)
print("\n") 
print("-----End-----")