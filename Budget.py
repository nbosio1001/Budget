# Editing Budget.xlsx Project using openpyxl
# Use https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
# for tutorial

#This is the original Budget File, Placed as a textfile.

import os
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy
# Create SQL Database with my standard format


# Importing multiple files from same folder
path=r'C:\Users\Nick Bosio\Documents\Python\Budget_App\Transactions\\'
dirs = os.listdir(path)


#df_list=[]

#phone_reg='[\d\d\d\d][/or-][/d/d][/or-][\d\d\d\d]'
date_regex='\d{1,2}\/\d{1,2}\/\d{4}$' # $:end of line
# This would print all the files and directories
df_list=[]
location_list=[]
#date_as_first_row=[]
date=[]
for file in dirs:
    #print(file)
    file_name=path+file
    #print(file_name)
    df=pd.read_csv(file_name,header=None)
    df=df.dropna(axis='columns',how='all') # Drops columns that contain all nan values
    #df_list.append(df)
    #df_list.append(df)
    # =============================================================================
    location=df.apply(lambda col: col.astype(str).str.contains(date_regex).any(), axis=1)
    # df.apply(applies function, to row(axis=0) or column (axis=1) assigned)
    # Lambda function is a nameless function that requires an argument followed by a colon
    # Probably it is a ndarray, an N-dimensional array type which describes a collection of “items” of the same type
    # =============================================================================
    #location_list.append(location)
    dates_as_first_row=df[location] # Drops the dataframe to the first date value, KEEP!!!!
    
    # =============================================================================
    # THIS SECTION BELOW IS FOR GETTING ONLY THE DATE, DESCRIPTION, AND AMOUNT DATAFRAMES
    date_column=dates_as_first_row.filter(regex=date_regex,axis='columns')
    for date in dates_as_first_row:
        cool=dates_as_first_row[date]
        boolean_series=cool.str.contains(date_regex)
    a=boolean_series.index[boolean_series]
    interesting=pd.DataFrame(date)
#    print(type(WOAH))
    #print(type(date_as_first_row))
    # =============================================================================

    #date.append(date_as_first_row[date_as_first_row.Type==attempt])
# clean_df=date_as_first_row.drop([1],axis=1)

#clean_df=clean_df.rename(columns={0:'Date',2:'Description',7:'Amount'})
#
#clean_df.to_csv(r'C:\Users\Nick Bosio\Desktop\Testing.csv')
#
#print(location)

#print(range(len(df)))
#print(type(range(len(df))))

#for series in df:
#    print(type(series))
#    location=df.apply(lambda row: row.astype(str).str.contains('Year Ended' or 'December 31,').any(), axis=1)
##        descript_bool=series.str.contains(attempt,na=False,case=False)
#df_list.append(df)
    
    
    
#print(type(df_list[3].iloc[2].Datetime))

#   df=pd.read_csv(file)

# Import CSV file into Python Pandas, manipulate data, push into a new csv file

#excelfilepath=r'C:\Users\Nick Bosio\Documents\Budget\Budget.xlsx' #Store this info in the cloud.

def dataframe_creation():
    df=pd.read_excel(excelfilepath,sheet_name='June 2019') # Reads Excel and imports into dataframe
    
    df.columns=df.iloc[0,:] # Uses the first index as the column title
    df.drop(df.index[0], inplace=True) # Drops the first row, there is still an issue with the index not resetting (ie Index starts at 1 instead of 0)
    df.Amount=pd.to_numeric(df.Amount) # Changes Amount column from an object to a float64
    
    amount=df['Amount'] # Creates a individual dataframe from 'Amount' Column
    description=df['Description'] # Creates a individual dataframe from 'Description' Column

def sql_formatting():
    year=input("Input cell containing year: ")
    sql="('"+year+"-"+month+"-"+day+"','"+description+"','"+amount+"'),"
 
    
def dictionaries():
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
             'Internet',
             'Water',
             'Electricity'
             ],
         'Transportation': [
                 'METROLINK',
                 'EXXONMOBIL',
                 '\<GAS\>',
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
                 'AEROTEK, INC'
                 ]
         }

# Regex ^ [caret] and $ [dollar] symbol represent start and end of a line of text respectivaely
# Word-based version are \< and \>
 
def Big_function(): 
    keys=expenses_dict.keys() # Gets the keys from the expenses dictionary
    #print(keys)
    values=expenses_dict.values() # Gets values from expenses dictionary
    
    keys=list(keys) # Cleans up keys and places in list
    values=list(values) # Cleans up values and places in list
     
     
    charge_amount=[]
    other_amount=[]
     
    joined_string=['|'.join(value) for value in values] #List Input, Outputs string with | between strings
    
    descript_bool_check=[]
    category_amount_check=[]
    value_check=[]
     
    for value in joined_string:
        value_check.append(value)
        descript_bool=description.str.contains(value,na=False,case=False)
        #descript_bool=description.str.contains('\b'+value or value+',' or ', '+value,na=False,case=False)
        #print(type(descript_bool))
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

def matplotlib():     
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