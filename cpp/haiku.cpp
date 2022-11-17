//Not Working (U.D.)
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

int main()
{
    int t;
    std::cin >> t;
    for (int i = 0; i < t; i++)
    {
        std::map<std::string, int> words;
        std::string first, second, third;
        int tt;
        std::cin >> tt;
        
        for (int x = 0; x < tt; i++) 
        {
            int syl;
            std::string word;
            std::cin >> syl >> word;
            words.insert(std::make_pair(word, syl));
        }
    }


    return 0;
}