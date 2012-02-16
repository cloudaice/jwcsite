#@+leo-ver=5-thin
#@+node:cloudaice.20120216102454.1163: * @file /home/cloudaice/pyrepo/jwcsite/stu_service/tests.py
#@@language python
#@@tabwidth -4
#@+others
#@+node:cloudaice.20120216102454.1164: ** tests declarations
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


#@+node:cloudaice.20120216102454.1165: ** class SimpleTest
class SimpleTest(TestCase):
    #@+others
    #@+node:cloudaice.20120216102454.1166: *3* test_basic_addition
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    #@-others
#@-others
#@-leo
