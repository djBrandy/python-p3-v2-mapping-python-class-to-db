#!/usr/bin/env python3
# lib/testing/debug.py

import ipdb
from department import Department
from __init__ import CONN, CURSOR

# Create the Department table
Department.create_table()

# Create the Payroll department
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

# Create the Human Resources department
hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# Update the Human Resources department
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr) 
 # <Department 2: HR, Building F, 10th Floor>

# Delete the Payroll department
payroll.delete()  

# delete from db table, object still exists in memory
print(payroll) 

# <Department 1: Payroll, Building A, 5th Floor>
print("Delete Payroll")

# Start the debugger
ipdb.set_trace()

# Drop the Department table
Department.drop_table()
