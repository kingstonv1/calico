    #include <iostream>
    #include <vector>
    #include <algorithm>

    using namespace std;

    void solve(vector<vector<char>> sw, int h, int w, int d) {
        vector<char> new_row(w + d + 1, ' ');
        vector<vector<char>> ns((h + d + 1));
        fill(ns.begin(), ns.end(), new_row);

        vector<pair<int, int>> edges(0);

        // transpose the original shape on the new list
        for (int row = 0; row < h; row++) {
            for (int col = 0; col < w; col++) {
                ns[row + d + 1][col + d + 1] = sw[row][col];

                if (sw[row][col] == '+') {
                    edges.push_back(make_pair(row +d + 1, col + d + 1));
                }
            }
        }

        // Extend edges
        for (int x = 0; x < edges.size(); x++) {
            for (int i = 1; i < d + 1; i++) {
                pair<int, int> p = edges[x];
                char ch = ns[p.first - i][p.second - i];
                
                if (ch == '-' || ch == '|' || ch == '+') {
                    continue;
                }

                ns[p.first - i][p.second - i] = '\\';
            }
        }

        // place backside of shape
        for (int row = 0; row < h; row++) {
            for (int col = 0; col < w; col++) {
                if (ns[row][col] == ' ') {
                    ns[row][col] = sw[row][col];
                }
            }
        }


        // print the vectors
        for (vector<char> v: ns) {
            for (char c: v) {
                cout << c;
            }
            cout << "\n";
        }
    }

    int main() {
        int T;
        cin >> T;

        for (int i = 0; i < T; i++) {
            int h, w, d;
            cin >> h >> w >> d;

            vector<vector<char>> sw(h);

            cin.ignore(); // idk why this is here

            for (int j = 0; j < h; j++) {
                string temp;
                getline(cin, temp);

                vector<char> r(temp.begin(), temp.end());
                sw[j] = r;
            }

            solve(sw, h, w, d);
        }
    }