//
// Created by ...
// Date:

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    cout << "PROBLEM 1\n";

    //declaring and initializing variables
    int num1, num2; // initializing integers to 0 for storing numbers
    int avg, product; // initializing integers to 0 for storing results

    cin>>num1;
    cin>>num2;

    avg=(num1+num2)/2; //add numbers and store result into sum
    product=num1*num2; //multiply numbers and store result into product

    //display sum and multiplication result
    cout<<"The result of average is equal to "<<avg<<endl;
    cout<<"The result of product is equal to "<<product<<endl;

    cout << "PROBLEM 2\n";

    double base, height;

    // Prompt the user to input the length of the base
    cin >> base;
    cin >> height;

    // Calculate the area of the triangle
    double area = 0.5 * base * height;

    // Display the calculated area
    cout << "The area of the triangle is: " << area << " square units" << endl;

    cout << "PROBLEM 3\n";
    //declaring and initializing variables
    float tempC; // initializing float to 0 for storing Celsius temperature
    float tempF; // initializing float to 0 for storing Fahrenheit temperature

    cin>>tempC; //read Celsius temperature from user

    tempF=tempC*1.8+32; //calculateFahrenheit temperature

    cout<<"The temperature in Farenheit is equal to "<<tempF<<endl; //display Fahrenheit temperature

    cout << "PROBLEM 4\n";

    long a, b, c, res;
    cin >> a >> b >> c;

    res = pow(pow(a, b), c);

    cout << res << endl;

    cout << "PROBLEM 5\n";

    int N;
    cin >> N;
    cout << N << '^' << '1' << '=' << pow(N,1) << endl;
    cout << N << '^' << '2' << '=' << pow(N,2) << endl;
    cout << N << '^' << '3' << '=' << pow(N,3) << endl;
    cout << N << '^' << '4' << '=' << pow(N,4) << endl;
    cout << N << '^' << '5' << '=' << pow(N,5) << endl;
    cout << N << '^' << '6' << '=' << pow(N,6) << endl;
    cout << N << '^' << '7' << '=' << pow(N,7) << endl;
    cout << N << '^' << '8' << '=' << pow(N,8) << endl;
    cout << N << '^' << '9' << '=' << pow(N,9) << endl;
    cout << N << '^' << "10" << '=' << pow(N,10) << endl;

    return 0;
}