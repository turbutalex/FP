class Nota:

    def __init__(self, std, prb, nota):
        self.__std = std
        self.__prb = prb
        self.__nota = nota

    def __str__(self):
        return str(self.__std) + " are la problema " + str(self.__prb) + " nota: " + str(self.__nota)

    def get_std(self):
        """
        Functie de get pentru student
        :return: self.__std
        """
        return self.__std

    def get_prb(self):
        """
        Functie de get pentru problema
        :return: self.__prb
        """
        return self.__prb

    def get_nota(self):
        """
        Functie de get pentru nota asignata unui student la o problema
        :return: self.__nota
        """
        return self.__nota
