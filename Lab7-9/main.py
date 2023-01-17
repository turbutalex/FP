from Business.ServiceStudent import *
from Business.ServiceProbleme import *
from Business.ServiceCatalog import *
from UI.Console import Console
from Repository.RepoStudent import *
from Repository.RepoProbleme import *
from Repository.RepoCatalog import *
from Validatori.ValidatorStudent import *
from Validatori.ValidatorProblema import *
from Validatori.ValidatorNote import *
from test.tests import Test

validator_student = Student_validator()
validator_problem = Problem_validator()
validator_note = Note_validator()
std_repo = FileRepoStudent("Student.txt")
prb_repo = FileRepoProblem("Probleme.txt")
note_repo = FileRepoCatalog("Note.txt")
student_srv = ServiceStudent(std_repo, validator_student)
problem_srv = ServiceProblema(prb_repo, validator_problem)
note_srv = ServiceNote(note_repo, validator_note)
console = Console(student_srv, problem_srv, note_srv)
tester = Test()

tester.run_tests()
console.run()
