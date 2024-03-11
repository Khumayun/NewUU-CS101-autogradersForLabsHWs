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
	"6.9",
	"3", "7", "2",
	"900.5", "25.5", "3.55",
	"5.5",
	"31",
	"2", "3",
	"143", "93",
	"15", "114", "38",
	"-16", "-1", "-35", "51", "0",
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
	is_correct = (studentResult[0].lower().strip() == trueResult[0].lower().strip())

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
	is_correct = (len(studentResult[1].lower().strip().split('\n')) == len(trueResult[1].lower().strip().split('\n')))

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
	is_correct = (studentResult[2].lower().strip() == trueResult[2].lower().strip())

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
	is_correct = (studentResult[3].lower().strip() == trueResult[3].lower().strip())

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
	is_correct = (studentResult[4].lower().strip() == trueResult[4].lower().strip())

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
	is_correct = (studentResult[5].lower().strip() == trueResult[5].lower().strip())

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
	is_correct = (studentResult[6].lower().strip() == trueResult[6].lower().strip())

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
	is_correct = (studentResult[7].lower().strip() == trueResult[7].lower().strip())

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
	is_correct = (studentResult[8].lower().strip() == trueResult[8].lower().strip())

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
	is_correct = (studentResult[9].lower().strip() == trueResult[9].lower().strip())

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
	is_correct = (studentResult[10].lower().strip() == trueResult[10].lower().strip())

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
	is_correct = (studentResult[11].lower().strip() == trueResult[11].lower().strip())

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
	is_correct = (studentResult[12].lower().strip() == trueResult[12].lower().strip())

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
	is_correct = (studentResult[13].lower().strip() == trueResult[13].lower().strip())

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
	is_correct = (studentResult[14].lower().strip() == trueResult[14].lower().strip())

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
	is_correct = (studentResult[15].lower().strip() == trueResult[15].lower().strip())

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
	is_correct = (studentResult[16].lower().strip() == trueResult[16].lower().strip())

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
	is_correct = (studentResult[17].lower().strip() == trueResult[17].lower().strip())

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
	is_correct = (studentResult[18].lower().strip() == trueResult[18].lower().strip())

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
	is_correct = (studentResult[19].lower().strip() == trueResult[19].lower().strip())

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
	is_correct = (studentResult[20].lower().strip() == trueResult[20].lower().strip())

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
	is_correct = (studentResult[21].lower().strip() == trueResult[21].lower().strip())

	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True
