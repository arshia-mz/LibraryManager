#the classes 
class Book():
    def __init__(self):
        self.BookId
        self.BookName
        self.Type
        self.Year
        self.give = False
    def AddBook(self,BookName,Type,Year):
        pass
    def RemoveBook(self,BookName):
        pass
    def search(self,BookName,Type,Year):
        pass
    def ShowAll():
        pass

class User():
    def __init__(self):
        self.Name
        self.Id
        self.UserName
        self.Password
        self.give = False
        self.book = Book
    def SignIn():
        pass
    def SignuP():
        pass
    def search():
        pass
    def Get():
        pass
    def Return():
        pass
class Admin(User):
    def __init__(self):
        super().__init__()
    def AddBook():pass
    def RemoveBook():pass
