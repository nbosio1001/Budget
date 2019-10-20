# Editing Budget.xlsx Project using openpyxl
# Use https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
# for tutorial

#This is the original Budget File, Placed as a textfile.


import pandas as pd
import matplotlib.pyplot as plt

excelfilepath=r'C:\Users\Nick Bosio\Documents\Budget\Budget.xlsx' #Store this info in the cloud.
df=pd.read_excel(excelfilepath,sheet_name='June 2019') # Reads Excel and imports into dataframe

df.columns=df.iloc[0,:] # Uses the first index as the column title
df.drop(df.index[0], inplace=True) # Drops the first row, there is still an issue with the index not resetting (ie Index starts at 1 instead of 0)
df.Amount=pd.to_numeric(df.Amount) # Changes Amount column from an object to a float64

amount=df['Amount'] # Creates a individual dataframe from 'Amount' Column
description=df['Description'] # Creates a individual dataframe from 'Description' Column
 
     
 
expenses_dict = {
    'Groceries': [
        'VONS',
        'RALPHS',
        'Ralphs',
        'PAVILIONS',
        'FOOD4LESS',
        'TRADER JOE\'S',
        'GROCERY OUTLET',
        'FOOD 4 LESS',
        'SPROUTS',
        'MARKET@WORK'
        ],
    'Rent and Utilities': [
         'Rent',
         'Gas',
         'Internet',
         'Water',
         'Electricity'
         ],
     'Transportation': [
             'METROLINK',
             'EXXONMOBIL',
             'GAS',
             'UNION 76',
             'DMV',
             'OIL'
             ],
     'Housing Supplies': [
             'LOWE\'S',
             'RITE AID'
             ],
     'Car Maintenance': [
             'SMOG'
             ],
     'Clothes': [
             'NIKE'
             ],
     'Going Out': [
             '85C',
             'RESTAURA',
             'COSTCO',
             'SUBWAY',
             'IN N OUT',
             'Starbucks',
             'PIZZA'
             ],
     'Salary': [
             'AEROTEK'
             ]
     }
 
 
keys=expenses_dict.keys() # Gets the keys from the expenses dictionary
values=expenses_dict.values() # Gets values from expenses dictionary

keys=list(keys) # Cleans up keys and places in list
values=list(values) # Cleans up values and places in list
 
 
charge_amount=[]
other_amount=[]
 
joined_string=['|'.join(value) for value in values] #List Input, Outputs string with | between strings

descript_bool_check=[]
category_amount_check=[]
 
for value in joined_string:
    #joined_string='|'.join(value) #List Input, Outputs string with | between strings
    descript_bool=description.str.contains('\b'+value or value+',' or ', '+value or value,na=False,case=False)
    descript_bool_check.append(descript_bool)
    category_amount=df.loc[descript_bool,'Amount'].sum()
    category_amount_check.append(df.loc[descript_bool,'Amount'].sum())
    clean_output=float(abs(round(category_amount,2)))
    charge_amount.append(clean_output) #Escape code is used: \b
    # pandas.Series.str.contains
    # Series is a one-dimensional labeled array capable of holding any data type (integers, strings,)    
    other_amount=abs(round(df.loc[~description.str.contains('\b'+value or value+',' or ', '+value or ' '+value+' ',na=False,case=False),
                                  'Amount'].sum(),2))
 #print(list(charge_amount))
 #print(list(expenses_dict.keys()))
cool=dict(zip(list(expenses_dict.keys()),charge_amount))
cool['Other Amount']=other_amount
 #print(cool.dtypes)
 
 
 
''' Looks at the dataframe with the column title 'Description'. \b is a escape code. There may be a problem with using escape codes (\b). But if I remove the escape\
code, then there is a problem with example gas being in vegas.'''
 
 #Plotting data in chart
 #https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
 
labels=cool.keys()
expense_chart_sizes=[list(cool.values())] #Size of pie chart section
 #colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']
 
fig1,ax1=plt.subplots()
ax1.pie(expense_chart_sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.legend()
plt.show()
 #return plt.show()
 
 #plt.pie(cool.values(),labels=cool.keys())
 #plt.axis('equal')
 #plt.show()