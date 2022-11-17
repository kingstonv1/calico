//Working!
#include <iostream>
#include <string>
#include <vector>

std::string operator * (std::string str, int num) 
{
    std::string out = "";
    while (num--) 
    {
        out += str;
    }

    return out;
}

int main() 
{
    int cases;
    std::cin >> cases;

    for (int i = 0 ; i < cases; i++) 
    {
        int size;
        std::string tower;
        std::cin >> size;

        for (int x = 1; x < (size + 1); x++) 
        {
            std::string card {"/\\"};
            std::string spaces((size + 1) - x, ' ');
            tower.append(spaces);
            tower.append(card * x);
            tower.append(spaces);
            tower.append("\n");
        }

        std::cout << tower;
    }

    return 0;
}