def writehotel():
    with open('hotel.txt','a') as file:
        c = 'y'
        while c == 'y':
             Name = input("Enter name: ")
             idRoom = input("Enter id room : ")
             IdGuest = input("Enter the id of the guest : ")
             BookingDate = input("Enter the booking date : ")
             LeavingDate = input("Enter the leaving date : ")
             PhoneNumber = input("Enter the phone number : ")
             file.write(Name + '\t' + IdGuest + '\t' + idRoom + '\t'  + PhoneNumber + '\t' 
                        + BookingDate + '\t' + LeavingDate + '\n') 
             c = input("If you want to continue click (y / n)")
        print("File save succefully !!")

def readhotel():
         with open('hotel.txt','r') as file:
              print('Name   id guest   Id room   phone number   booking date    Leaving date')
              print('---------------------------------------------------------------------')
              for line in file:
                print(line)

def searchstudent():
    Name = input('Enter the  Name guest for search: ')
    with open('hotel.txt' , 'r') as file :
         flag = False 
         for line in file :
             Feilds = line.split('\t')
             if Feilds[0] == Name :
                 flag = True
                 print('Name   id guest   Id room   phone number   booking date    Leaving date')
                 print('---------------------------------------------------------------------')
                 print(line)
    if not flag :
        print('The guest not here ')
        

def Updatehotel():
    import os 
    file = open('hotel.txt' , 'r')
    Tempfile = open('TempFile.txt' , 'a')
    Name = input('Enter the name you want to update ')
    ch = False 
    for line in file :
        fields = line.split('\t')
        if fields[0] == Name :
            ch = True 
            NewName = input("Enter new name you want to update : ")
            line = NewName + '\t' + fields[1] + '\t' + fields[2]+ '\t' + fields[3] + '\t'  + fields[4] + '\t' + fields[5] + '\n'
        Tempfile.write(line) 
    file.close()
    Tempfile.close()
    os.remove('hotel.txt')
    os.rename('TempFile.txt' ,'hotel.txt')
    if not ch :
        print('The Name not found !! ')
    else :
        print('The Name is Updated succesfully ..... ')          


def DeleteRecord() :
    import os 
    Name = input('Enter the Name you want to delete : ') 
    file = open('hotel.txt' , 'r')
    TempFile = open('TempFile.txt' , 'w')
    flag = False
    for line in file :
        fields = line.split('\t')
        if fields[0] == Name :
            flag = True 
        else :
            TempFile.write(line)
    file.close()
    TempFile.close()
    os.remove('hotel.txt')
    os.rename('TempFile.txt' ,'hotel.txt')
    if not flag :
        print('The Name not found !! ')
    else :
        print('The Name  is deleted succesfully ..... ')


def home():
    c = 'y'
    while c == 'y' :
        print('1 : To write a record : ')
        print('2 : To read  records : ')
        print('3 : To search a record : ')
        print('4 : To update a record : ')
        print('5 : To delete a record : ')
        c = input('Enter your choice : ')
        if c == '1':
            writehotel()
        elif c == '2':
            readhotel()
        elif c == '3':
            searchstudent()
        elif c == '4' :
            Updatehotel()
        elif c == '5':
            DeleteRecord()
        else :
            print('Please enter a correct choice : ')
        c = input('Do you want another operation y/n')
    print('The mission done succesfully ....')
        
home()     
