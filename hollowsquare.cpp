#include<iostream>
using namespace std;

int main()
{  
    int n=4;
    int i=0;
    while(i<n)
    {
        int j=0;
        while(j<n){
            if(i==0||i==n-1||j==0||j==n-1)
                cout<<'*';

            else
                cout<<"#";
            j=j+1;
        }
        cout<<endl;
        i=i+1;
        }
    
}
