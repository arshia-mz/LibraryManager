#Libraries
import random
import sqlite3

#Admins 
AdminUserName = ['Arshia85','AMZ']
AdminPassWord = ['Arshia85','AMZ']

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
    def search(self,BookName,Type,Year):
        pass
    def ShowAll(self):
        print(f'{self.BookId} | {self.BookName} | {self.Type} | {self.Year}')
    def getBook(self,BookName):
        pass
    def returnBook(self,BookName):
        pass
class User():
    def __init__(self):
        self.Name
        self.Id
        self.UserName
        self.Password
        self.give = False
        self.book = Book()
    def SignIn(self,Name,UserName,Password):
        pass
    def SignUp(self,UserName,Password):
        if self.UserName == UserName and self.UserName == Password:
            pass
    def search():
        pass
    def Get():
        pass
    def Return():
        pass
    def ShowAll(self):
        self.book.ShowAll()
class Admin(User):
    def __init__(self):
        super().__init__()
    def AddBook(self,BookName,Type,Year):
        self.book.AddBook(BookName,Type,Year)
    def RemoveBook(self,BookName):
        self.book.RemoveBook(BookName)


def main():
    book = Book()
    book.AddBook('The Sports','All',2015)


main()