from django.test import TestCase

from app.calc import add,mult,subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(add(3,8), 11)

    def test_mult_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(mult(3,8), 24)

    def test_subtract_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(subtract(5,4), 1)