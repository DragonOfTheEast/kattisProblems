#include <iostream>
#include <vector>

using  namespace std;

int main(){
    int n;
    int a;
    cin >> n ;
    vector <int> arr;
    for(int i = 0; i < n; i++){
        cin >> a;
        if(arr.size() > 0 && ((arr.back()+a) %2 == 0) ){
            arr.pop_back();
        }else
            arr.push_back(a);
    }
    cout << arr.size() << '\n';
    return 0;
}
