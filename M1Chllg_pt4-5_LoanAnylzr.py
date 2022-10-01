# coding: utf-8
import csv
from pathlib import Path 


#"Part 4: Conditionally filter lists of loans"
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for loan in loans: 
    if loan["loan_price"] <= 500: 
        inexpensive_loans.append(loan) 

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
print("The inexpensive loans of $500 or less are:", inexpensive_loans)  



# "Part 5: Save the results"
# Output this list of inexpensive loans to a csv file

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
with open (output_path, 'w' , newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for item in inexpensive_loans: 
        csvwriter.writerow(item.values()) 

print(item.values())
print(item.keys())
