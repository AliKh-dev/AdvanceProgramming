#include <iostream>
using namespace std;
int main()
{
    int basic_salary = 400, years_employed, number_of_children;
    cin >> years_employed >> number_of_children;
    cout << "Total amount of salary: " << (400 + (number_of_children * 20) + (years_employed * 30)) << endl;
}