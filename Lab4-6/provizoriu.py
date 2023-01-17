import app
def test_gettere_pachete():
    """
    functie de test pentru functiile de get
    """
    #pachet = app.creeaza_pachet(zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret)
    pachet = app.creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    assert (pachet["inceput"] == app.get_inceput(pachet))
    assert (pachet["sfarsit"] == app.get_sfarsit(pachet))
    assert (pachet["destinatie"] == app.get_destinatie(pachet))
    assert (pachet["pret"] == app.get_pret) 

def test_creeaza_pachet():
    """
    functie de test pentru functia de creeaza_pachet
    """
    pachet = app.creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    assert(pachet["inceput"].strftime("%d") == "10")
    assert(pachet["inceput"].strftime("%m") == "2")
    assert(pachet["inceput"].strftime("%Y") == "2020")
    assert(pachet["sfarsit"].strftime("%d") == "15")
    assert(pachet["sfarsit"].strftime("%m") == "2")
    assert(pachet["sfarsit"].strftime("%Y") == "2020")
    assert(pachet["destinatie"] == "Galati")
    assert(pachet["pret"] == 400)

def test_adauga_pachet():
    """
    functie de test pentru adaugarea unui pachet
    """
    l=[]
    pachet = app.creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    app.adauga_pachet(pachet,l)
    assert(len(l) == 1)

def test_data_valida():
    pass

def test_valideaza_pachet():
    pachet = app.creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    app.valideaza_pachet(pachet)

def test_nrOferte_cu_destinatie():
    """
    functie de test pentru functia nrOferte_cu_destinatie
    """
    l=[]
    pachet = app.creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    app.adauga_pachet(pachet,l)
    assert(app.nrOferte_cu_destinatie("Galati",l) == 1)

def test_medie_pret_destinatie():
    """
    functie de test pentru functia medie_pret_destinatie
    """
    l=[]
    pachet = app.creeaza_pachet(10,2,2020,15,2,2020,"Galati",400)
    app.adauga_pachet(pachet,l)
    pachet = app.creeaza_pachet(11,3,2020,15,3,2020,"Galati",600)
    app.adauga_pachet(pachet,l)
    assert(app.medie_pret_destinatie("Galati",l) == 500)


def run_tests():
    test_gettere_pachete()
    test_creeaza_pachet()
    test_adauga_pachet()
    test_nrOferte_cu_destinatie()
    test_medie_pret_destinatie()

run_tests()
