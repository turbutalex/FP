import datetime
import unittest
from Validatori.ValidatorStudent import *
from Validatori.ValidatorNote import *
from Validatori.ValidatorProblema import *
from Errors.errors import *
from Repository.RepoStudent import *
from Repository.RepoCatalog import *
from Repository.RepoProbleme import *
from Business.ServiceStudent import *
from Business.ServiceCatalog import *
from Business.ServiceProbleme import *


class NoteTestCase(unittest.TestCase):
    def setUp(self):
        validator_student = Student_validator()
        validator_problem = Problem_validator()
        validator_note = Note_validator()
        std_repo = RepoStudent()
        prb_repo = RepoProblem()
        note_repo = RepoCatalog()
        student_srv = ServiceStudent(std_repo, validator_student)
        problem_srv = ServiceProblema(prb_repo, validator_problem)
        self.note_srv = ServiceNote(note_repo, validator_note)
        # std = Student(1, "Alex", 217)
        # prb = Problema(1, "Exercitiul 1", datetime.date(2021, 12, 12))
        self.note_srv.adauga_nota(1, "Alex", 217, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 7)

    def test_creeaza_nota(self):
        self.assertEqual(len(self.note_srv), 1)
        self.assertEqual(self.note_srv.get_all()[0].get_std(), Student(1, "Alex", 217))
        self.assertEqual(self.note_srv.get_all()[0].get_prb(), Problema(1, "Exercitiul 1", datetime.date(2021, 12, 12)))
        self.assertEqual(self.note_srv.get_all()[0].get_nota(), 7)

    def test_adauga_nota(self):
        self.assertEqual(len(self.note_srv), 1)
        self.note_srv.adauga_nota(2, "Dan", 217, 2, "Exercitiul 2", datetime.date(2021, 12, 12), 8)
        self.assertEqual(len(self.note_srv), 2)
        self.assertEqual(self.note_srv.get_all()[1].get_std(), Student(2, "Dan", 217))
        self.assertEqual(self.note_srv.get_all()[1].get_prb(), Problema(2, "Exercitiul 2", datetime.date(2021, 12, 12)))
        self.assertEqual(self.note_srv.get_all()[1].get_nota(), 8)

    def test_raport_lab_dupa_nume(self):
        self.note_srv.adauga_nota(2, "Vlad", 217, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 7)
        self.note_srv.adauga_nota(3, "Marc", 216, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 9)
        self.note_srv.adauga_nota(4, "Dan", 218, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 8)
        self.assertEqual(len(self.note_srv.raport_lab_dupa_nume(1)), 4)
        self.assertEqual(self.note_srv.raport_lab_dupa_nume(1)[0].get_std(), Student(1, "Alex", 217))
        self.assertEqual(self.note_srv.raport_lab_dupa_nume(1)[1].get_std(), Student(4, "Dan", 218))
        self.assertEqual(self.note_srv.raport_lab_dupa_nume(1)[2].get_std(), Student(3, "Marc", 216))
        self.assertEqual(self.note_srv.raport_lab_dupa_nume(1)[3].get_std(), Student(2, "Vlad", 217))

    def test_raport_lab_dupa_nota(self):
        self.note_srv.adauga_nota(2, "Vlad", 217, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 6)
        self.note_srv.adauga_nota(3, "Marc", 216, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 9)
        self.note_srv.adauga_nota(4, "Dan", 218, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 8)
        self.assertEqual(len(self.note_srv.raport_lab_dupa_nota(1)), 4)
        self.assertEqual(self.note_srv.raport_lab_dupa_nota(1)[0].get_std(), Student(2, "Vlad", 217))
        self.assertEqual(self.note_srv.raport_lab_dupa_nota(1)[1].get_std(), Student(1, "Alex", 217))
        self.assertEqual(self.note_srv.raport_lab_dupa_nota(1)[2].get_std(), Student(4, "Dan", 218))
        self.assertEqual(self.note_srv.raport_lab_dupa_nota(1)[3].get_std(), Student(3, "Marc", 216))

    def test_raport_corigenti(self):
        self.note_srv.adauga_nota(2, "Vlad", 217, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 6)
        self.note_srv.adauga_nota(3, "Marc", 216, 1, "Exercitiul 2", datetime.date(2021, 12, 12), 3)
        self.note_srv.adauga_nota(4, "Dan", 218, 1, "Exercitiul 1", datetime.date(2021, 12, 12), 2)
        self.assertEqual(len(self.note_srv.raport_corigenti()), 2)
        self.assertEqual(self.note_srv.raport_corigenti()[0], Student(3, "Marc", 216))
        self.assertEqual(self.note_srv.raport_corigenti()[1], Student(4, "Dan", 216))
        self.assertEqual(self.note_srv.medie_note(self.note_srv.raport_corigenti()[0]), 3.0)
        self.assertEqual(self.note_srv.medie_note(self.note_srv.raport_corigenti()[1]), 2.0)


if __name__ == '__main__':

    unittest.main()
