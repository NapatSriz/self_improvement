""" import csv

with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data) """

import pandas as pd

df_serial = pd.read_csv('serial.csv', names=['Serial'], header=None)

#print(df_serial)

serial_ls = df_serial.values.tolist()

#print(serial_ls)

for item in serial_ls:
    print(item)
    


col_names = ['Date', 'Serial','Status','Result','CODE1','Status1','CODE2','Status2','MC','CELL','S1','S2','S3','S4','S5','S6','S7','S8','AVG']

ser_df = pd.DataFrame()

path = r'C:\Users\1000262917\Desktop'

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
            
            