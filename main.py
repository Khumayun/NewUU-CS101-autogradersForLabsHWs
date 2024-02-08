"""
/*
 * @Author: Khumayun [Khumoyun A.]
 * @Date: 2023-10-31
 * @Last Modified by: Khumayun [Khumoyun A.]
 * @Last Modified time: 2020-10-31
 */
"""

from GradescopeBase import Autograder, RateLimit, global_tests

if __name__ == "__main__":
	rate_limit = False

	rlim = None
	if rate_limit:
		"""
		Here is an example of how to use the ratelimit.
		We are giving students 6 tokens where a token will
		take 2 hours to regenerate. If you do not want to rate
		limit, can just set rlim to None.
		"""
		rlim = RateLimit(6, hours=2)

	autograder = Autograder(rate_limit=rlim)
	autograder.import_tests(tests_dir="tests", blacklist=["__init__.py", "lib.py"])
	autograder.run()
	autograder.run_tests()
	results = autograder.generate_results()

	print('\n\n\nRESULTS:')
	print(f'EXECUTION TIME: {results["execution_time"]}')
	for i, testcase in enumerate(results['tests']):
		print(f'TEST {testcase["name"]}: {testcase["score"]}/{testcase["max_score"]} points!')
