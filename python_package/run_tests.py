import unittest
import os


def run_tests():
    start_folder = os.path.dirname(__file__)
    test_loader = unittest.TestLoader()

    test_suite = test_loader.discover(start_dir=start_folder+'/tests', pattern='test_*.py', top_level_dir=start_folder)

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)

    result_summary = create_summary(test_result)
    print_tests_summary(result_summary)
    print_details_of_failed_tests(test_result)


def create_summary(test_result):
    result_summary = {"number_of_tests": test_result.testsRun, "details": {"passed": [], "failed": [], "skipped": []}}

    for test in test_result.failures:
        result_summary["details"]["failed"].append(test[0].id())
    for test in test_result.errors:
        result_summary["details"]["failed"].append(test[0].id())
    for test in test_result.skipped:
        result_summary["details"]["skipped"].append(test[0].id())

    return result_summary


def print_tests_summary(result_summary):
    number_of_failed_tests = len(result_summary["details"]["failed"])
    number_of_skipped_tests = len(result_summary["details"]["skipped"])
    number_of_passed_tests = result_summary["number_of_tests"] - number_of_failed_tests - number_of_skipped_tests

    print("Ran {} tests. {} passed, {} failed".format(number_of_passed_tests, number_of_failed_tests, number_of_skipped_tests))


def print_details_of_failed_tests(test_result):
    if len(test_result.failures) > 0:
        print("\nFailed tests:")
        for failed_test in test_result.failures:
            print(failed_test[0].id())


if __name__ == '__main__':
    run_tests()
