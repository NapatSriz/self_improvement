import pandas as pd
import os

#s_date = input("Input Date From:")
#e_date = input("Input Date To:")

s_date = '20200101'
e_date = '20200310'

#col_names = ['Result','CELL','S1','S2','S3','S4','S5','S6','S7']
col_names = ['Result','S1','S2','S3','S4','S5','S6','S7','S8']

path = r'\\10.144.134.139\engdata'
#path = r'C:\Users\1000262917\Desktop'

#print(type(path))

main_df = pd.DataFrame(columns = ['float'],)
#print(main_df)

mc_folder = list(filter(lambda x: 'MC' in x, os.listdir(path)))

#print(mc_folder)

for filename in mc_folder:
    if int(filename[-2:]) >= 21:
        print(filename)
        filepath = path + '\\' + filename
        print(filepath)
        mc_ls_file = list(filter(lambda x: 'HDD' in x, os.listdir(filepath)))
        #print(len(mc_file))
        #print(mc_file[0])
        #print(mc_ls_file)
        for item in mc_ls_file:
            print(item[7:-8])
            y1 = item[7:-12]
            m1 = item[11:-10]
            d1 = item[13:-8]
            print(y1,m1,d1)
            if 
            break
        break
        '''for item in mc_ls_file:
            #print(item)
            mc_file_dir = (os.path.join(path, filepath, item))
            #print(mc_file_dir)
            #df = pd.read_csv(mc_file_dir, names=col_names,usecols=[2,9,10,11,12,13,14,15,16])
            df = pd.read_csv(mc_file_dir, names=col_names,usecols=[2,10,11,12,13,14,15,16,17])
            #print(df)
            #print(df.isnull())
            #df = df.dropna()       
            
            df = df[(df['Result'] == 33) | (df['Result'] == 34) | 
                    (df['Result'] == 35) | (df['Result'] == 36) |
                    (df['Result'] == 37) | (df['Result'] == 38) |
                    (df['Result'] == 39)] 
                    
            
            
            print(df)
            
            #break
                        
            #df = df[(df[['S8']] != 0).all(axis=1)]
            
            #print(df)'''
            
            
            
            
        break
    


        
    