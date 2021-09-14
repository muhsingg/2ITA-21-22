import random

#Legge sammen to tall
def addere():    
    tall1 = input("Gi meg et tall: ")
    tall2 = input("Gi meg et annet tall: ")

    sum = int(tall1)+int(tall2)

    print("Summen av", tall1, "og", tall2, "er", sum)

#Multiplisere to tall
def multiplisere():
    tall1 = input("Gi meg et tall: ")
    tall2 = input("Gi meg et annet tall: ")

    produkt = int(tall1)+int(tall2)

    print("Prduktet av", tall1, "og", tall2, "er", produkt)


mylist = ["apple", "banana", "cherry"]


for i in range(5):
    print(i)


for navn in mylist:
    print(navn)


