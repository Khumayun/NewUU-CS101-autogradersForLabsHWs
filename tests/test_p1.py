import os
import subprocess
import re

from GradescopeBase import Autograder, AutograderTest, Test
from GradescopeBase.Utils import root_dir

PROBLEM_NO = os.path.basename(__file__)
PROBLEM_NO = PROBLEM_NO.split('_')[1].split('.')[0][1:]

INPUTS_FOR_CIN = [
	"38", "73",
	"2", "5",
	"3.45",
	"3", "7", "2",
	"900.5", "25.5", "3.55",
	"5.5",
	"20",
	"2", "3",
	"55", "14",
	"5", "14", "8",
	"-6", "-3", "-2", "1", "0",
	"15", "11",
	"172", "5.8"
]

def manualTest(studentResult, trueResult):
	for i, (studentSolution, trueSolution) in enumerate(zip(studentResult, trueResult)):
		if i == 1 and len(studentSolution.split('\n')) != len(trueSolution.split('\n')):
			return False
		if studentSolution != trueSolution:
			return False
	return True


@Test(f"Problem {PROBLEM_NO}", 10)
def is_valid(ag: Autograder, test: AutograderTest):
	student_submission = f"{root_dir()}/submission/main.cpp"
	true_result = f"{root_dir()}/tests/solutions/truemain.cpp"

	compiled_student_submission = os.system(
		f"g++ -c {student_submission} && g++ -o main main.o")

	compiled_true_result = os.system(
		f"g++ -c {true_result} && g++ -o truemain truemain.o")

	if compiled_student_submission != 0 or compiled_true_result != 0:
		test.print(f"There was an issue with compiling file")
		return False

	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	if process.returncode == 0:  # Execution successful
		test.print(output_true.decode('utf-8'))  # Decode bytes to string
	else:
		test.print(output_true.decode('utf-8'))  # Decode bytes to string

	studentResult = re.split(r'PROBLEM \d+\n', output_student.decode('utf-8'))
	trueResult = re.split(r'PROBLEM \d+\n', output_true.decode('utf-8'))
	is_correct = manualTest(studentResult, trueResult)

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	return True
