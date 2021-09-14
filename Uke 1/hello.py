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