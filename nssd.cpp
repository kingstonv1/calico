#include <iostream>
#include <vector>

int main() 
{
    float v {0};
    float x {0};
    char colon;
    unsigned int cases{0};

    std::vector<std::string> output;
    std::cin >> cases;

    for ( int i{0}; i < cases; i++ ) 
    {
        std::cin >> v >> colon >> x;
        if ( x - v <= 0 ) { output.push_back("Swerve\n"); }
        else if ( x - (v * 5) <= 0 ) { output.push_back("Brake\n"); }
        else { output.push_back("Safe\n"); }
        std::cout << "\n"; 
    }

    std::cout << "\n";
    for (int i{0}; i < output.size(); i++) { std::cout << output.at(i); }
    return 0; 
}