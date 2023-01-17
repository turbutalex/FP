from pachet import *
def test_gettere_pachete():
    """
    functie de test pentru functiile de get
    """
    #pachet = app.creeaza_pachet(zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret)
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    assert (pachet["inceput"] == get_inceput(pachet))
    assert (pachet["sfarsit"] == get_sfarsit(pachet))
    assert (pachet["destinatie"] == get_destinatie(pachet))
    assert (pachet["pret"] == get_pret(pachet)) 

def test_creeaza_pachet():
    """
    functie de test pentru functia de creeaza_pachet
    """
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    assert(pachet["inceput"].strftime("%d") == "10")
    assert(pachet["inceput"].strftime("%m") == "02")
    assert(pachet["inceput"].strftime("%Y") == "2020")
    assert(pachet["sfarsit"].strftime("%d") == "15")
    assert(pachet["sfarsit"].strftime("%m") == "02")
    assert(pachet["sfarsit"].strftime("%Y") == "2020")
    assert(pachet["destinatie"] == "Galati")
    assert(pachet["pret"] == 400)

def test_modifica_pachet():
    """
    functia de test pentru modificarea unui pachet
    """
    l = []
    ul=[]
    pachet = creeaza_pachet(11,11,2021,12,11,2021,"Dej",500)
    adauga_pachet(pachet,l,ul)
    modifica_pachet(ul,l,0,12,11,2021,12,11,2021,"Galati",500)
    pachet = l[0]
    assert(pachet["inceput"].strftime("%d") == "12")
    assert(pachet["inceput"].strftime("%m") == "11")
    assert(pachet["inceput"].strftime("%Y") == "2021")
    assert(pachet["sfarsit"].strftime("%d") == "12")
    assert(pachet["sfarsit"].strftime("%m") == "11")
    assert(pachet["sfarsit"].strftime("%Y") == "2021")
    assert(pachet["destinatie"] == "Galati")
    assert(pachet["pret"] == 500)

def test_adauga_pachet():
    """
    functie de test pentru adaugarea unui pachet
    """
    l=[]
    ul = []
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    adauga_pachet(pachet,l,ul)
    assert(len(l)==1)

def test_data_valida():
    data_valida(10,10,2021)
    try:
        data_valida(0,11,2022)
    except Exception as ex:
        assert(str(ex) == "zi invalida ")
    try:
        data_valida(1,13,2022)
    except Exception as ex:
        assert(str(ex) == "luna invalida ")
    try:
        data_valida(10,10,2010)
    except Exception as ex:
        assert(str(ex) == "an invalid ")

def test_valideaza_pachet():
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    valideaza_pachet(pachet)
    try:
        inceput_invalid = creeaza_pachet(10,2,2020,15,11,2021,"Galati",400)
        valideaza_pachet(inceput_invalid)
    except Exception as ex:
        assert(str(ex) == "Data de inceput invalida ")
    try:
        sfarsit_invalid = creeaza_pachet(10,11,2021,9,11,2021,"Galati",400)
        valideaza_pachet(sfarsit_invalid)
    except Exception as ex:
        assert(str(ex) == "Data de sfarsit invalida ")
    try:
        destinatie_invalid = creeaza_pachet(10,11,2021,15,11,2021,"",400)
        valideaza_pachet(destinatie_invalid)
    except Exception as ex:
        assert(str(ex) == "Destinatie invalida ")
    try:
        pret_invalid = creeaza_pachet(10,11,2021,15,11,2021,"Galati",-400)
        valideaza_pachet(pret_invalid)
    except Exception as ex:
        assert(str(ex) == "Pret invalid ")

def test_nrOferte_cu_destinatie():
    """
    functie de test pentru functia nrOferte_cu_destinatie
    """
    l=[]
    ul = []
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    adauga_pachet(pachet,l,ul)
    assert(nrOferte_cu_destinatie("Galati",l) == 1)

def test_medie_pret_destinatie():
    """
    functie de test pentru functia medie_pret_destinatie
    """
    l=[]
    ul = []
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    adauga_pachet(pachet,l,ul)
    pachet = creeaza_pachet(11,3,2020,15,3,2020,"Galati",600)
    adauga_pachet(pachet,l,ul)
    assert(medie_pret_destinatie("Galati",l) == 500)

def test_elimina_pret_mai_mare_si_destinatie():
    """
    functie de test pentru elimina_pret_mai_mare_si_destinatie
    """
    l=[]
    ul =[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    assert(elimina_pret_mai_mare_si_destinatie("Galati", 500 , l) == [0])
    assert(elimina_pret_mai_mare_si_destinatie("Galati", 300 , l) == [])

def test_elimina_cu_luna():
    """
    functie de test pentru elimina_cu_luna
    """
    l= []
    ul=[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    assert(elimina_cu_luna("11",l) == [])
    assert(elimina_cu_luna("10",l) == [0])
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    assert(elimina_cu_luna("11",l) == [1])
    assert(elimina_cu_luna("7",l) == [0,1])

def test_sterge_cu_destinatie():
    """
    functia de test pentru stergere cu destinatie
    """
    l=[]
    ul=[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Dej",400)
    adauga_pachet(pachet,l,ul)
    sterge_cu_destinatie("Galati",l,ul)
    assert(len(l) == 1)
    sterge_cu_destinatie("Dej",l,ul)
    assert(len(l) == 0)

def test_sterge_cu_pret():
    """
    functia de test pentru stergere cu pret mai mare decat cel dat
    """
    l=[]
    ul=[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet,l,ul)
    sterge_cu_pret(450,l,ul)
    assert(len(l) == 1)
    sterge_cu_pret(300,l,ul)
    assert(len(l) == 0)

def test_interval_sejur():
    """
    functie de test pentru cautarea sejururilor dintr un interval dat
    """
    l=[]
    ul=[]
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet,l,ul)
    assert(interval_sejur(10,11,2021,13,12,2021,l) == [1])

def test_pachet_cu_sfarsit():
    """
    functie de test pentru pachet_cu_sfarsit
    """
    l=[]
    ul=[]
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet,l,ul)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet,l,ul)
    assert(pachet_cu_sfarsit(15,12,2021,l) == [0])
    
def test_durata():
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    assert(durata(pachet) == 6)
    pachet = creeaza_pachet(7,11,2021,15,12,2021,"Galati",400)
    assert(durata(pachet) == 39)

def test_undo_1():
    l=[]
    ul=[]
    pachet1 = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet1,l,ul)
    pachet11 = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    pachet2 = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet2,l,ul)
    pachet3 = creeaza_pachet(12,11,2021,12,11,2021,"Galati",1000)
    undo_list(ul,l)
    assert l == [pachet1]
    modifica_pachet(ul,l,0,12,11,2021,12,11,2021,"Galati",1000)
    assert l == [pachet3]
    undo_list(ul,l)
    assert l == [pachet11]

def run_tests():
    """
    functie pentru rularea tuturor testelor
    """
    test_gettere_pachete()
    test_creeaza_pachet()
    test_adauga_pachet()
    test_nrOferte_cu_destinatie()
    test_medie_pret_destinatie()
    test_valideaza_pachet()
    test_data_valida()
    test_elimina_pret_mai_mare_si_destinatie()
    test_elimina_cu_luna()
    test_modifica_pachet()
    test_sterge_cu_destinatie()
    test_sterge_cu_pret()
    test_interval_sejur()
    test_pachet_cu_sfarsit()
    test_durata()
    test_undo_1()
