from unittest import TestCase
from app import app
from flask import session
from converter import Converter

class FlaskTests(TestCase):

    def testconver(self):
        old = "USD"
        new = "USD"
        amount = "1"

        currency_converter = Converter(old, new, amount)
        results = currency_converter.convert()
        self.assertEqual(results, "1")
