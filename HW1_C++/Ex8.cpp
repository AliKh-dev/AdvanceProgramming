#include <iostream>
using namespace std;
bool is_prime(int number)
{
    if (number == 1)
        return false;
    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
            return false;
    }
    return true;
}
int main()
{
    int num;
    cin >> num;
    cout << boolalpha << is_prime(num) << endl;
}
