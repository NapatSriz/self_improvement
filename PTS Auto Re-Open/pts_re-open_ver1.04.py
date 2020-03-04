import psutil
import time
import logging
import os
import urllib.request
from os import path
import mysql.connector


while True:        
    process_ls = []
    for proc in psutil.process_iter():
    #for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            #print(pinfo)
            process_ls.append(pinfo)

    print(type(process_ls))

    try:
        chk_process = next(item for item in process_ls if item["name"] == "notepad++.exe")
    except Exception as e:
        #os.startfile(r'C:\stock_part\PG\Convert_file_Cleaner.exe')
        os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
        logging.error(str(e))
        print('Open program')
        
        try:
            #drives = os.listdir('Z:\\')
            #print(drives)
            mydb = mysql.connector.connect(
            host="10.144.134.163",
            database="cleaner_log",
            user="AK800",
            passwd="zaq12wsx"
           )
            print(mydb)
                
        except Exception as e:
            logging.error(str(e))
            '''for proc in psutil.process_iter(attrs=['pid', 'name']):
                if 'Convert_file_Cleaner' in proc.info['name']:
                    proc.kill()
            os.startfile(r'C:\stock_part\PG\Convert_file_Cleaner.exe')'''
            for proc in psutil.process_iter(attrs=['pid', 'name']):
                if 'notepad++' in proc.info['name']:
                    proc.kill()
            os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
            
        
    time.sleep(1)
    #break
