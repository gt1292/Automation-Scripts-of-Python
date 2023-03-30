import psutil
from sys import*
import os
import time

def ProcessDisplay(log_dir = 'marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
        
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'wb')
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    for elemnt in listprocess:
        f.write("%s\n"%elemnt)
            
def main():
    print("Marvellous infosystem : Python and ML")
    
    print("Process Monitor with memory usage")
    print("Application name :"+argv[0])
    
    if(len(argv)!= 2):
        print("Error : Invalid number of arguments")

    try :
        ProcessDisplay(argv[1])
    except ValueError:
        print("ERROR: Invalid data type")
    except Exception:
        pass
    
    
if __name__ == "__main__":
    main()
    
    