import os

def ReadFile(Filename):
    if(os.path.exists(Filename)): 
       
       fd = open(Filename,"r")
       Data = fd.read()
       print("Data from file is:")
       print(Data)
       
       fd.close()

    else:
        print("File is not exissting")
        return

def main():
    print("Enter name of file to create :")
    Name = input()
    
    ReadFile(Name)
    
if __name__ == "__main__":
    main()
    