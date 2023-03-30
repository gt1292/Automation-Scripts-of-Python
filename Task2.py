import schedule
import time
import datetime

def fun():
    print("Inside fun at the time :",datetime.datetime.now())

def main():
    print("Inside Task Scheduler")
    print("Current is :",datetime.datetime.now())
    
    schedule.every(1).minute.do(fun)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
    