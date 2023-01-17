import datetime
from Errors.errors import *
from Domain.student import *


class Console:

    def __init__(self, srv_stud, srv_prb, srv_nota):
        self.__srv_stud = srv_stud
        self.__srv_prb = srv_prb
        self.__srv_nota = srv_nota

    def ui_print_menu(self):
        print("Type add_prb to add a problem to the repo")
        print("Type mod_prb to modify a problem")
        print("Type sterge_ex to delete a problem")
        print("Type print_prb to print all problems")
        print("Type add_std to add a student to the repo")
        print("Type mod_std to modify a student")
        print("Type sterge_id to delete a student")
        print("Type cauta_std_id to search for a student with an ID given")
        print("Type print_std to print all students")
        print("Type filtrare to show all student whose name begin with a string")
        print("Type notare to assign a grade to a student")
        print("Type print_note to show all the graded students")
        print("Type exit to close the project")

    def ui_random(self):
        self.__srv_stud.generator()

    def ui_random_prb(self):
        self.__srv_prb.generator()

    def ui_random_nota(self):
        self.__srv_nota.generator()

    def ui_adauga_problema(self):
        """
        Functie de ui pentru adaugarea unei probleme
        :return:
        """
        try:
            nr_prb = input("Exercitiul:")
            descriere = input("Descrierea:")
            deadline = datetime.date(2021, int(input("Luna:")), int(input("Ziua")))
            self.__srv_prb.adauga_prb(nr_prb, descriere, deadline)
        except ValidationError as ve:
            print(str(ve))
        except ValueError:
            print("Invalid input")

    def ui_modifica_problema(self):
        """
        Functie de ui pentru modificarea unei probleme
        :return:
        """
        try:
            ex = input("Problema ce urmeaza sa fie schimbata:")
            nr_prb = input("Exercitiul:")
            descriere = input("Descrierea:")
            deadline = datetime.date(2021, int(input("Luna:")), int(input("Ziua")))
            self.__srv_prb.modifica(ex, nr_prb, descriere, deadline)
        except ValidationError as ve:
            print(str(ve))

    def ui_adauga_nota(self):
        """
        Functie de ui pentru notarea unui student la o problema
        :return:
        """
        try:
            id = int(input("Id:"))
            std = self.__srv_stud.cauta_id(id)
        except ValueError:
            print("Id invalid")
            return
        try:
            nr_prb = input("Exercitiul:")
            prb = self.__srv_prb.cauta_ex(nr_prb)
        except ValueError:
            print("Exercitiu invalid")
            return
        try:
            nota = int(input("Nota:"))
        except ValueError:
            print("Valoare invalida")
            return
        try:
            self.__srv_nota.adauga_nota(std.get_id(), std.get_nume(), std.get_grupa(), prb.get_nr_prb(), prb.get_descriere(), prb.get_deadline(), nota)
            print("Studentul a fost notat cu succes")
        except ValidationError as ve:
            print(str(ve))
        except AttributeError:
            print("Studentul sau exercitiul nu a fost gasit")


    def ui_adauga_student(self):
        """
        Functie de ui pentru adaugarea unui student
        :return:
        """
        try:
            id = int(input("Id:"))
            nume = input("Nume:")
            grupa = int(input("Grupa:"))
            self.__srv_stud.adauga_stud(id, nume, grupa)
            print("Student adaugat cu succes")
        except ValidationError as ve:
            print(str(ve))
        except ValueError:
            print("Invalid input")

    def ui_modifica_student(self):
        """
        Functie de ui modificarea unui student
        :return:
        """
        try:
            id_std = int(input("Id:"))
            nume = input("Nume:")
            grupa = int(input("Grupa:"))
            self.__srv_stud.modifica(id_std, nume, grupa)
            print("Student modificat cu succes")
        except ValidationError as ve:
            print(str(ve))
        except ValueError:
            print("Invalid input")

    def ui_print_problem(self):
        """
        Functia de ui pentru afisarea unei probleme
        :return:
        """
        for prb in self.__srv_prb.get_all():
            print(prb)

    def ui_print_student(self):
        """
        Functie de ui pentru afisarea unui student
        :return:
        """
        for std in self.__srv_stud.get_all():
            print(std)

    def ui_print_note(self):
        """
        Functie de ui pentru afisarea notelor
        :return:
        """
        for _nota in self.__srv_nota.get_all():
            print(_nota)

    def ui_print_std_id(self):
        """
        Functie de ui pentru afisarea unui student cu id dat
        :return:
        """
        try:
            id = int(input("Id:"))
            print(self.__srv_stud.cauta_id(id))
        except ValueError:
            print("Id invalid")

    def ui_print_prb_ex(self):
        """
        Functie de ui pentru afisarea unei probleme cu ex dat
        :return:
        """
        try:
            nr_prb = input("Exercitiul:")
            print(self.__srv_prb.cauta_ex(nr_prb))
        except ValueError:
            print("Exercitiu invalid")

    def ui_sterge_id(self):
        """
        Functie de stergere a unui id
        :return:
        """
        try:
            id = int(input("Id:"))
            self.__srv_stud.sterge_id(id)
        except ValueError:
            print("Invalid Id")

    def ui_sterge_ex(self):
        """
        Functie de ui pentru stergerea unui ex
        :return:
        """
        try:
            ex = input("Exercitiul:")
            self.__srv_prb.sterge_ex(ex)
        except ValueError:
            print("Exercitiu invalid")

    def print_filtru(self):
        """
        Functie de ui pentru afisarea sirului filtrat dupa prefix
        :return:
        """
        filtru = input("Prefixul dupa care vom filtra:")
        for std in self.__srv_stud.filtru_prefix(filtru):
            print(std)

    def ui_raport_lab_dupa_nume(self):
        try:
            ex = input("Exercitiul: ")
            for _nota in self.__srv_nota.raport_lab_dupa_nume(ex):
                print(_nota)
        except ValueError:
            print("Invalid input")

    def ui_raport_corigenti(self):
        for _nota in self.__srv_nota.raport_corigenti():
            print(f"{_nota.get_nume()} {self.__srv_nota.medie_note(_nota)}")

    def ui_raport_lab_dupa_participare(self):
        for _nota in self.__srv_nota.raport_lab_dupa_participare():
            print(f"Exercitiul {_nota.get_prb().get_nr_prb()} {self.__srv_nota.medie_note_lab(_nota.get_prb().get_nr_prb())}")

    def run(self):
        while True:
            cmd = input(": ")
            if cmd == "exit":
                return
            elif cmd == "":
                continue
            elif cmd == "help":
                self.ui_print_menu()
            elif cmd == "print_prb":
                self.ui_print_problem()
            elif cmd == "add_prb":
                self.ui_adauga_problema()
            elif cmd == "mod_prb":
                self.ui_modifica_problema()
            elif cmd == "add_std":
                self.ui_adauga_student()
            elif cmd == "mod_std":
                self.ui_modifica_student()
            elif cmd == "print_std":
                self.ui_print_student()
            elif cmd == "cauta_std_id":
                self.ui_print_std_id()
            elif cmd == "sterge_id":
                self.ui_sterge_id()
            elif cmd == "sterge_ex":
                self.ui_sterge_ex()
            elif cmd == "filtru":
                self.print_filtru()
            elif cmd == "notare":
                self.ui_adauga_nota()
            elif cmd == "print_note":
                self.ui_print_note()
            elif cmd == "raport_lab_nume":
                self.ui_raport_lab_dupa_nume()
            elif cmd == "raport_corigenti":
                self.ui_raport_corigenti()
            elif cmd == "raport_participare":
                self.ui_raport_lab_dupa_participare()
            elif cmd == "random_std":
                self.ui_random()
            elif cmd == "random_prb":
                self.ui_random_prb()
            elif cmd == "random_nota":
                self.ui_random_nota()
            elif cmd == "print_ex":
                self.ui_print_prb_ex()
            else:
                print("Comanda necunoscuta tastati help pentru lista de comentzi")

