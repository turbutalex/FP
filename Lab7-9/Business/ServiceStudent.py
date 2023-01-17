import string
import random
from Domain.student import *


class ServiceStudent:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def get_repo(self):
        return self.__repo

    def get_validator(self):
        return self.__validator

    def adauga_stud(self, id, nume, grupa):
        """
        Functie pentru adaugarea unui student
        :param id:
        :param nume:
        :param grupa:
        :return:
        """
        std = Student(id, nume, grupa)
        self.__validator.validate(std)
        self.__repo.add_std(std)

    def __len__(self):
        return len(self.__repo)

    def get_all(self):
        return self.__repo.get_all()

    def cauta_id(self, id):
        """
        Functie pentru cautarea unui student dupa id
        :param id:
        :return:
        """
        return self.__repo.cauta_id(id)

    def sterge_id(self, id):
        """
        Functie pentru stergerea unui student dupa id
        :param id:
        :return:
        """
        self.__repo.sterge_id(id)

    def modifica(self, id_std, nume, grupa):
        """
        Functie pentru modificarea unui student
        :param id_std:
        :param nume:
        :param grupa:
        :return:
        """
        self.__repo.modifica(id_std, nume, grupa)

    def filtru_prefix(self, filtru):
        """
        Functie de filtrare in service
        :param filtru:
        :return:
        """
        return self.__repo.filtru_prefix(filtru)

    def generator(self):
        chars = string.digits
        id = ''
        for _ in range(2):
            id += ''.join(random.choice(chars))
        id = int(id)
        name = ''
        chars = string.ascii_letters
        for _ in range(7):
            name += ''.join(random.choice(chars))
        grupa = ''
        chars = string.digits
        for _ in range(4):
            grupa += ''.join(random.choice(chars))
        grupa = int(grupa)
        std = Student(id, name, grupa)
        self.__repo.add_std(std)





