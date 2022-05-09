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

    for ( int i {0}; i < vec.size(); i++ ) 
    {
        if ( vec.at(i).size() > currentSize ) { maxSize = vec.at(i).size(); }
    }

    for ( int i {0}; i < vec.size(); i++ ) 
    {
        temp.push_back(vec.at(i));
    }
    
    vec.clear();
    std::string tempString(maxSize + 2, '*');
    vec.push_back(tempString);

    for ( int i {0}; i < temp.size(); i++ ) 
    {
        vec.push_back(temp.at(i));
    }

    //This solution is garbage, but I don't want to use a deque.

    for ( int i {1}; i < vec.size(); i++ ) 
    {
        vec.at(i).insert(vec.at(i).begin(), '*');
        extra = maxSize - vec.at(i).size();
        std::string temporary(extra - 1, ' ');
        vec.at(i).append(temporary);
        vec.at(i).append("*");
    }
    vec.push_back(tempString);

    for ( int i {0}; i < vec.size(); i++ ) 
    {
        std::cout << vec.at(i);
    }
}

int main() 
{
    unsigned int cases {0};
    std::cin >> cases;

    std::vector<std::string> inputs;
    std::string input;
    
    for (int i {0}; i < cases; i++) 
    {
        std::getline(std::cin, input);
        inputs.push_back(input);
    }

    for (int i {0}; i < inputs.size(); i++)  
    {
        printFrame(stringSplit(inputs.at(i)));
    }

    return 0;
}