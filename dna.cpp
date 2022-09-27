//Working!
#include <iostream>
#include <vector>
#include <string>
#include <cstring>

int main() 
{
    std::vector<char> dna;
    std::string input;
    char inputArr[2500000];
    unsigned int cases;
    std::cin >> cases;
    for ( int i {0}; i < (cases + 1); i++ ) 
    {
        input = "";
        std::fill_n(inputArr, 100, ' ');
        std::getline(std::cin, input);
        strncpy(inputArr, input.c_str(), sizeof(inputArr)); 
        
        for ( int i {0}; i < input.length(); i++ ) 
            {
                switch (inputArr[i])
                {
                case 'A':
                    dna.push_back('T');
                    break;
                case 'T':
                    dna.push_back('A');
                    break;
                case 'C':
                    dna.push_back('G');
                    break;
                case 'G':
                    dna.push_back('C');
                    break;
                
                default:
                    break;
                }
            }
    }
    
    for (char i: dna) 
        { std::cout << i << "\n"; }
}