from math import ceil
from Utilities.utils import insertSort, combSort
import datetime
from Domain.Note import Nota
from Domain.student import Student
from Domain.Problema import Problema


class RepoCatalog:

    def __init__(self):
        self._note_repo = []

    def asignare_nota(self, nota):
        """
        Functie de notare a unui student
        :return:
        """
        self._note_repo.append(nota)

    def __len__(self):
        return len(self._note_repo)

    def get_all(self):
        """
        Functie de preluare a repoului intreg
        :return:
        """
        return self._note_repo[:]

    def raport_lab_dupa_nume(self, ex):
        """
        Complexitate: complexitatea sortarii
        Spatiu:
        caz favorabil: O/(1)
        caz nefavorabil: O/(n)
        caz general : O(n)
        Timp:
        Bubble sort:
        favorabil _-_(n)
        nefavorabil O(n^2)
        general O/(n^2)
        total:
        favorabil: O/(n)-lista sortata crescator
        nefavorabil O(n^2)-lista sortata descrescator
        general O/(n^2)
        Functie pentru crearea raportului in ordine alfabetica la un laborator dat
        :param ex:
        :return:
        """
        list = []
        for _note in self._note_repo:
            if ex == _note.get_prb().get_nr_prb():
                list.append(_note)
        """ok = 1
        while ok == 1:
            ok = 0
            for i in range(0, len(list) - 1):
                if list[i].get_std().get_nume() > list[i + 1].get_std().get_nume():
                    aux = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = aux
                    ok = 1 """
        insertSort(list, key=lambda x: (x.get_std().get_nume(), x.get_nota()))
        return list

    def raport_lab_dupa_nota(self, ex):
        """
        FUnctia pentru crearea raportului in ordine crescatoare dupa nota la un laborator dat
        :param ex:
        :return:
        """
        list = []
        for _note in self._note_repo:
            if ex == _note.get_prb().get_nr_prb():
                list.append(_note)
        ok = 1
        while ok == 1:
            ok = 0
            for i in range(0, len(list) - 1):
                if list[i].get_nota() > list[i + 1].get_nota():
                    aux = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = aux
                    ok = 1
        return list

    def medie_note(self, std):
        """
        FUnctie pentru aflarea mediei unui student
        :param std:
        :return:
        """
        counter = 0
        sum = 0
        index = 0
        for _note in self._note_repo:
            if _note.get_std().get_id() == std.get_id():
                counter += 1
                sum += self._note_repo[index].get_nota()
            index += 1
        return sum / counter

    def medie_note_lab(self, ex):
        """
        Functie pentru calcularea mediei notelor studentilor la o problema
        :param ex:
        :return:
        """
        counter = 0
        sum = 0
        index = 0
        for _note in self._note_repo:
            if _note.get_prb().get_nr_prb() == ex:
                counter += 1
                sum += self._note_repo[index].get_nota()
            index += 1
        return sum / counter

    def raport_corigenti(self):
        """
        Functie pentru crearea unui raport al studentilor corigenti
        :return:
        """
        list = []
        for _note in self._note_repo:
            if _note.get_std() not in list:
                if self.medie_note(_note.get_std()) < 5:
                    list.append(_note.get_std())
        combSort(list, key=lambda x: x.get_std().get_id())
        return list

    def std_asignati(self, ex):
        """
        Functie pentru verificarea numarului de studenti asignati la o problema
        :param ex:
        :return:
        """
        nr = 0
        for _note in self._note_repo:
            if _note.get_prb().get_nr_prb() == ex:
                nr += 1
        return nr

    def max_std_asignati(self):
        """
        FUnctie pentru gasirea nr maxim de studenti asignati la o problema
        :return:
        """
        mx = 0
        for _note in self._note_repo:
            if self.std_asignati(_note.get_prb().get_nr_prb()) > mx:
                mx = self.std_asignati(_note.get_prb().get_nr_prb())
        return mx

    def raport_lab_dupa_participare(self):
        """
        Functie penru crearea raportului la problemele cu cea mai mare participare
        :return:
        """
        list = []
        for _note in self._note_repo:
            if self.medie_note(_note.get_std()) > 5.0 and self.std_asignati(
                    _note.get_prb().get_nr_prb()) == self.max_std_asignati():
                if _note not in list:
                    list.append(_note)
        ok = 1
        while ok == 1:
            ok = 0
            for i in range(0, len(list) - 1):
                if list[i].get_prb().get_nr_prb() > list[i + 1].get_prb().get_nr_prb():
                    aux = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = aux
                    ok = 1
        mij = int(ceil(len(list) / 2))
        return list[:mij]


class FileRepoCatalog(RepoCatalog):
    def __init__(self, file_name):
        RepoCatalog.__init__(self)
        self.__file_name = file_name
        self.__load_from_file_randuri()

    def __len__(self):
        self.__load_from_file_randuri()
        return RepoCatalog.__len__(self)

    def get_all(self):
        """
        Suprascrie functia din repo
        :return:
        """
        self.__load_from_file_randuri()
        return RepoCatalog.get_all(self)

    def asignare_nota(self, nota):
        """
        Suprascrie functia din repo
        :param nota:
        :return:
        """
        self.__load_from_file_randuri()
        RepoCatalog.asignare_nota(self, nota)
        self.__append_to_file(nota)

    def __load_from_file(self):
        """
        Functia de luare a datelor din fisier
        :return:
        """
        with open(self.__file_name, "r") as f:
            self._note_repo = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    attrs = line.split(',')
                    id = int(attrs[0])
                    nume = attrs[1]
                    grupa = int(attrs[2])
                    nr_prb = attrs[3]
                    descriere = attrs[4]
                    zi = int(attrs[5])
                    luna = int(attrs[6])
                    an = int(attrs[7])
                    nota = int(attrs[8])
                    deadline = datetime.date(an, luna, zi)
                    std = Student(id, nume, grupa)
                    prb = Problema(nr_prb, descriere, deadline)
                    nota = Nota(std, prb, nota)
                    self._note_repo.append(nota)

    def __load_from_file_randuri(self):
        with open(self.__file_name, "r") as f:
            self._note_repo = []
            attrs = []
            index = 0
            for line in f.readlines():
                line = line.strip('\n')
                if len(line) > 0:
                    line = line.strip('\n')
                    attrs.append(line)
                    index += 1
                    if index % 9 == 0:
                        id = int(attrs[0])
                        nume = attrs[1]
                        grupa = int(attrs[2])
                        nr_prb = attrs[3]
                        descriere = attrs[4]
                        zi = int(attrs[5])
                        luna = int(attrs[6])
                        an = int(attrs[7])
                        nota = int(attrs[8])
                        deadline = datetime.date(an, luna, zi)
                        std = Student(id, nume, grupa)
                        prb = Problema(nr_prb, descriere, deadline)
                        nota = Nota(std, prb, nota)
                        attrs = []
                        self._note_repo.append(nota)

    def __append_to_file(self, nota):
        """
        Functia de atribuire a datelor in fisier
        :param nota:
        :return:
        """
        with open(self.__file_name, "a") as f:
            f.write(
                f"{nota.get_std().get_id()}\n{nota.get_std().get_nume()}\n{nota.get_std().get_grupa()}\n{nota.get_prb().get_nr_prb()}\n{nota.get_prb().get_descriere()}\n{nota.get_prb().get_deadline().strftime('%d')}\n{nota.get_prb().get_deadline().strftime('%m')}\n{nota.get_prb().get_deadline().strftime('%Y')}\n{nota.get_nota()}\n")
