#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int a, b;

    cin >> a >> b;
    vector <int> vec (a + 1, 0);
    vector<int> vec2;
    int temp;

    for (int i = 0; i < b; i++){
        cin >> temp;
        vec[temp] = temp;
        vec2.push_back(temp);
    }

    vec2.push_back(0);
    vec2.push_back(a);

    int ans;
    for(int i = 0; i < vec2.size() - 1; i++ ){

        for(int j = i + 1; j < vec2.size(); j++){
             ans = abs(vec2[j] - vec2[i]);

            if(vec[ans] == 0){
                vec[ans] = ans;
            }
        }

    }


    for ( int i = 1; i < vec.size(); i++){
        if(vec[i] != 0){
            cout << vec[i] << " ";
        }
    }


    return 0;
}
