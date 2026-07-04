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
            SET give = False, 
                count = count + 1 
            WHERE name = ? AND give = True
        """, (BookName,))
        BookData.commit()
    def returnBook(self,BookName):
        pass
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
            print(f"Welcom {UserName}")
        else:
            print('This UserName or Password is Not Define')

    def search(self,BookName):
        self.book.search(BookName)
    def Get():
        pass
    def Return():
        pass
    def ShowAll(self):
        self.book.ShowAll()
class Admin(User):
    def __init__(self):
        super().__init__()
    def SignIn(self,UserName,Password):
        if AdminUserName == UserName and AdminUserName == Password:
            print(f'Welcome {UserName}')
        else:
            print('The password or user is wrong')
    def AddBook(self,BookName,Type,Year):
        self.book.AddBook(BookName,Type,Year)
    def RemoveBook(self,BookName):
        self.book.RemoveBook(BookName)


def main():
    pass


if __name__ == "__main__":
    main()