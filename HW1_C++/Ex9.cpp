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
    int n;
    cin >> n;
    int num[n];
    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (is_prime(num[i]))
            cout << num[i] << " is prime!" << endl;
    }
    
    
    
}
