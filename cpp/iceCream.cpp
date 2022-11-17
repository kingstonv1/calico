//Working!
#include <bits/stdc++.h>

    using namespace std;

int solve(double i) 
{
    return (int) (0.5 * (sqrt(8 * i + 1) - 1));
}

int main() 
{
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++)
    {
        double N;
        cin >> N;
        cout << solve(N) << 'n';
    }
}