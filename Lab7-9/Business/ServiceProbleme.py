import datetime
import string
import random
from Domain.Problema import *


class ServiceProblema:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def get_repo(self):
        return self.__repo

    def get_validator(self):
        return self.__validator

    def adauga_prb(self, nr_prb, descriere, deadline):
        """
        Functie pentru adaugarea unei probleme
        :param nr_prb:
        :param descriere:
        :param deadline:
        :return:
        """
        prb = Problema(nr_prb, descriere, deadline)
        self.__validator.validate(prb)
        self.__repo.add_prb(prb)

    def __len__(self):
        return len(self.__repo)

    def get_all(self):
        """
        Functie pentru a vedea toata lista
        :return:
        """
        return self.__repo.get_all()

    def cauta_ex(self, ex):
        """
        Functie pentru cautarea unui exercitiu
        :param ex:
        :return:
        """
        return self.__repo.cauta_ex(ex)

    def sterge_ex(self, ex):
        """
        Functie pentru stergerea unui exercitiu
        :param ex:
        :return:
        """
        self.__repo.sterge_ex(ex)

    def modifica(self, ex, nr_prb, descriere, deadline):
        """
        Functie pentru modificarea unei probleme
        :param ex:
        :return:
        """
        self.__repo.modifica(ex, nr_prb, descriere, deadline)

    def generator(self):
        chars = string.digits
        ex = ''
        for _ in range(2):
            ex += ''.join(random.choice(chars))
        descriere = ''
        chars = string.ascii_letters
        for _ in range(9):
            descriere += ''.join(random.choice(chars))
        date = datetime.date(2022, 11, 20)
        prb = Problema(ex, descriere, date)
        self.__repo.add_prb(prb)

