#include <bits/stdc++.h>
using namespace std;

// naive solution. brute force greedy. doesn't pass.

int solve (int blocks, int jump_dist, string course) {
    if (blocks <= jump_dist) {
        return -1;
    }
        
    int playercount = 0;

    for (int i = 0; i < blocks; i++) {
        int pos = -1;
        bool done = false;

        for (int x = jump_dist + 1; x > 0; x--) {
            if (pos >= blocks - (jump_dist + 1)) {
                playercount += 1;
                break;
            }

            if (course[pos + x] == '#') {
                course[pos + x] = '-';
                pos = pos + x;
                x = jump_dist + 2;
            }

        }

        if (done) { break; }
    }

       return playercount;
}

int main () {
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        int blocks; int jump_dist;
        cin >> blocks >> jump_dist;

        string course;
        cin >> course;

        cout << solve(blocks, jump_dist, course) << endl;
    }


    return 0;
}
