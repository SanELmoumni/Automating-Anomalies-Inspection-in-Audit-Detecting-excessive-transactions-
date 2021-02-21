"""
# This script is used to generate randomly a file, containing informations about the employees transactions.

## For confideltiality purposes, i didn't share the original file !

We will need informations such as the employee's ID, the amount and the date of the transaction.

This file be used in the `anomaly_transactions.ipynb` notebook, to detect employees who exceeded 3 transactions per 10 days, because this is considered as a suspicious act and an anomaly.

Check the `README` repo's file for more details !
"""

import pandas as pd
import random
from random import randrange
from datetime import timedelta, datetime

while True:
    n = int(input("How many lines to generate ?"))
    if n <= 1000000 and n>0:
        break;
        
ids = []
nb_id = int(n/2)

# Function will be used to generate random dates. 

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
 

cols = ["employee_ID", "Amount", "Date"]
df = pd.DataFrame(columns = cols)

#Generating random IDs

for i in range(n):
    line_id = random.randint(1,nb_id)
    line_amount = random.randint(1000, 50000)
    
    d1 = datetime.strptime('1/1/2020', '%d/%m/%Y')
    d2 = datetime.strptime('31/1/2020', '%d/%m/%Y')

    line_date = random_date(d1, d2)

    new_row = {cols[0]:line_id, cols[1]:line_amount, cols[2]:line_date}
    df = df.append(new_row, ignore_index=True)

print(df)

df.to_excel("Generated_file.xlsx",header=True,index=None)