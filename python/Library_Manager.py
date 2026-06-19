#Libraries
import random


#Admins 
AdminUserName = ['Arshia85','AMZ']
AdminPassWord = ['Arshia85','AMZ']

#id generator
def IdGenerator():
    rnd = random.randint(0,100)
    return rnd

#the classes 
class Book():
    def __init__(self):
        self.BookId
        self.BookName
        self.Type
        self.Year
        self.give = False
    def AddBook(self,BookName,Type,Year):
        self.BookName = BookName
        self.Type = Type
        self.Year = Year
        self.BookId = IdGenerator()
    def RemoveBook(self,BookName):
        pass
    def search(self,BookName,Type,Year):
        pass
    def ShowAll(self):
        print(f'{self.BookId} | {self.BookName} | {self.Type} | {self.Year}')
class User():
    def __init__(self):
        self.Name
        self.Id
        self.UserName
        self.Password
        self.give = False
        self.book = Book
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
    pass


if main == __name__:
    pass