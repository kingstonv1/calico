//Not working.
#include <iostream>
#include <vector>
#include <string>

template<typename First, typename ... Strings>
std::vector<char> function(First arg, const Strings&... rest) 
{
    std::vector<char> vector;
    vector.push_back(arg);
    return vector;
}


int main() 
{
    int dimensions {0};
    int cases {0};
    int input {0};
    
    std::cin >> cases;

    for ( int i {0}; i < cases; i++ ) 
    {
        std::cin >> input;
        std::vector<std::vector<char>> vector;




    }

    

    return 0;
}