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
STUDENT_SUBMISSION = f"{root_dir()}/submission/main.cpp"
TRUE_RESULT = f"{root_dir()}/tests/solutions/truemain.cpp"

COMPILED_STUDENT_SUBMISSION = os.system(
	f"g++ -c {STUDENT_SUBMISSION} && g++ -o main main.o")

COMPILED_TRUE_RESULT = os.system(
	f"g++ -c {TRUE_RESULT} && g++ -o truemain truemain.o")


def manualTest(studentResult, trueResult):
	for i, (studentSolution, trueSolution) in enumerate(zip(studentResult, trueResult)):
		if i == 1 and len(studentSolution.split('\n')) != len(trueSolution.split('\n')):
			return False
		if studentSolution != trueSolution:
			return False
	return True


@Test(f"Problem 1", 2)
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


@Test(f"Problem 6", 2)
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
	is_correct = (studentResult[5] == trueResult[5])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True


#########
@Test(f"Problem 7", 2)
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
	is_correct = (studentResult[6] == trueResult[6])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 8", 2)
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
	is_correct = (studentResult[7] == trueResult[7])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 9", 2)
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
	is_correct = (studentResult[8] == trueResult[8])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 10", 2)
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
	is_correct = (studentResult[9] == trueResult[9])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 11", 2)
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
	is_correct = (studentResult[10] == trueResult[10])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 12", 2)
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
	is_correct = (studentResult[11] == trueResult[11])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 13", 2)
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
	is_correct = (studentResult[12] == trueResult[12])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 14", 2)
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
	is_correct = (studentResult[13] == trueResult[13])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 15", 2)
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
	is_correct = (studentResult[14] == trueResult[14])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 16", 2)
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
	is_correct = (studentResult[15] == trueResult[15])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 17", 2)
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
	is_correct = (studentResult[16] == trueResult[16])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 18", 2)
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
	is_correct = (studentResult[17] == trueResult[17])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 19", 2)
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
	is_correct = (studentResult[18] == trueResult[18])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 20", 2)
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
	is_correct = (studentResult[19] == trueResult[19])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 21", 2)
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
	is_correct = (studentResult[20] == trueResult[20])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 22", 2)
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
	is_correct = (studentResult[21] == trueResult[21])

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True
