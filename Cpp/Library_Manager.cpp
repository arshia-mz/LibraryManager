//includding the libraries
#include <iostream>
#include <string>
#include <stdlib.h>
#include "sqlite3.h"
#include <time.h>
using namespace std;

//id generator
int IdGenerator()
{
    int rnd = rand()%1000;
    return rnd;
}

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
void Book::AddBook(string BookName,string Type,int Year){
    this->BookName = BookName;
    this->Type = Type;
    this->year = Year;
    this->BookId = IdGenerator();
}

void Book::ShowAll()
{
    cout<<BookId<<" | "<<this->BookName<<" | "<<this->Type<<" | "<<this->year<<endl;
}
void Book::RemoveBook(string BookName)
{
    //deleting from db
}
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
    bool SignUp(string UserName,string Password);
    void search(string BookName);
    void Get(bool give);
    void Return(bool give);
    void ShowAll();
};

void User::SignIn(string Name,string UserName,string Password)
{
    this->UserName = UserName;
    this->Password = Password;
    this->Name = Name;
    this->Id = IdGenerator();
    /*adding to the db files */
}

bool User::SignUp(string UserName,string Password)
{
    for(int i = 0 ; i < 2 ; i++)
    {
        
        /*search in db*/
        
    }
    return false;
}
void User::ShowAll()
{
    book.ShowAll();
}
class Admin : public User
{
public:
    bool SignUp(string UserName,string Password);
    void AddBook(string BookName,string Type,int Year);
    void RemoveBook(string BookName);
    /*Admin user & pass*/
    string AdminUserName [2] = {"Arshia85","AMZ"};
    string AdminPassword [2] = {"Arshia85","AMZ"};
};

bool Admin::SignUp(string UserName,string Password)
{
    for(int i = 0 ; i <2  ; i++)
    {
        if (UserName == this->AdminUserName[i] && Password == this->AdminPassword[i])
           {
               return true;
           }
    }
      return false; 
}
void Admin::AddBook(string BookName,string Type,int Year)
{
    this->book.AddBook(BookName,Type,Year);
}

void Admin::RemoveBook(string BookName)
{
    this->book.RemoveBook(BookName);
}

int main()
{
    Admin user;
    user.AddBook("love","romance",2022);
    user.ShowAll();
}