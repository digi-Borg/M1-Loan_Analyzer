# M1-Valuing_MicroCredit_Loans 

![M1Title_Pic](./Pictures/M1TitlePic_2022-10-15003306.png) 

*"A Python program that automates tasks to value microcredit loans."* 

--- 
## Background 

A microcredit lending startup needs hired help in valuing loans. As the hired contract worker a decision is made to automate a process to automate loan calculations, analyze loan data, perform financial calculations, filter a list of loans and save the results.  

To analyze the loans detailed data for the loans are used to calculate present value(PV) or fair price, for each loans worth. A monthly version formula for present value is used to calculate the fair value of the loan. It requires a minimum return of 20% as the discount rate. 

The PV calculation is coded into a financial function to  perform future calculations on new loan data to consider.  The new data is a series of loans that needs filtering to find `inexpensive loans`. If the `loan price` is less than or equal to 500, it is appended to an `inexpensive_loans` ouput list. The list of `inexpensive loans` needs to be saved for the company's business analysts to a CSV file.   

---


---
#
## Technologies

The software operates on python 3.9 with the installation package imports embedded with Anaconda3 installation. The program code was developed using Visual Studio Code 1.72.2 in my first coding project effort.  

* [anaconda3](https://docs.anaconda.com/anaconda/install/windows/e)     
 
---

## Installation Guide

Before running the applications first activate the Conda development environment and launch JupyterLab to import the following required libraries apps. 

```python libraries
import csv
from pathlib import Path
 
``` 

---
#
## Usage

This program is run from `M1_pt1-3_LoanAnylzr.py` and `M1_pt4-5_LoanAnylzr.py` to deploy the Loan Analyzer in Visual Studio Code or Jupiter Notebook. `M1_pt1-3_LoanAnylzr.py` functions to 1) automate loan calculations; 2) analyze loan data; and 3) perform fincial calculations. `M1_pt4-5_LoanAnylzr.py` employs program function to 4) conditionally filter lists of loans and 5) save the results. 

```python 
M1_pt1-3_LoanAnylzr.py
M1_pt4-5_LoanAnylzr.py
```
 
---

## Contributors

*Provided to you by digi-Borg FinTek*, 
Dana Hayes: nydane1@gmail.com


--- 
#
## License  

Columbia U. Engineering 

#
[BSD 2-Clause LicenseCopyright (c) 2022, digi-Borg
All rights reserved.](/LICENSE)