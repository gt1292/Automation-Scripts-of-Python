import schedule
import time
import datetime

def Task_Minute():
    print("Task based on minutes scheduled at :",datetime.datetime.now())
    
def Task_Hours():
    print("Task based on Hours scheduled at :",datetime.datetime.now())
    
def Task_Day():
    print("Task based on Day scheduled at :",datetime.datetime.now())

def main():
    
    print("Inside Task Scheduler")
    print("Current time is :",datetime.datetime.now())
    
    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(1).hours.do(Task_Hours)
    schedule.every(1).saturday.at("18:00").do(Task_Day)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
    