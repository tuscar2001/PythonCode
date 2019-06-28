import pandas as pd

df = pd.DataFrame({'DOB': {0: '26/1/2016', 1: '26/1/2016'}})
print (df)


df['DOB'] = pd.to_datetime(df.DOB)
print (df)
         DOB
0 2016-01-26
1 2016-01-26

df['DOB1'] = df['DOB'].dt.strftime('%m/%d/%Y')
print (df)
         DOB        DOB1
0 2016-01-26  01/26/2016
1 2016-01-26  01/26/2016

#Changing date type
test['dateChanged'] = test['date'].astype('datetime64[ns]')
