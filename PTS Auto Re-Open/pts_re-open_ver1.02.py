import psutil
import time
import logging
import os
import urllib.request
from os import path

try:
    drives = os.listdir('z:\\')
    print(drives)
except Exception as e:
    logging.error(str(e))

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

        #print(chk_process)
        #print(type(chk_process))
        print(chk_process['name'])
    
    except Exception as e:
        #os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
        logging.error(str(e))
        print('Re-open program')
        
    
    if connect():
        print("Internet Connected")
        
        try:
            drives = os.listdir('t:\\')
            #print(drives)
        except Exception as e:
            logging.error(str(e))
            print("Line Send -> Connot connect to MapDrive.")
        
    else:
        print("Line Send -> Cannot connect the internet.")
    time.sleep(1)
    break
 