#include <iostream>
#include <vector>
#include <string>

size_t pos = 0;
std::string delimiter {" "};


std::vector<std::string> stringSplit( std::string s ) 
{
    std::vector<std::string > temp;

    while ((pos = s.find(delimiter)) != std::string::npos)
    { 
        temp.push_back(s.substr(0, pos));
        s.erase(0, pos + delimiter.length());
    }
    temp.push_back(s);
    
    return temp;
}

void printFrame( std::vector<std::string> vec ) 
{
    std::vector<std::string> temp;
    
    int maxSize {0};
    int currentSize {0};
    int extra {0};

    for ( long unsigned int i {0}; i < vec.size(); i++ ) 
    {
        if ( vec.at(i).size() > currentSize ) 
        { 
            maxSize = vec.at(i).size(); 
            currentSize = vec.at(i).size();
        }
    }

    for ( long unsigned int i {0}; i < vec.size(); i++ ) 
    {
        temp.push_back(vec.at(i));
    }
    
    vec.clear();
    std::string tempString(maxSize + 2, '*');
    vec.push_back(tempString);
    vec.push_back("\n");

    for ( long unsigned int i {0}; i < temp.size(); i++ ) 
    {
        vec.push_back(temp.at(i));
        vec.push_back("\n");
    }

    //This solution is garbage, but I don't want to use a deque.

    for ( long unsigned int i {1}; i < vec.size(); i++ ) 
    {
        if ( i % 2 == 0 ) 
        {
            extra = (maxSize - vec.at(i).size());
            extra++;
            vec.at(i).insert(vec.at(i).begin(), '*');
            std::string temporary((extra - 1), ' '); 
            vec.at(i).append(temporary);
            vec.at(i).append("*");
        }
    }
    vec.push_back(tempString);

    for ( long unsigned int i {0}; i < vec.size(); i++ ) 
    {
        std::cout << vec.at(i);
    }
}

int main() 
{
    unsigned int cases {0};
    std::cin >> cases;

    std::cin.ignore(1000, '\n');
    std::cin.clear();
    std::cin.sync();

    std::vector<std::string> inputs;
    std::string input;
    
    for ( long unsigned int i {0}; i < cases; i++) 
    {
        std::getline(std::cin, input);
        inputs.push_back(input);
        std::cin.clear();
        std::cin.sync();
    }

    std::cout << "\n";

    for ( long unsigned int i {0}; i < inputs.size(); i++)  
    {
        printFrame(stringSplit(inputs.at(i)));
        std::cout << "\n\n";
    }

    return 0;
}