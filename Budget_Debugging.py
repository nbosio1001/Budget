# Editing Budget.xlsx Project using openpyxl
# Use https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
# for tutorial

import pandas as pd
import matplotlib.pyplot as plt
from expenses_dict import expenses_dict

excelfilepath=r'C:\Python3\Working with Excel files in Python/Budget.xlsx'
df=pd.read_excel(excelfilepath,sheet_name='June 2019')

df.columns=df.iloc[0,:]
df.drop(df.index[0], inplace=True)
pd.set_option('display.max_columns',None) #Dont know what this column does
#amount=df['Amount']
#description=df['Description']

    
expenses_dict=expenses_dict()



keys=expenses_dict.keys()
values=expenses_dict.values()
keys=list(keys)
values=list(values)


charge_amount=[]
other_amount=[]

joined_string=['|'.join(value) for value in values] #List Input, Outputs string with | between strings
bleh=[]

    # pandas.Series.str.contains
    # Series is a one-dimensional labeled array capable of holding any data type (integers, strings,) 
for value in joined_string:
    #joined_string='|'.join(value) #List Input, Outputs string with | between strings
    #description_expenses_boolean
    df['Boolean']=(df['Description'].str.contains('\b'+value,na=False,case=False))\
    |(df['Description'].str.contains(value+',',na=False,case=False))\
    |(df['Description'].str.contains( ', '+value,na=False,case=False))
    #if df['Boolean'] is True:
#        De.append(df.loc[df,'Amount'].sum()) #Label-based Location (oc)
#        Simone.append(float(abs(round(De,2))))
#        charge_amount.append(Simone) #Escape code is used: \b
        #charge_amount=df[df.loc[df,'Amount'].sum()]
#        '''https://stackoverflow.com/questions/47480320/how-to-add-a-multidimensional-dataframe-to-another-multidimensional-dataframe-as'''
    
#    else:
#        other_amount.append(abs(round(df.loc[df,'Amount'].sum(),2)))
#print(list(charge_amount))
#print(list(expenses_dict.keys()))
#print(charge_amount)
#cool=dict(zip(list(expenses_dict.keys()),charge_amount))
'''cool['Other Amount']=other_amount
print(cool)
'''


''' Looks at the dataframe with the column title 'Description'. \b is a escape code. There may be a problem with using escape codes (\b). But if I remove the escape\
code, then there is a problem with example gas being in vegas.'''

#Plotting data in chart
#https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
def pie_chart(cool):
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