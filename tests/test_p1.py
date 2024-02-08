import os
import subprocess

from GradescopeBase import Autograder, AutograderTest, Test
from GradescopeBase.Utils import root_dir

PROBLEM_NO = os.path.basename(__file__)
PROBLEM_NO = PROBLEM_NO.split('_')[1].split('.')[0][1:]


@Test(f"Problem {PROBLEM_NO}", 2)
def is_valid(ag: Autograder, test: AutograderTest):
	test_problem = f"{root_dir()}/tests/problem_{PROBLEM_NO}/test_p{PROBLEM_NO}.cpp"
	compiled = os.system(
		f"g++ -c {test_problem} && g++ -o test_p{PROBLEM_NO} test_p{PROBLEM_NO}.o")
	if compiled != 0:
		test.print(f"There was an issue with compiling Problem {PROBLEM_NO} file")
		return False

	is_correct = subprocess.call([f"./test_p{PROBLEM_NO}"])
	if is_correct == 0:
		test.print("Your solution don't pass the test!")
		return False
	return True
