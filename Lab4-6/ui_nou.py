from pachet import *
def cmd_split(cmd):
    return cmd.split()

def ui_add_nou(cmd,l,ul):
    try:
        zi_inceput = int(cmd[0])
        cmd.pop(0)
        luna_inceput = int(cmd[0])
        cmd.pop(0)
        an_inceput = int(cmd[0])
        cmd.pop(0)
        data_valida(zi_inceput,luna_inceput,an_inceput)
        zi_sfarsit = int(cmd[0])
        cmd.pop(0)
        luna_sfarsit = int(cmd[0])
        cmd.pop(0)
        an_sfarsit = int(cmd[0])
        cmd.pop(0)
        data_valida(zi_sfarsit,luna_sfarsit,an_sfarsit)
        destinatie = cmd[0]
        cmd.pop(0)
        pret = int(cmd[0])
        cmd.pop(0)
        pachet = creeaza_pachet(zi_inceput,luna_inceput, an_inceput, zi_sfarsit, luna_sfarsit, an_sfarsit , destinatie, pret)
        valideaza_pachet(pachet)
        adauga_pachet(pachet,l,ul)
        print("Pachet adaugat cu succes")
    except ValueError:
        print("Invaid values")
    except Exception as ex:
        print(str(ex))

def ui_nr_oferte(cmd,l):
    destinatie = cmd[0]
    cmd.pop(0)
    print(nrOferte_cu_destinatie(destinatie,l))

def ui_pachet_cu_destinatie(cmd,l):
    destinatie = cmd[0]
    cmd.pop(0)
    try:
        pret = int(cmd[0])
        cmd.pop(0)
    except ValueError:
        print("Valoare inalida")
    for _pachet in l:
        if destinatie == get_destinatie(_pachet) and pret >= get_pret(_pachet):
            print(_pachet)

def ui_medie_pret(cmd,l):
    destinatie = cmd[0]
    cmd.pop(0)
    print(medie_pret_destinatie(destinatie,l))
