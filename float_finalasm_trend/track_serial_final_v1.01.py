import pandas as pd
import os
import sys

col_names = ['Date', 'Serial','Status','Result','CODE1','Status1','CODE2','Status2','MC','CELL','S1','S2','S3','S4','S5','S6','S7','S8','AVG']

ser_df = pd.DataFrame()

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

        try:
        
            dirs = os.path.join(filepath, item)
            
            df = pd.read_csv(dirs, names=col_names, engine='python', encoding ='utf-8')
            
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

            #serial = ['XHG030UD', 'XHG0D2JD']
            serial = ['1EKDJDLZ','X0GDDEKC','X0GAZYXC',
                      '1EKHVZDZ','X0GDH6KC','X0GB02NC',
                      'QGJTX1BT','QGJT99LT','X0GD0XUC',
                      'QGJUKMET','QGJTJ55T','X0GB02BC',
                      'QGJUKJET','VFG3X4GD','X0GDHNPC',
                      'QGJUETXT','1EKJLK9Z','D5GDBXNL',
                      'X0GB02HC','QGJTJ2KT','QGJTJ48T',
                      'QGJUKSDT','1EKJJM6Z','QGGM6SAT',
                      'QGGUVTMT','QGJV2B3T']
            
            serial_s = [' ' + s for s in serial]
            
            #print(serial_s)
            

            for s in serial_s:
                #print(s)
                #print(df)
                
            #serial = ' ' + '1EKDJDLZ'
            
            #serial = ' ' + 'XHG030UD'
            
            #serial = ' ' + '1EG9XVAZ'
            
                
                df1 = df.loc[df['Serial'] ==  s]
                
                if df1.empty:
                    print(dirs)
                    #pass
                else:
                    print(dirs)
                    #print(df1)
                    #pass
                    ser_df = ser_df.append(df1)
                    
            
            #print(df1)
            
            
            
            
            #ser_df.to_csv(r'C:\Users\1000262917\Desktop\MC_LINE34\track_serial.csv', index = False)
            #break
        #break
        except Exception as e:
            print(f"Error: {e}")

print(ser_df)
ser_df.to_csv(r'C:\Users\1000262917\Desktop\MC_LINE34\track_serial.csv', index = False)



        
    
