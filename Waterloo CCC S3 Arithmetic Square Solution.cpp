#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int xChecker(string j, string k, string l) {
    if (j == "X" && k!= "X" && l!= "X"){
        return 1;
    } else if (j != "X" && k == "X" && l != "X"){
        return 2;
    }else if (j != "X" && k != "X" && l == "X"){
        return 3;
    }else if (j == "X" && k == "X" && l != "X"){
        return 4;
    }else if (j == "X" && k != "X" && l == "X"){
        return 5;
    }else if (j != "X" && k == "X" && l == "X"){
        return 6;
    }else if (j != "X" && k != "X" && l != "X"){
        return 7;
    }else if (j == "X" && k == "X" && l == "X"){
        return 8;
    }
}

string display (string a, string b, string c, string d, string e, string f, string g, string h, string i) {
    cout << a << " " << b << " " << c << "\n";
    cout << d << " " << e << " " << f << "\n";
    cout << g << " " << h << " " << i << "\n";

    return std::__cxx11::string();
}

int main() {
    string x[4], y[4], z[4];
    int ix[4], iy[4], iz[4];
    cin >> x[1];
    cin >> x[2];
    cin >> x[3];
    cin >> y[1];
    cin >> y[2];
    cin >> y[3];
    cin >> z[1];
    cin >> z[2];
    cin >> z[3];
    
    switch (xChecker(x[1], x[2], x[3])) {
        case 1: {
            stringstream iss (x[3]);
            iss >> ix[3];
            stringstream iss2 (x[2]);
            iss2 >> ix[2];
            ix[1] = ix[2] - (ix[3] - ix[2]);
            x[1] = to_string(ix[1]);
            break;
            }

        case 2: {
            stringstream iss(x[3]);
            iss >> ix[3];
            stringstream iss2(x[1]);
            iss2 >> ix[1];
            ix[2] = (ix[3]-ix[1]) / 2 + ix[1];
            x[2] = to_string(ix[2]);
            break;
        }

        case 3: {
            stringstream iss(x[2]);
            iss >> ix[2];
            stringstream iss2(x[1]);
            iss2 >> ix[1];
            ix[3] = (ix[2]-ix[1]) + ix[2];
            x[3] = to_string(ix[3]);
            break;
        }

        case 4: {
            stringstream iss (x[3]);
            iss >> ix[3];
            ix[2] = ix[3] - 1;
            ix[1] = ix[3] - 2;
            x[1] = to_string(ix[1]);
            x[2] = to_string(ix[2]);
            break;
        }

        case 5: {
            stringstream iss(x[2]);
            iss >> ix[2];
            ix[3] = ix[2] + 1;
            ix[1] = ix[2] - 1;
            x[3] = to_string(ix[3]);
            x[1] = to_string(ix[1]);
            break;
        }

        case 6: {
            stringstream iss(x[1]);
            iss >> ix[1];
            ix[2] = ix[1] + 1;
            ix[3] = ix[1] + 2;
            x[3] = to_string(ix[3]);
            x[2] = to_string(ix[2]);
            break;
        }

        case 7: {
            x[1] = x[1];
            x[2] = x[2];
            x[3] = x[3];
            break;
        }

        case 8: {
            x[1] = "1";
            x[2] = "2";
            x[3] = "3";
            break;
        }
    }

    switch (xChecker(y[1], y[2], y[3])) {
        case 1: {
            stringstream iss (y[3]);
            iss >> iy[3];
            stringstream iss2 (y[2]);
            iss2 >> iy[2];
            iy[1] = iy[2] - (iy[3] - iy[2]);
            y[1] = to_string(iy[1]);
            break;
        }

        case 2: {
            stringstream iss(y[3]);
            iss >> iy[3];
            stringstream iss2(y[1]);
            iss2 >> iy[1];
            iy[2] = (iy[3]-iy[1]) / 2 + iy[1];
            y[2] = to_string(iy[2]);
            break;
        }

        case 3: {
            stringstream iss(y[2]);
            iss >> iy[2];
            stringstream iss2(y[1]);
            iss2 >> iy[1];
            iy[3] = (iy[2]-iy[1]) + iy[2];
            y[3] = to_string(iy[3]);
            break;
        }

        case 4: {
            stringstream iss (y[3]);
            iss >> iy[3];
            iy[2] = iy[3] - 1;
            iy[1] = iy[3] - 2;
            y[1] = to_string(iy[1]);
            y[2] = to_string(iy[2]);
            break;
        }

        case 5: {
            stringstream iss(y[2]);
            iss >> iy[2];
            iy[3] = iy[2] + 1;
            iy[1] = iy[2] - 1;
            y[3] = to_string(iy[3]);
            y[1] = to_string(iy[1]);
            break;
        }

        case 6: {
            stringstream iss(y[1]);
            iss >> iy[1];
            iy[2] = iy[1] + 1;
            iy[3] = iy[1] + 2;
            y[3] = to_string(iy[3]);
            y[2] = to_string(iy[2]);
            break;
        }

        case 7: {
            y[1] = y[1];
            y[2] = y[2];
            y[3] = y[3];
            break;
        }

        case 8: {
            y[1] = "1";
            y[2] = "2";
            y[3] = "3";
            break;
        }
    }

    switch (xChecker(z[1], z[2], z[3])) {
        case 1: {
            stringstream iss (z[3]);
            iss >> iz[3];
            stringstream iss2 (z[2]);
            iss2 >> iz[2];
            iz[1] = iz[2] - (iz[3] - iz[2]);
            z[1] = to_string(iz[1]);
            break;
        }

        case 2: {
            stringstream iss(z[3]);
            iss >> iz[3];
            stringstream iss2(z[1]);
            iss2 >> iz[1];
            iz[2] = (iz[3]-iz[1]) / 2 + iz[1];
            z[2] = to_string(iz[2]);
            break;
        }

        case 3: {
            stringstream iss(z[2]);
            iss >> iz[2];
            stringstream iss2(z[1]);
            iss2 >> iz[1];
            iz[3] = (iz[2]-iz[1]) + iz[2];
            z[3] = to_string(iz[3]);
            break;
        }

        case 4: {
            stringstream iss (z[3]);
            iss >> iz[3];
            iz[2] = iz[3] - 1;
            iz[1] = iz[3] - 2;
            z[1] = to_string(iz[1]);
            z[2] = to_string(iz[2]);
            break;
        }

        case 5: {
            stringstream iss(z[2]);
            iss >> iz[2];
            iz[3] = iz[2] + 1;
            iz[1] = iz[2] - 1;
            z[3] = to_string(iz[3]);
            z[1] = to_string(iz[1]);
            break;
        }

        case 6: {
            stringstream iss(z[1]);
            iss >> iz[1];
            iz[2] = iz[1] + 1;
            iz[3] = iz[1] + 2;
            z[3] = to_string(iz[3]);
            z[2] = to_string(iz[2]);
            break;
        }

        case 7: {
            z[1] = z[1];
            z[2] = z[2];
            z[3] = z[3];
            break;
        }

        case 8: {
            z[1] = "1";
            z[2] = "2";
            z[3] = "3";
            break;
        }
    }
    
    display(x[1], x[2], x[3], y[1], y[2], y[3], z[1], z[2], z[3]);
}