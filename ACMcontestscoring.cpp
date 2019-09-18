#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;
struct wrong{
    int pen = 20;
    char question;

    wrong(char question){
        this->question = question;
        this->pen = 20;
    }
};

int search(std::vector<wrong>arr , char data){
    for (int i = 0; i < arr.size(); i++){
        if(arr[i].question == data){
            return i;
        }
    }
    return -1;
}

int main() {

    int n;
    int a;
    char b;
    string c;
    bool stop = false;
    int tot= 0;
    int temp;
    vector<wrong> arr;
    int count = 0;

    for( int i = 0 ;!stop; i++){
            cin >> a;

            if ( a == -1){
                stop = true;
            }

            if(!stop){
                cin >> b >> c;

                if ( c == "right" && i == 0){
                    count++;
                    tot += a;
                }else if ( c == "right" && i > 0){
                    count++;
                    tot +=a;
                    temp = search(arr, b);

                    if(temp != -1){
                        tot+= arr[temp].pen;
                    }
                }
                else{
                    temp = search(arr, b);
                    if(temp == -1)
                        arr.push_back(wrong(b));
                    else{
                        arr[temp].pen += 20;
                    }
                }
            }
        }
    cout << count << " " << tot <<  endl;
    return 0;
}
