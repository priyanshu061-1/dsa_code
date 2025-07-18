#include<iostream>
using namespace std;
int main()

{
    int i=0;
    int n;
    cin>>n;
    while(i<n)
    {
        int j=0;
        char start;
        start='A'+n-1;
        while(j<i)
        {
            cout<<start;
            start=start+1;

            j=j+1;
            
        }
        cout<<endl;
        i=i+1;
    }
} 
