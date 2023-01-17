import os
from tests2 import *
from ui2 import *
def start():
    """
    Functia care porneste aplicatia
    """
    l=[]
    while True:
        cmd = input()
        if cmd == "1.1":
            ui_adauga_pachet(l)
        elif cmd == "1.2":
            ui_modifica_pachet(l)
        elif cmd == "2.1":
            ui_sterge_cu_destinatie(l)
        elif cmd == "2.3":
            ui_sterge_cu_pret(l)
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
        elif cmd == "help":
            print_menu()
        elif cmd == "exit":
            return
        elif cmd == "clear":
            clear = lambda: os.system('clear')
            clear()
        elif cmd == "print":
            ui_print_list(l)
        else:
            print("Comanda necunoscuta tastati help pentru lista de comenzi")


#-----------------------------------------------------------------------------------------------------------------




run_tests()
start()
