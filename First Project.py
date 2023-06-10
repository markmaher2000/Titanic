import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/mark maher/OneDrive - Higher Technological Institute\Desktop/Projects/First project/titanic.xls')

def error():
    df['age'].fillna(0, inplace = True)
    df['fare'].fillna(0, inplace = True)
error()

def alive_sex():
    for gen in df['sex'].unique():
        print(gen)
        gendear = df[df['sex'] == gen]
        survived = gendear[df['survived'] == 1]
        print(f"The total of {gen} is", gendear.shape[0])
        print(f"The number of the alive of {gen} is ", survived.shape[0])
        print("\n******\n")

def death_sex():
    for gen in df['sex'].unique():
        print(gen)
        gendear = df[df['sex'] == gen]
        survived = gendear[df['survived'] == 0]
        print(f"The total of {gen} is", gendear.shape[0])
        print(f"The number of the death of {gen} is ", survived.shape[0])
        print("\n******\n")

def alive_classes():
    for classes in df['pclass'].unique():
        print(classes)
        p_class = df[df['pclass']==classes]
        survived = p_class[df['survived'] == 1]
        print(f"The total of the class {classes} is", p_class.shape[0])
        print(f"The number of the alive is ", survived.shape[0])
        print("\n******\n")

def death_classes():
    for classes in df['pclass'].unique():
        print(classes)
        p_class = df[df['pclass']==classes]
        survived = p_class[df['survived'] == 0]
        print(f"The total of the class {classes} is", p_class.shape[0])
        print(f"The number of the death is ", survived.shape[0])
        print("\n******\n")

def histogram_alive_sex():
    gen = df['sex']
    survived = gen[df['survived'] == 1]
    survived.hist()
    print(plt.show())



def calc():
    
    sum = 0
    for i in df['fare']:
        sum += i
    print("The total of the fare: ", sum)
    
def fare_pclass():
    
    for classes in df['pclass'].unique():
        sum = 0
        print(f"The class {classes}")
        clc = df[df['pclass'] == classes]
        
        
        for i in clc['fare']:
            sum += i
        
        print(f"The total of the fare in the class {classes} is {sum}")
        print("\n******\n")

def hist_pclass_fare():
    
    k =0
    index = []
    sums = []
    for classes in df['pclass'].unique():
        sum = 0
        clc = df[df['pclass'] == classes]
        index.append(f"The {classes} pclass")
        for i in clc['fare']:
            sum += i
        sums.append(sum)      
    plt.bar(index, sums)
    print(plt.show())
        
def display():
    
    x = int(input("What do you want from the data:\n 1-how many are alive?\n 2-how many alive in different classes? \n 3-how many death?\n 4-how many death in different classes \n 5- how much the fare?\n 6-Visulaitaion?\n 7- how much the fare in the different pclasses?\n"))
    if x == 1:
        alive_sex()
    elif x == 2:
        alive_classes()
    elif x == 3:
        death_sex()
    elif x == 4:
        death_classes()
    elif x == 5:
        calc()
    elif x == 6:
        y = int(input("Do you want to see\n 1-alive people?\n 2-how much the fare in different classes?"))
        if y == 1:
            histogram_alive_sex()
        else:
            hist_pclass_fare()
    else:
        fare_pclass()
display()

def restart():
    while True:
        x = input("Restart? ok or no\n")
        if x.lower() == "ok":
            display()
        else:
            break
restart()
#Loading for New Update