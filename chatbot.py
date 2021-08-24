import time


valg = 1

print("Hei og velkommen. Bruk denne botten for å bli bedre kjent med meg \n \n")

print("Hva lurer du på? \n")


while valg!=0:
    print("1 - Navnet mitt")
    print("2 - Hvor gammel2 jeg er")
    print("3 - Mine interesser og hobbyer")
    print("4 - Teknologier jeg har jobbet med \n")

    print("0 - Avslutt \n \n")


    valg = int(input("Ditt valg: "))


    if valg==1: 
        print("\033[95m Jeg heter Muhsin Gunaydin \033[0m")
    elif valg ==2:
        print("\033[95m Jeg er 32 år gammel \033[0m")
    elif valg==3:
        print("\033[95mMine interesser er: \033[0m")
        print("\033[95m - Utvikling \033[0m")
        print("\033[95m - Fotball \033[0m")
        print("\033[95m - og mye annet \033[0m")
    elif valg ==4:
        print("\033[95m Jeg har jobbet med følgende teknologier \033[0m")
        print("\033[95m Programmeringsspråk: Java, JS, C++, Python, Kotlin \033[0m")
        print("\033[95m Databaser: MySQL, MongoDB \033[0m")
        print("\033[95m Versjonskontrollsystem: Git \033[0m")
        print("\033[95m Markeringsspråk: HTML, CSS, XML \033[0m")
        print("\033[95m Rammeverk: jQuery, Angular, React \033[0m")

    
    if valg!=0:
        time.sleep(2)
        print("\n\n\033[93m Noe annet du lurer på? \033[0m")


print("\033[95m Ha det bra! \033[0m")