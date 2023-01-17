import unittest
from Validatori.ValidatorProblema import *
from Errors.errors import *
from Repository.RepoStudent import *
from Repository.RepoProbleme import *
from Business.ServiceProbleme import *


class ProblemTestCases(unittest.TestCase):
    def setUp(self):
        validator_problem = Problem_validator()
        self.prb_repo = RepoProblem()
        self.prb_srv = ServiceProblema(self.prb_repo, validator_problem)
        prb_srv = self.prb_srv.adauga_prb("1", "Exercitiul 1", datetime.date(2021, 12, 12))

    def test_getteri_problema(self):
        self.assertEqual(self.prb_srv.get_all()[0].get_nr_prb(), "1")
        self.assertEqual(self.prb_srv.get_all()[0].get_descriere(), "Exercitiul 1")
        self.assertEqual(self.prb_srv.get_all()[0].get_deadline(), datetime.date(2021, 12, 12))

    def test_creeaza_problema_black_box(self):
        self.assertEqual(len(self.prb_srv), 1)
        self.assertRaises(ValidationError, self.prb_srv.adauga_prb, "1", "", datetime.date(2021, 12, 12))
        self.assertRaises(ValidationError, self.prb_srv.adauga_prb, "", "", datetime.date(2021, 12, 12))
        self.assertRaises(ValidationError, self.prb_srv.adauga_prb, "", "Ex 1", datetime.date(2021, 12, 12))
        self.assertRaises(ValueError, lambda: self.prb_srv.adauga_prb("1", "1", datetime.date(2021, 12, 40)))
        with self.assertRaises(ValueError):
            self.prb_srv.adauga_prb("1", "2", datetime.date(2021, 12, 40))
            self.prb_srv.adauga_prb("1","2",datetime.date(2021, 40, 40))
            self.prb_srv.adauga_prb("1", "2", datetime.date(2021, 23, 13))

    def test_adauga_problema(self):
        prb = Problema("2", "Exercitiul 2", datetime.date(2021, 12, 12))
        self.prb_srv.adauga_prb("2", "Exercitiul 2", datetime.date(2021, 12, 12))
        self.assertEqual(len(self.prb_srv), 2)
        self.assertEqual(self.prb_srv.get_all()[1], prb)

    def test_get_all(self):
        self.assertEqual(self.prb_srv.get_all(), self.prb_repo.get_all())
        self.assertEqual(self.prb_srv.get_repo(), self.prb_repo)

    def test_cauta_problema(self):
        self.assertEqual(self.prb_srv.get_all()[0], self.prb_srv.cauta_ex("1"))
        self.prb_srv.adauga_prb("2", "Exercitiul 2", datetime.date(2021, 12, 12))
        self.assertNotEqual(self.prb_srv.get_all()[1], self.prb_srv.cauta_ex("1"))

    def test_sterge_problema(self):
        self.assertEqual(len(self.prb_srv), 1)
        self.prb_srv.sterge_ex("1")
        self.assertEqual(len(self.prb_srv), 0)

    def test_modifica_problema(self):
        prb = Problema("1", "Exercitiul 1", datetime.date(2021, 12, 12))
        self.assertEqual(self.prb_srv.get_all()[0], prb)
        self.prb_srv.modifica("1", "2", "Exercitiul 2", datetime.date(2021, 12, 12))
        self.assertNotEqual(self.prb_srv.get_all()[0], prb)
        self.assertEqual(self.prb_srv.get_all()[0], Problema("2", "Exercitiul 2", datetime.date(2021, 12, 12)))


if __name__ == '__main__':
    print("Miau")
    unittest.main()
