class Problema:
    def __init__(self, nr_prb, descriere, deadline):
        self.__nr_prb = nr_prb
        self.__descriere = descriere
        self.__deadline = deadline

    def __eq__(self, other):
        return self.get_nr_prb() == other.get_nr_prb()

    def get_nr_prb(self):
        """
        Getter function for the Problem s index
        :return: The index of the Problem
        """
        return self.__nr_prb

    def get_descriere(self):
        """
        Getter funtion for the problems description
        :return:
        """
        return self.__descriere

    def get_deadline(self):
        """
        Getter funtion for the Problem's deadline
        :return: The problem's deadline
        """
        return self.__deadline

    def __str__(self):
        return str(self.__nr_prb) + " " + str(self.__descriere) + " " + str(self.__deadline)

    def modifica(self, nr_prb, descriere, deadline):
        """
        Functie pentru modificarea unei probleme
        :param nr_prb:
        :param descriere:
        :param deadline:
        :return:
        """
        self.__nr_prb = nr_prb
        self.__descriere = descriere
        self.__deadline = deadline

