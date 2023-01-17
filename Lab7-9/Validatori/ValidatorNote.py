import datetime
from Errors.errors import *


class Note_validator:

    def validate(self, student, problem, nota):
        """
        Functie de validare pentru o nota
        :param note:
        :return:
        """
        err = ""
        if student.get_id() < 1:
            err += "Id invalid "
        if student.get_nume() == "":
            err += "Nume invalid "
        if student.get_grupa() < 1:
            err += "Grupa invalida "
        if problem.get_nr_prb() == "":
            err += "Exercitiu invalid "
        if problem.get_descriere() == "":
            err += "Descriere invalida "
        if problem.get_deadline() < datetime.date.today():
            err += "Data invalida "
        if nota.get_nota() < 1 or nota.get_nota() > 10:
            err += "Nota invalida"
        if len(err) > 0:
            raise ValidationError(err)
