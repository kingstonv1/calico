#include <bits/stdc++.h>


std::string lower(std::string Text) 
{
    for (int i = 0; i < Text.length(); i ++)
    {
        std::cout << Text;
        if (Text[i] == Text[i + 1])
            Text.erase(1+i, 1);
    }
    
    for (int i = 0; i < Text.length(); i++)
        Text[i] = tolower(Text[i]);
    std::cout << Text;
    return Text;
}

std::vector<std::string> split(std::string& input) 
{
    int i = 0;
    std::vector<std::string> inSplit;
    char d = ' ';
    while (input.find(d) != std::string::npos)
    {
        inSplit.push_back(input.substr(0, input.find(d)));
        input.erase(0, inSplit.at(i).length() + 1);
        i++;
    }
    inSplit.push_back(input.substr(0, input.size()));
    return inSplit;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t;
    std::cin.ignore(1, '\n');
    std::vector<std::string> out;
    std::string ex1 = "im", ex2 = "i'm";
    while (t--)
    {
        std::string in;
        std::vector<std::string> v;
        std::getline(std::cin, in);
        v = split(in);
        
        for (int i = 0; i < v.size(); i++) 
        {
            if (ex1.find(lower(v[i]).c_str()) != std::string::npos || ex2.find(lower(v[i]).c_str()) != std::string::npos)
            {
                std::string output;
                i++;
                for (int p = 0; i < v.size(); i++) 
                {
                    output += " ";
                    output += v.at(i);
                }
                    output += ",";
                    out.push_back(output);
                    break;
            }   
        }
    }

    for (std::string i: out)
        std::cout << "Hi" << i << " I'm dad." << "\n";

    return 0;
}