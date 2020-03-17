#include <iostream>
#include <stack>
#include <map>
#include <set>

using namespace std;

int main() {

    map<char, char> pairing{
        {'[', ']'},
        {'{', '}'},
        {'(', ')'},
    };

    set<char> lefts, rights;
    for (auto p : pairing) {
        lefts.insert(p.first);
        rights.insert(pairing[p.first]);
    }

    stack<char> leftHandSide;

    string temp;
    while (cin >> temp) {
        for (auto c : temp) {
            if (lefts.count(c)) 
                leftHandSide.push(c);
            else if (rights.count(c)) {
                if (leftHandSide.empty()) {
                    cout << "Imbalanced! No left-hand-side symbols left to match " << c << endl;
                    return 0;
                }
                
                char left = leftHandSide.top();
                leftHandSide.pop();

                if (pairing[left] != c) {
                    cout << "Mismatch! " << left <<  " does not match " << c << "!" << endl;
                    return 0;
                }
            }
        }
    }

    if (!leftHandSide.empty()) {
        cout << "Too many left-hand-side symbols!" << endl;
        return 0;
    }

    cout << "Balanced!" << endl;
}
