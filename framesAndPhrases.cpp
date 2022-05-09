#include <iostream>
#include <vector>
#include <string>

int main() 
{
    unsigned int cases;
    std::cin >> cases;

    std::vector<std::string> inputs;
    std::string input;
    for (int i {0}; i < cases; i++) 
    {
    std::getline(std::cin, input);
    inputs.push_back(input);
    inputs.push_back("null");
    }

    for (int i {0}; i < inputs.size(); i++)  
    {
            
    }


    return 0;
}