#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
    int size,y = 0, x = 0,z,w, counter = 0;
     string input;
    getline(cin, input);
   size = input.size();
   while(counter <= size)
   {
    if (input[counter] == 'H'){
        x = x + 1;
    } else if(input[counter] == 'V'){
        y = y + 1;
    }
    counter = counter + 1;
   }

    w = x%2;
    z = y%2;
    switch(w+z) {
        case 0:
            cout << "1 2" << "\n" << "3 4";
            break;
        case 1:
            if (w == 1){
                cout << "3 4" << "\n" << "1 2";
            }else{
                cout << "2 1" << "\n" << "4 3";
            }
            break;
        case 2:
            cout << "4 3" << "\n" << "2 1";
            break;
    }

}