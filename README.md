# Software Test Case Document  
## Compounded Interest Calculator Project  

### Test Cases  

#### 1. Input Requirements Test Cases  

- [ ] **SRD-003: The Compound Calculator Application shall provide an input of annual interest in decimal form.**  
  - [ ] **Test Case 3.1**: Ensure and validate the sentence of decimal form interest rates. Like `.05` for `5%`.  
  - [ ] **Test Case 3.2**: Ensure the input is valid. For example, the user should not be able to proceed with the application if the user submits a non-decimal value or a negative value.  
  - [ ] **Test Case 3.3**: Ensure the principal amount entered has a minimum value of two decimal places (hundredths place), i.e., `0.01`.  

- [ ] **SRD-004: Input of Principal Amount (decimal form)**  
  - [ ] **Test Case 4.1**: Validate acceptance of the principal amount in decimal form (e.g., `1000.00`).  
  - [ ] **Test Case 4.2**: Ensure invalid input (e.g., non-numeric characters, negative values) triggers an error message.  

#### 2. Data Processing Requirements  

- [X] **SRD-005: Calculation for Compounded Interest (`A = P(1 + r/n)^(nt)`)**  
  - [X] **Test Case 5.1**: Verify that the compounded interest calculation returns correct values for various inputs.  

- [X] **SRD-006: Calculation for Rate of Return (`Rate of Return = A - P`)**  
  - [X] **Test Case 6.1**: Validate that the rate of return is calculated correctly and displayed.  

- [X] **SRD-007 to SRD-011: Representation of Variables (A, P, r, n, t)**  
  - [X] **Test Case 7.1**: Ensure that the variable `A` (final amount) is accurately calculated and represented in the output.  
  - [X] **Test Case 7.2**: Verify that the principal amount `P` is stored and used accurately in calculations.  
  - [X] **Test Case 7.3**: Validate that `r`, `n`, and `t` variables are correctly processed and used in formulas.  

#### 3. Output Requirements  

- [X] **SRD-012: Total Output Value Including Interest**  
  - [X] **Test Case 8.1**: Ensure the application outputs the correct total output value.
  - [X] **Test Case 8.2**: Ensure the application’s output of total output value is contained within two (2) decimal places (hundredths).

- [X] **SRD-013: Rate of Return**  
  - [X] **Test Case 9.1**: Ensure the application outputs the correct rate of return.
  - [X] **Test Case 9.2**: Ensure the application’s output rate of return is contained within two (2) decimal places (hundredths).

#### 4. User Interface and Other Requirements  

- [ ] **SRD-001: User Interface by command line.**  
  - [ ] **Test Case 10.1**: Ensure and validate command line is used to complete user data inputs.  
  - [ ] **Test Case 10.5**: Ensure an option allows for re-entry in case of an incorrectly entered option.  
  - [ ] **Test Case 10.6**: Ensure the user may halt the sequence or application.  

- [ ] **SRD-002: User Interface to provide instructions.**  
  - [ ] **Test Case 10.2**: Ensure and validate instructions are printed prior to user input.  
  - [ ] **Test Case 10.7**: Ensure instructions contain options for re-entry.  
  - [ ] **Test Case 10.8**: Ensure instructions contain an option for halt/pause/stopping application from execution.  

- [ ] **SRD-014: User Interface with Windows OS.**  
  - [ ] **Test Case 10.3**: Ensure and validate application is executed on Windows operating system.  

- [ ] **SRD-015: Coding language Python.**  
  - [ ] **Test Case 10.4**: Ensure and validate application is a Python script (`.py`).  
