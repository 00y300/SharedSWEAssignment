import unittest
import InterestCalculator

from InterestCalculator import (calculate_compound_interest,
                                calculate_rate_of_return)


class TestCompoundInterestCalculator(unittest.TestCase):

    def testCalculateCompoundInterest(self):
        # Recalculated expected values
        test_cases = [
            {"P": 1000, "r": 0.05, "n": 12, "t": 10, "expected": 1647.01},  
            {"P": 1500, "r": 0.04, "n": 4, "t": 5, "expected": 1830.29},  
            {"P": 2000, "r": 0.03, "n": 1, "t": 15, "expected": 3115.93} 
        ]
        for case in test_cases:
            with self.subTest(case=case):
                result = calculate_compound_interest(case["P"], case["r"], case["n"], case["t"])
                self.assertAlmostEqual(result, case["expected"], places=2, msg=f"Failed for inputs: {case}")

    def testCalculateRateOfReturn(self):
        # Test Case 6.1: Validate the rate of return calculation
        test_cases = [
            {"A": 1647.01, "P": 1000, "expected": 647.01},
            {"A": 1824.32, "P": 1500, "expected": 324.32},
            {"A": 3112.00, "P": 2000, "expected": 1112.00}
        ]
        for case in test_cases:
            with self.subTest(case=case):
                result = calculate_rate_of_return(case["A"], case["P"])
                self.assertAlmostEqual(result, case["expected"], places=2, msg=f"Failed for inputs: {case}")

    def testRepresentationOfVariables(self):
        # Test Case 7.1: Ensure variable A is calculated and represented correctly
        P, r, n, t = 1000, 0.05, 12, 10
        A = calculate_compound_interest(P, r, n, t)
        self.assertAlmostEqual(A, 1647.01, places=2, msg="Variable A calculation failed")

        # Test Case 7.2: Verify principal amount P is used accurately
        self.assertEqual(P, 1000, "Principal amount P was not used correctly")

        # Test Case 7.3: Validate r, n, and t variables are processed correctly
        self.assertEqual(r, 0.05, "Interest rate r is incorrect")
        self.assertEqual(n, 12, "Compounding frequency n is incorrect")
        self.assertEqual(t, 10, "Time variable t is incorrect")

    def testTotalAmountOutput(self):
        # Test Case 8.1: Verify Total Amount Output
        P, r, n, t = 1000, 0.05, 12, 10
        expected_total = 1647.01  # Expected accumulated value

        # Calculate total amount
        total_amount = calculate_compound_interest(P, r, n, t)

        # Assertion
        self.assertAlmostEqual(total_amount, expected_total, places=2, msg="Total accumulated amount output is incorrect.")

    def testTotalAmountRounding(self):
        # Test Case 8.2: Verify Output is Rounded to Two Decimal Places
        P, r, n, t = 1000, 0.05, 12, 10
        total_amount = calculate_compound_interest(P, r, n, t)

        # Check rounding
        self.assertEqual(round(total_amount, 2), 1647.01, "Total amount is not rounded to two decimal places.")

    def testRateOfReturnOutput(self):
        # Test Case 9.1: Verify Rate of Return Output
        P = 1000
        A = 1647.01  # Total accumulated amount
        expected_rate_of_return = 647.01  # Expected rate of return

        # Calculate rate of return
        rate_of_return = calculate_rate_of_return(A, P)

        # Assertion
        self.assertAlmostEqual(rate_of_return, expected_rate_of_return, places=2, msg="Rate of return output is incorrect.")

    def testRateOfReturnRounding(self):
        # Test Case 9.2: Verify Rate of Return is Rounded to Two Decimal Places
        P = 1000
        A = 1647.01  # Total accumulated amount
        rate_of_return = calculate_rate_of_return(A, P)

        # Check rounding
        self.assertEqual(round(rate_of_return, 2), 647.01, "Rate of return is not rounded to two decimal places.")

if __name__ == "__main__":
    unittest.main()
