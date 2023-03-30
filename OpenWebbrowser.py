import webbrowser
import re
from urllib.request import urlopen
from sys import *

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def is_connnected():
    try:
        urlopen('http://google.com')
        return True
    except Exception as err:
        return False
    
def WebLauncher(path):
    with open(path) as fp:
        for line in  fp:
            url = Find(line)
            for str in url:
                webbrowser.open(str,new = 2)


def main():
    print("--------------Marvellous Infosystem--------------")
    
    print("Application Name :"+argv[0])
    
    if(len(argv)!= 2):
        print("ERROR : invalid number of arguments")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used for open links from file")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage:ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        connected = is_connnected()
        
        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to create to internet")
    except ValueError:
        pass


if __name__ == "__main__":
    main()