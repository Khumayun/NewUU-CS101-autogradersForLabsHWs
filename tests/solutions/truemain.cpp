//
// Created by Khumoyun Aminaddinov on 08/02/24.
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

    cout << "Value of Integer is " << intNumber << ". " << "Size is " << sizeof(intNumber)<< endl;
    cout << "Value of Float is " << floatNumber << ". " << "Size is " << sizeof(floatNumber)<< endl;
    cout << "Value of Double is " << doubleNumber << ". " << "Size is " << sizeof(doubleNumber)<< endl;
    cout << "Value of Char is " << charName << ". " << "Size is " << sizeof(charName)<< endl;
    cout << "Value of Bool is " << boolean << ". " << "Size is " << sizeof(boolean)<< endl;

    cout << "PROBLEM 2\n";

    cout << "Khumoyun Aminaddinov" << endl;
    cout << "23423" << endl;
    cout << "Romeo and Juliet op.64" << endl;
    cout << "Cars" << endl;

    cout << "PROBLEM 3\n";

    cout<<"\"The rain\" is raining all around,\n"
          "\\It falls on field and tree\\\n"
          "It rains on the umbrellas here,\n"
          "And on the ships at sea.\n"
          "\'Rain\'\t Robert Louis Stevenson"<<endl;

    cout << "PROBLEM 4\n";

    int a=151;
    char b='B';
    float c=(float)a/3;
    int d=(int)b;
    int e=a+(int)b;
    char f=(char)(a/10-1)+b;
    cout<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<endl;

    cout << "PROBLEM 5\n";

    int a2=32;
    int b2=48;

    cout<<"Sum="<<a2+b2<<endl;
    cout<<"Product="<<a2*b2<<endl;


    cout << "PROBLEM 6\n";

    int a3,b3;
    cout<<"Enter two integer numbers:"<<endl;
    cin>>a3>>b3;

    cout<<"Sum:"<<a3<<"+"<<b3<<"="<<a3+b3<<endl;

    cout << "PROBLEM 7\n";

    double t;
    double x, y;
    cin >> x >> y;
    t = (2*(x*x+3))/(y/3+4);
    cout << "t=" << t << endl;

    cout << "PROBLEM 8\n";

    float r;
    cout<<"Enter the radius of the sphere:";
    cin>>r;

    cout<<"Area:"<<4*3.14*r*r<<endl;

    cout << "PROBLEM 9\n";

    float v0,v1,t1;
    cin>>v0>>v1>>t1;
    cout<<(v1-v0)/t1<<endl;

    cout << "PROBLEM 10\n";
    double a4, b4, c4;
    cout << "Enter the driving distance: ";
    cin >> a4;
    cout << "Enter the miles per gallon: ";
    cin >> b4;
    cout << "Enter the price per gallon: ";
    cin >> c4;
    cout << "The cost of driving is $" << a4/b4*c4 << endl;

    cout << "PROBLEM 11\n";

    double x2=5.23e3;
    double y2=25e-4;

    cout<<x2<<endl<<y2<<endl;

    cout << "PROBLEM 11\n";

    double x3=5.23e3;
    double y3=25e-4;

    cout<<x3<<endl<<y3<<endl;

    cout << "PROBLEM 12\n";

    int total=241;
    int n=11;
    cout<<"In first group:"<<total/n<<endl;
    cout<<"In last group:"<<total%n<<endl;

    cout << "PROBLEM 13\n";

    double a5;
    cout << "Enter the length of the side: ";
    cin >> a5;
    cout << "The area of the hexagon is " << 3*1.73/2*a5*a5 << endl;

    cout << "PROBLEM 14\n";

    int num;
    cout<<"Enter a number:";
    cin>>num;//20

    num++; //21
    num*=6; //126
    num-=4; //122
    num/=2; //61
    num--; // 60
    num %=5; //0

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

    float x4=13;
    float y4=1;

    float z=(x4++ + x4)/(++y4*(y4)*++y4);
    cout<<z<<endl;

    cout << "PROBLEM 17\n";

    int a6,b6;
    cin>>a6>>b6;
    cout<<(a6==b6)<<endl;

    cout << "PROBLEM 18\n";

    int a7,b7;
    cin>>a7>>b7;
    cout<<(a7<50)<<endl;
    cout<<(a7<b7)<<endl;

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
    cout<<"Sardor in cm.:";
    cin>>a12;
    cout<<"Mike in ft.:";
    cin>>b12;
    cout<<(b12*30.48>a12) << endl;

    return 0;
}