#include <iostream>
using namespace std;
int main()
{
    int a = 5, b = 10;
    int temp = a;
    a = b;
    b = temp;
    cout << "a: " << a << endl;
    cout << "b: " << b << endl;
}