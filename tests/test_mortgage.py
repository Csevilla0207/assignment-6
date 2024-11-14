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
    
    def test_invalid_loan_amount(self):
        """Test that ValueError is raised for invalid loan amount."""
        with self.assertRaises(ValueError) as context:
            Mortgage(0, "FIXED_5", "MONTHLY", 30)
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")
        
        with self.assertRaises(ValueError) as context:
            Mortgage(-100, "FIXED_5", "MONTHLY", 30)
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_invalid_rate(self):
        """Test that ValueError is raised for invalid rate."""
        with self.assertRaises(ValueError) as context:
            Mortgage(250000, "INVALID_RATE", "MONTHLY", 30)
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_invalid_frequency(self):
        """Test that ValueError is raised for invalid frequency."""
        with self.assertRaises(ValueError) as context:
            Mortgage(250000, "FIXED_5", "INVALID_FREQUENCY", 30)
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    def test_invalid_amortization(self):
        """Test that ValueError is raised for invalid amortization."""
        with self.assertRaises(ValueError) as context:
            Mortgage(250000, "FIXED_5", "MONTHLY", 35)  # 35 is not in VALID_AMORTIZATION
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

    def test_valid_inputs(self):
        """Test that the __init__() properly sets attributes for valid inputs."""
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 30)
        self.assertEqual(mortgage._Mortgage__loan_amount, 250000)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage._Mortgage__amortization, 30)

# This code can be executed to run the tests
if __name__ == "__main__":
    import unittest
    unittest.main()

