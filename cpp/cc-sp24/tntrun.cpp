#include <bits/stdc++.h>
using ll = long long;
using namespace std;

string solve(int n, string before, string after) {
   int count = 0;
   
   for (int i = 0; i < n; i++) {
      if (before[i] == '-' && after[i] == '#') {
         return "banned";
      }
      
      if (before[i] == '#' && after[i] == '-') {
         count = 0;
      } else {
         count++;

         if (count > 4) {
            return "banned";
         }
      }
   }

   return "YES";
}

int main() {
   int n; cin >> n;

   for (int l = 0; l < n; l++) {
        string before; string after; int blocks;
        cin >> blocks;
        cin >> before;
        cin >> after;

        cout << solve(blocks, before, after) << endl;
   }

    return 0;
}
