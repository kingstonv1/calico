
//This is a shortest path problem.
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>

int main()
{
    int t;
    std::cout << std::setprecision(2) << std::fixed;
    std::cin >> t;
    for (int i = 0; i < t; i++)
    {
        int tt;
        float costf = 0.0f;
        std::string cost;
        std::string start;
        std::string end;
        std::cin >> tt >> cost >> start >> end;
        cost.erase(0,1);
        costf = strtof(cost.c_str(), nullptr);
        


    }


    return 0;
}