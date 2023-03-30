import os

def DeleteFile(Filename):
    if(os.path.exists(Filename)): # if file doesn't contain data direct delete  
        size = os.path.getsize(Filename)
        
        if(size == 0): # if file contain data it will ask to delete
            os.remove(Filename)
        else:
            print("Are You Sure to Delete File ? Y/N")
            option = input()
            if(option == "Y" or option == "y"):
                os.remove(Filename)
            else:
                print("File Deletetion process stoped.")
                
    else:
        print("There is No such file")


def main():
    print("Enter name of file to Delete :")
    Name = input()
    
    DeleteFile(Name)
    
if __name__ == "__main__":
    main()
    