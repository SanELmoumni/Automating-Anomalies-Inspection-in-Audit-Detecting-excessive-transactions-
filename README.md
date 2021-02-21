# Automating Anomalies Inspection in Audit : Detecting excessive transactions !


![Suspicious behaviour, WARNING !](Images/Capture.PNG)

During my experience in the bank's internal audit, a special type of employees who committed more than 3 "super" transactions in their account represent a suspicious behaviour, and could be a very good target to focus more on them to detect the internal fraud.

For this, i created a script which takes as input a file, containing a dataset with informations about the employees, their transactions amount and date.

I use this file ```Generated_file.xlsx``` to feed it to a script, which detects the anomalies (the employees who commited more than 3 transactions), and returns an excel file ```Montant10Jours.xlsx```, which contains details as the total amount of the transactions, and the dates when the employee commited more than 4 transactions.

# NB : 

For confidentiality purposes, the data used in this notebook isn't real, but was generated randomly using the script ```generate_random_data.py```.

Text me if you need more details !echo # Automating-Anomalies-Inspection-in-Audit-Detecting-excessive-transactions-
