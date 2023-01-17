from pachet2 import *
def test_gettere_pachete():
    """
    functie de test pentru functiile de get
    """
    #pachet = app.creeaza_pachet(zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret)
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    assert (pachet[0] == get_inceput(pachet))
    assert (pachet[1] == get_sfarsit(pachet))
    assert (pachet[2] == get_destinatie(pachet))
    assert (pachet[3] == get_pret(pachet)) 

def test_creeaza_pachet():
    """
    functie de test pentru functia de creeaza_pachet
    """
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    assert(pachet[0].strftime("%d") == "10")
    assert(pachet[0].strftime("%m") == "02")
    assert(pachet[0].strftime("%Y") == "2020")
    assert(pachet[1].strftime("%d") == "15")
    assert(pachet[1].strftime("%m") == "02")
    assert(pachet[1].strftime("%Y") == "2020")
    assert(pachet[2] == "Galati")
    assert(pachet[3] == 400)

def test_modifica_pachet():
    """
    functia de test pentru modificarea unui pachet
    """
    l = []
    pachet = creeaza_pachet(11,11,2021,12,11,2021,"Dej",500)
    adauga_pachet(pachet,l)
    modifica_pachet(l,0,12,11,2021,12,11,2021,"Galati",500)
    pachet = l[0]
    assert(pachet[0].strftime("%d") == "12")
    assert(pachet[0].strftime("%m") == "11")
    assert(pachet[0].strftime("%Y") == "2021")
    assert(pachet[1].strftime("%d") == "12")
    assert(pachet[1].strftime("%m") == "11")
    assert(pachet[1].strftime("%Y") == "2021")
    assert(pachet[2] == "Galati")
    assert(pachet[3] == 500)

def test_adauga_pachet():
    """
    functie de test pentru adaugarea unui pachet
    """
    l=[]
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    adauga_pachet(pachet,l)
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
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    adauga_pachet(pachet,l)
    assert(nrOferte_cu_destinatie("Galati",l) == 1)

def test_medie_pret_destinatie():
    """
    functie de test pentru functia medie_pret_destinatie
    """
    l=[]
    pachet = creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    adauga_pachet(pachet,l)
    pachet = creeaza_pachet(11,3,2020,15,3,2020,"Galati",600)
    adauga_pachet(pachet,l)
    assert(medie_pret_destinatie("Galati",l) == 500)

def test_elimina_pret_mai_mare_si_destinatie():
    """
    functie de test pentru elimina_pret_mai_mare_si_destinatie
    """
    l=[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l)
    assert(elimina_pret_mai_mare_si_destinatie("Galati", 500 , l) == [0])
    assert(elimina_pret_mai_mare_si_destinatie("Galati", 300 , l) == [])

def test_elimina_cu_luna():
    """
    functie de test pentru elimina_cu_luna
    """
    l= []
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l)
    assert(elimina_cu_luna("11",l) == [])
    assert(elimina_cu_luna("10",l) == [0])
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet,l)
    assert(elimina_cu_luna("11",l) == [1])
    assert(elimina_cu_luna("7",l) == [0,1])

def test_sterge_cu_destinatie():
    """
    functia de test pentru stergere cu destinatie
    """
    l=[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Dej",400)
    adauga_pachet(pachet,l)
    sterge_cu_destinatie("Galati",l)
    assert(len(l) == 1)
    sterge_cu_destinatie("Dej",l)
    assert(len(l) == 0)

def test_sterge_cu_pret():
    """
    functia de test pentru stergere cu pret mai mare decat cel dat
    """
    l=[]
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",400)
    adauga_pachet(pachet,l)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet,l)
    sterge_cu_pret(450,l)
    assert(len(l) == 1)
    sterge_cu_pret(300,l)
    assert(len(l) == 0)

def test_interval_sejur():
    """
    functie de test pentru cautarea sejururilor dintr un interval dat
    """
    l=[]
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet,l)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet,l)
    assert(interval_sejur(10,11,2021,13,12,2021,l) == [1])

def test_pachet_cu_sfarsit():
    """
    functie de test pentru pachet_cu_sfarsit
    """
    l=[]
    pachet = creeaza_pachet(10,12,2021,15,12,2021,"Galati",400)
    adauga_pachet(pachet,l)
    pachet = creeaza_pachet(10,11,2021,15,11,2021,"Galati",500)
    adauga_pachet(pachet,l)
    assert(pachet_cu_sfarsit(15,12,2021,l) == [0])
    

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
