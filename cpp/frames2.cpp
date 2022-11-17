//Not working (autograder)
//A remaking of the "frames" program.
#include <iostream>
#include <string>
#include <vector>
#include <algorithm> 
#include <cctype>
#include <locale>

static inline void ltrim(std::string &s) {
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) {
        return !std::isspace(ch);
    }));
}

int largest(std::vector<std::string> &strs) //Gets the largest string length of a vector of strings
{
    size_t max = 0;
    for (std::string i: strs) 
    {
        if (i.length() > max)
            { max = i.length(); }
    }
        return static_cast<int>(max);
}

std::vector<std::string> split(std::string &input) //Splits a string into words by spaces, for use of the individual words
{
    int i = 0;
    std::vector<std::string> inSplit;
    
    do {
        inSplit.push_back(input.substr(0, input.find(' ')));
        input.erase(0, inSplit.at(i).length() + 1);
        i++;
    }
    while (input.find(' ') != std::string::npos);

    inSplit.push_back(input.substr(0, input.size()));

    return inSplit;
}

std::string constructFrame(std::vector<std::string> strs) 
{
    std::string frame = "";
    int max = largest(strs);
    std::string topBot(max + 2, '*'); //This is the top and bottom of the frame

    frame = frame + topBot + "\n";
    for (std::string i: strs) 
    {
        std::string spaces(max - i.length(), ' ');
        frame = frame + "*" + i + spaces + "*" + "\n";
    }
    frame = frame + topBot + "\n";

    return frame;
}

int main() 
{
    int t;
    std::cin >> t;

    std::cin.ignore(1, '\n');
    for (int i = 0; i < t; i++) 
    {
        std::string input;
        std::string output;
        std::getline(std::cin, input);
        ltrim(input);
        std::vector<std::string> inSplit = split(input);
        
        std::cout << constructFrame(inSplit);
    }

    return 0;
}