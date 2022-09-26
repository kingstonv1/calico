//Working (??)
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
    std::map<std::string, bool> m;
    int t;
    std::cin >> t;
    std::cin.ignore(1, '\n');

    for (int i = 0; i < t; i++) 
    {
        std::string input;
        std::string absentee;
        std::string missing;
        int returns;
        
        std::getline(std::cin, input);
        std::vector<std::string> inSplit = split(input);
        
        absentee = inSplit.at(0);
        returns = stoi(inSplit.at(1));
        
        for (int i = 0; i < returns; i++)
        {
            std::string input2;
            std::getline(std::cin, input2);
            std::vector<std::string> inSplit2 = split(input2);
            inSplit2.at(3).erase(inSplit2.at(3).length() - 2, 2); //Removes "'s" from the input name
            
            if (m.find(inSplit2.at(0)) == m.end()) //If the first name doesn't exist in the map
                { m.insert(std::make_pair(inSplit2.at(0), false)); }

            if (m.find(inSplit2.at(3)) == m.end()) 
                { m.insert(std::make_pair(inSplit2.at(3), true)); }
            else //If the book owner is already in the database
                { m[inSplit2.at(3)] = true; }
        }
        //Find the only key in the map with value "false"
        for (auto& it : m) 
        {
            if (it.second == false)
            missing = it.first;
        }
        
        output.push_back(absentee + " HAS " + missing + "'s BOOK\n"); //Unfinished line
    }

    for (std::string i : output) 
        { std::cout << i; }

    return 0;
}