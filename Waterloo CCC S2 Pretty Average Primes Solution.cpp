#include <iostream>
#include <string>
using namespace std;

bool checkPrime(int test) {
    int factor, alert = 0;
    for (factor = 1; factor <= test; factor = factor + 1 )
    {
        if (test % factor == 0) {
            alert = alert + 1;
        }
    }
    if (alert == 2) {
        return true;
    } else {
        return false;
    }
}


int akkiTheorem(int x) {
    int counter = 0, temp = 0, num1 = 0;
    while (counter < 1)
    {
        temp = temp + 1;
        if (checkPrime(x - temp) == true && checkPrime(x + temp) == true){
            num1 = x - temp;
            counter = 2;
        }
    }
    return num1;
}


int main()
{
    int n, y, times = 1, num2;
    cin >> n;
    int array[n];
    for (times; times <= n; times = times+1)
    {
        cin >> y;
        array[times] = y;
    }
    for (times = 1; times <=n; times = times + 1)
    {
        cout << akkiTheorem(array[times]);
        num2 = (array[times] - akkiTheorem(array[times])) + array[times];
        cout << " " << num2 << "\n";
    }

}