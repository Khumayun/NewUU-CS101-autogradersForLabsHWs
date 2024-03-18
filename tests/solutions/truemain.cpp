//
// Created by Khumoyun Aminaddinov 08/02/2024
//
#include <iostream>
using namespace std;

int main() {
    cout << "PROBLEM 1\n";

    int intNumber = 23;
    float floatNumber = 3.14;
    double doubleNumber = 45.1234;
    char charName = 'A';
    bool boolean = true;

    cout << "Value of Integer is " << intNumber << ". " << "Size is " << sizeof(intNumber) << endl;
    cout << "Value of Float is " << floatNumber << ". " << "Size is " << sizeof(floatNumber) << endl;
    cout << "Value of Double is " << doubleNumber << ". " << "Size is " << sizeof(doubleNumber) << endl;
    cout << "Value of Char is " << charName << ". " << "Size is " << sizeof(charName) << endl;
    cout << "Value of Bool is " << boolean << ". " << "Size is " << sizeof(boolean) << endl;

    cout << "PROBLEM 2\n";

    cout << "Khumoyun Aminaddinov" << endl;
    cout << "23423" << endl;
    cout << "Romeo and Juliet op.64" << endl;
    cout << "Cars" << endl;

    cout << "PROBLEM 3\n";

    cout << "\"I\'m standing\" on the edge of some crazy cliff.\n"
            "What I have to do, I have to catch everybody\\\n"
            "if they start to go over the cliff—I mean\\\n"
            "\\if they're running and they don't look\n"
            "where they're going I have to come out\n"
            "from somewhere and \tcatch them.";

    cout << "PROBLEM 4\n";

    int a=189;
    char b='B';
    float c=(float)a/3;
    int d=(int)b;
    int e=(a+(int)b)/5;
    char f=(char)(a/10-1)+b;
    cout << c << ' ' << d << ' ' << e << ' ' << f << endl;

    cout << "PROBLEM 5\n";

    int a2=12;
    int b2=38;

    cout << "Sum=" << a2+b2 << endl;
    cout << "Product=" << a2*b2 << endl;

    cout << "PROBLEM 6\n";

    int a3,b3;
    cin>>a3>>b3;

    cout<<"Sum: "<<a3<<" + "<<b3<<" = "<<a3+b3<<endl;

    cout << "PROBLEM 7\n";

    double t;
    double x, y;
    cin >> x >> y;
    t = (2*(x*x+3))/(y/3+4);
    cout << "t=" << t << endl;

    cout << "PROBLEM 8\n";

    float r;
    cin>>r;
    r/=2;
    cout<<"Area: "<<4*3.14*r*r<<endl;

    cout << "PROBLEM 9\n";

    float v0,v1,t1;
    cin>>v0>>v1>>t1;
    cout<<(v1-v0)/t1<<endl;

    cout << "PROBLEM 10\n";
    double a4, b4, c4;
    cin >> a4;
    cin >> b4;
    cin >> c4;
    cout << "The cost of driving is $" << a4/b4*c4 << endl;

    cout << "PROBLEM 11\n";

    double x2=5.23e3;
    double y2=25e-4;

    cout << x2 << ' ' << y2 << endl;

    cout << "PROBLEM 12\n";

    int total=241;
    int n=11;
    cout << "In first group: " << total/n << endl;
    cout << "In last group: " << total%n << endl;

    cout << "PROBLEM 13\n";

    double a5;
    cin >> a5;
    cout << "The area of the hexagon is " << 3*1.73/2*a5*a5 << endl;

    cout << "PROBLEM 14\n";

    int num;
    cin>>num;//20

    num++; //21
    num*=6; //126
    num-=4; //122
    num/=2; //61
    num--; // 60
    num %=5; //0
    cout << num << endl;

    cout << "PROBLEM 15\n";

    char c5='A';
    c5+=7;
    cout<<c5;
    c5-=3;
    cout<<c5;
    c5+=7;
    cout<<c5<<c5;
    c5+=3;
    cout<<c5;
    c5-=46;
    cout<<c5;
    cout<<endl;

    cout << "PROBLEM 16\n";

    float x4=17;
    float y4=1;

    float z=(x4++ + x4)/(++y4*(++y4));
    cout<<z<<endl;

    cout << "PROBLEM 17\n";

    int a6,b6;
    cin>>a6>>b6;
    cout<<(a6==b6)<<endl;

    cout << "PROBLEM 18\n";

    int a7,b7;
    cin>>a7>>b7;
    cout << ((a7<50) && (a7<b7)) << endl;

    cout << "PROBLEM 19\n";

    int a8,b8,c8;
    cin>>a8>>b8>>c8;
    cout<<((a8>b8)&&(a8>c8))<<endl;

    cout << "PROBLEM 20\n";

    int a9,b9,c9,d9,e9;
    cin>>a9>>b9>>c9>>d9>>e9;
    cout<<((a9>=0)||(b9>=0)||(c9>=0)||(d9>=0)||(e9>=0))<<endl;

    cout << "PROBLEM 21\n";

    int a11,b11;
    cin>>a11>>b11;
    cout<<((a11+b11>50)&&(a11*b11>50)) << ' ';
    cout<<((a11+b11-10>50)||(a11*(b11-10)>50)) << ' ';
    cout<<((a11>50)||(b11>50)) << endl;

    cout << "PROBLEM 22\n";

    float a12,b12;
    cin>>a12;
    cin>>b12;
    cout<<(b12*30.48>a12) << endl;

    return 0;
}