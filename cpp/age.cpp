//Not Working (U.D.)
#include <bits/stdc++.h>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::vector<std::string> out;
    std::cin >> t;
    while (t--)
    {
        std::string name1, name2;
        bool d = false;
        int age1, age2, comp;
        std::cin >> name1 >> age1 >> name2 >> age2;
        (age1 > age2)? comp = age1 : comp = age2;

        for (int i = 0; i <= comp; i++) 
        {
            if ((age1 + i) / (age2 + i) == 2 || (age2 + i) / (age1 + i) == 2)
            {
                out.push_back("In " + std::to_string(i) + " years, " + name1 + " will be " + std::to_string(age1 + i) + " and " + name2 + " will be " + std::to_string(age2 + i) + ".");
                d = true;
            }
        }
        if (!d)
            out.push_back("you will never be happy");
        for (std::string i: out) 
            { std::cout << i << "\n"; }
        
    }

    return 0;
}