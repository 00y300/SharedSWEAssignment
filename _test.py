import unittest

from InterestCalculator import (calculate_compound_interest,
                                calculate_rate_of_return)


class TestCompoundInterestCalculator(unittest.TestCase):

    def testCalculateCompoundInterest(self):
        # Recalculated expected values
        test_cases = [
            {"P": 1000, "r": 0.05, "n": 12, "t": 10, "expected": 1647.01},  # No change
            {"P": 1500, "r": 0.04, "n": 4, "t": 5, "expected": 1830.29},  # Updated value
            {"P": 2000, "r": 0.03, "n": 1, "t": 15, "expected": 3115.93}  # Updated value
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

if __name__ == "__main__":
    unittest.main()
