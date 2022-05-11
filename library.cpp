#include <iostream>
#include <vector>
#include <string>

void flushCin() 
{
std::cin.clear();
fflush(stdin);
std::cin.ignore(10000, '\n');
}
std::string formOutput(std::string student, std::string student2) 
{
    std::string temp;
    temp.append(student);
    temp.append(" HAS ");
    temp.append(student2);
    temp.append("'s BOOK");

    return temp;
}

int main() 
{
    unsigned int cases;
    std::cin >> cases;

    char space {' '}; //As a delimiter for cin
    std::string turns {"TURNS"};
    std::string in {"IN"};
    std::string book{"BOOK"};
    
    std::string absentStudent;
    int returns {0};
    std::vector<std::string> presentStudents;
    std::vector<std::string> booksIn;

    std::vector<std::string> output;

    for ( int i {0}; i < cases; i++ )
    {
        std::string presentStudent;
        std::string bookIn;

        flushCin();
        std::cin >> absentStudent >> returns;
        
        for ( int i {0}; i < returns; i++ )
        {    
            flushCin();
            std::cin >> presentStudent >> space >> turns >> space >> in >> space >> presentStudent >> space >> book;
            for (int i {0}; i < 2; i++) { bookIn.pop_back(); } //Remove "'s" from the string
        
            booksIn.push_back(bookIn);
            presentStudents.push_back(presentStudent);
        }   

        for ( int i {0}; i < booksIn.size(); i++ ) 
        {
            for ( int x {0}; x < presentStudents.size(); x++ )
            {
                if ( booksIn.at(i) == presentStudents.at(x) ) 
                {
                    booksIn.erase(booksIn.begin() + i);
                    presentStudents.erase(presentStudents.begin() + x);
                }
            }

        }

        output.push_back(formOutput(absentStudent, presentStudent.at(0)));
    }



    return 0;
}