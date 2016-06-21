import os
import unittest

from tests.task_tests import ModelTest
from tests.worktime_tests import WorkTimeTest

if __name__ == '__main__':
	test_database = 'data/test.sqlite'
	if os.path.exists(test_database): os.remove('data/test.sqlite')
	unittest.main()

