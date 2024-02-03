#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    double x, a, b, c, y, d;
    cout << "a=";
    cin >> a >> b;
    cout << "b=";
    cout << "c=";
    cin >> c;
    cout << "y=";
    cin >> y;
    d = pow(b,2) - 4 * a * c;
    cout << (-b + sqrt(d)) / 2 * a, cout << (-b - sqrt(d)) / 2 * a;
    return 0;
}


