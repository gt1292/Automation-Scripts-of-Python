from sys import *
import os
import hashlib
import time


def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    icnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
    else:
        print("No Duplicate Found")


def hashfile(path, blocksize=1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current Folder is :"+dirName)

            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")


def PrintResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicate Found :")
        print("The Following files are identical")

        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No Duplicate Found")


def main():
    print("-------------Marvellous Infosystem Scripts--------------")

    print("Application name :"+argv[0])

    if (len(argv) != 2):
        print("Error : invalid number of arguments")

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print(
            "This script is used to traverse specific directory and display Duplicate files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()
    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        PrintResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.' % (endTime-startTime))

    except ValueError:
        print("ERROR : invalid datatype of input")

    except Exception as E:
        print("ERROR : Invalid input", E)


if __name__ == "__main__":
    main()

