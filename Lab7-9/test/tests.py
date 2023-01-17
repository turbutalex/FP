from Validatori.ValidatorStudent import *
from Validatori.ValidatorNote import *
from Validatori.ValidatorProblema import *
# from Errors.errors import *
from Repository.RepoStudent import *
from Repository.RepoCatalog import *
from Repository.RepoProbleme import *
from Business.ServiceStudent import *
from Business.ServiceCatalog import *
from Business.ServiceProbleme import *


class Test:

    def test_creeaza_problema(self):
        prb = Problema("7_2", "Proiect pe clase", datetime.date(2022, 11, 12))
        assert (prb.get_nr_prb() == "7_2")
        assert (prb.get_descriere() == "Proiect pe clase")
        assert (prb.get_deadline() == datetime.date(2022, 11, 12))

    def test_creeaza_student(self):
        student = Student(279, "Alex", 217)
        assert student.get_id() == 279
        assert student.get_nume() == "Alex"
        assert student.get_grupa() == 217

    def test_valideaza_problema(self):
        prb = Problema("7_2", "Proiect pe clase", datetime.date(2022, 11, 12))
        prb_validator = Problem_validator()
        prb_validator.validate(prb)
        try:
            prb_invalid = Problema("", "", datetime.date(2020, 11, 12))
            prb_validator.validate(prb_invalid)
        except ValidationError as ve:
            assert (str(ve) == "Exercitiu invalid Descriere invalida Data invalida ")

    def test_valideaza_student(self):
        student = Student(279, "Alex", 217)
        std_validator = Student_validator()
        std_validator.validate(student)
        student_invalid = Student(0, "", 0)
        try:
            std_validator.validate(student_invalid)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "Id invalid Nume invalid Grupa invalida ")

    def test_adauga_problema(self):
        prb = Problema("7_2", "Proiect pe clase", datetime.date(2022, 11, 12))
        prb_repo = RepoProblem()
        assert (prb_repo.__len__() == 0)
        prb_repo.add_prb(prb)
        assert (prb_repo.__len__() == 1)

    def test_adauga_student(self):
        student = Student(279, "Alex", 217)
        std_repo = RepoStudent()
        assert (std_repo.__len__() == 0)
        std_repo.add_std(student)
        assert std_repo.__len__() == 1

    def test_adauga_nota(self):
        prb = Problema("7_2", "Proiect pe clase", datetime.date(2022, 11, 12))
        student = Student(279, "Alex", 217)
        nota = Nota(student, prb, 7)
        note_repo = RepoCatalog()
        assert (len(note_repo) == 0)
        note_repo.asignare_nota(nota)
        assert (len(note_repo) == 1)



    def test_adauga_problema_service(self):
        prb_repo = RepoProblem()
        prb_validator = Problem_validator()
        problem_srv = ServiceProblema(prb_repo, prb_validator)
        assert problem_srv.__len__() == 0
        problem_srv.adauga_prb("7_2", "Proiect pe clase", datetime.date(2022, 11, 12))
        assert problem_srv.__len__() == 1
        try:
            problem_srv.adauga_prb("", "", datetime.date(2020, 11, 12))
            assert False
        except ValidationError as ve:
            assert (str(ve) == "Exercitiu invalid Descriere invalida Data invalida ")

    def test_modifica_student(self):
        std_repo = RepoStudent()
        std_validator = Student_validator()
        std_srv = ServiceStudent(std_repo, std_validator)
        assert std_srv.__len__() == 0
        std_srv.adauga_stud(1, "Alex", 217)
        std_srv.modifica(1, "Gabi", 216)
        assert std_srv.get_repo().get_repo()[0].get_nume() == "Gabi"
        assert std_srv.get_repo().get_repo()[0].get_grupa() == 216

    def test_modifica_problema(self):
        prb_repo = RepoProblem()
        prb_validator = Problem_validator()
        problem_srv = ServiceProblema(prb_repo, prb_validator)
        problem_srv.adauga_prb("7_2", "Proiect pe clase", datetime.date(2022, 11, 12))
        assert problem_srv.__len__() == 1
        problem_srv.modifica("7_2", "8_2", "Nu", datetime.date(2022, 11, 12))
        assert (problem_srv.get_repo().get_repo()[0].get_nr_prb() == "8_2")
        assert (problem_srv.get_repo().get_repo()[0].get_descriere() == "Nu")
        assert (problem_srv.get_repo().get_repo()[0].get_deadline() == datetime.date(2022, 11, 12))

    def test_filtru(self):
        std_repo = RepoStudent()
        student = Student(1, "Alex", 217)
        std_validator = Student_validator()
        std_srv = ServiceStudent(std_repo, std_validator)
        std_srv.adauga_stud(1, "Alex", 217)
        for std in std_srv.filtru_prefix("Al"):
            assert (std == student)

    def test_adauga_nota_service(self):
        note_repo = RepoCatalog()
        note_validator = Note_validator()
        srv_note = ServiceNote(note_repo, note_validator)
        assert (len(srv_note) == 0)
        srv_note.adauga_nota(1, "Alex", 217, "7_2", "Proiect pe clase", datetime.date(2022, 11, 12), 7)
        assert (len(srv_note) == 1)

    def test_raport_lab_dupa_nume(self):
        note_repo = RepoCatalog()
        note_validator = Note_validator()
        srv_note = ServiceNote(note_repo, note_validator)
        srv_note.adauga_nota(1, "Alex", 217, "7_2", "Proiect pe clase", datetime.date(2022, 11, 12), 7)
        srv_note.adauga_nota(2, "Vlad", 217, "7_2", "Proiect pe clase", datetime.date(2022, 11, 12), 7)
        srv_note.adauga_nota(3, "Dani", 217, "7_2", "Proiect pe clase", datetime.date(2022, 11, 12), 7)
        assert(srv_note.raport_lab_dupa_nume("7_2")[1].get_std().get_nume() == "Dani")

    def test_raport_corigenti(self):
        note_repo = RepoCatalog()
        note_validator = Note_validator()
        srv_note = ServiceNote(note_repo, note_validator)
        srv_note.adauga_nota(1, "Alex", 217, "7_6", "Proiect pe clase", datetime.date(2022, 11, 12), 2)
        srv_note.adauga_nota(2, "Dani", 217, "7_2", "Proiect pe clase", datetime.date(2022, 11, 12), 7)
        assert(srv_note.raport_corigenti()[0].get_nume() == "Alex")
        assert(len(srv_note.raport_corigenti()) == 1)


    def run_tests(self):
        print("Started testing")
        self.test_creeaza_student()
        self.test_creeaza_problema()
        self.test_valideaza_problema()
        self.test_valideaza_student()
        self.test_adauga_problema()
        self.test_adauga_student()
        self.test_adauga_problema_service()
        self.test_modifica_problema()
        self.test_modifica_student()
        self.test_filtru()
        self.test_adauga_nota()
        self.test_adauga_nota_service()
        # self.test_raport_corigenti()
        # self.test_raport_lab_dupa_nume()
        print("Finished testing")
