import os
from sys import *


def Directory_Watcher(Dir_Name):
    print("Inside Watcher Method")
    print("Name of input Directory :", Dir_Name)

    for foldername, subfolder, Filename in os.walk(Dir_Name):
        print("Folder Name is :"+foldername)

        for sub in subfolder:
            print("subfolder name of "+foldername+" is "+sub)

        for fname in Filename:
            print("File inside folder "+foldername+" is "+fname)

        print(" ")


def main():
    print("Directory Watcher application")

    if (len(argv) < 2):
        print("Ivalid arguments")
        exit()

    if (argv[1] == "-h"):
        print("This Script will travel directory and display name of all entries")
        exit()

    if (argv[1] == "-u"):
        print("Usage : Application name Directory Name")
        exit()

    Directory_Watcher(argv[1])


if __name__ == "__main__":
    main()
