import schedule
import time
import datetime

def fun():
    print("Inside fun")

def main():
    print("Inside Task Scheduler")
    
    schedule.every(1).minute.do(fun)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()