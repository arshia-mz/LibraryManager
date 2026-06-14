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
    /*Admin user & pass*/
    string AdminUserName [2] = {"Arshia85","AMZ"};
    string AdminPassword [2] = {"Arshia85","AMZ"};

public:
    void SignIn(string UserName,string Password,string Name);
    void SignUp(string UserName,string Password);
    void search(string BookName);
    void Get(bool give);
    void Return(bool give);
};

void User::SignIn(string Name,string UserName,string Password)
{
    this->UserName = UserName;
    this->Password = Password;
    this->Name = Name;
    /*adding to the db files */
}

void User::SignUp(string UserName,string Password)
{
    for(int i = 0 ; i < 2 ; i++)
    {
        if (UserName == this->AdminUserName[i] && Password == this->AdminPassword[i])
        {
            cout<<"Welcom"<<AdminUserName[i];
        }
        /*search in db*/
        else
        {
            cout<<"Not Found";
        }
    }
    
}
class Admin : public User
{
public:
    void AddBook(string BookName,string Type,int Year);
    void RemoveBook(string BookName);
};



int main()
{
    Admin user;
    string UserName ,Password;
    cin>>UserName;
    cin>>Password;
    user.SignUp(UserName,Password);
    
    
    
}