import os

def CreateFile(FileName):
   
    if(os.path.exists(FileName)): #to check whether file is already in there
        print("File is Already Existing")
        return
    else:
        fd = open(FileName,"w")
    
def main():
    print("Enter name of file to create :")
    Name = input()
    
    CreateFile(Name)
    
if __name__ == "__main__":
    main()
    