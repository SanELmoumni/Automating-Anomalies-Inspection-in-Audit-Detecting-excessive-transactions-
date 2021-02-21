# Reminder !!!

# For confidentiality purposes, the data used in this notebook isn't real, but was generated randomly using the script (generate_random_data.py in the same repo).

import numpy as np
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import ExcelWriter
import xlsxwriter

# Reading the data.

# For better and clear results, I sorted the date in ascending order, using the employee's ID and then the transaction's date.

file_name = 'Generated_file.xlsx'
df = pd.read_excel(file_name, header=0)
print(df.dtypes)
#df.columns = ["ID",  "Montant",  "Date"]
#print(df.columns)
df.sort_values(["employee_ID","Date"],ascending=True, inplace=True)
#dfCopy = df.copy()

all_id = []
all_id = pd.unique(df["employee_ID"].sort_values())
print(len(all_id))

# Delete all employees who didn't knowing that we don't care if it's more or less than 3 days 
indexx = []
for i in range(len(all_id)):
    dfIndividu = df.query('employee_ID == {}'.format(all_id[i]))
    if dfIndividu.shape[0] <= 3:
        indexx.append(i)

print(len(all_id))
all_id = np.delete(all_id, indexx)
print(len(all_id))

dfCDF = pd.DataFrame(columns = ["employee_ID", "Amount", "Date"])
for i in all_id:
    temp = df.query('employee_ID == {}'.format(i))
    dfCDF = pd.concat([dfCDF,temp])

dfCDF['DateOp'] = pd.to_datetime(dfCDF['Date'], dayfirst=True)
#dfCDF['Date'] = pd.to_datetime(df['Date']) 
dfCDF = dfCDF.drop(['Date'], axis=1)
dfCDF.reset_index(drop=True, inplace=True)
print(dfCDF.query("employee_ID==101"))
print(dfCDF.dtypes)

for i in all_id :
    dfIndividu = dfCDF.query('employee_ID== {}'.format(i))
    dfIndividu.reset_index(drop=True, inplace=True)
    if( (dfIndividu['DateOp'].iloc[-1]- dfIndividu['DateOp'].iloc[0]).days < 10 and dfIndividu.shape[0]<=3):
        indexNames = dfCDF[ dfCDF['employee_ID'] == i].index
        dfCDF.drop(indexNames ,inplace=True)

all_id = []
all_id = pd.unique(dfCDF["employee_ID"].sort_values())
resultatFinal = pd.DataFrame(columns = ["employee_ID", "Depuis","Jusqu'au", "Montant Total"])
for i in all_id :
    #print(i)
    dfIndividu = dfCDF.query('employee_ID == {}'.format(i))
    dfIndividu.reset_index(drop=True, inplace=True)
    dateinit = dfIndividu['DateOp'].iloc[0]
    datefin = dfIndividu['DateOp'].iloc[-1]
    total = 0
    if (datefin - dateinit).days <= 10:
        total = dfIndividu['Amount'].sum()
        dfResult = pd.DataFrame({"employee_ID":[i],"Depuis":[dateinit],"Jusqu'au":datefin, "Montant Total":[total]})
        resultatFinal = pd.concat([resultatFinal,dfResult])
        continue
    else:
        k=0
        while(k < dfIndividu.shape[0]-1):
            dateinit = dfIndividu['DateOp'].iloc[k]
            total = dfIndividu['Amount'].iloc[k]
            l=k+1
            while(l < dfIndividu.shape[0] and (dfIndividu['DateOp'].iloc[l] - dateinit).days <= 10):
                #print("l = {}".format(l))
                total += dfIndividu['Amount'].iloc[l]
                l += 1
            dfResult = pd.DataFrame({"employee_ID":[i],"Depuis":[dateinit],"Jusqu'au":dfIndividu['DateOp'].iloc[l-1], "Montant Total":[total]})
            resultatFinal = pd.concat([resultatFinal,dfResult])
            k=l
            if(k==dfIndividu.shape[0]-1):
                break

resultatFinal['Du'] = resultatFinal['Depuis'].dt.strftime('%Y/%m/%d')
resultatFinal["Jusqu'a"] = resultatFinal["Jusqu'au"].dt.strftime('%Y/%m/%d')
resultatFinal = resultatFinal.drop(['Depuis',"Jusqu'au"], axis=1)
resultatFinal.reset_index(drop=True, inplace=True)
print(resultatFinal[0:20])
resultatFinal.to_excel("Montant10Jours.xlsx",header=True,index=None)