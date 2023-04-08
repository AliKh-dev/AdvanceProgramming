#include <iostream>
using namespace std;
int fibo(int number)
{
    if (number < 1)
        return -1;
    else if (number == 1 || number == 2)
        return 1;
    return fibo(number - 1) + fibo(number - 2);
}
int main()
{
    int num;
    cin >> num;
    if (fibo(num) != -1)
        cout << fibo(num) << endl;
    else
        cout << "This number you entered is invalid!" << endl;
}
