#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;
int main()
{
    int secret_number = rand() % 100;
    int input = 0, cnt = 0;
    do
    {
        cin >> input;
        if (input > secret_number)
            cout << "It is too large" << endl;
        else if (input < secret_number)
            cout << "It is too small" << endl;
        cnt++;
    } while (secret_number != input);
    cout << "You won this game and you have " << cnt << " tries!" << endl;
}
