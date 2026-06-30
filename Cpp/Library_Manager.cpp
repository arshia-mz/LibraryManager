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
    static bool seeded = false;
    if (!seeded)
    {
        srand(time(0));
        seeded = true;
    }
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
    int count = 0;
    bool give = false;
    sqlite3 *db;
public:
    void AddBook(string BookName,string Type,int Year);
    void RemoveBook(string BookName);
    void search(string BookName);
    void getBook(int PersonId,string BookName);
    void returnBook(string BookName);
    void ShowAll();
};
void Book::AddBook(string BookName,string Type,int Year){
    this->BookName = BookName;
    this->Type = Type;
    this->year = Year;
    this->BookId = IdGenerator();
    
    sqlite3_open("../Data/Book.db",&db);
    
    // ✅ اول جدول بساز (اگه نبود)
    sqlite3_exec(db,
        "CREATE TABLE IF NOT EXISTS book (id INT, name TEXT, type TEXT, year INT, count INT, give TEXT);",
        NULL, NULL, NULL);
    
    sqlite3_stmt *stmt;
    sqlite3_prepare_v2(db,
        "INSERT INTO book (id,name,type,year,count,give) VALUES(?,?,?,?,?,?);",
        -1, &stmt, NULL);

    sqlite3_bind_int(stmt,  1, BookId);
    sqlite3_bind_text(stmt, 2, BookName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 3, Type.c_str(),     -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt,  4, Year);
    sqlite3_bind_int(stmt,  5, 0);
    sqlite3_bind_text(stmt, 6, "False",          -1, SQLITE_STATIC);

    sqlite3_step(stmt);
    sqlite3_finalize(stmt);
    sqlite3_close(db);
}

void Book::ShowAll()
{
    cout<<BookId<<" | "<<this->BookName<<" | "<<this->Type<<" | "<<this->year<<endl;
}
void Book::RemoveBook(string BookName)
{
    sqlite3_open("../Data/Book.db", &db);

    sqlite3_stmt *stmt;
    sqlite3_prepare_v2(db,
        "DELETE FROM book WHERE name=?;",
        -1, &stmt, NULL);

    sqlite3_bind_text(stmt, 1, BookName.c_str(), -1, SQLITE_STATIC);

    sqlite3_step(stmt);
    sqlite3_finalize(stmt);
    sqlite3_close(db);
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
    void SignIn(string Name,string UserName,string Password);
    bool SignUp(string UserName,string Password);
    void search(string BookName);
    void Get(bool give);
    void Return(bool give);
    void ShowAll();
};


void User::SignIn(string Name, string UserName, string Password)
{
    this->UserName = UserName;
    this->Password = Password;
    this->Name = Name;
    /*adding to the db files */

    sqlite3 *db;
    int rc = sqlite3_open("../Data/User.db", &db);
    if (rc != SQLITE_OK)
    {
        cerr << "Cannot open DB: " << sqlite3_errmsg(db) << endl;
        return;
    }

    // ساخت جدول در صورت نبودن
    const char *createTableSQL =
        "CREATE TABLE IF NOT EXISTS user (id INT, name TEXT, username TEXT, password TEXT);";
    sqlite3_exec(db, createTableSQL, NULL, NULL, NULL);

    // ----------- تولید ID یکتا -----------
    bool idExists = true;
    while (idExists)
    {
        this->Id = IdGenerator(); // یه ID جدید تولید کن

        sqlite3_stmt *checkStmt;
        const char *checkSQL = "SELECT COUNT(*) FROM user WHERE id=?;";

        rc = sqlite3_prepare_v2(db, checkSQL, -1, &checkStmt, NULL);
        if (rc != SQLITE_OK)
        {
            // اگه prepare fail بشه، اینجا متوقف می‌شیم تا crash نکنیم
            cerr << "Cannot prepare check statement: " << sqlite3_errmsg(db) << endl;
            sqlite3_close(db);
            return;
        }

        sqlite3_bind_int(checkStmt, 1, this->Id);

        if (sqlite3_step(checkStmt) == SQLITE_ROW)
        {
            int count = sqlite3_column_int(checkStmt, 0);
            // اگه count صفر بود یعنی این ID توی دیتابیس نیست -> یکتاست
            idExists = (count > 0);
        }
        else
        {
            idExists = false; // اگه مشکلی در query بود، فرض می‌کنیم یکتاست تا گیر نکنیم
        }

        sqlite3_finalize(checkStmt); // آزاد کردن statement چک کردن
    }
    // ------------------------------------------------

    // حالا که ID یکتا داریم، insert رو انجام بده
    sqlite3_stmt *stmt;
    const char *insertSQL =
        "INSERT INTO user (id, name, username, password) VALUES (?, ?, ?, ?);";
    rc = sqlite3_prepare_v2(db, insertSQL, -1, &stmt, NULL);
    if (rc != SQLITE_OK)
    {
        cerr << "Cannot prepare statement: " << sqlite3_errmsg(db) << endl;
        sqlite3_close(db);
        return;
    }

    sqlite3_bind_int(stmt, 1, this->Id);
    sqlite3_bind_text(stmt, 2, this->Name.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 3, this->UserName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 4, this->Password.c_str(), -1, SQLITE_STATIC);

    rc = sqlite3_step(stmt);
    if (rc != SQLITE_DONE)
    {
        cerr << "Insert failed: " << sqlite3_errmsg(db) << endl;
    }
    else
    {
        cout << "User registered successfully with ID: " << this->Id << endl;
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);
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
    
}