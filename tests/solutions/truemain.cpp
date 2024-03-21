//
// Created by ...
// Date:

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    cout << "PROBLEM 1\n";
    float cost=0, consumed_water;
    cin >> consumed_water;
    // write your code here
    if (consumed_water <= 30){
        cost = 13 + consumed_water*0.4;
    }
    else if (consumed_water > 30 && consumed_water <= 50){
        cost = 13 + 30*0.4 + (consumed_water-30)*0.12;
    }
    else if (consumed_water > 50 && consumed_water <= 60){
        cost = 13 + 30*0.4 + (consumed_water-30)*0.12 + (consumed_water-50)*1.4;
    }
    else if (consumed_water > 60){
        cost = 13 + 30*0.4 + (consumed_water-30)*0.12 + (consumed_water-50)*1.4 + (consumed_water-60)*1.5;
    }
    cout << "The maximum number is " << cost << endl;

    cout << "PROBLEM 2\n";

    int i, j, k;
    cin >> i >> j >> k;
    cout << ((i > j) ? ((i > k) ? i : k) : ((j > k) ? j : k)) << endl;

    cout << "PROBLEM 3\n";

    char male = 'M';
    char female = 'F';
    char S;
    float height;
    cin >> S;
    cin >> height;
    if (S == male) {
        if (height < 1.7) {
            cout << "Short\n";
        } else if (height >= 1.7 && height < 1.85) {
            cout << "Normal\n";
        } else {
            cout << "Tall\n";
        }
    }else if (S == female) {
        if (height < 1.6) {
            cout << "Short\n";
        } else if (height >= 1.6 && height < 1.75) {
            cout << "Normal\n";
        } else {
            cout << "Tall\n";
        }
    }else {
        cout << "Wrong input\n";
    }

    cout << "PROBLEM 4\n";

    string macAddress;

    cin >> macAddress; // read the sequence of characters from input

    std::istringstream ss(macAddress);
    int firstOctet;
    ss >> std::hex >> firstOctet;

    if (macAddress == "FF:FF:FF:FF:FF:FF") {
        cout << "Broadcast\n";
    }
    if (firstOctet % 2 == 0) {
        cout << "Unicast\n";
    }
    if (firstOctet % 2 != 0) {
        cout << "Multicast\n";
    }else { cout << "Unknown\n";}

    cout << "PROBLEM 5\n";

    float result, x, y;
    char operation;
    cin >> x >> operation >> y;

    switch (operation) {
        case '+':
            result = x + y;
            break;
        case '-':
            result = x - y;
            break;
        case '*':
            result = x * y;
            break;
        case '/':
            if (y != 0) {
                result = x / y;
            } else {
                std::cerr << "Error: Division by zero!" << std::endl;
                result = 0.0;
            }
            break;
        default:
            std::cerr << "Error: Invalid operation!" << std::endl;
            result = 0.0;
            break;
    }
    cout << result << endl;

    return 0;
}