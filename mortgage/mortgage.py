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
    
    # Accessor for Loan Amount
    def get_loan_amount(self) -> float:
        """Accessor method to return the loan amount."""
        return self.__loan_amount

    # Mutator for Loan Amount
    def set_loan_amount(self, loan_amount: float):
        """Mutator method to set the loan amount with validation."""
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

    # Accessor for Rate
    def get_rate(self) -> MortgageRate:
        """Accessor method to return the rate."""
        return self.__rate

    # Mutator for Rate
    def set_rate(self, string_rate_value: str):
        """Mutator method to set the rate with validation."""
        try:
            self.__rate = MortgageRate[string_rate_value]
        except KeyError:
            raise ValueError("Rate provided is invalid.")
        
    # Accessor for Amortization
    def get_amortization(self) -> int:
        """Accessor method to return the amortization."""
        return self.__amortization

    # Mutator for Amortization
    def set_amortization(self, amortization: int):
        """Mutator method to set the amortization with validation."""
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

if __name__ == "__main__":
    mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 30)
    print(mortgage)

    mortgage.set_amortization(25)
    print(mortgage.get_amortization())

    try:
        mortgage.set_amortization(40)
    except ValueError as e:
        print(e)



