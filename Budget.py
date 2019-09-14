# Editing Budget.xlsx Project using openpyxl
# Use https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
# for tutorial

import pandas as pd
import matplotlib.pyplot as plt
import pdb


df=pd.read_excel('Budget.xlsx',sheet_name='June 2019')
df.columns=df.iloc[0,:]
df.drop(df.index[0], inplace=True)
pd.set_option('display.max_columns',None) #Dont know what this column does
#print(df)
amount=df['Amount']
description=df['Description']

    

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
   'Utilities': [
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
            ]
    }


keys=expenses_dict.keys()
keys=list(keys)
#print(keys)
values=expenses_dict.values()
values=list(values)
print(values)

charge_amount=[]
for value in values:
    joined_string='|'.join(value) #List Input, Outputs string with | between strings
    charge_amount.append(abs(round(df.loc[df['Description'].str.contains('\b'+joined_string or joined_string+',' or ', '+joined_string,na=False),
                                 'Amount'].sum(),2))) #Escape code is used: \b
    # pandas.Series.str.contains
    # Series is a one-dimensional labeled array capable of holding any data type (integers, strings,)    
    other_amount=abs(round(df.loc[~df['Description'].str.contains('\b'+joined_string or joined_string+',' or ', '+joined_string or ' '+joined_string+' ',na=False),
                                 'Amount'].sum(),2))
#print(list(charge_amount))
#print(list(expenses_dict.keys()))
cool=dict(zip(list(expenses_dict.keys()),charge_amount))
cool['Other Amount']=other_amount
#print(cool)



''' Looks at the dataframe with the column title 'Description'. \b is a escape code. There may be a problem with using escape codes (\b). But if I remove the escape\
code, then there is a problem with example gas being in vegas.'''

#Plotting data in chart
#https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py

#labels='Groceries'+'\n'+str(abs(groc_amount)),'Other'+'\n'+str(abs(other_amount)) # Creates labels for pie pieces
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
