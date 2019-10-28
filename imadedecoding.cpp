#include <iostream>
using namespace std;

void flip(char &ch){
    if(ch == '.'){
        ch = '#';
    }else{
        ch = '.';
    }
}
int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int a;
    int input;
    char ch;
    int count = 1;
    while(true){
        cin >> a;
        int sum = 0;
        bool error = false;
        if ( a == 0){
            break;
        }

        if(count != 1){
            cout << endl;
        }
        for (int i = 0; i <a ; i++){
            int oldSum = 0;
            cin >> ch;
            while((cin.peek()!='\n') && (cin >> input)){
                oldSum+= input;
                if(i == 0){
                    sum += input;
                }
                for (int num = 0; num <input; num++){
                    cout << ch;
                }
                flip(ch);
            }
            if(oldSum != sum && i != 0){
                    error = true;
            }
            oldSum = 0 ;
            cout << endl;
        }
        if(error){
            cout << "Error decoding image" << endl;
        }
        count++;
    }
    return 0;
}
