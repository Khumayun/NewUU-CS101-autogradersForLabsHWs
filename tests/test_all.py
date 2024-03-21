import os
import subprocess
import re

from GradescopeBase import Autograder, AutograderTest, Test
from GradescopeBase.Utils import root_dir

PROBLEM_NO = os.path.basename(__file__)
PROBLEM_NO = PROBLEM_NO.split('_')[1].split('.')[0][1:]

INPUTS_FOR_CIN = [
	"5", "15",
	"2", "3",
	"36.6",
	"10", "20", "9"
	"5"
]

STUDENT_SUBMISSION = f"{root_dir()}/submission/main.cpp"
TRUE_RESULT = f"{root_dir()}/tests/solutions/truemain.cpp"

COMPILED_STUDENT_SUBMISSION = os.system(
	f"g++ -c {STUDENT_SUBMISSION} && g++ -o main main.o")

COMPILED_TRUE_RESULT = os.system(
	f"g++ -c {TRUE_RESULT} && g++ -o truemain truemain.o")


def compile_solutions():
	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	_output_student, _error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	_output_true, _error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))
	return _output_true, _output_student


output_true, output_student = compile_solutions()


@Test(f"Problem 1", 2)
def is_valid(ag: Autograder, test: AutograderTest):

	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	studentResult = re.split(r'PROBLEM \d+\n', output_student.decode('utf-8'))
	trueResult = re.split(r'PROBLEM \d+\n', output_true.decode('utf-8'))
	is_correct = (studentResult[0] == trueResult[0])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 2", 2)
def is_valid(ag: Autograder, test: AutograderTest):

	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	studentResult = re.split(r'PROBLEM \d+\n', output_student.decode('utf-8'))
	trueResult = re.split(r'PROBLEM \d+\n', output_true.decode('utf-8'))
	is_correct = (len(studentResult[1].split('\n')) == len(trueResult[1].split('\n')))

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 3", 2)
def is_valid(ag: Autograder, test: AutograderTest):

	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	studentResult = re.split(r'PROBLEM \d+\n', output_student.decode('utf-8'))
	trueResult = re.split(r'PROBLEM \d+\n', output_true.decode('utf-8'))
	is_correct = (studentResult[2] == trueResult[2])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 4", 2)
def is_valid(ag: Autograder, test: AutograderTest):

	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	studentResult = re.split(r'PROBLEM \d+\n', output_student.decode('utf-8'))
	trueResult = re.split(r'PROBLEM \d+\n', output_true.decode('utf-8'))
	is_correct = (studentResult[3] == trueResult[3])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 5", 2)
def is_valid(ag: Autograder, test: AutograderTest):

	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).encode('utf-8'))

	studentResult = re.split(r'PROBLEM \d+\n', output_student.decode('utf-8'))
	trueResult = re.split(r'PROBLEM \d+\n', output_true.decode('utf-8'))
	is_correct = (studentResult[4] == trueResult[4])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True
