//Working, but not bonus set.
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

int main()
{
    int t;
    std::vector<long long> out;
    std::cin >> t;

    for (int i = 0; i < t; i++) 
    { 
        long long rows;
        std::cin >> rows;
        out.push_back(std::ceil((rows * (rows + 1) * 0.5 * 3 - rows) / 54));
    }

    for (int i: out) 
        { std::cout << i << '\n'; }

    return 0;
}