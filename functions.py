#Rolling dates
Method1
the data level is at key,datetime. I have to go back one level up in the group by
test['datediff'] = test['datetime'] - test.groupby(['key'])['datetime'].transform(lambda x: x.iloc[0])
test['datediff']=test['datediff'] / np.timedelta64(1,'D')

Method2
test['dur'] = test.groupby(['key']).datetime.apply(lambda x: x - x.iloc[0])
test['dur']=test['dur'] / np.timedelta64(1,'D')
