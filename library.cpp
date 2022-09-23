#include <iostream>
#include <vector>
#include <string>

void flushCin() 
{
std::cin.clear();
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

    std::string absentStudent;
    std::string presentStudent;
    std::string bookIn;
    std::string input;

    std::vector<std::string> students;
    std::vector<std::string> booksIn;
    std::vector<std::string> output;
    int returns {0};


    for ( int i {0}; i < cases; i++ )
    {

        flushCin();
        std::getline(std::cin, input);
        
        absentStudent = input.substr(0, input.find(" "));
        input.erase(0, input.find(" ") + 1);
        std::string returnsStr = input.substr(0, input.find(" "));
        returns = std::stoi(returnsStr);
        students.push_back(absentStudent);

        for ( int i {0}; i < returns; i++ )
        {    
            flushCin();
            std::getline(std::cin, input);
            //Set up a similar string-splitting system as above to get the present student and the book they're turning in.
            for (int i {0}; i < 2; i++) { bookIn.pop_back(); } //Remove "'s" from the string
        
            booksIn.push_back(bookIn);
            students.push_back(presentStudent);
        }   

        for ( int i {0}; i < booksIn.size(); i++ ) 
        {
            for ( int x {0}; x < students.size(); x++ )
            {
                if ( booksIn.at(i) == students.at(x) ) 
                {
                    booksIn.erase(booksIn.begin() + i);
                    students.erase(students.begin() + x);
            }
            }

        }

        
        output.push_back(formOutput(absentStudent, students.at(0)));
    }

    for ( int k {0}; k < output.size(); k++ ) 
    {
        std::cout << output.at(k);
        std::cout << "\n";
    }

    return 0;
}