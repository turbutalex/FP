import datetime
import copy
def creeaza_pachet(zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret):
    """
    functie care creaza un pachet de calatorie
    input: zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit - intregi care reprezinta ziua,luna si anul pentru date de inceput respectiv sfarsit
           destinatie-string
           pret - intreg
    output: un pachet cu datele din input
    """
    return { 
        "inceput" : datetime.date(an_inceput,luna_inceput,zi_inceput),
        "sfarsit" : datetime.date(an_sfarsit,luna_sfarsit,zi_sfarsit),
        "destinatie":destinatie,
        "pret":pret
    }

def to_tuple(pachet):
    p1 = (get_inceput(pachet), get_sfarsit(pachet), get_destinatie(pachet), get_pret(pachet))
    """pachet_curent=creeaza_pachet((int(p1[0].strftime("%d")),
        int(p1[0].strftime("%m")),
        int(p1[0].strftime("%Y")),
        int(p1[1].strftime("%d")),
        int(p1[1].strftime("%m")),
        int(p1[1].strftime("%Y")),
        p1[2],
        p1[3])) """
    return p1

def to_pachet(p1):
    return creeaza_pachet(int(p1[0].strftime("%d")),int(p1[0].strftime("%m")),int(p1[0].strftime("%Y")),int(p1[1].strftime("%d")),int(p1[1].strftime("%m")),int(p1[1].strftime("%Y")),p1[2],p1[3])
    #return creeaza_pachet(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7])    

def adauga_undo(ul,l,i = -1):
    """if isinstance(l,tuple):
        l1 = []
        for _pachet in l:
            l1.append(to_pachet(_pachet)) 
        ul.append(l1)
    else:
        ul.append(l)"""
    if i==-1:
        ul.append(l[:])
    else:
        pachet = to_pachet(l)
        ul.append(pachet)
        ul.append(i)

   
        
    
def modifica_pachet(ul,l,i,zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret):
    """l1=[]
    zi_inc = int(get_inceput(l[i]).strftime("%d"))
    luna_inc = int(get_inceput(l[i]).strftime("%m"))
    an_inc = int(get_inceput(l[i]).strftime("%y"))
    zi_sf = int(get_sfarsit(l[i]).strftime("%d"))
    luna_sf = int(get_sfarsit(l[i]).strftime("%m"))
    an_sf = int(get_sfarsit(l[i]).strftime("%y"))
    pachet = creeaza_pachet(zi_inc,luna_inc,an_inc,zi_sf,luna_sf,an_sf,get_destinatie(l[i]),get_pret(l[i]))
    l1.append(pachet) 
    p = ()
    for _pachet in l:
        p = p + tuple(tuple(to_tuple(_pachet))) 
    print(p) """
    if ul != -1:
        zi_inc = int(get_inceput(l[i]).strftime("%d"))
        luna_inc = int(get_inceput(l[i]).strftime("%m"))
        an_inc = int(get_inceput(l[i]).strftime("%Y"))
        zi_sf = int(get_sfarsit(l[i]).strftime("%d"))
        luna_sf = int(get_sfarsit(l[i]).strftime("%m"))
        an_sf = int(get_sfarsit(l[i]).strftime("%Y"))
        pachet = creeaza_pachet(zi_inc,luna_inc,an_inc,zi_sf,luna_sf,an_sf,get_destinatie(l[i]),get_pret(l[i]))
        p = to_tuple(pachet)

        adauga_undo(ul,p,i)
    #updateUndoList(l,ul)
    #pachet = creeaza_pachet(zi_inceput,luna_inceput,an_inceput,zi_sfarsit,luna_sfarsit,an_sfarsit,destinatie,pret)
    #l.append(pachet)
    l[i]["inceput"] = datetime.date(an_inceput,luna_inceput,zi_inceput)
    l[i]["sfarsit"] = datetime.date(an_sfarsit,luna_sfarsit,zi_sfarsit)
    l[i]["destinatie"] = destinatie
    l[i]["pret"] = pret
     
    


def get_inceput(pachet):
    """
    functie care returneaza data de inceput a unui pachet
    params: pachet
    output: pachet["inceput"]
    """
    return pachet["inceput"]

def get_sfarsit(pachet):
    """
    functie care returneaza data de sfarsit a unui pachet
    params: pachet
    output: pachet["sfarsit"]
    """
    return pachet["sfarsit"]
def get_destinatie(pachet):
    """
    functie care returneaza destinatia unui pachet
    params: pachet
    output: pachet["destinatie"]
    """
    return pachet["destinatie"]

def get_pret(pachet):
    """
    functie care returneaza pretul unui pachet
    params: pachet
    output: pachet["pret"]
    """
    return pachet["pret"]

def adauga_pachet(pachet,l,ul):
    """
    functie care adauga pachet in lista de pachete
    params: pachet,l
    output: -
    """
    adauga_undo(ul,l,-1)
    #ul = updateUndoList(l,ul)
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
        if d1<=_pachet["inceput"] and d2>=_pachet["sfarsit"]:
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
        if d == _pachet["sfarsit"]:
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
        if pret>=_pachet["pret"] and _pachet["destinatie"] == destinatie:
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

def sterge_cu_destinatie(destinatie,l,ul):
    """
    functia de stergere a tuturor pachetelor cu o destinatie data
    params: destinatia, l
    output:-
    """
    adauga_undo(ul,l,-1)
    #ul = updateUndoList(l,ul)
    index = 0
    for _pachet in l:
        if get_destinatie(_pachet) == destinatie:
            l.pop(index)
        index += 1

def sterge_cu_pret(pret,l,ul):
    """
    functia de stergere a tuturor pachetelor cu un pret mai mare decat cel dat
    """
    adauga_undo(ul,l,-1)
    #ul = updateUndoList(l,ul)
    index = 0
    for _pachet in l:
        if get_pret(_pachet) > pret:
            l.pop(index)
        index += 1
def durata(pachet):
    """
    functie care returneaza durata unui sejur
    """
    luni = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dur = 0
    zi_inc = int(get_inceput(pachet).strftime("%d"))
    luna_inc = int(get_inceput(pachet).strftime("%m"))
    an_inc = int(get_inceput(pachet).strftime("%y"))
    zi_sf = int(get_sfarsit(pachet).strftime("%d"))
    luna_sf = int(get_sfarsit(pachet).strftime("%m"))
    an_sf = int(get_sfarsit(pachet).strftime("%y"))
    if an_sf > an_inc:
        dur += zi_sf
        dur += luni[luna_inc]-zi_inc + 1
    elif luna_sf > luna_inc:
        dur += zi_sf
        dur += luni[luna_inc]-zi_inc + 1
    else:
        return (zi_sf - zi_inc + 1)
    return dur


def sterge_cu_durata_mai_mica(dur,l,ul):
    """
    functia de stergere a pachetelor cu o durata mai mica decat cea data
    """
    adauga_undo(ul,l,-1)
    #ul = updateUndoList(l,ul)
    index = 0
    for _pachet in l:
        if(durata(_pachet) < dur):
            l.pop(index)
    index += 1

def undo_list(ul,l):
    """
    functie pt undo
    """
    try:
        if ul[len(ul)-1] != []:
            if type(ul[len(ul)-1]) == int:
                i = ul[len(ul)-1]
                ul.pop(len(ul)-1)
                #print(l[0])
                #print(ul[len(ul)-1])
                zi_inc = int(get_inceput(ul[len(ul)-1]).strftime("%d"))
                luna_inc = int(get_inceput(ul[len(ul)-1]).strftime("%m"))
                an_inc = int(get_inceput(ul[len(ul)-1]).strftime("%Y"))
                zi_sf = int(get_sfarsit(ul[len(ul)-1]).strftime("%d"))
                luna_sf = int(get_sfarsit(ul[len(ul)-1]).strftime("%m"))
                an_sf = int(get_sfarsit(ul[len(ul)-1]).strftime("%Y"))
                destinatie = get_destinatie(ul[len(ul)-1])
                pret = get_pret(ul[len(ul)-1])
                modifica_pachet(-1,l,i,zi_inc,luna_inc,an_inc,zi_sf,luna_sf,an_sf,destinatie,pret)
                #l.extend(ul[len(ul)-1])
            else:
                l.clear()
                l.extend(ul[len(ul)-1])

        else:
            l.clear()
        ul.pop(len(ul)-1)
    except IndexError:
        print("Nothing to undo")

