#include <bits/stdc++.h>
using namespace std;

int main() {
    int p;
    cin >> p;

    // パターン2
    if (p == 2) {
        string text;
        cin >> text;
        cout << text << "!" << endl;
    }
    int price, n;
    cin >> price >> n;
    cout << price * n << endl;
}
