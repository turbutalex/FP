import string
import random
import datetime
from Domain.student import Student
from Domain.Problema import Problema
from Domain.Note import Nota

class ServiceNote:

    def __init__(self, note_repo, note_validator):
        self.__note_repo = note_repo
        self.__note_validator = note_validator

    def get_note_repo(self):
        return self.__note_repo

    def get_note_validator(self):
        return self.__note_validator

    def get_all(self):
        return self.__note_repo.get_all()

    def __len__(self):
        return len(self.__note_repo)

    def adauga_nota(self, id, nume, grupa, nr_prb, descriere, deadline, nota):
        std = Student(id, nume, grupa)
        prb = Problema(nr_prb, descriere, deadline)
        note = Nota(std, prb, nota)
        self.__note_validator.validate(std, prb, note)
        self.__note_repo.asignare_nota(note)

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
        chars = string.digits
        nota = ''
        for _ in range(1):
            nota += ''.join(random.choice(chars))
        nota = int(nota)
        note = Nota(std, prb, nota)
        self.__note_repo.asignare_nota(note)

    def raport_lab_dupa_nume(self, ex):
        return self.__note_repo.raport_lab_dupa_nume(ex)

    def raport_lab_dupa_nota(self, ex):
        return self.__note_repo.raport_lab_dupa_nota(ex)

    def raport_corigenti(self):
        return self.__note_repo.raport_corigenti()

    def medie_note(self, std):
        return self.__note_repo.medie_note(std)

    def medie_note_lab(self, ex):
        return self.__note_repo.medie_note_lab(ex)

    def raport_lab_dupa_participare(self):
        return self.__note_repo.raport_lab_dupa_participare()
