# coding: utf-8
import csv
from pathlib import Path


# "Part 1: Automate the Calculations"

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} number of loans.")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
total_loans = sum(loan_costs)
print(f"The total amount of the loans are ${total_loans}")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
average_loan_amount = sum(loan_costs) / len(loan_costs)
print(f"The averge loan amount  is ${average_loan_amount}.") 



# "Part 2: Analyze Loan Data" 
 # Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!
print(loan.get("future_value"))
print(loan.get("remaining_months"))

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# YOUR CODE HERE!
loan_price = 500
remaining_months = 9
future_value = 1000
discount_rate = 0.20

present_value = future_value / (1 + (discount_rate/12))**remaining_months
print(f"Present value is ${present_value:.2f}")


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
if present_value >= loan_price: 
    print("Take the loan, it is worth at least the cost to buy it")
else:
    print("This loan is too expensive and not worth the price to borrow.") 



  # "Part 3: "Perform Financial Calculations"
# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!
future_value = 1000
remaining_months = 12
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    
    return present_value 
      
# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
annual_discount_rate = 0.20 
calculate_present_value(future_value, remaining_months, annual_discount_rate)
present_value = calculate_present_value(       
        new_loan["future_value"], 
        new_loan["remaining_months"], 
        annual_discount_rate)
new_loan_present_value = present_value

print(f"The present value of the loan is: ${new_loan_present_value:.2f}")
#print(f"The present value of the loan is: {present_value}")  