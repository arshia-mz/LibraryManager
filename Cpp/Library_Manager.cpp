//includding the libraries
#include <iostream>
#include <string>

using namespace std;

//the classes
class Book
{
private:
    string BookName;
    int BookId;
    string Type;
    int year;
    bool give = false;
public:
    void AddBook(string BookName,string Type,int Year);
    void RemoveBook(string BookName);
    void search(string BookName);
    void ShowAll();
};

class User 
{
protected:
    int Id;
    string Name;
    string UserName;
    string Password;
    bool give = false;
    Book book;
public:
    void SignIn(string UserName,string Password,string Name);
    void SignUp(string UserName,string Password);
    void search(string BookName);
    void Get(bool give);
    void Return(bool give);
};


class Admin : public User
{
public:
    void AddBook(string BookName,string Type,int Year);
    void RemoveBook(string BookName);
};



