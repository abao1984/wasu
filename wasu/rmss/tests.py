from django.test import TestCase
from rmss.models import *
# Create your tests here.

class SimpleTestCase(TestCase):
    def test_plus(self):
        self.assertEqual(1+1, 2)
