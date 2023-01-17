import datetime
def creeaza_pachet(zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret):
    """
    functie care creaza un pachet de calatorie
    input: zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit - intregi care reprezinta ziua,luna si anul pentru date de inceput respectiv sfarsit
           destinatie-string
           pret - intreg
    output: un pachet cu datele din input
    """
    return [ 
         datetime.date(an_inceput,luna_inceput,zi_inceput),
         datetime.date(an_sfarsit,luna_sfarsit,zi_sfarsit),
        destinatie,
        pret

    ]

def modifica_pachet(l,i,zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret):
    l[i][0] = datetime.date(an_inceput,luna_inceput,zi_inceput)
    l[i][1] = datetime.date(an_sfarsit,luna_sfarsit,zi_sfarsit)
    l[i][2] = destinatie
    l[i][3] = pret

def get_inceput(pachet):
    """
    functie care returneaza data de inceput a unui pachet
    params: pachet
    output: pachet["inceput"]
    """
    return pachet[0]

def get_sfarsit(pachet):
    """
    functie care returneaza data de sfarsit a unui pachet
    params: pachet
    output: pachet["sfarsit"]
    """
    return pachet[1]
def get_destinatie(pachet):
    """
    functie care returneaza destinatia unui pachet
    params: pachet
    output: pachet["destinatie"]
    """
    return pachet[2]

def get_pret(pachet):
    """
    functie care returneaza pretul unui pachet
    params: pachet
    output: pachet["pret"]
    """
    return pachet[3]

def adauga_pachet(pachet,l):
    """
    functie care adauga pachet in lista de pachete
    params: pachet,l
    output: -
    """
    l.append(pachet)

def data_valida(zi,luna,an):
    """
    functie care valideaza o data
    input : zi,luna,an
    output: nimic daca este valida
    raises: sir cu erorile aferente
    """
    luni = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    err = ""
    if an % 4 == 0 and (an%100 != 0 or an%400 == 0):
        luni[2] = 29
    if luna < 1 or luna >12:
        err += "luna invalida "
    if zi < 1 or (1<=luna<=12 and zi > luni[luna]):
        err += "zi invalida "
    if an < 2021:
        err += "an invalid "
    if len(err)>0:
        raise Exception(err)
    #return (1<=luna and luna <= 12 and zi>=1 and zi <= luni[luna])



def valideaza_pachet(pachet):
    """
    functie care valideaza datele dintr-un pachet de calatorie
    input: pachet
    output: nimic daca jocul este valid
    raises: date de inceput invalida-> data de inceput este inainte datei de azi
            data de sfarsit invalida -> data de sfarsit este inainte  de inceput
            destinatie invalida -> destinatia este vida
            pret invalid -> pretul este un numar negativ
    """
    err = ""
    if get_inceput(pachet)<datetime.date.today():
        err += "Data de inceput invalida "
    if get_sfarsit(pachet) < get_inceput(pachet):
        err += "Data de sfarsit invalida "
    if(get_destinatie(pachet) == ""):
        err += "Destinatie invalida "
    if get_pret(pachet) <0:
        err += "Pret invalid "
    if len(err)> 0 :
        raise Exception(err)

def interval_sejur(zi_inceput,luna_inceput,an_inceput , zi_sfarsit,luna_sfarsit,an_sfarsit,l):
    """
    functie de cautare pentru toate pachetele dintr un interval dat
    params: zi_inceput,luna_inceput,an_inceput , zi_sfarsit,luna_sfarsit,an_sfarsit,l
    output: array cu indexi pachetelor cautate
    """
    d1 = datetime.date(an_inceput,luna_inceput,zi_inceput)
    d2 = datetime.date(an_sfarsit,luna_sfarsit,zi_sfarsit)
    indexi = []
    index = 0
    for _pachet in l:
        if d1<=_pachet[0] and d2>=_pachet[1]:
            indexi.append(index)
        index += 1
    return indexi

def pachet_cu_sfarsit(zi_sfarsit,luna_sfarsit,an_sfarsit,l):
    """
    functie de cautare pentru toate pachetele cu o data de sfarsit data
    """
    d = datetime.date(an_sfarsit,luna_sfarsit,zi_sfarsit)
    indexi = []
    index = 0
    for _pachet in l:
        if d == _pachet[1]:
            indexi.append(index)
        index += 1
    return indexi

def nrOferte_cu_destinatie(destinatie,l):
    """
    functie care numara pachetele cu o anumita destinatie
    params: destinatie,l
    output: counter- nr pachetelor cu proprietatea
    """
    counter = 0
    for _pachet in l:
        if destinatie == get_destinatie(_pachet):
            counter = counter+1
    return counter

def medie_pret_destinatie(destinatie,l):
    """
    functie care calculeaza media de pret pentru o destinatie data
    params: destinatie,l
    output: media preturilor
    """
    counter = nrOferte_cu_destinatie(destinatie,l)
    avg = 0
    sum = 0
    for _pachet in l:
        if destinatie == get_destinatie(_pachet):
            sum += get_pret(_pachet)
    if(counter == 0):
        avg = sum/1
    else:
        avg = sum/counter
    return avg

def elimina_pret_mai_mare_si_destinatie(destinatie,pret,l):
    """
    functie care arata toate pachetele cu un pret mai mic decat cel dat si care nu contin destinatia data
    params: destinatie,pret,l
    output: array de indexi pt pachetele cu proprietatea dorita
    """
    indexi = []
    index = 0
    for _pachet in l:
        if pret>=_pachet[3] and _pachet[2] == destinatie:
            indexi.append(index)
        index +=1
    return indexi

def elimina_cu_luna(luna,l):
    """
    functie care arata toate pachetele cu exceptia celor din luna data
    params: luna , l
    output: array de indexi pt pachetele cu proprietatea dorita
    """
    indexi = []
    index = 0
    if int(luna)<10:
        luna = "0"+luna
    for _pachet in l:
        if luna != get_inceput(_pachet).strftime("%m") and luna != get_sfarsit(_pachet).strftime("%m"):
            indexi.append(index)
        index += 1
    return indexi

def sterge_cu_destinatie(destinatie,l):
    """
    functia de stergere a tuturor pachetelor cu o destinatie data
    params: destinatia, l
    output:-
    """
    index = 0
    for _pachet in l:
        if get_destinatie(_pachet) == destinatie:
            l.pop(index)
        index += 1

def sterge_cu_pret(pret,l):
    """
    functia de stergere a tuturor pachetelor cu un pret mai mare decat cel dat
    """
    index = 0
    for _pachet in l:
        if get_pret(_pachet) > pret:
            l.pop(index)
        index += 1

