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
                if ( inputArr[i] == 'A' ) { dna.push_back('T'); }
                else if ( inputArr[i] == 'T' ) { dna.push_back('A'); }
                else if ( inputArr[i] == 'C' ) { dna.push_back('G'); }
                else if ( inputArr[i] == 'G' ) { dna.push_back('C'); }
            }
        dna.push_back('\n');
    }
    
    for (int i {0}; i < dna.size(); i++ ) 
    {
        std::cout << dna[i];
    }

}