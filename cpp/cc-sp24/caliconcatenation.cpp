#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string solve(string message) {
    const string calico = "calico";

    for (int x = 0; x < min(6, (int) message.length()); x++) {
        string fragment = message.substr(0, x + 1);

        if (fragment == calico.substr(5 - x, x + 1)) {
            return "CALICO" + message.substr(x + 1, message.length() - x + 1);
        }
    }

    return message;
}

int main() {
    int n; cin >> n;

    for (int p = 0; p < n; p++) {
        string message; cin >> message;
        cout << solve(message) << endl;
    }
  
    return 0;
}
