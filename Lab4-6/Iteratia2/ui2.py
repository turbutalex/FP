from pachet2 import *
def print_menu():
    print("1.1: Adaugarea pachetului")
    print("1.2: Modificarea pachetului")
    print("2.1: Stergerea pachetelor pentru o destinatie data")
    print("2.3: Stergerea pachetelor cu un pret mai mare decat cel dat")
    print("3.1: Tiparirea pachetelor ce presupun sejurul intr-un interval dat")
    print("3.2: Ofertele cu o destinatie data si cu un pret maxim admis")
    print("3.3: Tiparirea pachetelor cu o anumita data de sfarsit")
    print("4.1: Numarul de oferte cu o destinatie data")
    print("4.2: Tiparirea pachetelor intr-o anumita perioada citita in ordinea crescatoare a pretului")
    print("4.3: Media de pret pentru o destinatie data")
    print("5.1: Toate pachetele de la o destinatie data cu un pret mai mic decat cel dat")
    print("5.2: Toate pachetele exceptand cele din luna citita")
    print("exit: iesirea din aplicatie")
    print("clear: Stergerea textului din consola")

def ui_print_list(l):
    print(l)

def print_pachet_cu_destinatie(l):
    """
    functie care tipareste toate pachetele cu o destinatie data si cu pret mai mic sau egal cu cel dat
    """
    destinatie = input("Destinatia dorita: ")
    try:
        pret = int(input("Pretul maxim: "))
    except ValueError:
        print("Valoare invalida")
    for _pachet in l:
        if destinatie == get_destinatie(_pachet) and pret >= get_pret(_pachet):
            print(_pachet)
def print_nrOferte_cu_destinatie(l):
    """
    functie care tipareste numarul de pachete cu o anumita destinatie
    """
    destinatie = input("Destinatia dorita: ")
    print(nrOferte_cu_destinatie(destinatie,l))

def print_medie_pret_destinatie(l):
    """
    functie care tipareste media de pret pentru o destinatie data
    """
    destinatie = input("Destinatia dorita: ")
    print(medie_pret_destinatie(destinatie,l))

def ui_adauga_pachet(l):
    """
    Functia care adauga un pachet dupa ce primeste input de la utilizator
    """
    try:
        zi_inceput = int(input("ziua inceperii: "))
        luna_inceput = int(input("luna inceperii: "))
        an_inceput = int(input("anul inceperii: "))
        data_valida(zi_inceput,luna_inceput,an_inceput)
        zi_sfarsit = int(input("zi final: "))
        luna_sfarsit = int(input("luna final: "))
        an_sfarsit = int(input("an final: "))
        data_valida(zi_sfarsit,luna_sfarsit,an_sfarsit)
        destinatie = input("destinatia: ")
        pret = int(input("pret: "))
        pachet = creeaza_pachet(zi_inceput,luna_inceput, an_inceput, zi_sfarsit, luna_sfarsit, an_sfarsit , destinatie, pret)
        valideaza_pachet(pachet)
        adauga_pachet(pachet,l)
        print("Pachet adaugat cu succes")
    except ValueError:
        print("Valoarea trebuie sa fie un numar")
    except Exception as ex:
        print(str(ex))
def ui_modifica_pachet(l):
    """
    functia de ui pentru modificarea unui pachet
    """
    try:
        i = int(input("indexul pachetului: "))
        zi_inceput = int(input("ziua inceperii: "))
        luna_inceput = int(input("luna inceperii: "))
        an_inceput = int(input("anul inceperii: "))
        data_valida(zi_inceput,luna_inceput,an_inceput)
        zi_sfarsit = int(input("zi final: "))
        luna_sfarsit = int(input("luna final: "))
        an_sfarsit = int(input("an final: "))
        data_valida(zi_sfarsit,luna_sfarsit,an_sfarsit)
        destinatie = input("destinatia: ")
        pret = int(input("pret: "))
        modifica_pachet(l,i,zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret)
        valideaza_pachet(l[i])
        print(l[i])
        print("Pachet modificat cu succes")
    except ValueError:
        print("Valoarea trebuie sa fie un numar")
    except Exception as ex:
        print(str(ex))
    

def print_elimina_pret_mai_mare_si_destinatie(l):
    """
    Functia care asteapta input de la user pe urma apeleaza pachetele cu proprietatea dorita 
    """
    destinatie = input("Destinatia dorita: ")
    try:
        pret = int(input("Pretul maxim: "))
    except ValueError:
        print("Valoare invalida")
    for i in elimina_pret_mai_mare_si_destinatie(destinatie,pret,l):
        print(l[i])

def ui_elimina_cu_luna(l):
    """
    functia de UI pentru functia elimina_cu_luna
    """
    luna = input("luna care sa fie exclusa(1-12): ")
    for i in elimina_cu_luna(luna,l):
        print(l[i])

def ui_sterge_cu_destinatie(l):
    """
    functia de ui pentru stergere cu destinatie
    """
    try:
        destinatie = input("Destinatia dorita: ")
    except ValueError:
        print("Valoare invalida")
    sterge_cu_destinatie(destinatie,l)

def ui_sterge_cu_pret(l):
    """
    functia de ui pentru stergere cu pret mai mare decat cel dat
    """
    try:
        pret = int(input("Pretul maxim admis"))
    except ValueError:
        print("Valoare invalida")
    sterge_cu_pret(pret,l)

def ui_interval_sejur(l):
    """
    functie de ui pentru cautarea pachetelor dintr un interval dat
    """
    try:
        zi_inceput = int(input("ziua inceperii: "))
        luna_inceput = int(input("luna inceperii: "))
        an_inceput = int(input("anul inceperii: "))
        data_valida(zi_inceput,luna_inceput,an_inceput)
        zi_sfarsit = int(input("zi final: "))
        luna_sfarsit = int(input("luna final: "))
        an_sfarsit = int(input("an final: "))
        data_valida(zi_sfarsit,luna_sfarsit,an_sfarsit)
    except ValueError:
        print("Valori invalide")
    except Exception as ex:
        print(str(ex))
    for i in interval_sejur(zi_inceput,luna_inceput,an_inceput , zi_sfarsit,luna_sfarsit,an_sfarsit,l):
        print(l[i])

def ui_pachet_sfarsit(l):
    """
    functie de ui pentru cautarea pachetelor cu o data de sfarsit data
    """
    try:
        zi_sfarsit = int(input("zi final: "))
        luna_sfarsit = int(input("luna final: "))
        an_sfarsit = int(input("an final: "))
        data_valida(zi_sfarsit,luna_sfarsit,an_sfarsit)
    except ValueError:
        print("Valori invalide")
    except Exception as ex:
        print(str(ex))
    for i in pachet_cu_sfarsit(zi_sfarsit,luna_sfarsit,an_sfarsit,l):
        print(l[i])
    
def ui_interval_sejur_pret_crescator(l):
    """
    functie pentru tiparirea tuturor pachetelor intr un interval dat in ordine crescatoare a pretului
    """
    try:
        zi_inceput = int(input("ziua inceperii: "))
        luna_inceput = int(input("luna inceperii: "))
        an_inceput = int(input("anul inceperii: "))
        data_valida(zi_inceput,luna_inceput,an_inceput)
        zi_sfarsit = int(input("zi final: "))
        luna_sfarsit = int(input("luna final: "))
        an_sfarsit = int(input("an final: "))
        data_valida(zi_sfarsit,luna_sfarsit,an_sfarsit)
        l_prim = l
        l_prim.sort(key = get_pret)
        for i in interval_sejur(zi_inceput,luna_inceput,an_inceput , zi_sfarsit,luna_sfarsit,an_sfarsit,l):
            print(l_prim[i])
    except ValueError:
        print("Valori invalide")
    except Exception as ex:
        print(str(ex))
   

