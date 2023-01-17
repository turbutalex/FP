from Domain.Problema import Problema
import datetime


class RepoProblem:

    def __init__(self):
        self._prb_repo = []

    def __eq__(self, other):
        if len(self._prb_repo) != len(other.get_repo()):
            return False
        for index in range(0, len(self._prb_repo)):
            if self._prb_repo[index] != other.get_repo()[index]:
                return False
        return True

    def get_repo(self):
        """
        Getter function for problems repository
        :return: repo list
        """
        return self._prb_repo

    def __len__(self):
        return len(self._prb_repo)

    def add_prb(self, prb):
        """
        Adds prb to problem repo
        :param prb:
        :return:
        """
        self._prb_repo.append(prb)

    def get_all(self):
        """
        Functie pentru a lua toata lista
        :return:
        """
        return self._prb_repo[:]

    def cauta_ex(self, ex):
        """
        caz favorabil:O/(1) cand elementul se afla la inceputul listei
        caz nefavorabil:O/(n) cand elementul se afla la sfarsitul listei
        caz general suma (1->n)/n = n(n+1)/2*n = O(n)
        Functie pentru cautarea unui exercitiu
        :param ex:
        :return:
        """
        for _prb in self._prb_repo:
            if _prb.get_nr_prb() == ex:
                return _prb

    def cauta_ex_rec(self, ex, i=0):
        """
        Functie pentru cautarea unui exercitiu
        :param i:
        :param ex:
        :return:
        """
        if i == len(self._prb_repo):
            return
        if ex == self._prb_repo[i].get_nr_prb():
            return self._prb_repo[i]
        else:
            self.cauta_ex_rec(ex, i + 1)

    def sterge_ex(self, ex):
        """
        Functie pentru stergerea unui exercitiu
        :param ex:
        :return:
        """
        index = 0
        for _prb in self._prb_repo:
            if _prb.get_nr_prb() == ex:
                self._prb_repo.pop(index)
            index += 1

    def sterge_ex_rec(self, ex, i=0):
        """
        Functie pentru stergerea unui exercitiu
        :param i:
        :param ex:
        :return:
        """

        if ex == self._prb_repo[i].get_nr_prb():
            self._prb_repo.pop(i)
        else:
            self.sterge_ex_rec(ex, i + 1)
        if i == len(self._prb_repo)-1:
            return

    def modifica(self, ex, nr_prb, descriere, deadline):
        """
        Functie pentru modificarea unei probleme
        :return:
        """
        index = 0
        for _prb in self._prb_repo:
            if _prb.get_nr_prb() == ex:
                self._prb_repo[index].modifica(nr_prb, descriere, deadline)
            index += 1


class FileRepoProblem(RepoProblem):
    def __init__(self, file_name):
        RepoProblem.__init__(self)
        self.__file_name = file_name

    def __len__(self):
        self.__load_from_file_randuri()
        return RepoProblem.__len__(self)

    def get_all(self):
        """
        Suprascrie functia din repo
        :return:
        """
        self.__load_from_file_randuri()
        return RepoProblem.get_all(self)

    def cauta_ex(self, ex):
        """
        Suprascrie functia din repo
        :param ex:
        :return:
        """
        self.__load_from_file_randuri()
        return RepoProblem.cauta_ex(self, ex)

    def sterge_ex(self, ex):
        """
        Suprascrie functia din repo
        :param ex:
        :return:
        """
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                list = line.split(',')
                if list[0] != ex:
                    f.write(line)

    def modifica(self, ex, nr_prb, descriere, deadline):
        """
        Suprascrie functia din Repo
        :param ex:
        :param nr_prb:
        :param descriere:
        :param deadline:
        :return:
        """
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                list = line.split(",")
                if list[0] == ex:
                    prb = Problema(nr_prb, descriere, deadline)
                    f.write(
                        f"{prb.get_nr_prb()},{prb.get_descriere()},{prb.get_deadline().strftime('%d')},{prb.get_deadline().strftime('%m')},{prb.get_deadline().strftime('%Y')}\n")
                else:
                    f.write(line)

    def add_prb(self, prb):
        """
        Suprascrie functia din repo
        :param prb:
        :return:
        """
        self.__load_from_file_randuri()
        RepoProblem.add_prb(self, prb)
        self.__append_to_file_randuri(prb)

    def __load_from_file(self):
        """
        Functia de luare a datelor din fisier
        :return:
        """
        with open(self.__file_name, "r") as f:
            self._prb_repo = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    attrs = line.split(',')
                    nr_prb = attrs[0]
                    descriere = attrs[1]
                    zi = int(attrs[2])
                    luna = int(attrs[3])
                    an = int(attrs[4])
                    deadline = datetime.date(an, luna, zi)
                    prb = Problema(nr_prb, descriere, deadline)
                    self._prb_repo.append(prb)

    def __load_from_file_randuri(self):
        with open(self.__file_name, "r") as f:
            self._prb_repo = []
            attrs = []
            index = 0
            for line in f.readlines():
                line = line.strip('\n')
                if len(line) > 0:
                    attrs.append(line)
                    index += 1
                    if index % 5 == 0:
                        nr_prb = attrs[0]
                        descriere = attrs[1]
                        zi = int(attrs[2])
                        luna = int(attrs[3])
                        an = int(attrs[4])
                        deadline = datetime.date(an, luna, zi)
                        prb = Problema(nr_prb, descriere, deadline)
                        attrs = []
                        self._prb_repo.append(prb)

    def __append_to_file(self, prb):
        """
        Functia de atribuire datelor in fisier
        :param prb:
        :return:
        """
        with open(self.__file_name, "a") as f:
            f.write(
                f"{prb.get_nr_prb()},{prb.get_descriere()},{prb.get_deadline().strftime('%d')},{prb.get_deadline().strftime('%m')},{prb.get_deadline().strftime('%Y')}\n")

    def __append_to_file_randuri(self, prb):
        with open(self.__file_name, "a") as f:
            f.write(
                f"{prb.get_nr_prb()}\n{prb.get_descriere()}\n{prb.get_deadline().strftime('%d')}\n{prb.get_deadline().strftime('%m')}\n{prb.get_deadline().strftime('%Y')}\n")
