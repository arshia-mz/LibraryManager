#Libraries
import random
import sqlite3

#Admins #you Change to every UserPass you Want
AdminUserName = ['arshia','***']
AdminPassWord = ['arshia','***']

#id generator
def IdGenerator():
    rnd = random.randint(0,100)
    return rnd


BookData = sqlite3.connect('Data/Book.db')
UserData = sqlite3.connect('Data/Users.db')
Bookcursor = BookData.cursor()
Usercursor = UserData.cursor()
#the classes 
class Book():
    def __init__(self):
        self.BookId = None
        self.BookName = ""
        self.Type = ""
        self.Year = 0
        self.give = False
    def AddBook(self,BookName,Type,Year):
        self.BookName = BookName
        self.Type = Type
        self.Year = Year
        self.BookId = IdGenerator()
        Bookcursor.execute("INSERT INTO book (id,name,type,year,count,give) VALUES(?,?,?,?,?,?);",(self.BookId,self.BookName,self.Type,self.Year,0,'False'))
        BookData.commit()
    def RemoveBook(self,BookName):#function for deletting the Data from Data Base
        self.BookName = BookName
        Bookcursor.execute('DELETE FROM book WHERE name=?;',(self.BookName))
    def search(self,BookName):
        Bookcursor.execute('SELECT * FROM book WHERE name=?;', (BookName))
    def ShowAll(self):
        Bookcursor.execute('SELECT * FROM book;')
        result = Bookcursor.fetchall()
        for i in result:
            print(f'{i[0]} | {i[1]} | {i[3]}')
    def getBook(self,BookName):
        Bookcursor.execute("""
            UPDATE book 
            SET give = True, 
                count = count + 1 
            WHERE name = ? AND give = False
        """, (BookName))
        BookData.commit()
    def returnBook(self,BookName):#problem is not work
        Bookcursor.execute("""
            UPDATE book 
            SET give = Ture, 
                count = count + 1 
            WHERE name = ? AND give = False
        """, (BookName))
        BookData.commit()
class User():
    def __init__(self):
        self.Name = ''
        self.Id = None
        self.UserName = ''
        self.Password = ''
        self.give = False
        self.book = Book()
    def SignUp(self,Name,UserName,Password):
        self.Name = Name 
        self.UserName = UserName
        self.Password = Password
        self.Id = IdGenerator()
        Usercursor.execute("""INSERT INTO users (id, name, username, password) VALUES (?, ?, ?, ?);""",(self.Id,self.Name,self.UserName,self.Password))
        UserData.commit()
    def SignIn(self,UserName,Password):
        Usercursor.execute("SELECT * FROM users WHERE username=? AND password=?", (UserName, Password))
        result = Usercursor.fetchone()
        if result:
            return True
        else:
            return False

    def search(self,BookName):
        self.book.search(BookName)
    def Get(self,BookName):
        self.book.getBook(BookName)
    def Return(self,BookName):
        self.book.returnBook(BookName)
    def ShowAll(self):
        self.book.ShowAll()
class Admin(User):
    def __init__(self):
        super().__init__()
    def SignIn(self,UserName,Password):
        for i,j in zip(AdminUserName,AdminPassWord):
            if i == UserName and j == Password:
                return True
        else:
            return False
    def AddBook(self,BookName,Type,Year):
        self.book.AddBook(BookName,Type,Year)
    def RemoveBook(self,BookName):
        self.book.RemoveBook(BookName)


def main():
    while True:
        idandity = input('chose your role (Amin(A),User(U)) for Exit(E): ')
        if(idandity.upper() == 'A'):
            admin = Admin()
            while True:
                UserName = input('Enter UserName: ')
                Password = input('Enter Password: ')
                if admin.SignIn(UserName,Password):
                    number = 0
                    print('Welcom')
                    while number != 7:
                        #pannel
                        print('Pannel: ' \
                        '1)AddBook'\
                        '2)RemoveBook'\
                        '3)GetBook'\
                        '4)ReturnBook'\
                        '5)ShowAll'\
                        '6)Search'\
                        '7)exit'
                        )
                        number = int(input(""))
                        if number == 1:
                            BookName = input("Enter BookName: ")
                            Type = input("Enter Type: ")
                            Year = int(input("Enter Year: "))
                            admin.AddBook(BookName,Type,Year)
                        if number == 2:
                            BookName = input("Enter BookName: ")
                            admin.RemoveBook(BookName)
                        if number == 3:
                            BookName = input("Enter BookName: ")
                            admin.Get(BookName)
                        if number == 4:
                            BookName = input("Enter BookName: ")
                            admin.Return(BookName)
                        if number == 5:
                            admin.ShowAll()
                        if number == 6:
                            BookName = input("Enter BookName: ")
                            admin.search(BookName)
                        if number == 7:
                            break
                else:
                    print ('UserName or Password is wrong')
        if(idandity.upper() == 'U'):
            while True:
                inup = input('Sign in (I) or sign up (U) , exite(E): ')
                user = User()
                if inup.upper() == 'U':
                    Name = input('Enter Name: ')
                    UserName = input('Enter UserName: ')
                    Password = input('Enter Password: ')
                    user.SignUp(Name,UserName,Password)
                if inup.upper() == 'I':
                    UserName = input('Enter UserName: ')
                    Password = input('Enter Password: ')
                    if user.SignIn(UserName,Password):
                        number = 0
                        print('Welcom')
                        while number != 5:
                            #pannel
                            print('Pannel: ' \
                            '1)GetBook'\
                            '2)Return'\
                            '3)ShowAll'\
                            '4)Search'\
                            '5)exite'
                            )
                            number = int(input(""))
                            if number == 1:
                                BookName = input("Enter BookName: ")
                                user.Get(BookName)
                            if number == 2:
                                BookName = input("Enter BookName: ")
                                user.Return(BookName)
                            if number == 3:
                                user.ShowAll()
                            if number == 4:
                                BookName = input("Enter BookName: ")
                                user.search(BookName)
                            if number == 7:
                                break
                    else:
                        print ('UserName or Password is wrong')
                if inup.upper() == 'E':
                    break
        if idandity.upper() == 'E':
            exit()
            
if __name__ == "__main__":
    main()