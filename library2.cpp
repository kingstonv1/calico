//Working!
//A remaking of the library program.
#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <array>

std::vector<std::string> split(std::string &input)
{
    int i = 0;
    std::vector<std::string> inSplit;
    char d = ' ';
    while (input.find(d) != std::string::npos) 
    {
        inSplit.push_back(input.substr(0, input.find(d)));
        input.erase(0, inSplit.at(i).length() + 1);
        i++;
    }
    inSplit.push_back(input.substr(0, input.size()));
    return inSplit;
}

int main() 
{
    std::vector<std::string> output;
    int t;
    std::cin >> t;
    std::cin.ignore(1, '\n');

    for (int i = 0; i < t; i++) 
    {
        std::map<std::string, bool> m;
        std::string absentee;
        std::string returnsS;
        std::string missing;
        int returns;
        
        std::cin >> absentee >> returnsS;
        returns = stoi(returnsS);
        m.insert(std::make_pair(absentee, false));
        
        for (int i = 0; i < returns; i++)
        {
            std::string buf;
            std::string student;
            std::string book;

            //We only care about the student and book being turned in.
            std::cin >> student >> buf >> buf >> book >> buf; 
            
            book.erase(book.length() - 2, 2); //Removes "'s" from the input name

            if (m.find(student) == m.end()) 
                { m.insert(std::make_pair(student, false)); }

            if (m.find(book) == m.end())
                { m.insert(std::make_pair(book, true)); }
            else //If the book owner is already in the database
                { m[book] = true; }
        }
        //Find the only key in the map with value "false"
        for (auto& it : m) 
        {
            if (it.second == false)
            missing = it.first;
        }
        
        output.push_back(absentee + " HAS " + missing + "'s BOOK\n");
    }

    for (std::string i : output) 
        { std::cout << i; }

    return 0;
}