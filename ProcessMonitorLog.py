from sys import *
import os
import time
import psutil

def ProcessLog(log_dir='Automation Programs'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-"*80

    log_path = os.path.join(log_dir, "AutomationPrograms%s.log" % (time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous infosystem process logger :"+time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))

def main():
    
    print("--------Marvellous Infosystem------------")
    
    print("Application Name :"+argv[0])
    
    if(len(argv)!= 2):
        print("Error : Invalid number of arguments")

    try :
        ProcessLog(argv[1])
    except ValueError:
        print("ERROR: Invalid data type")
    except Exception:
        pass

if __name__ == "__main__":
    main()