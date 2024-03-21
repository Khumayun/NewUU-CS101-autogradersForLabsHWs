import os
import subprocess
import re
from functools import wraps

from GradescopeBase import Autograder, AutograderTest, Test

PROBLEM_NO = os.path.basename(__file__)
PROBLEM_NO = PROBLEM_NO.split('_')[1].split('.')[0][1:]

INPUTS_FOR_CIN = [
    "29.9",
    "328", "23", "92",
    "F", "1.65",
    "18:20:3F:20:AB:11",
    "5", "+", "42"
]
STUDENT_SUBMISSION = f"/autograder/submission/main.cpp"
TRUE_RESULT = f"/autograder/source/tests/solutions/truemain.cpp"

# for local run
# STUDENT_SUBMISSION = f"submission/main.cpp"
# TRUE_RESULT = f"tests/solutions/truemain.cpp"

COMPILED_STUDENT_SUBMISSION = os.system(
    f"g++ -c {STUDENT_SUBMISSION} && g++ -o main main.o")

COMPILED_TRUE_RESULT = os.system(
    f"g++ -c {TRUE_RESULT} && g++ -o truemain truemain.o")

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            test = args[1]  # Assuming the test object is passed as the second argument
            test.print(f"An error occurred: {e}")
            return False
    return wrapper

def applyPattern(full_text, solution_words, no):
    full_text = full_text[no].strip()
    solution_words = solution_words[no].strip()

    pattern = r'\b'
    for word in solution_words.split(' ')[:-1]:
        pattern += word
        pattern += r'\W*(?:\w+\W*)*'
    pattern += r'\b'

    # print(no)
    # print('true - ', solution_words)
    # print('student - ', full_text)
    # print(pattern)

    return (re.search(pattern, full_text) and len(full_text) != 0)


def compileCPP():

    process = subprocess.Popen([f"./main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output_student, error_student = process.communicate(input=' '.join(INPUTS_FOR_CIN).
                                                                    encode('utf-8'))

    process = subprocess.Popen([f"./truemain"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output_true, error_true = process.communicate(input=' '.join(INPUTS_FOR_CIN).
                                                                    encode('utf-8'))

    pattern = r'problem (\d+)\n(.*?)(?=problem \d+|$)'

    stud_matches = re.findall(pattern, output_student.decode('utf-8').lower(), re.DOTALL)
    true_matches = re.findall(pattern, output_true.decode('utf-8').lower(), re.DOTALL)

    # Generate dictionaries from the matches
    stud_res = {int(match[0]): match[1] for match in stud_matches}
    true_res = {int(match[0]): match[1] for match in true_matches}

    return true_res, stud_res


trueResult, studentResult = compileCPP()


@Test(f"Problem 1", 2)
@handle_exceptions
def is_valid(ag: Autograder, test: AutograderTest):
    if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
        test.print(f"There was an issue with compiling file")
        return False

    studSol = studentResult[1].strip()
    trueSol = trueResult[1].strip()

    is_correct = (trueSol in studSol and len(studSol) != 0)

    if is_correct == 0:
        test.print("Your solution don't pass the test!")
        return False
    else:
        test.print("Correct solution!")
    return True


@Test(f"Problem 2", 2)
@handle_exceptions
def is_valid(ag: Autograder, test: AutograderTest):
    if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
        test.print(f"There was an issue with compiling file")
        return False

    if applyPattern(studentResult, trueResult, 2):
        test.print("Correct solution!")
    else:
        test.print("Your solution don't pass the test!")
        return False
    return True


@Test(f"Problem 3", 2)
@handle_exceptions
def is_valid(ag: Autograder, test: AutograderTest):
    if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
        test.print(f"There was an issue with compiling file")
        return False

    if applyPattern(studentResult, trueResult, 3):
        test.print("Correct solution!")
        return True
    else:
        test.print("Your solution don't pass the test!")
        return False


@Test(f"Problem 4", 2)
@handle_exceptions
def is_valid(ag: Autograder, test: AutograderTest):
    if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
        test.print(f"There was an issue with compiling file")
        return False

    if applyPattern(studentResult, trueResult, 4):
        test.print("Correct solution!")
        return True
    else:
        test.print("Your solution don't pass the test!")
        return False


@Test(f"Problem 5", 2)
@handle_exceptions
def is_valid(ag: Autograder, test: AutograderTest):
    if COMPILED_STUDENT_SUBMISSION != 0 or COMPILED_TRUE_RESULT != 0:
        test.print(f"There was an issue with compiling file")
        return False

    if applyPattern(studentResult, trueResult, 5):
        test.print("Correct solution!")
        return True
    else:
        test.print("Your solution don't pass the test!")
        return False
