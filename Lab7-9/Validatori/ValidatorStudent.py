import datetime
from Errors.errors import *


class Student_validator:

    def validate(self, student):
        """
        Functie de validare pentru un student
        :param student:
        :return:
        """
        err = ""
        if student.get_id() < 1:
            err += "Id invalid "
        if student.get_nume() == "":
            err += "Nume invalid "
        if student.get_grupa() < 1:
            err += "Grupa invalida "
        if len(err) > 0:
            raise ValidationError(err)


