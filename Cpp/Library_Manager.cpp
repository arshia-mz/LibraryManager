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
    sqlite3 *db;
    int rc = sqlite3_open("../Data/Book.db", &db);
    if (rc != SQLITE_OK)
    {
        cerr << "Cannot open Book.db: " << sqlite3_errmsg(db) << endl;
        return;
    }

    // اطمینان از وجود جدول
    sqlite3_exec(db,
        "CREATE TABLE IF NOT EXISTS book (id INT, name TEXT, type TEXT, year INT, count INT, give TEXT);",
        NULL, NULL, NULL);

    sqlite3_stmt *stmt;
    const char *sql = "SELECT id, name, type, year, count, give FROM book;";
    
    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK)
    {
        cerr << "Cannot prepare statement: " << sqlite3_errmsg(db) << endl;
        sqlite3_close(db);
        return;
    }

    cout << "\n========== All Books ==========\n";
    cout << "ID\t| Name\t\t| Type\t| Year\t| Count\t| Give\n";
    cout << "-------------------------------------------------------\n";

    bool hasData = false;
    while (sqlite3_step(stmt) == SQLITE_ROW)
    {
        hasData = true;
        int id      = sqlite3_column_int(stmt, 0);
        const char* name = (const char*)sqlite3_column_text(stmt, 1);
        const char* type = (const char*)sqlite3_column_text(stmt, 2);
        int year    = sqlite3_column_int(stmt, 3);
        int count   = sqlite3_column_int(stmt, 4);
        const char* give = (const char*)sqlite3_column_text(stmt, 5);

        cout << id << "\t| " 
             << (name ? name : "") << "\t\t| " 
             << (type ? type : "") << "\t| " 
             << year << "\t| " 
             << count << "\t| " 
             << (give ? give : "") << endl;
    }

    if (!hasData)
    {
        cout << "No books found in database.\n";
    }

    cout << "================================\n";

    sqlite3_finalize(stmt);
    sqlite3_close(db);
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
    sqlite3 *db;
    int rc = sqlite3_open("../Data/User.db", &db);
    if (rc != SQLITE_OK)
    {
        cerr << "Cannot open DB: " << sqlite3_errmsg(db) << endl;
        return false;
    }

    // اطمینان از وجود جدول
    const char *createTableSQL =
        "CREATE TABLE IF NOT EXISTS user (id INT, name TEXT, username TEXT, password TEXT);";
    sqlite3_exec(db, createTableSQL, NULL, NULL, NULL);

    // جستجو برای یوزرنیم و پسورد
    sqlite3_stmt *stmt;
    const char *sql = "SELECT COUNT(*) FROM user WHERE username=? AND password=?;";
    
    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK)
    {
        cerr << "Cannot prepare statement: " << sqlite3_errmsg(db) << endl;
        sqlite3_close(db);
        return false;
    }

    sqlite3_bind_text(stmt, 1, UserName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, Password.c_str(), -1, SQLITE_STATIC);

    bool found = false;
    if (sqlite3_step(stmt) == SQLITE_ROW)
    {
        int count = sqlite3_column_int(stmt, 0);
        found = (count > 0);
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return found;
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
    while (true)
    {
        cout << "chose your role (Admin(A), User(U)) for Exit(E): ";
        string identity;
        cin >> identity;

        // تبدیل به حروف بزرگ
        for (char &c : identity) c = toupper(c);

        if (identity == "A")   // Admin
        {
            Admin admin;
            while (true)
            {
                string UserName, Password;
                cout << "Enter UserName: ";
                cin >> UserName;
                cout << "Enter Password: ";
                cin >> Password;

                if (admin.SignUp(UserName, Password))   // لاگین ادمین
                {
                    cout << "Welcome" << endl;
                    int number = 0;

                    while (number != 7)
                    {
                        cout << "\nPannel:\n"
                             << "1) AddBook\n"
                             << "2) RemoveBook\n"
                             << "3) GetBook\n"
                             << "4) ReturnBook\n"
                             << "5) ShowAll\n"
                             << "6) Search\n"
                             << "7) Exit\n";
                        cin >> number;

                        switch (number)
                        {
                        case 1:
                        {
                            string BookName, Type;
                            int Year;
                            cout << "Enter BookName: ";
                            cin >> BookName;
                            cout << "Enter Type: ";
                            cin >> Type;
                            cout << "Enter Year: ";
                            cin >> Year;
                            admin.AddBook(BookName, Type, Year);
                            break;
                        }
                        case 2:
                        {
                            string BookName;
                            cout << "Enter BookName: ";
                            cin >> BookName;
                            admin.RemoveBook(BookName);
                            break;
                        }
                        case 3:
                        {
                            string BookName;
                            cout << "Enter BookName: ";
                            cin >> BookName;
                            // admin.Get(BookName);   // اگر متد را پیاده کردید
                            break;
                        }
                        case 4:
                        {
                            string BookName;
                            cout << "Enter BookName: ";
                            cin >> BookName;
                            // admin.Return(BookName);
                            break;
                        }
                        case 5:
                            admin.ShowAll();
                            break;
                        case 6:
                        {
                            string BookName;
                            cout << "Enter BookName: ";
                            cin >> BookName;
                            // admin.search(BookName);
                            break;
                        }
                        case 7:
                            break;
                        default:
                            cout << "Invalid option!" << endl;
                        }
                    }
                    break; // از حلقه لاگین ادمین خارج شو
                }
                else
                {
                    cout << "UserName or Password is wrong" << endl;
                }
            }
        }
        else if (identity == "U")   // User
        {
            while (true)
            {
                cout << "Sign in (I) or sign up (U) , exit(E): ";
                string inup;
                cin >> inup;
                for (char &c : inup) c = toupper(c);

                User user;

                if (inup == "U")   // ثبت‌نام
                {
                    string Name, UserName, Password;
                    cout << "Enter Name: ";
                    cin >> Name;
                    cout << "Enter UserName: ";
                    cin >> UserName;
                    cout << "Enter Password: ";
                    cin >> Password;

                    user.SignIn(Name, UserName, Password);  // طبق کلاس فعلی شما ثبت‌نام است
                }
                else if (inup == "I")   // ورود
                {
                    string UserName, Password;
                    cout << "Enter UserName: ";
                    cin >> UserName;
                    cout << "Enter Password: ";
                    cin >> Password;

                    if (user.SignUp(UserName, Password))   // طبق کلاس فعلی شما لاگین است
                    {
                        cout << "Welcome" << endl;
                        int number = 0;

                        while (number != 5)
                        {
                            cout << "\nPannel:\n"
                                 << "1) GetBook\n"
                                 << "2) Return\n"
                                 << "3) ShowAll\n"
                                 << "4) Search\n"
                                 << "5) Exit\n";
                            cin >> number;

                            switch (number)
                            {
                            case 1:
                            {
                                string BookName;
                                cout << "Enter BookName: ";
                                cin >> BookName;
                                // user.Get(BookName);
                                break;
                            }
                            case 2:
                            {
                                string BookName;
                                cout << "Enter BookName: ";
                                cin >> BookName;
                                // user.Return(BookName);
                                break;
                            }
                            case 3:
                                user.ShowAll();
                                break;
                            case 4:
                            {
                                string BookName;
                                cout << "Enter BookName: ";
                                cin >> BookName;
                                // user.search(BookName);
                                break;
                            }
                            case 5:
                                break;
                            default:
                                cout << "Invalid option!" << endl;
                            }
                        }
                    }
                    else
                    {
                        cout << "UserName or Password is wrong" << endl;
                    }
                }
                else if (inup == "E")
                {
                    break;
                }
            }
        }
        else if (identity == "E")
        {
            break;
        }
        else
        {
            cout << "Invalid choice!" << endl;
        }
    }

    return 0;
}