import pandas as pd
import os

col_names = ['Date', 'Serial','Status','Result','CODE1','Status1','CODE2','Status2','MC','CELL','S1','S2','S3','S4','S5','S6','S7','S8','AVG']

path = r'\\10.144.134.139\engdata'
#path = r'C:\Users\1000262917\Desktop'

mc_folder = list(filter(lambda x: 'MC' in x, os.listdir(path)))

print('Directory:',path)
print('----------------------------------------------------------------------')

for filename in mc_folder:
    filepath = path + '\\' + filename
    #print(filepath)
    file = list(filter(lambda x: 'HDD' in x, os.listdir(filepath)))
    #print(file)
    for item in file:
        
        dirs = os.path.join(filepath, item)
        
        df = pd.read_csv(dirs, names=col_names)
        
        #print(df['Serial'].head())
        
        """ print(df)
        
        print(df['Serial'].head())
        
        df1 = df['Serial']
        
        x = df1.iloc[0]
        
        y = ' XHG030UD'
        
        
        if x == y:
            print('1')
        else:
            
            print(f"x is {x}")
            print(f"y is {y}")
            print('0') """
            
        serial = ' ' + '1EKDJDLZ'
        
        #serial = ' ' + 'XHG030UD'
        
        #serial = ' ' + '1EG9XVAZ'
        
            
        df1 = df.loc[df['Serial'] ==  serial]
        
        if df1.empty:
            print(dirs)
        else:
            print(dirs)
            print(df1)
        
        #print(df1)
        
        
        
        

        #break
    #break



        
    