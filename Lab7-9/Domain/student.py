import datetime


class Student:
    def __init__(self, id, nume, grupa):
        self.__id = id
        self.__nume = nume
        self.__grupa = grupa
        self.laborator = {
            "lab": "",
            "ex": "",
            "descriere": "",
            "deadline": "",
            "nota": ""
        }

    def get_id(self):
        """
        Getter function for student Id
        :return: Student's Id
        """
        return self.__id

    def get_nume(self):
        """
        Getter function for student name
        :return: Student's name
        """
        return self.__nume

    def get_grupa(self):
        """
        Getter function for Student's group
        :return: Student's group
        """
        return self.__grupa

    def modifica(self, nume, grupa):
        """
        Functie pentru modificarea unui student
        :param nume:
        :param grupa:
        :return:
        """
        self.__nume = nume
        self.__grupa = grupa

    def __eq__(self, other):
        return self.__id == other.get_id()

    def __str__(self):
        return str(self.__id) + " " + str(self.__nume) + " " + str(self.__grupa)

    def are_prefix(self, prefix):
        """
        Functie pentru verificarea daca un student are un prefix la nume
        :param prefix:
        :return:
        """
        index = 0
        for i in prefix:
            if prefix[index] != self.__nume[index]:
                return False
            index += 1
        return True

    def assign_prb(self, prb):
        pass



