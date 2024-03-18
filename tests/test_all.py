import os
import subprocess
import re

from GradescopeBase import Autograder, AutograderTest, Test
from GradescopeBase.Utils import root_dir

PROBLEM_NO = os.path.basename(__file__)
PROBLEM_NO = PROBLEM_NO.split('_')[1].split('.')[0][1:]

INPUTS_FOR_CIN = [
"-8",
"67",
"34", "321", "1",
"13", "2",
"2024",
"2", "-6", "21"
"30", "90", "50",
"F",
"64",
"2", "34",
"13", "55",
"46", "150",
"363",
"y",
"1", "3",
"75",
"66",
"u",
"13",
"7",
"1"
]
# STUDENT_SUBMISSION = f"/autograder/submission/main.cpp"
# TRUE_RESULT = f"/autograder/source/tests/solutions/truemain.cpp"

STUDENT_SUBMISSION = f"submission/main.cpp"
TRUE_RESULT = f"tests/solutions/truemain.cpp"

COMPILED_STUDENT_SUBMISSION = os.system(
	f"g++ -c {STUDENT_SUBMISSION} && g++ -o main main.o")

COMPILED_TRUE_RESULT = os.system(
	f"g++ -c {TRUE_RESULT} && g++ -o truemain truemain.o")


def applyPattern(full_text, solution_words, no):
	full_text = full_text[no].strip()
	solution_words = solution_words[no].strip()

	pattern = r'\b'
	for word in solution_words:
		pattern += word
		pattern += '\b\W+(?:\w+\W+)*'
	pattern += '\b'
	if no == 21:
		print(full_text)
		print(solution_words)

	return (re.search(pattern, full_text) and full_text != [''])


def compileCPP():

	process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
							   stderr=subprocess.PIPE, shell=True)
	output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).
																	encode('utf-8'))

	process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
							   stderr=subprocess.PIPE, shell=True)
	output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).
												  					encode('utf-8'))

	stud_res = re.split(r'problem \d+\n', output_student.decode('utf-8').lower())
	true_res = re.split(r'problem \d+\n', output_true.decode('utf-8').lower())

	return true_res, stud_res


trueResult, studentResult = compileCPP()


@Test(f"Problem 1", 2)
def is_valid(ag: Autograder, test: AutograderTest):
	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	studSol = studentResult[1].strip()
	trueSol = trueResult[1].strip()

	is_correct = (trueSol in studSol and studSol != [''])

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

	if applyPattern(studentResult, trueResult, 1) == 0:
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

	if applyPattern(studentResult, trueResult, 3) == 0:
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

	if applyPattern(studentResult, trueResult, 4) == 0:
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

	if applyPattern(studentResult, trueResult, 5) == 0:
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

	if applyPattern(studentResult, trueResult, 6) == 0:
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True

@Test(f"Problem 7", 2)
def is_valid(ag: Autograder, test: AutograderTest):
	if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
		test.print(f"There was an issue with compiling file")
		return False

	if applyPattern(studentResult, trueResult, 7) == 0:
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

	if applyPattern(studentResult, trueResult, 8) == 0:
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

	if applyPattern(studentResult, trueResult, 9) == 0:
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

	if applyPattern(studentResult, trueResult, 10) == 0:
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

	if applyPattern(studentResult, trueResult, 11) == 0:
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

	if applyPattern(studentResult, trueResult, 12) == 0:
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

	if applyPattern(studentResult, trueResult, 13) == 0:
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

	if applyPattern(studentResult, trueResult, 14) == 0:
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

	if applyPattern(studentResult, trueResult, 15) == 0:
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

	if applyPattern(studentResult, trueResult, 16) == 0:
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

	if applyPattern(studentResult, trueResult, 17) == 0:
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

	if applyPattern(studentResult, trueResult, 18) == 0:
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

	if applyPattern(studentResult, trueResult, 19) == 0:
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

	if applyPattern(studentResult, trueResult, 20) == 0:
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

	if len(studentResult[21].strip()) != len(trueResult[21].strip()):
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

	if len(studentResult[22].strip()) != len(trueResult[22].strip()):
		test.print("Your solution don't pass the test!")
		return False
	else:
		test.print("Correct solution!")
	return True
