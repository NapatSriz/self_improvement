import psutil
import time
import logging
import os
import urllib.request
from os import path
import mysql.connector
import sys
import subprocess





while True:        
    process_ls = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        #print(proc.name())
        process_ls.append(proc.name())
        if 'Convert_file_Cleaner' in proc.info['name']:
            try:
                mydb = mysql.connector.connect(
                host="10.144.134.163",
                database="cleaner_log",
                user="AK800",
                passwd="zaq12wsx"
               )
                #print(mydb)
                print("DATABASE Connected")
            except Exception as e:
                logging.error(str(e))
                print("Cannot connect to DATABASE")
                proc.kill()
                os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\Convert_file_Cleaner.exe')
    if not 'Convert_file_Cleaner.exe' in process_ls:
        os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\Convert_file_Cleaner.exe')
        print("Program Re-Open")
    else:
        print("Program Openning")

    time.sleep(1)
    

        
            
            
      
