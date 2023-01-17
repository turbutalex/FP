import os
from tests import *
from ui import *
from ui_nou import *
def start():
    """
    Functia care porneste aplicatia
    """
    l=[]
    ul=[]
    while True:
        cmd = input()
        if len(cmd)>7:
            cmd = cmd_split(cmd)
            while(cmd!=[]):
                if cmd[0] == "Add":
                    cmd.pop(0)
                    ui_add_nou(cmd,l,ul)
                elif cmd[0] == "Nr_Oferte":
                    cmd.pop(0)
                    ui_nr_oferte(cmd,l)
                elif cmd[0] == "Medie":
                    cmd.pop(0)
                    ui_medie_pret(cmd,l)
                elif cmd[0] == "Pachet_cu_destinatie":
                    cmd.pop(0)
                    ui_pachet_cu_destinatie(cmd,l)
        else:
            if cmd == "1.1":
                ui_adauga_pachet(l,ul)
            elif cmd == "1.2":
                ui_modifica_pachet(l,ul)
            elif cmd == "2.1":
                ui_sterge_cu_destinatie(l,ul)
            elif cmd == "2.2":
                ui_sterge_cu_durata_mai_mica(l,ul)
            elif cmd == "2.3":
                ui_sterge_cu_pret(l,ul)
            elif cmd == "3.1":
                ui_interval_sejur(l)
            elif cmd == "3.2":
                print_pachet_cu_destinatie(l)
            elif cmd == "3.3":
                ui_pachet_sfarsit(l)
            elif cmd == "4.1":
                print_nrOferte_cu_destinatie(l)
            elif cmd == "4.2":
                ui_interval_sejur_pret_crescator(l)
            elif cmd == "4.3":
                print_medie_pret_destinatie(l)
            elif cmd == "5.1":
                print_elimina_pret_mai_mare_si_destinatie(l)
            elif cmd == "5.2":
                ui_elimina_cu_luna(l)
            elif cmd == "undo":
                ui_undo_list(ul,l)
            elif cmd == "print":
                print_list(l,ul)
            elif cmd == "help":
                print_menu()
            elif cmd == "exit":
                return
            elif cmd == "clear":
                clear = lambda: os.system('clear')
                clear()
            else:
                print("Comanda necunoscuta tastati help pentru lista de comenzi")


#-----------------------------------------------------------------------------------------------------------------


run_tests()
start()

