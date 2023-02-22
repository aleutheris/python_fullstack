import unittest
import os


def run_tests():
    start_folder = os.path.dirname(__file__)
    tests_subfolders = get_subfolders(start_folder)

    for subfolder in tests_subfolders:
        run_tests_in_folder(subfolder)


def run_tests_in_folder(folder):
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(folder, pattern='test_*.py')

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)

    print(test_result)


def get_subfolders(folder):
    excluded_folders = ['__pycache__']
    subfolders = []
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path) and item not in excluded_folders:
            subfolders.append(item_path)
            subfolders.extend(get_subfolders(item_path))
    return subfolders


if __name__ == '__main__':
    run_tests()
