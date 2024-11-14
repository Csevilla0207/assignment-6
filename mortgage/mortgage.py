"""
Description: A class meant to manage Mortgage options.
Author: Kimi Sevilla
Date: 11/14/2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount: float, string_rate_value: str, string_frequency_value: str, amortization: int):
        # Validate Loan Amount
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        # Validate Rate
        try:
            self.__rate = MortgageRate[string_rate_value]
        except KeyError:
            raise ValueError("Rate provided is invalid.")

        # Validate Frequency
        try:
            self.__frequency = PaymentFrequency[string_frequency_value]
        except KeyError:
            raise ValueError("Frequency provided is invalid.")

        # Validate Amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

    def __str__(self):
        return (f"Mortgage(Loan Amount: {self.__loan_amount}, Rate: {self.__rate.name}, "
                f"Frequency: {self.__frequency.name}, Amortization: {self.__amortization})")


