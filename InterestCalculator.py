import math

def display_instructions():
    print("Welcome to the Compound Interest Calculator!")
    print("This application calculates the compound interest based on the following formula:")
    print("A = P * (1 + r / n) ^ (n * t)")
    print("Where:")
    print("A = the amount of money accumulated after n years, including interest.")
    print("P = the principal amount (the initial investment).")
    print("r = the annual interest rate (in decimal form).")
    print("n = the number of times the interest is compounded per year.")
    print("t = the time the money is invested in years.")
    print()

def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_compound_interest(P, r, n, t):
    A = P * (1 + r / n) ** (n * t)
    return A

def calculate_rate_of_return(A, P):
    return A - P

def main():
    display_instructions()
    
    # Input
    P = get_input("Enter the principal amount (P): ")
    r = get_input("Enter the annual interest rate (r) in decimal form (e.g., 0.05 for 5%): ")
    n = get_input("Enter the number of times the interest is compounded per year (n): ")
    t = get_input("Enter the time in years (t): ")
    
    # Calculation
    A = calculate_compound_interest(P, r, n, t)
    rate_of_return = calculate_rate_of_return(A, P)
    
    # Output
    print(f"\nThe total amount after {t} years, including interest, is: ${A:.2f}")
    print(f"The rate of return is: ${rate_of_return:.2f}")

if __name__ == "__main__":
    main()
