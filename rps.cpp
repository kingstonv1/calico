//Under Development (Not Working).
#include <bits/stdc++.h>

char beats(char c) 
{
    switch (c)
    {
        case 'R':
            return 'P';
        
        case 'P':
            return 'S';

        case 'S': 
            return 'R';
        
        default:
            return 'R';
    }
}

char chooseMove(std::vector<char>& me, std::vector <char>& bot, int i)
{
    char botMove {'?'};
    //Determine the bot's move
    if (i > 1) 
    {
        if (bot.at(i) == me.at(i - 1)) 
        {
            botMove = beats(me.at(i));
        }
        else if (bot.at(i) == bot.at(i - 1)) 
        {
            botMove = beats(beats(bot.at(i)));
        }
    }
    //Determine our response
    return beats(botMove);
}

int main() 
{
    int T;
    std::vector<char> me;
    std::vector<char> bot;

    std::cin >> T;
    

    for(int i = 0; i < T; i++) 
    {
        char botMove = 'R';
        char myMove;
        myMove = chooseMove(me, bot, i - 1);
        std::cout << myMove;
        std::cin >> botMove;
        bot.push_back(botMove);
        me.push_back(myMove);
    }


    return 0;
}