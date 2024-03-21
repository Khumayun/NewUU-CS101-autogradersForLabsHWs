//
// Created by ...
//
#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main() {
    cout << "PROBLEM 1\n";
    int p1_var1;
    cin >> p1_var1;
    if(p1_var1 >= 0) {
        cout << "Positive\n";
    } else {
        cout << "Negative\n";
    }

    cout << "PROBLEM 2\n";
    cin >> p1_var1;
    if(p1_var1 >= 0) {
        if(p1_var1 % 2 == 0) {
            cout << "positive even\n";
        } else {
            cout << "positive odd\n";
        }
    } else {
        if(p1_var1 % 2 == 0) {
            cout << "negative even\n";
        } else {
            cout << "negative odd\n";
        }
    }

    cout << "PROBLEM 3\n";
    int p3_var1, p3_var2, p3_var3;
    cin >> p3_var1 >> p3_var2 >> p3_var3;

    if ((p3_var1>p3_var2)&&(p3_var1>p3_var3)){
        cout<<p3_var1<<" is largest\n";

    }
    else if((p3_var2>p1_var1)&&(p3_var2>p3_var3)){

        cout<<p3_var2<<" is largest\n";
    }
        //at last if two previous numbers did not meet condition. the largest is third and we print it in the last else block
    else{
        cout<<p3_var3<<" is largest\n";
    }

    cout << "PROBLEM 4\n";
    int p4_var1, p4_var2;
    cin>>p4_var1>>p4_var2;
    if(p4_var1%p4_var2==0 &&p4_var1>p4_var2){
        cout<<"is divisible "<<endl;
    }else {
        cout << "not divisible" << endl;
    }

    cout << "PROBLEM 5\n";

    int p5_var1;
    cin>>p5_var1;

    //Leap is checking if remainder of x divided by four hundred is 0.
    if ((p5_var1%400)==0){
        //print the result in case condition is true
        cout<<"leap year\n";
    }
        //next if previous block did not work,that means we need to exclude years that are divided by hundred
    else if((p5_var1%100)==0){
        cout<<"not\n";
    }
        //at last we check if x is divided by four
    else if ((p5_var1%4)==0){
        cout<<"leap year\n";
    }

    cout << "PROBLEM 6\n";
    float p6_var1, p6_var2, p6_var3;

    cin>>p6_var1;
    cin>>p6_var2;
    cin>>p6_var3;

    float d=p6_var2*p6_var2-4*p6_var1*p6_var3;

    float x1,x2;

    if(d==0){
        x1=-p6_var2/(2.0*p6_var1);
        x2=x1;
        cout<<"x1=" << x1 << endl;
        cout<<"x2=" << x2 <<endl;
    } else if(d>0){
        x1=(-p6_var2+sqrt(d))/(2*p6_var1);
        x2=(-p6_var2-sqrt(d))/(2*p6_var1);
        cout<<"x1="<<x1<<endl<<"x2="<<x2;
    }
    else{
        cout<<"no solution\n";

    cout << "PROBLEM 7\n";

    int p7_var1, p7_var2, p7_var3;

    //input the value
    cin>>p7_var1>>p7_var2>>p7_var3;

    if ((p7_var1+p7_var2+p7_var3)==180){
        cout<<"is valid\n";
    }else{
        cout<<"is not valid\n";
    }

    cout << "PROBLEM 8\n";
    char character;

    cin>>character;

    if((character>='A' && character<='Z')) {
        cout<<"Uppercase\n";
    } else if((character>='a' && character<='z')) {
        cout<<"Lowercase\n";;
    } else{
        cout<<"not\n";
    }

    cout << "PROBLEM 9\n";
    float speed = 0;
    cin>>speed;
    if(speed<80&&speed>20){
        cout<<"just right"<<endl;
    }else if(speed<20){
        cout<<"too slow"<<endl;
    }else{
        cout<<"too fast"<<endl;
    }

    cout << "PROBLEM 10\n";
    int p10_var1, p10_var2;
    cin>>p10_var1>>p10_var2;
    float d10=sqrt(p10_var1*p10_var1+p10_var2*p10_var2);
    if(d10<=10){
        cout<<"is in\n";
    }else{
        cout<<"is not in\n";
    }

    cout << "PROBLEM 11\n";
    double weight1, price1, weight2, price2;

    cin >> weight1;
    cin >> price1;

    cin >> weight2;
    cin >> price2;

    double pricePerPound1 = price1 / weight1;
    double pricePerPound2 = price2 / weight2;

    if (pricePerPound1 < pricePerPound2) {
        cout << "first better" << endl;
    } else if (pricePerPound2 < pricePerPound1) {
        cout << "second better" << endl;
    } else {
        cout << "same" << endl;
    }

    cout << "PROBLEM 12\n";
    int number;

    cin >> number;

    if (number >= 100 && number <= 999) {
        int originalNumber = number;
        int reverseNumber = 0;

        while (number > 0) {
            int digit = number % 10;
            reverseNumber = reverseNumber * 10 + digit;
            number /= 10;
        }

        if (originalNumber == reverseNumber) {
            cout << "is a" << endl;
        } else {
            cout << "is not" << endl;
        }
    } else {
        cout << "valid" << endl;
    }

    cout << "PROBLEM 13\n";
    char light;
    cin>>light;
    switch(light){
        case 'g':
            cout<<"Go!"<<endl;
            break;
        case 'y':
            cout<<"Get ready!"<<endl;
            break;
        case 'r':
            cout<<"Stop"<<endl;
            break;
        default:
            cout<<"no\n";
    }

    cout << "PROBLEM 14\n";
    int x;
    int y;
    cin>>x;
    cin>>y;
    string t,f;
    //compare the value of x with cases values and print corresponding weekday
    switch (x) {
        case 1:
            t="Monday";
            break;
        case 2:
            t="Tuesday";
            break;
        case 3:
            t="Wednesday";
            break;
        case 4:
            t="Thursday";
            break;
        case 5:
            t="Friday";
            break;
        case 6:
            t="Saturday";
            break;
        case 0:
            t="Sunday";
            break;
        default:
            //if there is number that is not in the range of 1-7, print message:
            cout<<"no\n";
    }
    switch ((x+y)%7) {
        case 1:
            f="Monday";
            break;
        case 2:
            f="Tuesday";
            break;
        case 3:
            f="Wednesday";
            break;
        case 4:
            f="Thursday";
            break;
        case 5:
            f="Friday";
            break;
        case 6:
            f="Saturday";
            break;
        case 0:
            f="Sunday";
            break;
        default:
            //if there is number that is not in the range of 1-7, print message:
            cout<<"no\n";
    }
    cout<<"Today is "<<t<<" and the future day is "<<f<<endl;

    cout << "PROBLEM 15\n";
    int grade;
    cin>>grade;

    switch(grade/10){
        case 10:
        case 9: cout <<"A\n";
            break;
        case 8: cout <<"B\n";
            break;
        case 7: cout <<"C\n";
            break;
        case 6: cout <<"D\n";
            break;
        default: cout <<"F\n";
            break;
    }}

    cout << "PROBLEM 16\n";
    int p16_var1;
    cin>>p16_var1;

    switch(p16_var1>0){
        case 1:
            cout<<"Positive\n";
            break;
        case 0:
            switch(p16_var1<0){
                case 1:
                    cout<<"Negative\n";
                    break;
                case 0:
                    cout<<"zero\n";
            }
    }

    cout << "PROBLEM 17\n";
    char l;
    cin>>l;
    switch(l){
        case 'u':
            cout<<"salom"<<endl;
            break;
        case 'e':
            cout<<"Hello"<<endl;
            break;
        case 'r':
            cout<<"Здравствуйте"<<endl;
            break;
        case 'g':
            cout<<"Hallo"<<endl;
            break;
        default:
            cout<<"know";
    }

    cout << "PROBLEM 18\n";

    int weight;
    cin>>weight;

    switch(weight>0){
        case 0:
            cout<<"Invalid\n";
        case 1:
            switch(weight){
                case 1:
                    cout<<"3500\n";
                    break;
                case 2:
                case 3:
                    cout<<"5500\n";
                    break;
                case 4:
                case 5:
                case 6:
                case 7:
                case 8:
                case 9:
                case 10:
                    cout<<"8500\n";
                    break;
                case 11:
                case 12:
                case 13:
                case 14:
                case 15:
                case 16:
                case 17:
                case 18:
                case 19:
                case 20:
                    cout<<"10500\n";
                    break;
                default:
                    cout<<"shipped\n";
            }
    }

    cout << "PROBLEM 19\n";
    int n;

    cin>>n;

    switch(n){
        case 0:
            cout<<"Zero\n";
            break;
        case 1:
            cout<<"One\n";
            break;
        case 2:
            cout<<"Two\n";
            break;
        case 3:
            cout<<"Three\n";
            break;
        case 4:
            cout<<"Four\n";
            break;
        case 5:
            cout<<"Five\n";
            break;
        case 6:
            cout<<"Six\n";
            break;
        case 7:
            cout<<"Seven\n";
            break;
        case 8:
            cout<<"Eight\n";
            break;
        case 9:
            cout<<"Nine\n";
            break;
        default:
            cout<<"not\n";
    }

    cout << "PROBLEM 20\n";
    cin>>n;

    switch(n){
        case 1:
            cout<<"In January there is:\n";
            cout<<"--New Year, 1st January\n";
            cout<<"--Homeland Defenders’ Day, 14 January\n";
            break;
        case 3:
            cout<<"In March there is:\n";
            cout<<"-- International Women's Day, 8 March\n";
            cout<<"-- Navruz, 21 March\n";
            break;
        case 5:
            cout<<"In May there is:\n";
            cout<<"Memorial Day, 9 May\n";
            break;
        case 9:
            cout<<"In September there is:\n";
            cout<<" Independence Day, 1 September\n";
            break;
        case 10:
            cout<<"In October there is:\n";
            cout<<" Teacher's Day, 1 October\n";
            break;
        case 12:
            cout<<"In December there is:\n";
            cout<<" Constitution Day, 8 December\n";
            break;
        case 2:
        case 4:
        case 6:
        case 7:
        case 8:
        case 11:
            cout<<"In February, April, June, July, August, November there is no holidays. There are Ramadan Hayit and Kurban Hayit but their dates change.\n";
            break;
        default:
            cout<<"There is no such month\n";
    }

    cout << "PROBLEM 21\n";

    int randomNumber = rand();
    cout << randomNumber << endl;


    cout << "PROBLEM 22\n";

    srand((unsigned) time(NULL));

    int my_rand = rand();

    cout<<my_rand<<endl;

    return 0;
}