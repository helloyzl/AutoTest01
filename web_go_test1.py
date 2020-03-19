from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
import web_test1

example_tests = TestLoader().loadTestsFromTestCase(web_test1.MyTest1)


suite = TestSuite([example_tests,])

runner = HTMLTestRunner(output='example_suite')

runner.run(suite)