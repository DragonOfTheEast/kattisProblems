#include <iostream>
#include <bits/stdc++.h>

using  namespace std;
int main(){
    int a;
    int y;
    vector<vector<char>> vector1;
    char ch;
    int ymax = 0 , xmax = 0;
    cin>> a;
    while(true){

        cin.get(ch);
        if (a==0){
            break;
        }
        if(ymax > 0){
            cout << endl;
        }

        int x = 0;
        for (int i = 0; i < a; i++){
            vector1.emplace_back();
            while(true) {
                cin.get(ch);
                if (ch == '\n') {
                    break;
                }
                vector1[i].push_back(ch);
                x++;
            }
            if(x > xmax){
                xmax = x;
            }
            x = 0;
        }

        y = a;

        vector<vector<char>> charVec;
        for (int i = 0; i < xmax; i++){
           charVec.emplace_back();
           for (int j = 0; j < y; j++){
               charVec[i].push_back(' ');
           }
        }
        y--;
        for (int i = 0; i< vector1.size(); i++){
            for (int j = 0; j < vector1[i].size(); j++){
                if(vector1[i][j] == '-'){
                    charVec[j][y-i] = '|';
                } else if(vector1[i][j] == '|'){
                    charVec[j][y-i] = '-';
                }else{
                    charVec[j][y-i] = vector1[i][j];
                }

            }
        }
        cin >> a;
        for(int i = 0; i < charVec.size(); i++){

            for(int j = charVec[i].size() - 1; j >= 0; j--){
                if(charVec[i][j] == ' '){
                    charVec[i][j] = '^';
                }
                else{
                    break;
                }
            }
            for(int j = 0; j < charVec[i].size(); j++){
                if(charVec[i][j] == '^'){
                    break;
                }
                cout << charVec[i][j];
            }
            cout<< '\n';
        }
        xmax = 0;
        vector1.clear();
        charVec.clear();
        ymax++;
    }


    return 0;

}
