import unittest
from Domain.student import Student
from Repository.RepoStudent import RepoStudent
from Validatori.ValidatorStudent import Student_validator
from Errors.errors import ValidationError
from Business.ServiceStudent import ServiceStudent


class StudentTestCases(unittest.TestCase):
    def setUp(self):
        validator_student = Student_validator()
        self.std_repo = RepoStudent()
        self.std_srv = ServiceStudent(self.std_repo, validator_student)
        self.std_srv.adauga_stud(1, "Alex", 217)

    def test_creeaza_student(self):
        self.assertEqual(len(self.std_srv), 1)
        self.assertEqual(self.std_srv.get_all()[0].get_id(), 1)
        self.assertEqual(self.std_srv.get_all()[0].get_nume(), "Alex")
        self.assertEqual(self.std_srv.get_all()[0].get_grupa(), 217)
        with self.assertRaises(ValidationError):
            self.std_srv.adauga_stud(1, "Dan", 217)

    def test_adauga_student(self):
        self.assertEqual(len(self.std_srv), 1)
        std = Student(2, "Dan", 217)
        self.std_srv.adauga_stud(2, "Dan", 217)
        self.assertEqual(len(self.std_srv), 2)
        self.assertEqual(self.std_srv.get_all()[1], std)

    def test_get_all(self):
        self.assertEqual(self.std_srv.get_all(), self.std_repo.get_all())
        self.assertEqual(self.std_srv.get_repo(), self.std_repo)

    def test_cauta_student(self):
        self.assertEqual(self.std_srv.cauta_id(1), self.std_repo.get_all()[0])
        self.std_srv.adauga_stud(2, "Dan", 217)
        self.assertNotEqual(self.std_srv.cauta_id(1), self.std_srv.get_all()[1])

    def test_sterge_student(self):
        self.std_srv.adauga_stud(2, "Dan", 217)
        self.assertEqual(len(self.std_srv), 2)
        self.std_srv.sterge_id(1)
        self.assertEqual(len(self.std_srv), 1)
        self.assertEqual(self.std_srv.get_all()[0], Student(2, "Dan", 217))

    def test_modifica_student(self):
        self.std_srv.adauga_stud(2, "Dan", 217)
        self.assertEqual(self.std_srv.get_all()[0], Student(1, "Alex", 217))
        self.std_srv.modifica(1, "Marc", 216)
        self.assertEqual(self.std_srv.get_all()[1], Student(2, "Dan", 217))
        self.assertEqual(self.std_srv.get_all()[0].get_nume(), "Marc")
        self.assertEqual(self.std_srv.get_all()[0].get_grupa(), 216)


if __name__ == '__main__':
    print("Miau")
    unittest.main()
