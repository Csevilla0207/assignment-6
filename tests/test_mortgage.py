"""
Description: A class used to test the Mortgage class.
Author: Kimi Sevilla
Date: 11/14/024
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

# This file will be used to define unit tests for the Mortgage class.

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
    
    # Existing test cases...

    def test_set_amortization_valid(self):
        """Test that the Amortization can be successfully modified to a valid value."""
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 30)
        mortgage.set_amortization(25)  # Assume 25 is a valid amortization value in VALID_AMORTIZATION
        self.assertEqual(mortgage.get_amortization(), 25)

    def test_set_amortization_invalid(self):
        """Test that ValueError is raised for invalid amortization."""
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 30)
        with self.assertRaises(ValueError) as context:
            mortgage.set_amortization(35)  # Assume 35 is NOT a valid amortization value
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

# This code can be executed to run the tests
if __name__ == "__main__":
    import unittest
    unittest.main()
    