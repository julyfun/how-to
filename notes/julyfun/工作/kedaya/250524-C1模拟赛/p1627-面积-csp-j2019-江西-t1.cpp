#include <iostream>
using namespace std;
int main() {
    long long a, b, c;
    cin >> a >> b >> c;
    if (a * a > b * c)
        cout << "Alice";
    else
        cout << "Bob";
    return 0;
}
