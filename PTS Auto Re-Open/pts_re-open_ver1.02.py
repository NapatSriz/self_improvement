import psutil
import time
import logging
import os
import urllib.request
from os import path


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
    except Exception as e:
        #os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
        logging.error(str(e))
        print('Re-open program')
        
        try:
            drives = os.listdir('z:\\')
            #print(drives)
        except Exception as e:
            logging.error(str(e))
            
        
    time.sleep(1)
    break
 