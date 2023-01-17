import datetime
from Errors.errors import *

class Problem_validator:

    def validate(self, problem):
        """
        Functie de validare pentru o problema
        :param problem:
        :return:
        """
        err = ""
        if problem.get_nr_prb() == "":
            err += "Exercitiu invalid "
        if problem.get_descriere() == "":
            err += "Descriere invalida "
        if problem.get_deadline() < datetime.date.today():
            err += "Data invalida "
        if len(err) > 0:
            raise ValidationError(err)
