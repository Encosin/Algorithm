#include<iostream>
#include<string>
#include<stack>  // STL 라이브러리
using namespace std;
stack<int> S;

int main()
{
    int n = 0;
    cin >> n;
    for(int i=0; i<n; i++) {
        string str;
        cin >> str;
        if (str == "push") {
            int x; 
            cin >> x;
            S.push(x);
        }
        else if(str == "top") {
            if (S.empty()) 
                cout << "-1" << "\n";
            
            else
                cout << S.top() << "\n"; 
        }
        else if (str == "pop") {
            if(S.empty()) 
                cout << "-1" << '\n';
            else {
                cout << S.top() << '\n';
                S.pop();
            }
        }
        else if(str == "empty") 
            cout << S.empty() << '\n';

        else 
            cout << S.size() << '\n';
    }
    return 0;
}
