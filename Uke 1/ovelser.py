import random



def terningkast():
    terning1 = 0
    terning2 = 0
    sum = 0

    while sum!=12:
        input("Trykk for å kaste terning")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        sum= terning1+terning2
        print("Du fikk", sum)



def telle():
    for i in range(1,70):
        print(i)
        if i==35:
            print("Du er halveis")


klasseliste = ["Henrik", "Mathias", "Tobias H", "Jakub", "Max",
"Emil", "Bjørn Tore", "Henrik Ø", "Mats Fredrik", "Herman", "Tobias D",
"Wang", "Isa", "Ole", "Muhsin", "Marius"]

print(len(klasseliste))







frukt = "agurk"
gronnsak = "eple"

temp = frukt #lager en variabel for å holde på verdien i frukt
fruk = gronnsak
gronnsak = temp



tall1 = 14
tall2 = 7
tall3 = 11

if tall1 > tall2:
    print("tall1 er størst")
elif tall2 > tall1:
    print("tall2 er størst")
else: #dette er ekstre, det er ikke et krav og sjekke om de er like stor 
    print("tall1 og tall2 er like store")


if tall1 > tall2 and tall1 > tall3:
    print("tall1 er størst")
elif tall2 > tall1 and tall2 > tall3:
    print("tall2 er størst")
else:
    print("tall3 er størst")





navnEn = "Jonatan"
navnTo = "Tobias"

if len(navnEn) > len(navnTo):
    print(navnEn, "er lengts og den har", len(navnEn), "bokstaver")
elif len(navnTo > navnEn):
    print(navnTo, "er lengts og den har", len(navnTo), "bokstaver")
else:
    print("Begge navnene er like lange, og de har", len(navnEn), "bokstaver")





start = 1
slutt = 12

for i in range(start, slutt):
    print(i)


for j in range(slutt, start, -1):
    print(j)




import random

while True:
    tall = random.randint(1,999)
    print(tall)
    if tall == 571:
        break
    



a=[1,1,2,3,5,8,13,21,34,55,89]

#Lag et program som skriver ut alle tallene i lista
for tall in a:
    print(a)

#alternativ måte:
for i in range(len(a)):
    print(a[i])


#Lag et program som skriver ut alle tall som er mindre enn 5 i lista over.
for tall in a:
    if tall < 5:
        print(tall)


##Lag et program som skriver ut alle partall i lista over.
for tall in a:
    if tall % 2 == 0:
        print(tall)



##Lag en ny liste hvor du legger inn alle tall som er større enn 5 i lista over. Skriv ut den nye lista

b = []
for tall in a:
    if tall > 5:
        b.append(tall)
print(b)







print("KMI kalkulator")

hoyde = int(input("Din høyde i cm: "))
vekt = int(input("Din vekt i kg: "))

vektMeter = vekt / 100

KMI = vektMeter / hoyde ** 2  #alternativ skrivemåte: KMI = vektMeter / hoyde * hoyde

KMI = 26.01

if KMI <= 16:
    print("Undervekt grad 3")
elif KMI <=17:
    print("Undervekt grad 2")
elif KMI <=18.5:
    print("Undervekt grad 1")
elif KMI > 18.5 and KMI < 25:
    print("Normal vekt")
elif KMI >=40:
    print("Svært alvorlig fedme")
elif KMI >= 35:
    print("Alvorlig fedme")
elif KMI >= 30:
    print("Fedme")
elif KMI >= 25:
    print("Overvekt")
