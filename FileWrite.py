import os

def WriteFile(Filename):
    if(os.path.exists(Filename)):
       print("Enter the Data You want To write in file :")
       Data = input() 
       
       fd = open(Filename,"a")
       fd.write(Data)

    else:
        print("File is not exissting")
        return

def main():
    print("Enter name of file to create :")
    Name = input()
    
    WriteFile(Name)
    
if __name__ == "__main__":
    main()
    