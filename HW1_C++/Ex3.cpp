#include <iostream>
using namespace std;
int main()
{
    double geometry, algebra, physics;
    cin >> geometry >> algebra >> physics;
    cout << "average of grades: " << ((geometry + algebra + physics) / 3) << endl;
}