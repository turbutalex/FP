from math import ceil
from Domain.student import Student
from Errors.errors import *


class RepoStudent:
    def __init__(self):
        self._std_repo = []

    def get_repo(self):
        """
        Getter function for student repository
        :return: repo list
        """
        return self._std_repo

    def __len__(self):
        return len(self._std_repo)

    def add_std(self, std):
        """
        Adds std to the Student repo
        :param std:
        :return:
        """
        for _std in self._std_repo:
            if _std.get_id() == std.get_id():
                raise ValidationError("id existent")
                #return
        self._std_repo.append(std)

    def get_all(self):
        """
        Functie pentru a lua toata lista
        :return:
        """
        return self._std_repo[:]

    def cauta_id(self, id):
        """
        Functie pentru cautarea unui student dupa id
        :param id:
        :return:
        """
        for _std in self._std_repo:
            if _std.get_id() == id:
                return _std

    def sterge_id(self, id):
        """
        Functie pentru stergerea unui student dupa id
        :param id:
        :return:
        """
        index = 0
        for _std in self._std_repo:
            if _std.get_id() == id:
                self._std_repo.pop(index)
            index += 1

    def modifica(self, id, nume, grupa):
        """
        Functie pentru modificarea unui student
        :param id_prb:
        :param nume:
        :param grupa:
        :return:
        """
        index = 0
        for _std in self._std_repo:
            if _std.get_id() == id:
                self._std_repo[index].modifica(nume, grupa)
            index += 1

    def filtru_prefix(self, filtru):
        """
        Functie de filtrare in repo
        :param filtru:
        :return:
        """

        indexes = []
        for _std in self._std_repo:
            if _std.are_prefix(filtru):
                indexes.append(_std)
        return indexes


class FileRepoStudent(RepoStudent):

    def __init__(self, file_name):
        RepoStudent.__init__(self)
        self.__file_name = file_name

    def __len__(self):
        self.__load_from_file_randuri()
        return RepoStudent.__len__(self)

    def get_all(self):
        """
        Suprascrie functia din Repo
        :return:
        """
        self.__load_from_file_randuri()
        return RepoStudent.get_all(self)

    def modifica(self, id, nume, grupa):
        """
                Suprascrie functia din Repo
                :return:
                """
        with open(self.__file_name,"r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                list = line.split(',')
                if int(list[0]) == id:
                    std = Student(id, nume, grupa)
                    f.write(f"{std.get_id()},{std.get_nume()},{std.get_grupa()}\n")
                else:
                    f.write(line)

    def add_std(self, std):
        """
        Suprascrie functia din Repo
        :return:
        """
        self.__load_from_file_randuri()
        RepoStudent.add_std(self, std)
        self.__append_to_file_randuri(std)

    def cauta_id(self, id):
        """
        Suprascrie functia din Repo
        :return:
        """
        self.__load_from_file_randuri()
        return RepoStudent.cauta_id(self, id)

    def sterge_id(self, id):
        """
        Suprascrie functia din repo
        :param id:
        :return:
        """

        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                list = line.split(',')
                if int(list[0]) != id:
                    f.write(line)

    def __load_from_file(self):
        """
        Funcctia de luare a datelor din fisier
        :return:
        """
        with open(self.__file_name, "r") as f:
            self._std_repo = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    attrs = line.split(',')
                    std = Student(int(attrs[0]), attrs[1], int(attrs[2]))
                    self._std_repo.append(std)


    def __load_from_file_randuri(self):
        with open(self.__file_name, "r") as f:
            self._std_repo = []
            attrs = []
            index = 0
            for line in f.readlines():
                line = line.strip('\n')
                if len(line) > 0:
                    attrs.append(line)
                    index += 1
                    if index % 3 == 0:
                        std = Student(int(attrs[0]), attrs[1], int(attrs[2]))
                        attrs = []
                        self._std_repo.append(std)

    def __append_to_file(self, std):
        """
        Functia de atribuire datelor in fisier
        :param std:
        :return:
        """
        with open(self.__file_name, "a") as f:
            f.write(f"{std.get_id()},{std.get_nume()},{std.get_grupa()}\n")

    def __append_to_file_randuri(self, std):
        with open(self.__file_name, "a") as f:
            f.write(f"{std.get_id()}\n{std.get_nume()}\n{std.get_grupa()}\n")
