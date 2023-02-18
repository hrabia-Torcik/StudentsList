
def otw():
    jakasZm = open("dane85.txt", "r", encoding="utf8")
    x = jakasZm.readlines()
    jakasZm.close()
    return x

def dodaj():

    plik = open("dane85.txt", "a", encoding="utf8")
    plik.write(f"{jy};{kuj};{klo}\n")
    plik.close()
    print(f"Uczestniczka dodany.")

def szukacz():
    x = otw()
    pom = []
    pom2 = []
    dort = 0
    for v in x:
        t = v.split(";")
        # print(t)
        if (t[1] == cechaChar):
            pom.append(v)
        else:
            pom2.append(t)

    if (len(x) == len(pom2)):
        print()
        print("Niestety, nie mamy nikogo o takim nazwisku.")
        print("Może wkradła się literówka?")
        print()

    else:
        print()
        print("W naszym zbiorze istnieje taka zawodniczka! Istnieje też możliwość, że to zawodnik.")
        dort = 1
    return dort
    # return pom

def usun():
    x = otw()
    pom = []
    pom3 = 0
    for v in x:
        t = v.split(";")
        if (t[1] != cechaChar):
            pom.append(v)
            # print("gg")
    print("Właściwie to po tej operacji precyzyjniej byłoby napisać: istniała... (bądź istniał).")
    print()
    jakasZm2 = open("dane85.txt", "w", encoding="utf8")

    jakasZm2.writelines(pom)   # Tu wrzucam od razu całą listę.
    # for i in pom:         # Tą pętlą wrzucam kolejne indeksy z listy.
    #     jakasZm2.write(i)
    jakasZm2.close()

def pokaz():

    x = otw()
    print()
    for v in x:
        tes = v.split(";")
        if (len(tes)>3):
            cos = f"{tes[0]};{tes[1]};{tes[2]};"
            greg = v.replace(cos, " ")
            greg = greg.strip()
            greg = greg.replace(";", " ")
            print(f"Imię: {tes[0]}, Nazwisko: {tes[1]}, Grupa: {tes[2].strip()}, Oceny: {greg}")
        else:
            print(f"Imię: {tes[0]}, Nazwisko: {tes[1]}, Grupa: {tes[2].strip()}")

    print()


def zmienI():
    x = otw()
    pom = []
    pom3 = []
    for ggg in x:
        kkkk = ggg.split(";")

        if (kkkk[1] == cechaChar):
            pom3.append(noweImie)
            pom3.append(kkkk[1])
            pom3.append(kkkk[2])
            if (len(kkkk) > 3):
                oceny = ggg.replace(kkkk[0],"")
                oceny = oceny.replace(kkkk[1],"")
                oceny = oceny.replace(kkkk[2],"")
                oceny = oceny.replace(";;;","")
                oceny = oceny.replace(";", " ")
                wydruk = f"Imię: {pom3[0]}, Nazwisko: {pom3[1]}, Grupa: {pom3[2].strip()}, Oceny: {oceny}"

            else:
                wydruk = f"Imię: {pom3[0]}, Nazwisko: {pom3[1]}, Grupa: {pom3[2].strip()}"
            typej1 = ggg.replace(kkkk[0],noweImie)
            pom.append(typej1)
        else:
            pom.append(ggg)

    print()
    print("Nowe dane to:")
    print(wydruk)
    print()
    print("Co dalej?")
    return pom


def zmienN():
    x = otw()
    pom = []
    pom3 = []
    for ggg in x:
        kkkk = ggg.split(";")

        if (kkkk[1] == cechaChar):
            pom3.append(kkkk[0])
            pom3.append(noweNazwisko)
            pom3.append(kkkk[2])
            if (len(kkkk) > 3):
                oceny = ggg.replace(kkkk[0],"")
                oceny = oceny.replace(kkkk[1],"")
                oceny = oceny.replace(kkkk[2],"")
                oceny = oceny.replace(";;;","")
                oceny = oceny.replace(";", " ")
                wydruk = f"Imię: {pom3[0]}, Nazwisko: {pom3[1]}, Grupa: {pom3[2].strip()}, Oceny: {oceny}"

            else:
                wydruk = f"Imię: {pom3[0]}, Nazwisko: {pom3[1]}, Grupa: {pom3[2].strip()}"
            typej1 = ggg.replace(kkkk[1], noweNazwisko)
            pom.append(typej1)
        else:
            pom.append(ggg)

    print()
    print("Nowe dane to:")
    print(wydruk)
    print()
    print("Co dalej?")
    return pom


def zmienG():
    x = otw()
    pom = []
    pom3 = []
    for ggg in x:
        kkkk = ggg.split(";")

        if (kkkk[1] == cechaChar):
            pom3.append(kkkk[0])
            pom3.append(kkkk[1])
            pom3.append(noweGrupa)
            if (len(kkkk) > 3):
                typej1 = ggg.replace(kkkk[2], noweGrupa)
                oceny = ggg.replace(kkkk[0],"")
                oceny = oceny.replace(kkkk[1],"")
                oceny = oceny.replace(kkkk[2],"")
                oceny = oceny.replace(";;;","")
                oceny = oceny.replace(";", " ")
                wydruk = f"Imię: {pom3[0]}, Nazwisko: {pom3[1]}, Grupa: {pom3[2].strip()}, Oceny: {oceny}"

            else:
                hhh = noweGrupa+"\n"
                typej1 = ggg.replace(kkkk[2],hhh)
                wydruk = f"Imię: {pom3[0]}, Nazwisko: {pom3[1]}, Grupa: {pom3[2].strip()}"
            pom.append(typej1)
        else:
            pom.append(ggg)

    print()
    print("Nowe dane to:")
    print(wydruk)
    print()
    print("Co dalej?")
    return pom


def dodOcene():
    x = otw()
    pom = []
    for ggg in x:
        kkkk = ggg.split(";")

        if (kkkk[1] == cechaChar):
            typej1 = f"{ggg.strip()};{nowaOcena}\n"
            pom.append(typej1)
            pom2 = kkkk[0]
            pom3 = kkkk[1]
            cos = f"{kkkk[0]};{kkkk[1]};{kkkk[2]};"
            greg = typej1.replace(cos," ")
            greg = greg.strip()
            greg = greg.replace(";"," ")
        else:
            pom.append(ggg)

    print()
    print(f"Aktualne oceny studentki {pom2} {pom3} to:")
    print(greg)
    print()
    print("Co dalej?")
    return pom


def frazSzuk():
    zmieniak = {"A": "a",
                "Ą": "ą",
                "B": "b",
                "C": "c",
                "Ć": "ć",
                "D": "d",
                "E": "e",
                "F": "f",
                "G": "g",
                "H": "h",
                "I": "i",
                "J": "j",
                "K": "k",
                "L": "l",
                "Ł": "ł",
                "M": "m",
                "N": "n",
                "Ń": "ń",
                "O": "o",
                "Ó": "ó",
                "P": "p",
                "Q": "q",
                "R": "r",
                "S": "s",
                "Ś": "ś",
                "T": "t",
                "U": "u",
                "V": "v",
                "W": "w",
                "X": "x",
                "Y": "y",
                "Z": "z",
                "Ź": "ź",
                "Ż": "ż"}  # ten słownik służy mi do zamiany dużych liter na małe
    napis = list(cechaChar2)
    cechaChar = ""
    for t in napis:
        if (t.isupper()):
            cechaChar = cechaChar+zmieniak[t]
        else:
            cechaChar = cechaChar+t

    x = otw()
    pomoc = 0
    pom2 = []
    for ggg in x:
        ###########################################################
        #  Ta część kodu służy tylko do zamiany wielkości liter

        napis2 = list(ggg)
        giet = ""
        for t in napis2:
            if (t.isupper()):
                giet = giet + zmieniak[t]
            else:
                giet = giet + t
        ###########################################################
        kkkk = ggg.split(";")
        if (giet.count(cechaChar) >0):
            tej = f"{kkkk[0]};{kkkk[1]}"
            pom2.append(tej)
            pomoc = 1

    if (pomoc == 0):
        print()
        print("Nikogo nie umiem dopasować do tej frazy. Jestem rozczarowany sam sobą...")
        print()
    else:

        print("Chyba jest ktoś, kto pasuje:")
        print()
        for d in pom2:
            print(d.replace(";", " "))
        print()


def wyliczSred():
    ##############################
    x = otw()
    for ggg in x:
        kkkk = ggg.split(";")
        if (kkkk[1] == cechaChar):
            grot = kkkk
            f1 = kkkk[0]
            f2 = kkkk[1]
            if (len(kkkk) > 3):
                del grot[0]
                del grot[0]
                del grot[0]
                suma = 0
                for d in grot:
                    d = int(d)
                    suma = suma + d
                    srednia = suma / len(grot)
                wydruk = f"{f1} {f2} ma taką średnią: {srednia}"
                print()
            else:
                wydruk = f"Ta gapa jeszcze nie ma ocen."

    ###############################################

    # print(z)
    # f1 = kkkk[0]
    # f2 = kkkk[1]
    # if (len(kkkk) > 3):
    #     del grot[0]
    #     del grot[0]
    #     del grot[0]
    #     suma = 0
    #     for d in grot:
    #         d = int(d)
    #         suma = suma + d
    #         srednia = suma / len(grot)
    #     wydruk = f"{f1} {f2} ma taką średnią: {srednia}"
    #     print()
    # else:
    #     wydruk = f"Ta gapa jeszcze nie ma ocen."

    ################################################

    print(wydruk)
    print()


def zapis():

    jakasZm2 = open("dane85.txt", "w", encoding="utf8")
    jakasZm2.writelines(r)  # Tu wrzucam od razu całą listę.
    jakasZm2.close()

###############################################################################################

while(True):
    menu = input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5- wyszukaj studenta wg frazy, 6 - wylicz średnią gagatka, 7-wyjscie: ")

    if (menu == "1"):
        jy = input("Podaj imie: ")
        kuj = input("Podaj nazwisko: ")
        klo = input("Podaj grupę: ")
        dodaj()
    elif (menu == "2"):
        pokaz()


    elif (menu == "3"):
        cechaChar = input("Podaj nazwisko: ")
        z = szukacz()
        if (z == 0):
            pass
        elif (z == 1):
            usun()
    elif (menu == "4"):
        cechaChar = input("Podaj nazwisko: ")
        z = szukacz()
        if (z == 0):
            pass
        elif (z == 1):
            while (True):
                print("Możesz wybrać następujące opcje:")
                print("1 - Zmiana imienia;")
                print("2 - Zmiana nazwiska;")
                print("3 - Zmiana grupy;")
                print("4 - Dodawanie oceny;")
                print("0 - opuszczenie trybu zmian cech uczestnika")
                menu = input("Co wybierasz? Wpisz odpowiednią cyfrę: ")
                if (menu == "1"):
                    noweImie = input("Podaj nowe imie: ")
                    r = zmienI()
                    zapis()

                elif (menu == "2"):
                    noweNazwisko = input("Podaj nowe nazwisko: ")
                    r = zmienN()
                    zapis()

                elif (menu == "3"):
                    noweGrupa = input("Podaj nową grupę: ")
                    # zmienG()  #### Wywołanie funkcji jest już niepotrzebne. Wystarczy definicja zmiennej i funkcja uruchamia się.
                    r = zmienG()
                    zapis()

                elif (menu == "4"):
                    nowaOcena = int(input("Podaj ocenę do dodania: "))
                    r = dodOcene()
                    zapis()

                elif (menu == "0"):
                    break

    elif (menu == "5"):
        cechaChar2 = input("Podaj jakąś część nazwy poszukiwanego osobniczki: ")
        frazSzuk()

    elif (menu == "6"):
        cechaChar = input("Podaj nazwisko zawodniczki/zawodnika: ")
        z = szukacz()
        if (z == 0):
            pass
        elif (z == 1):
            wyliczSred()

    elif (menu == "7"):
        break
