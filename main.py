"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Kimi Sevilla
Date: 11/14/2024
"""

### REQUIREMENT
# ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS
from mortgage import Mortgage  # Assuming the Mortgage class is in a file named mortgage.py

try:
    # ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK
    with open("data\\pixell_river_mortgages.txt", "r") as input:
        print("**************************************************")

        for data in input:
            items = data.split(",")

            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2])
                frequency = items[3]

                # INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
                mortgage = Mortgage(amount, rate, amortization, frequency)

                # PRINT THE MORTGAGE OBJECT
                print(mortgage)

            except ValueError as e:
                # This except block will catch Explicit exceptions
                print(f"Data: {data.strip()} caused Exception: {e}")

            except Exception as e:
                # This except block will catch Implicit exceptions
                print(f"Data: {data.strip()} caused Exception: {e}")

            finally:
                print("**************************************************")
except FileNotFoundError as e:
    print(f"Error: The file was not found. Details: {e}")
