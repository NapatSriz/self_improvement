import psutil
import time
import logging
import os
import urllib.request
from os import path

drives = os.listdir('z:\\')
print(drives)

def connect(host=r'http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

while True:
    process_ls = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            #print(pinfo)
            process_ls.append(pinfo)

    #print(process_ls)

    try:
        chk_process = next(item for item in process_ls if item["name"] == "notepad++.exe")

        print(chk_process)
        #print(type(chk_process))
        print(chk_process['name'])
    
    except Exception as e:
        #os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
        logging.error(str(e))
        print('Re-open program')
        
    
    if connect():
        print("Internet Connected")
        
    else:
        print("Line Send -> Cannot connect the internet.")
        

    time.sleep(1)
